# -*- coding: utf-8 -*-
"""
log_archiver.py

This module implements the 'archive-log' command for weaverSG.
It safely archives the current Log Semantic Graph (LSG) file by renaming it
with a timestamp. It then creates a new, empty LSG file and adds an initial
transaction that points to the archived file, ensuring the chain of history
is maintained.

Membra Open Development License (MODL) v1.0
Copyright (c) Rustam Kunafin 2025. All rights reserved.
Licensed under MODL v1.0. See LICENSE or https://cyberries.org/04_Resources/0440_Agreements/MODL.
"""

import os
from pathlib import Path
from datetime import datetime

from ..core import graph_io
from ..core import utils
from ..core import operations

def handle_archive_log(file_path: Path):
    """
    Handles the archiving of the LSG file associated with the given SG file.

    Args:
        file_path (Path): The path to the main SG file.
    """
    print(f"Starting log archival process for: {file_path}")

    lsg_path = file_path.with_name(f"LSG_{file_path.name}")

    if not lsg_path.is_file():
        print(f"Log file not found at {lsg_path}. Nothing to archive.")
        return

    try:
        # 1. Define the name for the archive file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        archive_path = lsg_path.with_name(f"{lsg_path.stem}.archive_{timestamp}{lsg_path.suffix}")

        # 2. Rename the current log file to its archive name
        lsg_path.rename(archive_path)
        print(f"Successfully archived current log to: {archive_path}")

        # 3. Create a new, empty LSG
        new_lsg_metadata, new_lsg_data = {
            'title': f"Log for {file_path.name}",
            'graph_version': "1.0",
            'description': "Transactional log for a Semantic Graph."
        }, {
            'nodes': [],
            'relations': []
        }
        
        # 4. Create a "breadcrumb" transaction pointing to the archive
        changeset = [{
            "action": "archive_log",
            "details": {
                "message": "Previous log was archived.",
                "archive_file": str(archive_path)
            }
        }]
        
        transaction_muid = utils.generate_transaction_id()
        transaction_node = {
            "MUID": transaction_muid,
            "type": "Transaction",
            "timestamp": utils.datetime.now().isoformat(),
            "recipe_id": "archive_log_operation",
            "changeset": changeset
        }
        new_lsg_data = operations.add_node(new_lsg_data, transaction_node)
        
        # 5. Save the new LSG file with the initial transaction
        graph_io.save_graph_to_file(lsg_path, new_lsg_metadata, new_lsg_data)
        print(f"Created new empty log file at: {lsg_path}")
        print("A breadcrumb transaction pointing to the archive has been added.")

    except OSError as e:
        print(f"\nAn OS error occurred during file operation: {e}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
