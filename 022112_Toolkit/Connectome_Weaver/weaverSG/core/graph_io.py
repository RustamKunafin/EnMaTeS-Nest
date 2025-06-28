"""
Модуль для низкоуровневых операций ввода/вывода: загрузка и сохранение семантических графов (SG и LSG).

Membra Open Development License (MODL) v1.0
Copyright (c) Rustam Kunafin 2025. All rights reserved.
Licensed under MODL v1.0. See LICENSE or https://cyberries.org/04_Resources/0440_Agreements/MODL.
"""
import json
import re
import os

def get_lsg_filepath(sg_filepath: str) -> str:
    """
    Генерирует путь к файлу лога (LSG) на основе пути к основному графу (SG).
    """
    directory, filename_with_ext = os.path.split(sg_filepath)
    filename, ext = os.path.splitext(filename_with_ext)
    lsg_filename = f"{filename}_log.md"
    return os.path.join(directory, lsg_filename)

def load_graph(filepath: str, is_log_file=False) -> tuple[str, dict]:
    """
    Загружает данные графа (SG или LSG) из markdown-файла.
    Возвращает кортеж (полное_содержимое_файла, данные_графа).
    В случае с LSG, если файл не найден, возвращает пустую структуру.
    """
    print(f"Загрузка графа из {filepath}...")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            match = re.search(r'```json\n(.*?)\n```', content, re.DOTALL)
            if match:
                json_str = match.group(1)
                return content, json.loads(json_str)
            else:
                raise ValueError("JSON блок не найден в файле.")
    except FileNotFoundError:
        if is_log_file:
            print(f"Файл лога {filepath} не найден. Будет создан новый.")
            return "", {"transactions": [], "history_anchors": [], "relations": []}
        raise FileNotFoundError(f"Файл не найден: {filepath}")
    except json.JSONDecodeError:
        raise ValueError(f"Ошибка декодирования JSON в файле: {filepath}")

def save_graph(graph_data: dict, filepath: str, original_content: str = "") -> None:
    """
    Сохраняет данные графа обратно в markdown-файл с канонической сортировкой.
    """
    print(f"Сохранение графа в {filepath}...")
    
    # Каноническая сортировка для консистентности
    if 'nodes' in graph_data:
      graph_data['nodes'] = sorted(graph_data['nodes'], key=lambda x: x.get('MUID', ''))
    if 'relations' in graph_data:
      # Сортировка по MUID или LID
      graph_data['relations'] = sorted(graph_data['relations'], key=lambda x: (x.get('MUID', x.get('LID', ''))))
    
    # Сортировка ключей внутри каждого объекта
    def sort_keys_recursive(obj):
        if isinstance(obj, dict):
            return {k: sort_keys_recursive(v) for k, v in sorted(obj.items())}
        if isinstance(obj, list):
            return [sort_keys_recursive(i) for i in obj]
        return obj

    sorted_graph_data = sort_keys_recursive(graph_data)

    pretty_json = json.dumps(sorted_graph_data, indent=2, ensure_ascii=False)
    new_json_block = f"```json\n{pretty_json}\n```"
    
    if original_content and '```json' in original_content:
        updated_content, num_replacements = re.subn(r'```json\n(.*?)\n```', new_json_block, original_content, flags=re.DOTALL)
    else: # Создание файла с нуля
        updated_content = f"# Semantic Graph\n\n{new_json_block}\n"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(updated_content)
