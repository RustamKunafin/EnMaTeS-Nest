"""
Менеджер транзакций. Отвечает за создание, управление и запись транзакций в Log Semantic Graph (LSG).

Membra Open Development License (MODL) v1.0
Copyright (c) Rustam Kunafin 2025. All rights reserved.
Licensed under MODL v1.0. See LICENSE or https://cyberries.org/04_Resources/0440_Agreements/MODL.
"""
from datetime import datetime
from .graph_io import load_graph, save_graph
import os

class TransactionManager:
    """
    Управляет созданием и записью транзакций, а также сохранением основного графа.
    """
    def __init__(self, recipe_name: str, lsg_filepath: str, sg_filepath: str):
        self.recipe_name = recipe_name
        self.lsg_filepath = lsg_filepath
        self.sg_filepath = sg_filepath
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

        # 1. Добавить узел транзакции
        lsg_data.setdefault("nodes", []).append(transaction_node)
        
        # 2. Обновить якоря истории
        for change in self.changeset:
            entity_id = change.get("entity_id")
            entity_type = change.get("entity_type")
            if not entity_id or not entity_type:
                continue
                
            haid = f"ha_{entity_id}"
            
            # Найти или создать якорь
            anchor = next((a for a in lsg_data.get("nodes", []) if a.get("MUID") == haid), None)
            if not anchor:
                anchor = {
                    "MUID": haid,
                    "entity_ID": entity_id,
                    "type": "HistoryAnchor",
                    "entity_type": entity_type
                }
                lsg_data.setdefault("nodes", []).append(anchor)

            # Создать связь от якоря к транзакции
            relation = {
                "class": "link", # Связи в логе всегда link
                "LID": f"l_ha_{haid}_to_{transaction_node['MUID']}",
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
        
        # Шаг 1: Записать лог. Это первая точка невозврата.
        self._update_lsg(transaction_node)
        print("Транзакция успешно записана в лог.")
        
        # Шаг 2: Только после успешной записи лога, сохранить основной граф.
        save_graph(final_graph_data, self.sg_filepath, original_sg_content)
        print(f"Основной граф сохранен в {self.sg_filepath}.")
