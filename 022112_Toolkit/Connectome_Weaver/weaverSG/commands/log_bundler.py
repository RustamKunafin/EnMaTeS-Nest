"""
Обработчики команд 'bundle-log' и 'detach-log'.

Membra Open Development License (MODL) v1.0
Copyright (c) Rustam Kunafin 2025. All rights reserved.
Licensed under MODL v1.0. See LICENSE or https://cyberries.org/04_Resources/0440_Agreements/MODL.
"""
import os
import glob
from core.graph_io import get_lsg_filepath, load_graph, save_graph, load_yaml_header
from core.lsg_manager import TransactionManager

def process_bundle_log(args):
    """Обрабатывает команду 'bundle-log'."""
    sg_filepath = args.file
    lsg_filepath = get_lsg_filepath(sg_filepath)
    
    # Проверка на наличие архивных файлов
    directory, filename = os.path.split(lsg_filepath)
    base_name = filename.replace('_log.md', '')
    archive_pattern = os.path.join(directory, f"{base_name}_log_archive_*.md")
    if glob.glob(archive_pattern):
        raise FileExistsError("Ошибка: Обнаружены архивные файлы логов. Упаковка невозможна. Для транспортировки используйте команду 'package-sg' (в будущем) или соберите все файлы вручную.")

    if not os.path.exists(lsg_filepath):
        raise FileNotFoundError(f"Внешний лог-файл не найден: {lsg_filepath}. Упаковка невозможна.")

    sg_original_content, sg_data = load_graph(sg_filepath)
    if "log_history" in sg_data:
        raise ValueError("Ошибка: Внутри графа уже есть упакованный лог.")

    lsg_original_content, lsg_data = load_graph(lsg_filepath, is_log_file=True)
    
    print("Упаковка лога внутрь основного графа...")
    
    # Получаем метаданные родителя для корректной записи транзакции
    yaml_header = load_yaml_header(sg_original_content)
    parent_sg_muid = yaml_header.get('muid', 'UNKNOWN_PARENT_SG')
    has_real_title = 'title' in yaml_header
    filename_without_ext = os.path.splitext(os.path.basename(sg_filepath))[0]
    parent_sg_title = yaml_header.get('title', filename_without_ext)

    # Добавляем транзакцию об упаковке в сам лог ПЕРЕД его перемещением
    tm = TransactionManager("bundle_log_operation", lsg_filepath, sg_filepath, parent_sg_muid, parent_sg_title, has_real_title)
    bundle_change = {"action": "log_bundled", "details": {"message": "Log was bundled into the parent SG."}}
    tm.add_changes([bundle_change])
    
    # Вручную вызываем внутренний метод для обновления данных лога в памяти
    transaction_node = tm.create_transaction_node()
    final_lsg_data = tm._get_updated_lsg_data(lsg_data, transaction_node)
    
    # Помещаем обновленный лог внутрь основного графа
    sg_data["log_history"] = final_lsg_data
    
    # Сохраняем основной граф с упакованным логом
    save_graph(sg_data, sg_filepath, sg_original_content)
    
    # Удаляем старый внешний файл лога
    os.remove(lsg_filepath)
    print(f"Внешний лог {lsg_filepath} удален.")
    
    # Возвращаем None, так как транзакция уже обработана вручную
    return None, [], None


def process_detach_log(args):
    """Обрабатывает команду 'detach-log'."""
    sg_filepath = args.file
    lsg_filepath = get_lsg_filepath(sg_filepath)

    if os.path.exists(lsg_filepath):
        raise FileExistsError(f"Внешний лог-файл уже существует: {lsg_filepath}. Распаковка невозможна.")

    sg_original_content, sg_data = load_graph(sg_filepath)
    if "log_history" not in sg_data:
        raise ValueError("Ошибка: Внутри графа не найден упакованный лог.")

    print("Распаковка внутреннего лога во внешний файл...")
    lsg_data = sg_data.pop("log_history")

    # Получаем метаданные родителя для корректной записи транзакции
    yaml_header = load_yaml_header(sg_original_content)
    parent_sg_muid = yaml_header.get('muid', 'UNKNOWN_PARENT_SG')
    has_real_title = 'title' in yaml_header
    filename_without_ext = os.path.splitext(os.path.basename(sg_filepath))[0]
    parent_sg_title = yaml_header.get('title', filename_without_ext)

    # Добавляем транзакцию о распаковке
    tm = TransactionManager("detach_log_operation", lsg_filepath, sg_filepath, parent_sg_muid, parent_sg_title, has_real_title)
    detach_change = {"action": "log_detached", "details": {"message": "Log was detached into an external file."}}
    tm.add_changes([detach_change])
    
    tm.commit_and_save(final_graph_data=lsg_data, original_sg_content="", is_log_only=True)

    # Сохраняем основной граф уже без лога
    save_graph(sg_data, sg_filepath, sg_original_content)
    print("Внутренний лог успешно распакован.")

    return None, [], None
