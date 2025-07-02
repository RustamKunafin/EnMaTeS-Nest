# -*- coding: utf-8 -*-
"""
validator.py

This module implements the 'validate' command for weaverSG.
It performs a series of checks on a Semantic Graph to ensure its integrity.
The output is structured and unified for both human and machine processing.

Membra Open Development License (MODL) v1.0
Copyright (c) Rustam Kunafin 2025. All rights reserved.
Licensed under MODL v1.0. See LICENSE or https://cyberries.org/04_Resources/0440_Agreements/MODL.
"""

import json
from pathlib import Path
from typing import List, Dict, Any, Set, Tuple

from ..core.lsg_manager import LSGManager
from ..core import operations

# --- Private Validation Functions ---

def _find_dangling_relations(graph_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Checks for relations pointing to non-existent nodes."""
    issues = []
    node_muids: Set[str] = {node['MUID'] for node in graph_data.get('nodes', []) if 'MUID' in node}
    
    for relation in graph_data.get('relations', []):
        from_muid, to_muid = relation.get('from_MUID'), relation.get('to_MUID')
        if to_muid and to_muid not in node_muids:
            issues.append({
                "issue_type": "dangling_relation_to",
                "from_MUID": from_muid,
                "missing_target_MUID": to_muid,
                "problematic_relation": relation
            })
        if from_muid and from_muid not in node_muids:
            issues.append({
                "issue_type": "dangling_relation_from",
                "missing_source_MUID": from_muid,
                "to_MUID": to_muid,
                "problematic_relation": relation
            })
    return issues

def _find_duplicate_nodes(graph_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Finds duplicate nodes and reports the count and a canonical instance."""
    issues = []
    muid_locations: Dict[str, List[Dict[str, Any]]] = {}
    
    for node in graph_data.get('nodes', []):
        muid = node.get('MUID')
        if muid:
            muid_locations.setdefault(muid, []).append(node)

    for muid, instances in muid_locations.items():
        if len(instances) > 1:
            issues.append({
                "issue_type": "duplicate_node",
                "MUID": muid,
                "count": len(instances),
                "canonical_instance": instances[0] # Show the first found instance as an example
            })
    return issues

def _find_duplicate_relations(graph_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Finds duplicate relations and reports the count and a canonical instance."""
    issues = []
    seen_relations: Dict[Tuple[str, str, str], List[Dict[str, Any]]] = {}
    
    for relation in graph_data.get('relations', []):
        from_muid, to_muid, rel_type = relation.get('from_MUID'), relation.get('to_MUID'), relation.get('type')
        if not all([from_muid, to_muid, rel_type]): continue
        
        relation_key = (from_muid, to_muid, rel_type)
        seen_relations.setdefault(relation_key, []).append(relation)

    for key, instances in seen_relations.items():
        if len(instances) > 1:
            issues.append({
                "issue_type": "duplicate_relation",
                "relation_key": {"from_MUID": key[0], "to_MUID": key[1], "type": key[2]},
                "count": len(instances),
                "canonical_instance": instances[0] # Show the first found instance as an example
            })
    return issues

# --- Public Command Handler ---

def handle_validation(file_path: Path, output_format: str = 'human'):
    """
    Orchestrates the validation process for a given SG file.

    Args:
        file_path (Path): The path to the main SG file to validate.
        output_format (str): 'human' for readable summary, 'json' for machine-readable output.
    """
    if output_format != 'json':
        print(f"Starting validation for: {file_path}")
    
    try:
        lsg_manager = LSGManager(file_path)
        all_issues = []
        all_issues.extend(_find_dangling_relations(lsg_manager.sg_data))
        all_issues.extend(_find_duplicate_nodes(lsg_manager.sg_data))
        all_issues.extend(_find_duplicate_relations(lsg_manager.sg_data))

        # --- Machine-Readable Output Handling ---
        if output_format == 'json':
            # In JSON mode, we only output the issues and do not modify the file.
            print(json.dumps(all_issues, indent=2, ensure_ascii=False))
            return

        # --- Human-Readable Output and File Modification ---
        if not all_issues:
            print("Validation complete. No issues found.")
            if 'validation_issues' in lsg_manager.sg_data and lsg_manager.sg_data['validation_issues']:
                 print("Clearing previous validation issues block.")
                 lsg_manager.sg_data['validation_issues'] = []
                 changeset = [{"action": "clear_validation_issues", "details": "No issues found, clearing old validation block."}]
                 lsg_manager.record_transaction(changeset, recipe_id="validation_clear")
                 lsg_manager.save_changes()
                 print("Cleared old issues and saved the graph.")
            return

        print(f"\nValidation found {len(all_issues)} issue group(s):")
        for issue in all_issues:
            if issue['issue_type'] == 'duplicate_node':
                print(f"  - Duplicate Node: {issue['MUID']} ({issue['count']} instances)")
            elif issue['issue_type'] == 'duplicate_relation':
                key = issue['relation_key']
                print(f"  - Duplicate Relation: from {key['from_MUID']} to {key['to_MUID']} ({issue['count']} instances)")
            else:
                print(f"  - Dangling Relation: from {issue.get('from_MUID')} to {issue.get('missing_target_MUID')}")

        # Update the graph file with the issues
        old_issues = lsg_manager.sg_data.get('validation_issues')
        changeset = [{
            "action": "validate_graph", "entity_id": "graph_meta", "entity_type": "graph",
            "details": {"issues_found": len(all_issues)},
            "old_state": {"validation_issues": old_issues}, "new_state": {"validation_issues": all_issues}
        }]
        lsg_manager.sg_data = operations.update_graph_properties(
            lsg_manager.sg_data, {"validation_issues": all_issues}
        )
        lsg_manager.record_transaction(changeset, recipe_id="validation_run")
        lsg_manager.save_changes()
        print("\nValidation results have been saved to the graph file and logged.")

    except Exception as e:
        # Avoid printing error details in JSON mode to keep output clean
        if output_format != 'json':
            print(f"\nAn error occurred during validation: {e}")
