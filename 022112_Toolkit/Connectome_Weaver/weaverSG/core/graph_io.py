# -*- coding: utf-8 -*-
"""
graph_io.py

Core module for handling low-level input/output operations for Semantic Graphs (SG).
This module is responsible for:
- Loading graph data from .md files.
- Parsing YAML frontmatter and JSON graph content.
- Saving graph data back to .md files.
- Creating backups of graph files before modification.

This version incorporates robust error handling, type hinting,
and uses the pathlib library for modern path management.

Membra Open Development License (MODL) v1.0
Copyright (c) Rustam Kunafin 2025. All rights reserved.
Licensed under MODL v1.0. See LICENSE or https://cyberries.org/04_Resources/0440_Agreements/MODL.
"""

import json
import re
import shutil
import yaml
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Tuple

# --- Custom Exceptions for Clearer Error Reporting ---

class GraphFileError(Exception):
    """Base exception for errors in this module."""
    pass

class GraphFileNotFoundError(GraphFileError):
    """Raised when the graph file does not exist."""
    pass

class GraphFileParseError(GraphFileError):
    """Raised when the file content cannot be parsed (e.g., malformed YAML or JSON)."""
    pass

class GraphFileSaveError(GraphFileError):
    """Raised during the file saving process."""
    pass


def load_graph_from_file(file_path: Path) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """
    Loads a Semantic Graph from a specified .md file.

    The file is expected to have a YAML frontmatter section and a JSON content block.

    Args:
        file_path (Path): The path to the .md file.

    Returns:
        A tuple containing two dictionaries:
        - The first is the parsed YAML metadata.
        - The second is the parsed JSON graph data.

    Raises:
        GraphFileNotFoundError: If the file does not exist at the given path.
        GraphFileParseError: If the file content is malformed and cannot be parsed.
    """
    if not file_path.is_file():
        raise GraphFileNotFoundError(f"Graph file not found at: {file_path}")

    try:
        with file_path.open('r', encoding='utf-8') as f:
            content = f.read()

        # Split the content into YAML frontmatter and the rest
        parts = content.split('---', 2)
        if len(parts) < 3:
            raise GraphFileParseError("File does not contain a valid YAML frontmatter section.")

        yaml_content = parts[1]
        rest_of_content = parts[2]

        # Parse YAML metadata
        metadata = yaml.safe_load(yaml_content)
        if not isinstance(metadata, dict):
            raise GraphFileParseError("Failed to parse YAML metadata or it is not a dictionary.")

        # Find and parse the JSON block
        json_match = re.search(r'```json\s*\n(.*?)\n```', rest_of_content, re.DOTALL)
        if not json_match:
            raise GraphFileParseError("Could not find a ```json ... ``` block in the file.")

        json_content = json_match.group(1)
        graph_data = json.loads(json_content)
        if not isinstance(graph_data, dict):
            raise GraphFileParseError("Failed to parse JSON graph data or it is not a dictionary.")

        return metadata, graph_data

    except yaml.YAMLError as e:
        raise GraphFileParseError(f"Error parsing YAML frontmatter: {e}") from e
    except json.JSONDecodeError as e:
        raise GraphFileParseError(f"Error parsing JSON graph data: {e}") from e
    except Exception as e:
        # Catch-all for other unexpected errors during file processing
        raise GraphFileParseError(f"An unexpected error occurred while loading the graph: {e}") from e


def save_graph_to_file(file_path: Path, metadata: Dict[str, Any], graph_data: Dict[str, Any]) -> None:
    """
    Saves the Semantic Graph data to a specified .md file.

    This function serializes the metadata to YAML and the graph data to JSON,
    then writes them into the file in the standard format.

    Args:
        file_path (Path): The path to the target .md file.
        metadata (Dict[str, Any]): The dictionary containing the graph's metadata.
        graph_data (Dict[str, Any]): The dictionary containing the graph's nodes and relations.

    Raises:
        GraphFileSaveError: If an error occurs during the file writing process.
    """
    try:
        # Serialize metadata to a clean YAML string
        yaml_string = yaml.dump(
            metadata,
            allow_unicode=True,
            sort_keys=False,
            default_flow_style=False,
            indent=2
        )

        # Serialize graph data to a formatted JSON string
        json_string = json.dumps(graph_data, indent=2, ensure_ascii=False)

        # Assemble the full file content
        file_content = (
            f"---\n"
            f"{yaml_string.strip()}\n"
            f"---\n\n"
            f"```json\n"
            f"{json_string}\n"
            f"```\n"
        )

        # Write the content to the file
        with file_path.open('w', encoding='utf-8') as f:
            f.write(file_content)

    except (yaml.YAMLError, TypeError) as e:
        raise GraphFileSaveError(f"Error serializing data to YAML or JSON: {e}") from e
    except IOError as e:
        raise GraphFileSaveError(f"Error writing to file at {file_path}: {e}") from e
    except Exception as e:
        raise GraphFileSaveError(f"An unexpected error occurred while saving the graph: {e}") from e


def create_backup(file_path: Path) -> Path:
    """
    Creates a timestamped backup of the given file.

    The backup is created in the same directory as the original file.

    Args:
        file_path (Path): The path to the file to be backed up.

    Returns:
        Path: The path to the newly created backup file.

    Raises:
        GraphFileNotFoundError: If the source file does not exist.
        GraphFileError: If the backup operation fails.
    """
    if not file_path.is_file():
        raise GraphFileNotFoundError(f"Cannot create backup. Source file not found: {file_path}")

    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = f"{file_path.stem}_backup_{timestamp}{file_path.suffix}"
        backup_path = file_path.parent / backup_filename

        shutil.copy2(file_path, backup_path)
        
        print(f"Created backup: {backup_path}")
        return backup_path
    except Exception as e:
        raise GraphFileError(f"Failed to create backup for {file_path}: {e}") from e
