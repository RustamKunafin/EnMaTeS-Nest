"""
Ядро системы. Содержит атомарные функции-операции для манипуляции данными графа в памяти.

Membra Open Development License (MODL) v1.0
Copyright (c) Rustam Kunafin 2025. All rights reserved.
Licensed under MODL v1.0. See LICENSE or https://cyberries.org/04_Resources/0440_Agreements/MODL.
"""
import uuid
from datetime import datetime
import os
from collections import Counter

# --- Вспомогательные функции ---

def _is_uuid(value: str) -> bool:
    """Проверяет, является ли строка валидным UUID."""
    try:
        uuid.UUID(str(value))
        return True
    except (ValueError, TypeError):
        return False

CONDITIONS = {"is_not_uuid": lambda node: not _is_uuid(node.get("MUID"))}

def _generate_lid() -> str:
    """Генерирует легковесный, локально-уникальный ID для link."""
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    random_part = os.urandom(2).hex() # 4 hex-символа
    return f"l_{timestamp}_{random_part}"

# --- Функции валидации (только возвращают данные) ---

def find_dangling_relations(graph_data: dict) -> list:
    """Возвращает список 'висячих' связей."""
    nodes_muids = {node['MUID'] for node in graph_data.get('nodes', [])}
    dangling_relations = []

    for relation in graph_data.get('relations', []):
        from_muid = relation.get('from_MUID')
        to_muid = relation.get('to_MUID')
        
        if from_muid and from_muid not in nodes_muids:
            dangling_relations.append({
                "issue_type": "dangling_relation_from",
                "relation_id": relation.get('MUID', relation.get('LID')),
                "from_MUID": from_muid,
                "missing_MUID": from_muid
            })
        if to_muid and to_muid not in nodes_muids:
            dangling_relations.append({
                "issue_type": "dangling_relation_to",
                "relation_id": relation.get('MUID', relation.get('LID')),
                "from_MUID": from_muid,
                "missing_MUID": to_muid
            })
    return dangling_relations

def find_duplicate_nodes(graph_data: dict) -> dict:
    """Возвращает словарь дублирующихся узлов (по MUID) и их количество."""
    muids = [node['MUID'] for node in graph_data.get('nodes', []) if 'MUID' in node]
    muid_counts = Counter(muids)
    return {muid: count for muid, count in muid_counts.items() if count > 1}

def find_duplicate_relations(graph_data: dict) -> list:
    """Находит дублирующиеся связи."""
    signatures = []
    for rel in graph_data.get('relations', []):
        signature = (
            rel.get('from_MUID'),
            rel.get('to_MUID'),
            rel.get('class'),
            rel.get('type')
        )
        signatures.append(signature)
    
    signature_counts = Counter(signatures)
    duplicates = []
    for sig, count in signature_counts.items():
        if count > 1:
            duplicates.append({
                "issue_type": "duplicate_relation",
                "count": count,
                "from_MUID": sig[0],
                "to_MUID": sig[1],
                "class": sig[2],
                "type": sig[3]
            })
    return duplicates

VALIDATION_CHECKS = {
    'dangling_relations': find_dangling_relations,
    'duplicate_nodes': find_duplicate_nodes,
    'duplicate_relations': find_duplicate_relations,
}

# --- Функции-операции (модифицирующие) ---

def add_node(graph_data: dict, params: dict) -> tuple[dict, dict | None]:
    node_data = params['node_data'].copy()
    muid = node_data.get('MUID')
    if any(node.get('MUID') == muid for node in graph_data.get('nodes', [])):
        print(f"Предупреждение: Узел с MUID {muid} уже существует. Пропускаем.")
        return graph_data, None
    graph_data.setdefault('nodes', []).append(node_data)
    change_record = {"action": "add_node", "entity_id": muid, "entity_type": "node", "new_state": node_data}
    print(f"Узел с MUID {muid} успешно добавлен.")
    return graph_data, change_record

def add_relation(graph_data: dict, params: dict) -> tuple[dict, dict]:
    relation_data = params['relation_data'].copy()
    relation_class = relation_data.get('class', 'link')
    relation_data['class'] = relation_class
    entity_id = None
    if relation_class == 'link':
        relation_data.setdefault('LID', _generate_lid())
        entity_id = relation_data['LID']
    elif relation_class == 'bind':
        if 'MUID' not in relation_data:
            raise ValueError("Для связи с class: 'bind' необходимо явно указать MUID.")
        entity_id = relation_data['MUID']
    graph_data.setdefault('relations', []).append(relation_data)
    change_record = {"action": "add_relation", "entity_id": entity_id, "entity_type": "relation", "new_state": relation_data}
    print(f"Операция: Добавление связи ({relation_class}) от {relation_data.get('from_MUID')} к {relation_data.get('to_MUID')}")
    return graph_data, change_record

