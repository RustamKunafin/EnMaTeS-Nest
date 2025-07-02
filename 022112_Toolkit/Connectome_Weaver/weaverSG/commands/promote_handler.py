# -*- coding: utf-8 -*-
"""
promote_handler.py

This module implements the 'promote-relation' command for weaverSG.
This command upgrades a lightweight 'link' relation to a more significant 'bind'
relation. It finds the link by its LID, changes its class, assigns it a new MUID
for system-wide uniqueness, and preserves its original LID for historical tracking.

Membra Open Development License (MODL) v1.0
Copyright (c) Rustam Kunafin 2025. All rights reserved.
Licensed under MODL v1.0. See LICENSE or https://cyberries.org/04_Resources/0440_Agreements/MODL.
"""

import copy
from pathlib import Path
from typing import Dict, Any, Optional, Tuple

from ..core.lsg_manager import LSGManager
from ..core import operations
from ..core import utils

def _find_relation_by_lid(graph_data: Dict[str, Any], lid: str) -> Optional[Tuple[Dict[str, Any], int]]:
    """
    Finds a relation and its index by its LID.

    Args:
        graph_data: The dictionary representing the graph.
        lid: The Link ID (LID) of the relation to find.

    Returns:
        A tuple containing the relation dictionary and its index, or None if not found.
    """
    for i, relation in enumerate(graph_data.get('relations', [])):
        if relation.get('LID') == lid:
            return relation, i
    return None

def handle_promote_relation(file_path: Path, lid: str):
    """
    Handles the promotion of a 'link' relation to a 'bind' relation.

    Args:
        file_path (Path): The path to the main SG file.
        lid (str): The LID of the link relation to promote.
    """
    print(f"Attempting to promote relation with LID '{lid}' in file: {file_path}")

    try:
        lsg_manager = LSGManager(file_path)

        # Find the target relation
        find_result = _find_relation_by_lid(lsg_manager.sg_data, lid)
        if find_result is None:
            raise operations.RelationNotFoundError(f"Relation with LID '{lid}' not found.")
        
        original_relation, _ = find_result
        
        # Validate that it's a promotable 'link'
        if original_relation.get('class') != 'link':
            raise operations.OperationError(
                f"Cannot promote relation with LID '{lid}'. It is not of class 'link'."
            )

        # Prepare the updates and the changeset for logging
        new_muid = utils.generate_muid()
        updates = {
            "class": "bind",
            "MUID": new_muid,
            "legacy_LID": lid
        }
        
        # Create a deep copy for the changeset to record the state before the update
        old_state = copy.deepcopy(original_relation)
        new_state = copy.deepcopy(original_relation)
        new_state.update(updates)

        changeset = [{
            "action": "promote_relation",
            "entity_id": lid,
            "entity_type": "relation",
            "details": f"Promoted link {lid} to bind {new_muid}",
            "old_state": old_state,
            "new_state": new_state
        }]

        # Apply the update using the operations module
        lsg_manager.sg_data = operations.update_relation(lsg_manager.sg_data, lid, updates)
        
        # Record the transaction
        lsg_manager.record_transaction(changeset, recipe_id="promote_relation")

        # Save all changes
        lsg_manager.save_changes()

        print(f"\nSuccessfully promoted relation '{lid}' to a 'bind' with new MUID '{new_muid}'.")
        print("Changes have been saved and logged.")

    except (operations.OperationError, FileNotFoundError) as e:
        print(f"\nAn error occurred: {e}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
