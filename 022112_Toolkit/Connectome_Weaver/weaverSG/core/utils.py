# -*- coding: utf-8 -*-
"""
utils.py

This module provides a collection of utility functions used across the weaverSG application.
It includes helpers for generating unique identifiers and for loading configuration files.

Membra Open Development License (MODL) v1.0
Copyright (c) Rustam Kunafin 2025. All rights reserved.
Licensed under MODL v1.0. See LICENSE or https://cyberries.org/04_Resources/0440_Agreements/MODL.
"""

import uuid
import yaml
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional

# --- Custom Exceptions ---

class UtilityError(Exception):
    """Base exception for errors in the utility module."""
    pass

class RecipeFileError(UtilityError):
    """Custom exception for errors related to recipe file loading."""
    pass

# --- ID Generation Functions ---

def generate_muid() -> str:
    """
    Generates a new Membra Universal ID (MUID) using UUIDv4.

    Returns:
        A string representing a new, unique MUID.
    """
    return str(uuid.uuid4())

def generate_lid(prefix: str = 'l') -> str:
    """
    Generates a new Link ID (LID) with a given prefix.

    LIDs are shorter, human-readable identifiers for relations of class 'link'.

    Args:
        prefix (str): The prefix for the ID, defaults to 'l'.

    Returns:
        A string representing a new, unique LID.
    """
    # Uses the first 8 characters of a UUID for brevity.
    short_uuid = str(uuid.uuid4())[:8]
    return f"{prefix}_{short_uuid}"

def generate_transaction_id() -> str:
    """
    Generates a new Transaction ID (TID).

    The format combines a precise timestamp with a short unique hash to ensure
    both chronological order and uniqueness.

    Returns:
        A string representing a new, unique transaction ID.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    short_uuid = str(uuid.uuid4())[:8]
    return f"t_{timestamp}_{short_uuid}"

# --- Data Validation Functions (RESTORED & INTEGRATED) ---

def is_uuid(text: Optional[str]) -> bool:
    """
    Checks if a given string is a valid UUID.
    This is required for conditional operations in recipes.
    Returns False if the input is None or not a string.
    """
    if not isinstance(text, str):
        return False
    try:
        # Attempt to create a UUID object from the text.
        # A ValueError is raised if the string is not a valid UUID.
        uuid.UUID(text)
        return True
    except ValueError:
        return False

# --- File Loading Functions ---

def load_yaml_file(file_path: Path) -> Dict[str, Any]:
    """
    Loads and parses a YAML file.

    This is a generic utility for loading configuration files like recipes.

    Args:
        file_path (Path): The path to the YAML file.

    Returns:
        A dictionary containing the parsed YAML content.

    Raises:
        RecipeFileError: If the file is not found, cannot be read, or is malformed.
    """
    if not file_path.is_file():
        raise RecipeFileError(f"File not found: {file_path}")

    try:
        with file_path.open('r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        if not isinstance(data, dict):
            raise RecipeFileError(f"YAML content is not a dictionary in file: {file_path}")
        return data
    except yaml.YAMLError as e:
        raise RecipeFileError(f"Error parsing YAML file {file_path}: {e}") from e
    except Exception as e:
        raise RecipeFileError(f"An unexpected error occurred while reading {file_path}: {e}") from e
