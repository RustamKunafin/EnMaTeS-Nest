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
import uuid

class TransactionManager:
    """
    Управляет созданием и записью транзакций, а также сохранением основного графа.
    """
    def __init__(self, recipe_name: str, lsg_filepath: str, sg_filepath: str, parent_sg_muid: str, parent_sg_title: str, has_real_title: bool):
        self.recipe_name = recipe_name
        self.lsg_filepath = lsg_filepath
        self.sg_filepath = sg_filepath
        self.parent_sg_muid = parent_sg_muid
        self.parent_sg_title = parent_sg_title
        self.has_real_title = has_real_title
        self.changeset = []

    def add_changes(self, change_records: list):
        """Добавляет записи об изменениях в текущую транзакцию."""
        if change_records:
            self.changeset.extend(change_records)
            
    def _get_transaction_id(self) -> str:
        """Генерирует уникальный ID для транзакции."""
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        random_part = os.urandom(4).hex()
        return f"t_{timestamp}_{random_part}"

    def create_transaction_node(self) -> dict:
        """Создает узел транзакции на основе текущего changeset."""
        return {
            "MUID": self._get_transaction_id(),
            "type": "Transaction",
            "timestamp": datetime.now().isoformat(),
            "recipe_id": self.recipe_name,
            "changeset": self.changeset
        }

    def _get_updated_lsg_data(self, lsg_data: dict, transaction_node: dict) -> dict:
        """
        Чистая функция для обновления данных лога в памяти. Не читает и не пишет файлы.
        Возвращает обновленные данные лога.
        """
        # 1. Добавить узел транзакции
        lsg_data.setdefault("nodes", []).append(transaction_node)
        
        # 2. Обновить якоря истории
        for change in self.changeset:
            entity_id = change.get("entity_id")
            entity_type = change.get("entity_type")
            if not entity_id or not entity_type: continue
                
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
        
        return lsg_data

    def commit_and_save(self, final_graph_data: dict, original_sg_content: str):
        """
        Основной транзакционный метод для стандартных операций (validate, batch-modify).
        """
        if not self.changeset:
            print("Нет изменений для записи в лог.")
            # Важно: если изменений нет, но была валидация, основной граф все равно нужно сохранить,
            # так как в него мог быть добавлен блок validation_issues.
            save_graph(final_graph_data, self.sg_filepath, original_sg_content)
            return

        transaction_node = self.create_transaction_node()
        
        print(f"\nКоммит транзакции {transaction_node['MUID']}...")
        
        # Шаг 1: Загрузить, обновить и сохранить лог
        lsg_original_content, lsg_data = load_graph(self.lsg_filepath, is_log_file=True)

        if not lsg_original_content:
            title_to_display = f'"{self.parent_sg_title}"' if self.has_real_title else self.parent_sg_title
            new_description = f"Транзакционный лог для Семантического Графа {title_to_display} (MUID: {self.parent_sg_muid})."
            new_title = f"Log for {title_to_display}"
            header_data = {
                'yamlTemplate': 'membraLog', 'muid': str(uuid.uuid4()), 'title': new_title,
                'parent_SG_MUID': self.parent_sg_muid, 'lsg_version': "1.0",
                'description': new_description, 'tags': ['LSG', 'Log', 'Transaction', 'EnMaTeS'], 'publish': False
            }
            yaml_header = yaml.dump(header_data, sort_keys=False, allow_unicode=True)
            lsg_original_content = f"---\n{yaml_header}---\n"
        
        updated_lsg_data = self._get_updated_lsg_data(lsg_data, transaction_node)
        save_graph(updated_lsg_data, self.lsg_filepath, lsg_original_content)
        print("Транзакция успешно записана в лог.")
        
        # Шаг 2: Сохранить основной граф
        save_graph(final_graph_data, self.sg_filepath, original_sg_content)
        print(f"Основной граф сохранен в {self.sg_filepath}.")
