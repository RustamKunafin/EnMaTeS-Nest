"""
Главный файл-оркестратор, отвечающий за парсинг команд и управление транзакциями.

Membra Open Development License (MODL) v1.0
Copyright (c) Rustam Kunafin 2025. All rights reserved.
Licensed under MODL v1.0. See LICENSE or https://cyberries.org/04_Resources/0440_Agreements/MODL.
"""
import argparse
import os
from core.graph_io import load_graph, get_lsg_filepath, load_yaml_header
from core.lsg_manager import TransactionManager
from core.utils import create_backup
from commands.batch_modifier import process_batch_recipe
from commands.promote_handler import process_promote_relation
from commands.validator import process_validation

def main():
    """
    Главная функция-оркестратор для обработки команд CLI.
    Отвечает за последовательность действий: бэкап, выполнение, коммит.
    """
    parser = argparse.ArgumentParser(description="weaverSG: Инструмент для работы с семантическими графами EnMaTeS.")
    subparsers = parser.add_subparsers(dest='command', required=True, help='Доступные команды')

    # --- Команда batch-modify ---
    parser_batch = subparsers.add_parser('batch-modify', help='Выполнить пакетное изменение графа по файлу-рецепту.')
    parser_batch.add_argument('--recipe', required=True, help='Путь к YAML/JSON файлу с рецептом изменений.')
    parser_batch.add_argument('--file', required=True, help='Путь к файлу семантического графа (SG).')
    parser_batch.add_argument('--no-backup', action='store_true', help='Отключить автоматическое создание бэкапа.')
    parser_batch.set_defaults(process_func=process_batch_recipe)

    # --- Команда promote-relation ---
    parser_promote = subparsers.add_parser('promote-relation', help='Продвинуть связь "link" до "bind".')
    parser_promote.add_argument('--lid', required=True, help='LID связи, которую нужно продвинуть.')
    parser_promote.add_argument('--file', required=True, help='Путь к файлу семантического графа (SG).')
    parser_promote.add_argument('--no-backup', action='store_true', help='Отключить автоматическое создание бэкапа.')
    parser_promote.set_defaults(process_func=process_promote_relation)
    
    # --- Команда validate ---
    parser_validate = subparsers.add_parser('validate', help='Проверить граф на целостность и записать ошибки в файл.')
    parser_validate.add_argument('--file', required=True, help='Путь к файлу семантического графа (SG).')
    parser_validate.add_argument('--no-backup', action='store_true', help='Отключить автоматическое создание бэкапа.')
    parser_validate.set_defaults(process_func=process_validation)

    args = parser.parse_args()
    
    # --- Шаг 1: Подготовка ---
    original_content, graph_data = load_graph(args.file)
    lsg_filepath = get_lsg_filepath(args.file)
    yaml_header = load_yaml_header(original_content)
    parent_sg_muid = yaml_header.get('muid', 'UNKNOWN_PARENT_SG')

    # --- Шаг 2: Бэкап (по умолчанию) ---
    if not args.no_backup:
        create_backup(args.file, command=args.command)
    
    # --- Шаг 3: Выполнение команды и сбор изменений ---
    updated_graph, changeset, recipe_name = args.process_func(graph_data, args)
        
    # --- Шаг 4: Коммит транзакции и сохранение ---
    if changeset:
        tm = TransactionManager(recipe_name, lsg_filepath, args.file, parent_sg_muid)
        tm.add_changes(changeset)
        tm.commit_and_save(updated_graph, original_content)
        print(f"\nТранзакция успешно зафиксирована. Операция завершена для файла: {args.file}")
    else:
        print("\nНет изменений для фиксации. Операция завершена.")

if __name__ == '__main__':
    main()
