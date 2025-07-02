# -*- coding: utf-8 -*-
"""
log_bundler.py

This module implements the 'bundle-log' and 'detach-log' commands for weaverSG.
'bundle-log': Moves the content of the external LSG file into the main SG file
              under the 'log_history' key.
'detach-log': Extracts the 'log_history' from an SG file and saves it as a
              separate, external LSG file.

Membra Open Development License (MODL) v1.0
Copyright (c) Rustam Kunafin 2025. All rights reserved.
Licensed under MODL v1.0. See LICENSE or https://cyberries.org/04_Resources/0440_Agreements/MODL.
"""

import os
from pathlib import Path

from ..core.lsg_manager import LSGManager
from ..core import graph_io
from ..core import operations
from ..core import utils

# --- Bundle Log Command ---

def _check_for_archives(directory: Path) -> bool:
    """Checks if any log archive files exist in the directory."""
    return any(directory.glob("*.archive_*.md"))

def handle_bundle_log(file_path: Path):
    """
    Handles bundling the LSG content into the main SG file.

    Args:
        file_path (Path): The path to the main SG file.
    """
    print(f"Starting log bundling process for: {file_path}")
    
    try:
        lsg_manager = LSGManager(file_path)

        # --- Pre-flight checks for safety ---
        if 'log_history' in lsg_manager.sg_data:
            print("Error: Graph file already contains a bundled log ('log_history'). Cannot bundle.")
            return
        
        if not lsg_manager.lsg_path.is_file():
            print(f"Error: Log file not found at {lsg_manager.lsg_path}. Nothing to bundle.")
            return

        if _check_for_archives(file_path.parent):
            print("Error: Log archive files found in the directory. Please handle them before bundling.")
            return

        # --- Operation ---
        # 1. Add a final transaction to the in-memory log to record the bundle operation
        changeset = [{"action": "log_bundled", "details": {"message": "Log was bundled into the parent SG."}}]
        lsg_manager.record_transaction(changeset, recipe_id="bundle_log_operation")

        # 2. Add the entire log history to the main SG data
        lsg_manager.sg_data = operations.update_graph_properties(
            lsg_manager.sg_data,
            {"log_history": lsg_manager.lsg_data}
        )
        
        # 3. Save the modified SG file (without the LSGManager, as it would create a backup)
        graph_io.create_backup(lsg_manager.sg_path)
        graph_io.save_graph_to_file(lsg_manager.sg_path, lsg_manager.sg_metadata, lsg_manager.sg_data)
        print(f"Successfully saved bundled graph to: {lsg_manager.sg_path}")

        # 4. Delete the now-redundant external LSG file
        lsg_manager.lsg_path.unlink()
        print(f"Successfully deleted external log file: {lsg_manager.lsg_path}")
        
    except Exception as e:
        print(f"\nAn unexpected error occurred during bundling: {e}")

# --- Detach Log Command ---

def handle_detach_log(file_path: Path):
    """
    Handles detaching the bundled log from an SG file into an external LSG file.

    Args:
        file_path (Path): The path to the main SG file.
    """
    print(f"Starting log detachment process for: {file_path}")
    
    try:
        lsg_manager = LSGManager(file_path)
        
        # --- Pre-flight checks ---
        if 'log_history' not in lsg_manager.sg_data:
            print("Error: No 'log_history' found in the graph file. Nothing to detach.")
            return
            
        if lsg_manager.lsg_path.is_file():
            print(f"Error: An external log file already exists at {lsg_manager.lsg_path}. Cannot detach.")
            return

        # --- Operation ---
        # 1. Extract the log data
        detached_log_data = lsg_manager.sg_data.pop('log_history')
        
        # 2. Create a new transaction to record the detachment
        changeset = [{"action": "log_detached", "details": {"message": "Log was detached to an external file."}}]
        transaction_muid = utils.generate_transaction_id()
        transaction_node = {
            "MUID": transaction_muid, "type": "Transaction",
            "timestamp": utils.datetime.now().isoformat(),
            "recipe_id": "detach_log_operation", "changeset": changeset
        }
        detached_log_data = operations.add_node(detached_log_data, transaction_node)
        
        # 3. Save the detached log to a new external LSG file
        lsg_metadata = {"title": f"Log for {file_path.name}"} # Basic metadata
        graph_io.save_graph_to_file(lsg_manager.lsg_path, lsg_metadata, detached_log_data)
        print(f"Successfully created external log file: {lsg_manager.lsg_path}")

        # 4. Save the main SG file (now without the log_history)
        lsg_manager.save_changes() # Use the manager to handle backup and save
        print(f"Successfully saved main graph without bundled log to: {file_path}")

    except Exception as e:
        print(f"\nAn unexpected error occurred during detachment: {e}")
