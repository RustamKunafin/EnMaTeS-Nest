# -*- coding: utf-8 -*-
"""
operations.py

This module provides a set of atomic, in-memory operations for manipulating
the data of a Semantic Graph (SG). Each function takes the graph data as input,
performs a single, specific modification, and returns the modified graph data.

This approach ensures that data flow is explicit and predictable. All functions
include robust error checking to prevent common issues like modifying non-existent
entities.

This is a final, integrated version containing both basic and advanced schema
migration operations with conditional logic, based on the user's FS version.

Membra Open Development License (MODL) v1.0
Copyright (c) Rustam Kunafin 2025. All rights reserved.
Licensed under MODL v1.0. See LICENSE or https://cyberries.org/04_Resources/0440_Agreements/MODL.
"""

from typing import Dict, Any, List, Optional, Callable
import uuid

# --- Custom Exceptions for Operation Failures ---

class OperationError(Exception):
    """Base exception for errors during graph operations."""
    pass

class NodeNotFoundError(OperationError):
    """Raised when an operation targets a node that does not exist."""
    pass

class RelationNotFoundError(OperationError):
    """Raised when an operation targets a relation that does not exist."""
    pass

class DuplicateNodeError(OperationError):
    """Raised when attempting to add a node with an MUID that already exists."""
    pass

# --- Internal Helper Functions ---

def _find_node_index(graph_data: Dict[str, Any], muid: str) -> Optional[int]:
    """Finds the index of a node by its MUID."""
    for i, node in enumerate(graph_data.get('nodes', [])):
        if node.get('MUID') == muid:
            return i
    return None

def _find_relation_index(graph_data: Dict[str, Any], lid: str) -> Optional[int]:
    """Finds the index of a relation by its LID."""
    for i, relation in enumerate(graph_data.get('relations', [])):
        if relation.get('LID') == lid:
            return i
    return None

# --- Node Operations ---

