"""
Ядро системы. Содержит атомарные функции-операции для манипуляции данными графа в памяти.

Membra Open Development License (MODL) v1.0
Copyright (c) Rustam Kunafin 2025. All rights reserved.
Licensed under MODL v1.0. See LICENSE or https://cyberries.org/04_Resources/0440_Agreements/MODL.
"""
import uuid
from datetime import datetime
import os

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

# Все функции-операции здесь возвращают кортеж (graph_data, change_record или список change_records)

def add_node(graph_data: dict, params: dict) -> tuple[dict, dict | None]:
    """Добавляет новый узел в граф."""
    node_data = params['node_data'].copy()
    muid = node_data.get('MUID')
    print(f"Операция: Добавление узла с MUID {muid}...")
    
    if any(node.get('MUID') == muid for node in graph_data.get('nodes', [])):
        print(f"Предупреждение: Узел с MUID {muid} уже существует. Пропускаем.")
        return graph_data, None

    graph_data.setdefault('nodes', []).append(node_data)
    
    change_record = {
        "action": "add_node",
        "entity_id": muid,
        "entity_type": "node",
        "new_state": node_data
    }
    print("Узел успешно добавлен.")
    return graph_data, change_record

def add_relation(graph_data: dict, params: dict) -> tuple[dict, dict]:
    """Добавляет новую связь, автоматически обрабатывая LID/MUID."""
    relation_data = params['relation_data'].copy()
    relation_class = relation_data.get('class', 'link') # По умолчанию 'link'
    relation_data['class'] = relation_class

    entity_id = None
    if relation_class == 'link':
        if 'LID' not in relation_data:
            relation_data['LID'] = _generate_lid()
        entity_id = relation_data['LID']
    elif relation_class == 'bind':
        if 'MUID' not in relation_data:
            raise ValueError("Для связи с class: 'bind' необходимо явно указать MUID.")
        entity_id = relation_data['MUID']

    graph_data.setdefault('relations', []).append(relation_data)
    
    change_record = {
        "action": "add_relation",
        "entity_id": entity_id,
        "entity_type": "relation",
        "new_state": relation_data
    }
    print(f"Операция: Добавление связи ({relation_class}) от {relation_data.get('from_MUID')} к {relation_data.get('to_MUID')}")
    return graph_data, change_record

def update_relation(graph_data: dict, params: dict) -> tuple[dict, dict | None]:
    """Обновляет параметры существующей связи."""
    identity, updates = params['identity'], params['updates']
    print(f"Операция: Обновление связи по {identity}...")
    
    relation_to_update = None
    for relation in graph_data.get('relations', []):
        if all(relation.get(key) == value for key, value in identity.items()):
            relation_to_update = relation
            break
            
    if not relation_to_update:
        print("Предупреждение: не найдено связей для обновления.")
        return graph_data, None

    old_state = relation_to_update.copy()
    relation_to_update.update(updates)
    
    entity_id = relation_to_update.get("MUID") or relation_to_update.get("LID")
    change_record = {
        "action": "update_relation",
        "entity_id": entity_id,
        "entity_type": "relation",
        "old_state": old_state,
        "new_state": relation_to_update.copy()
    }
    
    print(f"Связь с ID '{entity_id}' успешно обновлена.")
    return graph_data, change_record

def promote_relation_op(graph_data: dict, params: dict) -> tuple[dict, dict]:
    """Операция для продвижения link до bind."""
    lid_to_promote = params['lid']
    relation_found = None
    for rel in graph_data.get('relations', []):
        if rel.get('LID') == lid_to_promote:
            relation_found = rel
            break
    
    if not relation_found:
        raise ValueError(f"Связь с LID '{lid_to_promote}' не найдена.")
        
    if relation_found.get('class') != 'link':
        raise ValueError(f"Связь с LID '{lid_to_promote}' уже не является 'link'.")

    old_state = relation_found.copy()

    # Трансформация
    new_muid = str(uuid.uuid4())
    relation_found['class'] = 'bind'
    relation_found['MUID'] = new_muid
    relation_found['legacy_LID'] = relation_found.pop('LID')

    change_record = {
        "action": "promote_relation",
        "entity_id": new_muid,
        "entity_type": "relation",
        "details": {"from_LID": lid_to_promote},
        "old_state": old_state,
        "new_state": relation_found.copy()
    }
    
    print(f"Операция: Продвижение LID '{lid_to_promote}' до MUID '{new_muid}'")
    return graph_data, change_record

def add_node_field(graph_data: dict, params: dict) -> tuple[dict, list]:
    """Добавляет новое поле ко всем узлам графа."""
    field_name = params['field_name']
    default_value = params.get('default_value', None)
    changeset = []
    
    print(f"Операция: Добавление поля '{field_name}'...")
    for node in graph_data.get('nodes', []):
        if field_name not in node:
            old_state = node.copy()
            node[field_name] = default_value
            changeset.append({
                "action": "add_node_field",
                "entity_id": node['MUID'],
                "entity_type": "node",
                "details": {"field_name": field_name},
                "old_state": old_state,
                "new_state": node.copy()
            })
    print(f"Поле '{field_name}' добавлено/проверено для {len(graph_data.get('nodes', []))} узлов.")
    return graph_data, changeset

def copy_field(graph_data: dict, params: dict) -> tuple[dict, list]:
    """Копирует значение из одного поля в другое для узлов, удовлетворяющих условию."""
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
            changeset.append({
                "action": "copy_field",
                "entity_id": node['MUID'],
                "entity_type": "node",
                "details": {"source": source_field, "target": target_field},
                "old_state": old_state,
                "new_state": node.copy()
            })
    print(f"Поле скопировано для {len(changeset)} узлов.")
    return graph_data, changeset

def set_field_from_generated_uuid(graph_data: dict, params: dict) -> tuple[dict, list]:
    """Устанавливает значение поля из нового UUID для узлов, удовлетворяющих условию."""
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
            node[target_field] = str(uuid.uuid4())
            changeset.append({
                "action": "set_field_from_generated_uuid",
                "entity_id": node['MUID'], # Старый MUID все еще здесь
                "entity_type": "node",
                "details": {"target_field": target_field},
                "old_state": old_state,
                "new_state": node.copy()
            })
    print(f"Новый UUID сгенерирован для {len(changeset)} узлов.")
    return graph_data, changeset


OPERATIONS_MAP = {
    'add_node': add_node,
    'add_relation': add_relation,
    'update_relation': update_relation,
    'add_node_field': add_node_field,
    'copy_field': copy_field,
    'set_field_from_generated_uuid': set_field_from_generated_uuid,
}
