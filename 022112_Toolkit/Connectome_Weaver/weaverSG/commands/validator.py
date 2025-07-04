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
from collections import defaultdict

# Assuming lsg_manager and operations are available from parent packages
from ..core.lsg_manager import LSGManager
from ..core import operations

# --- Private Validation Functions (Updated to v3 format) ---

def _find_duplicate_nodes(nodes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Finds duplicate nodes and reports them in the v3 issue format."""
    issues = []
    node_muids = defaultdict(list)
    for i, node in enumerate(nodes):
        if 'MUID' in node:
            node_muids[node['MUID']].append(i)

    for muid, indices in node_muids.items():
        if len(indices) > 1:
            issue_details = {
                "node_signature": {"MUID": muid},
                "first_occurrence": nodes[indices[0]],
                "duplicate_indices": indices
            }
            issues.append({
                "issue_code": "DUPLICATE_NODE",
                "severity": "ERROR",
                "message": "Обнаружено несколько узлов с одинаковым MUID.",
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
            issues.append({
                "issue_code": "DUPLICATE_RELATION",
                "severity": "ERROR",
                "message": "Обнаружено несколько идентичных связей.",
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

# --- Public Command Handler (Updated to use v3 format AND correct transaction logic) ---

def main(lsg_manager: LSGManager, output_format: str = 'human'):
    """
    Orchestrates the validation process for a given SG file.
    This is the main entry point called by the CLI handler.

    Args:
        lsg_manager (LSGManager): An initialized LSGManager instance for the target file.
        output_format (str): 'human' for readable summary, 'json' for machine-readable output.
    """
    try:
        if output_format != 'json':
            print(f"Starting validation for: {lsg_manager.filepath}")

        graph_data = lsg_manager.get_graph_data()
        if not graph_data:
            return # Error is already logged by the manager

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
        if not all_issues:
            print("Validation complete. No issues found.")
            old_issues = lsg_manager.metadata.get('validation_issues')
            if old_issues: # Clear previous validation issues if they exist
                 print("Clearing previous validation issues block from metadata.")
                 lsg_manager.update_metadata({'validation_issues': []})
                 lsg_manager.record_and_save_transaction([{"action": "clear_validation_issues"}], "validation_run")
                 print("Cleared old issues and saved the graph.")
            return

        print(f"\nValidation found {len(all_issues)} issue(s):")
        for issue in all_issues:
            # Human-readable summary generation...
            details_summary = ""
            if issue['issue_code'] == 'DUPLICATE_NODE':
                details_summary = f"MUID: {issue['details']['node_signature']['MUID']}"
            elif issue['issue_code'] == 'DUPLICATE_RELATION':
                sig = issue['details']['relation_signature']
                details_summary = f"From: {sig['from_MUID']}, To: {sig['to_MUID']}, Type: {sig['type']}"
            elif issue['issue_code'] == 'DANGLING_RELATION':
                endpoints = issue['details']['dangling_endpoints']
                dangling_info = ', '.join([f"{e['direction']}:{e['muid']}" for e in endpoints])
                details_summary = f"Missing MUID(s): {dangling_info}"
            print(f"  - [{issue['severity']}] {issue['issue_code']}: {issue['message']} ({details_summary})")

        # --- Correct Transactional Logic (Restored from original) ---
        print("\nUpdating file metadata with new validation results...")
        old_issues = lsg_manager.metadata.get('validation_issues', [])
        
        # Create a detailed changeset for the log
        changeset = [{
            "action": "validate_graph",
            "entity_id": "graph_meta",
            "entity_type": "metadata",
            "details": {"issues_found": len(all_issues)},
            "old_state": {"validation_issues_count": len(old_issues)},
            "new_state": {"validation_issues_count": len(all_issues), "issues": all_issues}
        }]
        
        # Update metadata in the manager's state
        lsg_manager.update_metadata({"validation_issues": all_issues})
        
        # Record the transaction and save all changes atomically
        lsg_manager.record_and_save_transaction(changeset, recipe_id="validation_run")
        
        print("Validation results have been saved to the graph file and logged.")

    except Exception as e:
        if output_format != 'json':
            print(f"\nAn error occurred during validation: {e}")