def update_relation(graph_data: dict, params: dict) -> tuple[dict, dict | None]:
    identity, updates = params['identity'], params['updates']
    relation_to_update = next((rel for rel in graph_data.get('relations', []) if all(rel.get(k) == v for k, v in identity.items())), None)
    if not relation_to_update:
        print(f"Предупреждение: не найдено связей для обновления по {identity}.")
        return graph_data, None
    old_state = relation_to_update.copy()
    relation_to_update.update(updates)
    entity_id = relation_to_update.get("MUID") or relation_to_update.get("LID")
    change_record = {"action": "update_relation", "entity_id": entity_id, "entity_type": "relation", "old_state": old_state, "new_state": relation_to_update.copy()}
    print(f"Связь с ID '{entity_id}' успешно обновлена.")
    return graph_data, change_record

def promote_relation_op(graph_data: dict, params: dict) -> tuple[dict, dict]:
    lid_to_promote = params['lid']
    relation_found = next((rel for rel in graph_data.get('relations', []) if rel.get('LID') == lid_to_promote), None)
    if not relation_found:
        raise ValueError(f"Связь с LID '{lid_to_promote}' не найдена.")
    if relation_found.get('class') != 'link':
        raise ValueError(f"Связь с LID '{lid_to_promote}' уже не является 'link'.")
    old_state = relation_found.copy()
    new_muid = str(uuid.uuid4())
    relation_found['class'] = 'bind'
    relation_found['MUID'] = new_muid
    relation_found['legacy_LID'] = relation_found.pop('LID')
    change_record = {"action": "promote_relation", "entity_id": new_muid, "entity_type": "relation", "details": {"from_LID": lid_to_promote}, "old_state": old_state, "new_state": relation_found.copy()}
    print(f"Операция: Продвижение LID '{lid_to_promote}' до MUID '{new_muid}'")
    return graph_data, change_record

def add_node_field(graph_data: dict, params: dict) -> tuple[dict, list]:
    field_name, default_value = params['field_name'], params.get('default_value')
    changeset = []
    print(f"Операция: Добавление поля '{field_name}'...")
    for node in graph_data.get('nodes', []):
        if field_name not in node:
            old_state = node.copy()
            node[field_name] = default_value
            changeset.append({"action": "add_node_field", "entity_id": node['MUID'], "entity_type": "node", "details": {"field_name": field_name}, "old_state": old_state, "new_state": node.copy()})
    print(f"Поле '{field_name}' добавлено/проверено для {len(graph_data.get('nodes', []))} узлов.")
    return graph_data, changeset

def copy_field(graph_data: dict, params: dict) -> tuple[dict, list]:
    source_field, target_field = params['source_field'], params['target_field']
    condition_name = params.get('where', {}).get('condition')
    changeset = []
    print(f"Операция: Копирование из '{source_field}' в '{target_field}'...")
    if not condition_name or condition_name not in CONDITIONS:
        raise ValueError(f"Неизвестное или не указанное условие: {condition_name}")
    condition_func = CONDITIONS[condition_name]
    for node in graph_data.get('nodes', []):
        if condition_func(node) and source_field in node:
            old_state = node.copy()
            node[target_field] = node[source_field]
            changeset.append({"action": "copy_field", "entity_id": node['MUID'], "entity_type": "node", "details": {"source": source_field, "target": target_field}, "old_state": old_state, "new_state": node.copy()})
    print(f"Поле скопировано для {len(changeset)} узлов.")
    return graph_data, changeset

def set_field_from_generated_uuid(graph_data: dict, params: dict) -> tuple[dict, list]:
    target_field = params['target_field']
    condition_name = params.get('where', {}).get('condition')
    changeset = []
    print(f"Операция: Генерация UUID для поля '{target_field}'...")
    if not condition_name or condition_name not in CONDITIONS:
        raise ValueError(f"Неизвестное или не указанное условие: {condition_name}")
    condition_func = CONDITIONS[condition_name]
    for node in graph_data.get('nodes', []):
        if condition_func(node):
            old_state = node.copy()
            new_muid = str(uuid.uuid4())
            old_muid = node.get('MUID')
            node[target_field] = new_muid
            changeset.append({"action": "set_field_from_generated_uuid", "entity_id": old_muid, "entity_type": "node", "details": {"target_field": target_field, "new_muid": new_muid}, "old_state": old_state, "new_state": node.copy()})
    print(f"Новый UUID сгенерирован для {len(changeset)} узлов.")
    return graph_data, changeset

def add_lid_to_links(graph_data: dict, params: dict) -> tuple[dict, list]:
    """Добавляет LID ко всем связям типа 'link', у которых его еще нет."""
    changeset = []
    print("Операция: Проверка и добавление LID для связей 'link'...")
    for relation in graph_data.get('relations', []):
        if relation.get('class') == 'link' and 'LID' not in relation:
            old_state = relation.copy()
            relation['LID'] = _generate_lid()
            changeset.append({
                "action": "add_lid_to_links",
                "entity_id": relation['LID'],
                "entity_type": "relation",
                "old_state": old_state,
                "new_state": relation.copy()
            })
    print(f"LID добавлен для {len(changeset)} связей.")
    return graph_data, changeset

OPERATIONS_MAP = {
    'add_node': add_node,
    'add_relation': add_relation,
    'update_relation': update_relation,
    'add_node_field': add_node_field,
    'copy_field': copy_field,
    'set_field_from_generated_uuid': set_field_from_generated_uuid,
    'add_lid_to_links': add_lid_to_links,
}
