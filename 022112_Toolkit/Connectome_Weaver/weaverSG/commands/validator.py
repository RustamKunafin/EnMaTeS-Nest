# -*- coding: utf-8 -*-
"""
validator.py

This module implements the 'validate' command for weaverSG.
It performs a series of checks on a Semantic Graph to ensure its integrity,
such as finding dangling relations and duplicate nodes.

The results of the validation are recorded directly into the SG file within a
'validation_issues' block, and this operation is logged as a transaction.

Membra Open Development License (MODL) v1.0
Copyright (c) Rustam Kunafin 2025. All rights reserved.
Licensed under MODL v1.0. See LICENSE or https://cyberries.org/04_Resources/0440_Agreements/MODL.
"""

from pathlib import Path
from typing import List, Dict, Any, Set

from ..core.lsg_manager import LSGManager
from ..core import operations

# --- Private Validation Functions ---

def _find_dangling_relations(graph_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Checks for relations pointing to non-existent nodes."""
    issues = []
    node_muids: Set[str] = {node['MUID'] for node in graph_data.get('nodes', []) if 'MUID' in node}
    
    for relation in graph_data.get('relations', []):
        from_muid = relation.get('from_MUID')
        to_muid = relation.get('to_MUID')

        if from_muid and from_muid not in node_muids:
            issues.append({
                "issue_type": "dangling_relation_from",
                "missing_MUID": from_muid,
                "relation_id": relation.get('LID') or relation.get('MUID')
            })
        if to_muid and to_muid not in node_muids:
            issues.append({
                "issue_type": "dangling_relation_to",
                "missing_MUID": to_muid,
                "relation_id": relation.get('LID') or relation.get('MUID')
            })
    return issues

def _find_duplicate_nodes(graph_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Checks for nodes with duplicate MUIDs."""
    issues = []
    seen_muids: Set[str] = set()
    for node in graph_data.get('nodes', []):
        muid = node.get('MUID')
        if muid:
            if muid in seen_muids:
                issues.append({"issue_type": "duplicate_node", "MUID": muid})
            else:
                seen_muids.add(muid)
    return issues

# --- Public Command Handler ---

def handle_validation(file_path: Path):
    """
    Orchestrates the validation process for a given SG file.

    Initializes the LSGManager, runs all validation checks, records the results
    as a transaction, and saves the changes.

    Args:
        file_path (Path): The path to the main SG file to validate.
    """
    print(f"Starting validation for: {file_path}")
    
    try:
        # Initialize the manager, which loads both SG and LSG
        lsg_manager = LSGManager(file_path)

        # Run all validation checks
        all_issues = []
        all_issues.extend(_find_dangling_relations(lsg_manager.sg_data))
        all_issues.extend(_find_duplicate_nodes(lsg_manager.sg_data))
        # Future checks (e.g., schema validation) can be added here.

        if not all_issues:
            print("Validation complete. No issues found.")
            # Even if no issues are found, we can optionally clear any old validation blocks.
            # For now, we only act if new issues are found.
            if 'validation_issues' in lsg_manager.sg_data:
                 print("Clearing previous validation issues block.")
                 lsg_manager.sg_data['validation_issues'] = []
            else:
                return


        else:
            print(f"\nValidation found {len(all_issues)} issue(s):")
            for issue in all_issues:
                print(f"  - {issue}")
        
        # Prepare the changeset for the transaction log
        old_issues = lsg_manager.sg_data.get('validation_issues')
        changeset = [{
            "action": "validate_graph",
            "entity_id": "graph_meta",
            "entity_type": "graph",
            "details": {"issues_found": len(all_issues)},
            "old_state": {"validation_issues": old_issues},
            "new_state": {"validation_issues": all_issues}
        }]

        # Update the main graph data with the validation results
        lsg_manager.sg_data = operations.update_graph_properties(
            lsg_manager.sg_data,
            {"validation_issues": all_issues}
        )
        
        # Record this entire operation as a single transaction
        lsg_manager.record_transaction(changeset, recipe_id="validation_run")

        # Save all changes to disk
        lsg_manager.save_changes()
        
        print("\nValidation results have been saved to the graph file and logged.")

    except Exception as e:
        print(f"\nAn error occurred during validation: {e}")
        # Depending on the desired behavior, you might want to log this error
        # or handle it in a more specific way.
