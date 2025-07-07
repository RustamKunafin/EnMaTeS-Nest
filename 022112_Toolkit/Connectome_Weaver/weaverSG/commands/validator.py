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
from typing import List, Dict, Any, Set
from collections import defaultdict
import copy

# Assuming lsg_manager and operations are available from parent packages
from ..core.lsg_manager import LSGManager
from ..core import graph_io
from ..core import operations

# --- Private Validation Functions ---

def _find_duplicate_nodes(nodes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Finds duplicate nodes and reports them in the v3 issue format."""
    """
    Finds duplicate nodes based on MUID (strict duplicates) and alias (potential pre-migration duplicates).
    Reports them in the v3 issue format.
    """
    issues = []

    # --- Check for strict duplicates by MUID ---
    muid_groups = defaultdict(list)
    for i, node in enumerate(nodes):
        if 'MUID' in node:
            muid_groups[node['MUID']].append(i)

    for muid, indices in muid_groups.items():
        if len(indices) > 1:
            # For strict duplicates by MUID, report as ERROR
            issue_details = {
                "node_signature": {"MUID": muid},
                "first_occurrence": nodes[indices[0]],
                "duplicate_indices": indices
            }
            count = len(indices)
            issues.append({
                "issue_code": "DUPLICATE_NODE",
                "severity": "ERROR", # Strict duplicates are errors
                "message": f"Обнаружено {count} узла(ов) с одинаковым MUID.",
                "details": issue_details
            })

    # --- Check for potential pre-migration duplicates by alias ---
    # Only check if 'alias' field exists in at least one node (present after schema migration)
    if any('alias' in node and node['alias'] for node in nodes):
        alias_groups = defaultdict(list)
        for i, node in enumerate(nodes):
            # Group by non-empty alias
            if 'alias' in node and node['alias']:
                 # Store MUID and index for nodes with this alias
                alias_groups[node['alias']].append({'muid': node.get('MUID'), 'index': i})

        for alias_value, node_infos in alias_groups.items():
            # A potential duplicate group exists if more than one node shares the same alias
            # AND not all nodes in the group have the same MUID (which would be a strict MUID duplicate, already caught above)
            if len(node_infos) > 1 and len(set(ni['muid'] for ni in node_infos if ni['muid'])) > 1:
                # For potential duplicates by alias, report as WARNING
                issue_details = {
                    "alias_signature": {"alias": alias_value},
                    "nodes_info": node_infos # List of {'muid': ..., 'index': ...} for nodes with this alias
                }
                count = len(node_infos)
                issues.append({
                    "issue_code": "POTENTIAL_PRE_MIGRATION_DUPLICATE",
                    "severity": "WARNING", # Potential duplicates are warnings
                    "message": f"Обнаружено {count} узла(ов) с одинаковым alias (вероятно, дубликаты до миграции).",
                    "details": issue_details
                })
    return issues

def _find_duplicate_relations(relations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Finds duplicate relations and reports them in the v3 issue format."""
    issues = []
    relation_signatures = defaultdict(list)
    for i, rel in enumerate(relations):
        signature = (rel.get('from_MUID'), rel.get('to_MUID'), rel.get('type'))
        relation_signatures[signature].append(i)

    for sig, indices in relation_signatures.items():
        if len(indices) > 1:
            issue_details = {
                "relation_signature": {
                    "from_MUID": sig[0],
                    "to_MUID": sig[1],
                    "type": sig[2]
                },
                "first_occurrence": relations[indices[0]],
                "duplicate_indices": indices
            }
            count = len(indices)
            issues.append({
                "issue_code": "DUPLICATE_RELATION",
                "severity": "ERROR",
                "message": f"Обнаружено {count} идентичных связей.",
                "details": issue_details
            })
    return issues

def _find_dangling_relations(nodes: List[Dict[str, Any]], relations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Checks for relations pointing to non-existent nodes, reports in v3 format."""
    issues = []
    existing_muids: Set[str] = {node['MUID'] for node in nodes if 'MUID' in node}
    
    for i, rel in enumerate(relations):
        dangling_endpoints = []
        from_muid = rel.get('from_MUID')
        to_muid = rel.get('to_MUID')

        if from_muid and from_muid not in existing_muids:
            dangling_endpoints.append({"direction": "from", "muid": from_muid})
        
        if to_muid and to_muid not in existing_muids:
            dangling_endpoints.append({"direction": "to", "muid": to_muid})

        if dangling_endpoints:
            issue_details = {
                "relation": rel,
                "relation_index": i,
                "dangling_endpoints": dangling_endpoints
            }
            issues.append({
                "issue_code": "DANGLING_RELATION",
                "severity": "ERROR",
                "message": "Связь ссылается на несуществующий узел.",
                "details": issue_details
            })
    return issues

# --- Public Command Handler (Corrected Logic) ---

def handle_validation(file_path: Path, output_format: str = 'human'):
    """
    Orchestrates the validation process for a given SG file.
    This is the main entry point called by the CLI handler.

    Args:
        file_path (Path): Path to the main SG file.
        output_format (str): 'human' for readable summary, 'json' for machine-readable output.
    """
    try:
        if output_format != 'json':
            print(f"Starting validation for: {file_path}")

        # In JSON mode, we only need to load the file, not the full manager
        if output_format == 'json':
            _, graph_data = graph_io.load_graph_from_file(file_path)
        else:
            lsg_manager = LSGManager(file_path)
            graph_data = lsg_manager.sg_data

        if not graph_data:
            return # Error is already logged by the manager or loader

        # Make a deep copy to get the old state before any changes
        old_issues = copy.deepcopy(graph_data.get('validation_issues', []))

        nodes = graph_data.get('nodes', [])
        relations = graph_data.get('relations', [])
        
        all_issues = []
        all_issues.extend(_find_dangling_relations(nodes, relations))
        all_issues.extend(_find_duplicate_nodes(nodes))
        all_issues.extend(_find_duplicate_relations(relations))

        # --- Machine-Readable Output Handling ---
        if output_format == 'json':
            print(json.dumps(all_issues, indent=2, ensure_ascii=False))
            return

        # --- Human-Readable Output and File Modification ---
        
        # CORRECTED LOGIC: First, always print the report if issues are found.
        if not all_issues:
            print("Validation complete. No issues found.")
        else:
            print(f"\nValidation found {len(all_issues)} issue(s):")
            for issue in all_issues:
                # Human-readable summary generation...
                details_summary = ""
                if issue['issue_code'] == 'DUPLICATE_NODE':
                    count = len(issue['details']['duplicate_indices'])
                    details_summary = f"MUID: {issue['details']['node_signature']['MUID']} (found {count} times)"
                elif issue['issue_code'] == 'DUPLICATE_RELATION':
                    count = len(issue['details']['duplicate_indices'])
                    sig = issue['details']['relation_signature']
                    details_summary = f"From: {sig['from_MUID']}, To: {sig['to_MUID']}, Type: {sig['type']} (found {count} times)"
                elif issue['issue_code'] == 'DANGLING_RELATION':
                    endpoints = issue['details']['dangling_endpoints']
                    dangling_info = ', '.join([f"{e['direction']}:{e['muid']}" for e in endpoints])
                    # CORRECTED: Added specific relation details to the summary
                    rel = issue['details']['relation']
                    details_summary = f"Missing MUID(s): {dangling_info} in relation from '{rel.get('from_MUID')}' to '{rel.get('to_MUID')}'"
                print(f"  - [{issue['severity']}] {issue['issue_code']}: {issue['message']} ({details_summary})")

        # Second, decide if the file needs to be updated.
        if old_issues == all_issues:
            print("\nNo changes in issues found. File will not be modified.")
            return

        # If we are here, it means the issues list has changed.
        print("\nUpdating graph data with new validation results...")
        
        updates = {"validation_issues": all_issues}
        lsg_manager.sg_data = operations.update_graph_properties(lsg_manager.sg_data, updates)
        
        changeset = [{
            "action": "update_graph_properties",
            "entity_id": "graph_data",
            "entity_type": "graph_data",
            "details": f"Updated validation_issues block. Found {len(all_issues)} issues.",
            "old_state": {"validation_issues": old_issues},
            "new_state": {"validation_issues": all_issues}
        }]
        
        lsg_manager.record_transaction(changeset, recipe_id="validation_run")
        lsg_manager.save_changes()
        
        print("Validation results have been saved to the graph data and logged.")

    except Exception as e:
        if output_format != 'json':
            print(f"\nAn unexpected error occurred during validation: {e}")
