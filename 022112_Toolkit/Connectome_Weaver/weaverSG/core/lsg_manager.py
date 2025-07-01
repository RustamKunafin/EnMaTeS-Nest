"""
Менеджер транзакций. Отвечает за создание, управление и запись транзакций в Log Semantic Graph (LSG).

Membra Open Development License (MODL) v1.0
Copyright (c) Rustam Kunafin 2025. All rights reserved.
Licensed under MODL v1.0. See LICENSE or https://cyberries.org/04_Resources/0440_Agreements/MODL.
"""
from datetime import datetime
from .graph_io import load_graph, save_graph
import os
import yaml

class TransactionManager:
    """
    Управляет созданием и записью транзакций, а также сохранением основного графа.
    """
    def __init__(self, recipe_name: str, lsg_filepath: str, sg_filepath: str, parent_sg_muid: str):
        self.recipe_name = recipe_name
        self.lsg_filepath = lsg_filepath
        self.sg_filepath = sg_filepath
        self.parent_sg_muid = parent_sg_muid
        self.changeset = []

    def add_changes(self, change_records: list):
        if change_records:
            self.changeset.extend(change_records)
            
    def _get_transaction_id(self):
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        random_part = os.urandom(4).hex()
        return f"t_{timestamp}_{random_part}"

    def _update_lsg(self, transaction_node: dict):
        """Загружает, обновляет и сохраняет LSG."""
        lsg_original_content, lsg_data = load_graph(self.lsg_filepath, is_log_file=True)

        # Если это новый файл лога, создаем для него YAML-шапку
        if not lsg_original_content:
            header_data = {
                'yamlTemplate': 'membraLog',
                'muid': f"log_{self.parent_sg_muid}_{datetime.now().strftime('%Y%m%d')}",
                'title': f"Log for SG {self.parent_sg_muid}",
                'parent_SG_MUID': self.parent_sg_muid,
                'lsg_version': "1.0",
                'description': "Хронологический, транзакционный лог всех изменений, примененных к родительскому Семантическому Графу.",
                'tags': ['LSG', 'Log', 'Transaction', 'EnMaTeS'],
                'publish': False
            }
            yaml_header = yaml.dump(header_data, sort_keys=False)
            lsg_original_content = f"---\n{yaml_header}---\n"

        # 1. Добавить узел транзакции
        lsg_data.setdefault("nodes", []).append(transaction_node)
        
        # 2. Обновить якоря истории
        for change in self.changeset:
            entity_id = change.get("entity_id")
            entity_type = change.get("entity_type")
            if not entity_id or not entity_type:
                continue
                
            haid = f"ha_{entity_id}"
            
            anchor = next((a for a in lsg_data.get("nodes", []) if a.get("MUID") == haid), None)
            if not anchor:
                anchor = { "MUID": haid, "entity_ID": entity_id, "type": "HistoryAnchor", "entity_type": entity_type }
                lsg_data.setdefault("nodes", []).append(anchor)

            relation = {
                "class": "link",
                "LID": f"l_{haid}_to_{transaction_node['MUID']}",
                "from_MUID": haid,
                "to_MUID": transaction_node["MUID"],
                "type": "includes_change"
            }
            lsg_data.setdefault("relations", []).append(relation)

        # 3. Сохранить LSG
        save_graph(lsg_data, self.lsg_filepath, lsg_original_content)


    def commit_and_save(self, final_graph_data: dict, original_sg_content: str):
        """Создает узел транзакции, записывает его в LSG и только потом сохраняет основной SG."""
        if not self.changeset:
            print("Нет изменений для записи в лог.")
            return

        transaction_node = {
            "MUID": self._get_transaction_id(),
            "type": "Transaction",
            "timestamp": datetime.now().isoformat(),
            "recipe_id": self.recipe_name,
            "changeset": self.changeset
        }
        
        print(f"\nКоммит транзакции {transaction_node['MUID']}...")
        
        self._update_lsg(transaction_node)
        print("Транзакция успешно записана в лог.")
        
        save_graph(final_graph_data, self.sg_filepath, original_sg_content)
        print(f"Основной граф сохранен в {self.sg_filepath}.")
