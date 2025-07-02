"""
Обработчик команды 'archive-log'.

Membra Open Development License (MODL) v1.0
Copyright (c) Rustam Kunafin 2025. All rights reserved.
Licensed under MODL v1.0. See LICENSE or https://cyberries.org/04_Resources/0440_Agreements/MODL.
"""
import os
from datetime import datetime
from core.graph_io import get_lsg_filepath, load_graph, load_yaml_header
from core.lsg_manager import TransactionManager

def process_archive_log(args):
    sg_filepath = args.file
    lsg_filepath = get_lsg_filepath(sg_filepath)

    sg_original_content, sg_data = load_graph(sg_filepath)
    if "log_history" in sg_data:
        raise ValueError("Ошибка: Лог является внутренним (bundled). Архивация невозможна. Сначала выполните 'detach-log'.")

    if not os.path.exists(lsg_filepath):
        raise FileNotFoundError(f"Активный лог-файл не найден: {lsg_filepath}. Архивация невозможна.")

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    archive_path = lsg_filepath.replace('_log.md', f'_log_archive_{timestamp}.md')
    print(f"Архивация текущего лога в: {archive_path}")
    os.rename(lsg_filepath, archive_path)

    print("Создание нового активного лога...")
    yaml_header = load_yaml_header(sg_original_content)
    parent_sg_muid = yaml_header.get('muid', 'UNKNOWN_PARENT_SG')
    has_real_title = 'title' in yaml_header
    filename_without_ext = os.path.splitext(os.path.basename(sg_filepath))[0]
    parent_sg_title = yaml_header.get('title', filename_without_ext)

    tm = TransactionManager("archive_log_operation", lsg_filepath, sg_filepath, parent_sg_muid, parent_sg_title, has_real_title)
    
    breadcrumb_change = {
        "action": "log_archived",
        "entity_id": "log_meta",
        "entity_type": "log_file",
        "details": {
            "archived_log_path": os.path.basename(archive_path),
            "message": "This is the start of a new log file. The previous history can be found in the specified archive."
        }
    }
    tm.add_changes([breadcrumb_change])
    
    # Так как мы создаем новый лог, передаем пустые данные.
    tm.commit_and_save(final_graph_data={}, original_sg_content="", is_log_only=True)

    # Возвращаем пустые значения, так как основной граф не менялся
    return None, [], None
