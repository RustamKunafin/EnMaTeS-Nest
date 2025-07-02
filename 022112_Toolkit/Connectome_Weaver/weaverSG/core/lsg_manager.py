# -*- coding: utf-8 -*-
"""
lsg_manager.py

This module defines the LSGManager class, the core engine for handling
transactional operations between a Semantic Graph (SG) and its corresponding
Log Semantic Graph (LSG). It ensures that every change is recorded reliably.

Membra Open Development License (MODL) v1.0
Copyright (c) Rustam Kunafin 2025. All rights reserved.
Licensed under MODL v1.0. See LICENSE or https://cyberries.org/04_Resources/0440_Agreements/MODL.
"""

from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple

# Import revised core modules
from . import graph_io
from . import operations
from . import utils

class LSGManager:
    """
    Manages all transactional operations for a Semantic Graph and its Log.

    This class encapsulates the logic for loading SG and LSG files,
    recording changes as transactions in the LSG, and saving both files safely.
    """

    def __init__(self, sg_path: Path):
        """
        Initializes the manager for a given Semantic Graph file.

        Args:
            sg_path (Path): The path to the main SG file.

        Raises:
            graph_io.GraphFileNotFoundError: If the main SG file does not exist.
        """
        self.sg_path = sg_path
        self.lsg_path = self._get_lsg_path_for_sg(sg_path)

        # Load main graph data
        self.sg_metadata, self.sg_data = graph_io.load_graph_from_file(self.sg_path)

        # Load or initialize log graph data
        try:
            self.lsg_metadata, self.lsg_data = graph_io.load_graph_from_file(self.lsg_path)
        except graph_io.GraphFileNotFoundError:
            print(f"Log file not found at {self.lsg_path}. A new one will be created.")
            self.lsg_metadata, self.lsg_data = self._initialize_lsg()

    def _get_lsg_path_for_sg(self, sg_path: Path) -> Path:
        """Determines the conventional path for the LSG file."""
        return sg_path.with_name(f"LSG_{sg_path.name}")

    def _initialize_lsg(self) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        """Creates the basic structure for a new, empty LSG."""
        metadata = {
            'title': f"Log for {self.sg_path.name}",
            'graph_version': "1.0",
            'description': "Transactional log for a Semantic Graph."
        }
        data = {
            'nodes': [],
            'relations': []
        }
        return metadata, data

    def _find_or_create_history_anchor(self, entity_id: str, entity_type: str) -> str:
        """
        Finds an existing HistoryAnchor for an entity or creates a new one.

        Args:
            entity_id (str): The ID of the entity (e.g., MUID or 'graph_meta').
            entity_type (str): The type of the entity (e.g., 'node', 'graph').

        Returns:
            The MUID of the found or created HistoryAnchor node.
        """
        # Search for an existing anchor
        for node in self.lsg_data.get('nodes', []):
            if node.get('type') == 'HistoryAnchor' and node.get('entity_ID') == entity_id:
                return node['MUID']
        
        # If not found, create a new one
        anchor_muid = f"ha_{entity_id.replace('-', '_')}"
        anchor_node = {
            "MUID": anchor_muid,
            "type": "HistoryAnchor",
            "entity_ID": entity_id,
            "entity_type": entity_type
        }
        self.lsg_data = operations.add_node(self.lsg_data, anchor_node)
        print(f"Created new History Anchor: {anchor_muid}")
        return anchor_muid

    def record_transaction(self, changeset: List[Dict[str, Any]], recipe_id: str) -> None:
        """
        Creates and records a new transaction in the LSG.

        Args:
            changeset (List[Dict[str, Any]]): A list of change objects describing the operation.
            recipe_id (str): An identifier for the operation/command being performed.
        """
        if not changeset:
            print("No changes to record. Skipping transaction.")
            return

        transaction_muid = utils.generate_transaction_id()
        timestamp = utils.datetime.now().isoformat()

        transaction_node = {
            "MUID": transaction_muid,
            "type": "Transaction",
            "timestamp": timestamp,
            "recipe_id": recipe_id,
            "changeset": changeset
        }
        
        # Add the transaction node to the log
        self.lsg_data = operations.add_node(self.lsg_data, transaction_node)

        # For simplicity, we currently link all transactions to a single graph-level anchor.
        # This can be expanded to link to entity-specific anchors if needed.
        # The first change's entity is used to find the anchor.
        first_change = changeset[0]
        entity_id = first_change.get('entity_id', 'graph_meta')
        entity_type = first_change.get('entity_type', 'graph')
        
        anchor_muid = self._find_or_create_history_anchor(entity_id, entity_type)

        # Create a relation from the anchor to the new transaction
        relation = {
            "LID": utils.generate_lid(),
            "from_MUID": anchor_muid,
            "to_MUID": transaction_muid,
            "type": "includes_change",
            "class": "link"
        }
        self.lsg_data = operations.add_relation(self.lsg_data, relation)
        print(f"Recorded transaction {transaction_muid} linked to anchor {anchor_muid}.")

    def save_changes(self) -> None:
        """
        Saves all changes to the SG and LSG files, after creating a backup.
        """
        print("Saving changes...")
        # 1. Create a backup of the original SG file before overwriting
        graph_io.create_backup(self.sg_path)

        # 2. Save the (potentially modified) main SG file
        graph_io.save_graph_to_file(self.sg_path, self.sg_metadata, self.sg_data)
        print(f"Successfully saved main graph to: {self.sg_path}")

        # 3. Save the updated LSG file
        graph_io.save_graph_to_file(self.lsg_path, self.lsg_metadata, self.lsg_data)
        print(f"Successfully saved log graph to: {self.lsg_path}")
