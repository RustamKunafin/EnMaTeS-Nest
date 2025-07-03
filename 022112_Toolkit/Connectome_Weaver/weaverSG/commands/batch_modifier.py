# -*- coding: utf-8 -*-
"""
batch_modifier.py

This module implements the 'batch-modify' command for weaverSG.
It processes a YAML recipe file containing a list of operations and applies them
sequentially to a Semantic Graph.

Membra Open Development License (MODL) v1.0
Copyright (c) Rustam Kunafin 2025. All rights reserved.
Licensed under MODL v1.0. See LICENSE or https://cyberries.org/04_Resources/0440_Agreements/MODL.
"""

import copy
from pathlib import Path
from typing import Dict, Any, List, Callable, Tuple

from ..core.lsg_manager import LSGManager
from ..core import operations
from ..core import utils

def _execute_operation(
    graph_data: Dict[str, Any], op_details: Dict[str, Any]
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """
    Executes a single operation from a recipe and generates its changeset.

    Args:
        graph_data: The current state of the graph data.
        op_details: A dictionary describing the operation from the recipe.

    Returns:
        A tuple containing:
        - The modified graph data.
        - The changeset dictionary for this operation.

    Raises:
        operations.OperationError: If the action is unknown or fails.
    """
    action = op_details.get('action')
    if not action:
        raise operations.OperationError("Operation missing 'action' field.")

    # A dispatch table mapping action strings to functions from the operations module.
    # This is cleaner and more scalable than a large if/elif/else block.
    OPERATION_HANDLERS: Dict[str, Callable] = {
        'add_node': operations.add_node,
        'update_node': operations.update_node,
        'delete_node': operations.delete_node,
        'add_relation': operations.add_relation,
        'update_relation': operations.update_relation,
        'add_lid_to_all_links': operations.add_lid_to_all_links,
        'update_relations_by_query': operations.update_relations_by_query,
    }

    handler = OPERATION_HANDLERS.get(action)
    if not handler:
        raise operations.OperationError(f"Unknown action: {action}")

    # Prepare arguments for the handler
    params = op_details.get('params', {})
    
    # Store old state for the changeset (good practice, though currently unused in simplified changeset)
    old_graph_data = copy.deepcopy(graph_data)

    # Execute the operation based on its specific signature
    if action == 'update_relations_by_query':
        query = params.get('query')
        updates = params.get('updates')
        if not query or not updates:
            raise operations.OperationError("Action 'update_relations_by_query' requires 'query' and 'updates' in params.")
        new_graph_data = handler(graph_data, query=query, updates=updates)
    elif action == 'add_lid_to_all_links':
        # This is a special case that doesn't fit the standard parameter model
        new_graph_data = handler(graph_data, utils.generate_lid)
    else:
        new_graph_data = handler(graph_data, **params)

    # For now, we create a simplified changeset. This can be enhanced later
    # to show detailed diffs for each operation if needed.
    changeset = {
        "action": action,
        "params": params,
        "details": f"Executed batch action: {action}"
    }
    
    return new_graph_data, changeset

def handle_batch_modify(file_path: Path, recipe_path: Path):
    """
    Handles the batch modification of an SG file based on a recipe.

    Args:
        file_path (Path): The path to the main SG file.
        recipe_path (Path): The path to the YAML recipe file.
    """
    print(f"Starting batch modification for '{file_path}' using recipe '{recipe_path}'.")

    try:
        # Load the recipe first to fail early if it's invalid
        recipe = utils.load_yaml_file(recipe_path)
        operations_list = recipe.get('operations')
        if not isinstance(operations_list, list):
            raise utils.RecipeFileError("Recipe must contain a list under the 'operations' key.")

        # Initialize the manager for the graph
        lsg_manager = LSGManager(file_path)
        
        all_changesets = []
        
        # Sequentially execute each operation from the recipe
        for i, op_details in enumerate(operations_list):
            print(f"  - Executing step {i+1}: {op_details.get('action')}...")
            
            # Pass the current state of the graph data to the executor
            new_sg_data, changeset = _execute_operation(lsg_manager.sg_data, op_details)
            
            # Update the manager's graph data with the new state
            lsg_manager.sg_data = new_sg_data
            all_changesets.append(changeset)

        # Record all accumulated changes as a single transaction
        if all_changesets:
            recipe_id = recipe.get('id', 'unknown_batch_recipe')
            lsg_manager.record_transaction(all_changesets, recipe_id=recipe_id)
            
            # Save all changes to disk
            lsg_manager.save_changes()
            print(f"\nBatch modification successful. {len(all_changesets)} operation(s) applied and logged.")
        else:
            print("\nRecipe contained no operations. No changes made.")

    except (utils.RecipeFileError, operations.OperationError, FileNotFoundError) as e:
        print(f"\nAn error occurred during batch modification: {e}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