def add_node(graph_data: Dict[str, Any], node_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Adds a new node to the graph.

    Args:
        graph_data: The dictionary representing the graph.
        node_data: A dictionary containing the data for the new node. Must include 'MUID'.

    Returns:
        The modified graph_data dictionary.

    Raises:
        DuplicateNodeError: If a node with the same MUID already exists.
        OperationError: If node_data is missing 'MUID'.
    """
    if 'MUID' not in node_data:
        raise OperationError("Cannot add node: 'MUID' is a required field.")
    
    muid = node_data['MUID']
    if _find_node_index(graph_data, muid) is not None:
        raise DuplicateNodeError(f"Node with MUID '{muid}' already exists.")

    if 'nodes' not in graph_data:
        graph_data['nodes'] = []
        
    graph_data['nodes'].append(node_data)
    return graph_data

def update_node(graph_data: Dict[str, Any], muid: str, updates: Dict[str, Any]) -> Dict[str, Any]:
    """
    Updates an existing node with new data.

    Args:
        graph_data: The dictionary representing the graph.
        muid: The MUID of the node to update.
        updates: A dictionary of fields to add or update in the node.

    Returns:
        The modified graph_data dictionary.

    Raises:
        NodeNotFoundError: If no node with the given MUID is found.
    """
    node_index = _find_node_index(graph_data, muid)
    if node_index is None:
        raise NodeNotFoundError(f"Node with MUID '{muid}' not found for update.")
    
    graph_data['nodes'][node_index].update(updates)
    return graph_data

def delete_node(graph_data: Dict[str, Any], muid: str) -> Dict[str, Any]:
    """
    Deletes a node from the graph.

    Args:
        graph_data: The dictionary representing the graph.
        muid: The MUID of the node to delete.

    Returns:
        The modified graph_data dictionary.

    Raises:
        NodeNotFoundError: If no node with the given MUID is found.
    """
    node_index = _find_node_index(graph_data, muid)
    if node_index is None:
        raise NodeNotFoundError(f"Node with MUID '{muid}' not found for deletion.")
        
    del graph_data['nodes'][node_index]
    return graph_data

def add_or_update_node(graph_data: Dict[str, Any], node_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Adds a new node if its MUID doesn't exist, or updates the existing node with the given data.

    Args:
        graph_data: The dictionary representing the graph.
        node_data: A dictionary containing the data for the node. Must include 'MUID'.

    Returns:
        The modified graph_data dictionary.

    Raises:
        OperationError: If node_data is missing 'MUID'.
    """
    if 'MUID' not in node_data:
        raise OperationError("Cannot add or update node: 'MUID' is a required field.")

    muid = node_data['MUID']
    node_index = _find_node_index(graph_data, muid)

    if node_index is not None:
        print(f"Node with MUID '{muid}' found. Updating existing node.")
        graph_data['nodes'][node_index].update(node_data)
    else:
        print(f"Node with MUID '{muid}' not found. Adding new node.")
        if 'nodes' not in graph_data:
            graph_data['nodes'] = []
        graph_data['nodes'].append(node_data)

    return graph_data

# --- Relation Operations ---

def add_relation(graph_data: Dict[str, Any], relation_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Adds a new relation to the graph.

    Args:
        graph_data: The dictionary representing the graph.
        relation_data: A dictionary containing the data for the new relation.

    Returns:
        The modified graph_data dictionary.
    """
    if 'relations' not in graph_data:
        graph_data['relations'] = []
        
    graph_data['relations'].append(relation_data)
    return graph_data

def update_relation(graph_data: Dict[str, Any], lid: str, updates: Dict[str, Any]) -> Dict[str, Any]:
    """
    Updates an existing relation with new data, identified by its LID.

    Args:
        graph_data: The dictionary representing the graph.
        lid: The LID of the relation to update.
        updates: A dictionary of fields to add or update in the relation.

    Returns:
        The modified graph_data dictionary.

    Raises:
        RelationNotFoundError: If no relation with the given LID is found.
    """
    relation_index = _find_relation_index(graph_data, lid)
    if relation_index is None:
        raise RelationNotFoundError(f"Relation with LID '{lid}' not found for update.")
        
    graph_data['relations'][relation_index].update(updates)
    return graph_data

def update_relations_by_query(graph_data: Dict[str, Any], query: Dict[str, Any], updates: Dict[str, Any]) -> Dict[str, Any]:
    """
    Finds all relations matching a query dictionary and applies updates to them.

    This is a powerful operation for batch updates where relations may not have
    a unique, simple ID.

    Args:
        graph_data: The dictionary representing the graph.
        query: A dictionary of key-value pairs to find matching relations.
        updates: A dictionary of key-value pairs to apply to matched relations.

    Returns:
        The modified graph_data dictionary.
    """
    if 'relations' not in graph_data:
        return graph_data

    updated_indices = []
    for i, relation in enumerate(graph_data['relations']):
        is_match = all(item in relation.items() for item in query.items())
        if is_match:
            relation.update(updates)
            updated_indices.append(i)
    
    if not updated_indices:
        print(f"Warning: No relations found matching query {query}. No changes made.")
    else:
        print(f"Updated {len(updated_indices)} relation(s) matching query.")
    
    return graph_data

# --- Advanced Schema Migration & Other Operations (RESTORED & INTEGRATED) ---

def add_node_field(graph_data: Dict[str, Any], field_name: str, default_value: Any = None) -> Dict[str, Any]:
    """Adds a new field to all nodes if it doesn't exist."""
    for node in graph_data.get('nodes', []):
        if field_name not in node:
            node[field_name] = default_value
    return graph_data

def copy_field(graph_data: Dict[str, Any], source_field: str, target_field: str, where: Optional[Dict[str, Any]] = None, entity_type: str = 'node') -> Dict[str, Any]:
    """Copies a value from a source field to a target field for entities matching a condition."""
    entities = graph_data.get(f"{entity_type}s", [])
    
    if where:
        field_to_check = where.get('field')
        condition = where.get('condition')
        if not field_to_check or not condition:
            raise OperationError("Invalid 'where' clause in copy_field operation.")
        
        if condition == 'is_not_uuid':
            # Filter entities based on the condition
            entities_to_process = [e for e in entities if not utils.is_uuid(e.get(field_to_check))]
        else:
            raise OperationError(f"Unsupported 'where' condition: {condition}")
    else:
        # If no 'where' clause, process all entities
        entities_to_process = entities
    
    for entity in entities_to_process:
        if source_field in entity:
            entity[target_field] = entity[source_field]
    return graph_data

def set_field_from_generated_uuid(graph_data: Dict[str, Any], target_field: str, where: Optional[Dict[str, Any]] = None, entity_type: str = 'node') -> Dict[str, Any]:
    """Sets a field to a newly generated UUID for entities matching a condition."""
    entities = graph_data.get(f"{entity_type}s", [])

    if where:
        field_to_check = where.get('field')
        condition = where.get('condition')
        if not field_to_check or not condition:
            raise OperationError("Invalid 'where' clause in set_field_from_generated_uuid operation.")
            
        if condition == 'is_not_uuid':
            entities_to_process = [e for e in entities if not utils.is_uuid(e.get(field_to_check))]
        else:
            raise OperationError(f"Unsupported 'where' condition: {condition}")
    else:
        entities_to_process = entities

    for entity in entities_to_process:
        entity[target_field] = str(uuid.uuid4())
    return graph_data

def add_lid_to_all_links(graph_data: Dict[str, Any], id_generator_func: Callable) -> Dict[str, Any]:
    """
    Scans all relations and adds a unique LID to those of class 'link' that lack one.

    This is a specialized operation for schema migration.

    Args:
        graph_data: The dictionary representing the graph.
        id_generator_func: A function that returns a new unique ID (e.g., from utils).

    Returns:
        The modified graph_data dictionary.
    """
    if 'relations' not in graph_data:
        return graph_data

    for relation in graph_data['relations']:
        # The logic from your FS version is preserved
        if relation.get('class') == 'link' and 'LID' not in relation:
            relation['LID'] = id_generator_func()
            
    return graph_data

def update_relation_endpoints_after_muid_change(graph_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Updates relation 'from_MUID' and 'to_MUID' based on node MUIDs that were migrated
    (where the old MUID is stored in the 'alias' field and the new MUID is in 'MUID').
    """
    if 'nodes' not in graph_data or 'relations' not in graph_data:
        print("Warning: Missing 'nodes' or 'relations' in graph data. Skipping relation endpoint update.")
        return graph_data

    # Build a mapping from old MUID (now in alias) to new MUID (UUID) for migrated nodes
    # This requires that the 'copy_field' operation (Step 2 in recipe) was already executed.
    muid_migration_map = {}
    for node in graph_data['nodes']:
        if 'MUID' in node and 'alias' in node and node['alias'] and node['MUID'] != node['alias']:
             # Assuming alias contains the OLD MUID and MUID contains the NEW UUID
            muid_migration_map[node['alias']] = node['MUID']

    if not muid_migration_map:
        print("No migrated nodes found (no old MUIDs in 'alias' field). No relation endpoints to update.")
        return graph_data

    updated_relations_count = 0
    for relation in graph_data['relations']:
        original_from_muid = relation.get('from_MUID')
        original_to_muid = relation.get('to_MUID')
        changes_made = False

        if original_from_muid in muid_migration_map:
            relation['from_MUID'] = muid_migration_map[original_from_muid]
            changes_made = True

        if original_to_muid in muid_migration_map:
            relation['to_MUID'] = muid_migration_map[original_to_muid]
            changes_made = True

        if changes_made:
            updated_relations_count += 1

    print(f"Updated endpoints for {updated_relations_count} relation(s).")
    return graph_data

# --- Graph-level Operations ---

def update_graph_properties(graph_data: Dict[str, Any], updates: Dict[str, Any]) -> Dict[str, Any]:
    """
    Updates top-level properties of the graph data object.

    This is useful for modifying fields like 'validation_issues'.

    Args:
        graph_data: The dictionary representing the graph.
        updates: A dictionary of top-level keys and values to update.

    Returns:
        The modified graph_data dictionary.
    """
    graph_data.update(updates)
    return graph_data

# This import is placed here to avoid circular dependency issues,
# as utils might need to be expanded in the future.
from . import utils
