"""
Главный файл-оркестратор, отвечающий за парсинг команд и управление транзакциями.

Membra Open Development License (MODL) v1.0
Copyright (c) Rustam Kunafin 2025. All rights reserved.
Licensed under MODL v1.0. See LICENSE or https://cyberries.org/04_Resources/0440_Agreements/MODL.
"""
import argparse
import os
import sys
from core.graph_io import load_graph, get_lsg_filepath, load_yaml_header
from core.lsg_manager import TransactionManager
from core.utils import create_backup
from commands.batch_modifier import process_batch_recipe
from commands.promote_handler import process_promote_relation
from commands.validator import process_validation
from commands.log_archiver import process_archive_log
from commands.log_bundler import process_bundle_log, process_detach_log
from commands.cleaner import process_cleanup_backups

def main():
    """
    Главная функция-оркестратор для обработки команд CLI.
    """
    parser = argparse.ArgumentParser(description="weaverSG: Инструмент для работы с семантическими графами EnMaTeS.")
    subparsers = parser.add_subparsers(dest='command', required=True, help='Доступные команды')

    # --- Определение всех команд ---
    # Команда validate
    parser_validate = subparsers.add_parser('validate', help='Проверить граф на целостность и записать ошибки в файл.')
    parser_validate.add_argument('--file', required=True, help='Путь к файлу семантического графа (SG).')
    parser_validate.add_argument('--no-backup', action='store_true', help='Отключить автоматическое создание бэкапа.')
    parser_validate.set_defaults(process_func=process_validation)

    # Команда batch-modify
    parser_batch = subparsers.add_parser('batch-modify', help='Выполнить пакетное изменение графа по файлу-рецепту.')
    parser_batch.add_argument('--recipe', required=True, help='Путь к YAML/JSON файлу с рецептом изменений.')
    parser_batch.add_argument('--file', required=True, help='Путь к файлу семантического графа (SG).')
    parser_batch.add_argument('--no-backup', action='store_true', help='Отключить автоматическое создание бэкапа.')
    parser_batch.set_defaults(process_func=process_batch_recipe)

    # Команда promote-relation
    parser_promote = subparsers.add_parser('promote-relation', help='Продвинуть связь "link" до "bind".')
    parser_promote.add_argument('--lid', required=True, help='LID связи, которую нужно продвинуть.')
    parser_promote.add_argument('--file', required=True, help='Путь к файлу семантического графа (SG).')
    parser_promote.add_argument('--no-backup', action='store_true', help='Отключить автоматическое создание бэкапа.')
    parser_promote.set_defaults(process_func=process_promote_relation)
    
    # Команды управления логами
    parser_archive = subparsers.add_parser('archive-log', help='Архивировать текущий внешний файл лога.')
    parser_archive.add_argument('--file', required=True, help='Путь к основному SG, чей лог нужно архивировать.')
    parser_archive.add_argument('--no-backup', action='store_true', help='Отключить бэкап архивируемого лога.')
    parser_archive.set_defaults(process_func=process_archive_log)

    parser_bundle = subparsers.add_parser('bundle-log', help='Упаковать внешний лог внутрь основного SG.')
    parser_bundle.add_argument('--file', required=True, help='Путь к основному SG.')
    parser_bundle.add_argument('--no-backup', action='store_true', help='Отключить бэкап.')
    parser_bundle.set_defaults(process_func=process_bundle_log)

    parser_detach = subparsers.add_parser('detach-log', help='Распаковать внутренний лог в отдельный файл.')
    parser_detach.add_argument('--file', required=True, help='Путь к основному SG.')
    parser_detach.add_argument('--no-backup', action='store_true', help='Отключить бэкап.')
    parser_detach.set_defaults(process_func=process_detach_log)

    # Команды для очистки бэкапов
    parser_cleanup = subparsers.add_parser('cleanup-backups', help='Удалить все временные страховочные бэкапы для указанного SG.')
    parser_cleanup.add_argument('--file', required=True, help='Путь к основному SG, чьи бэкапы нужно очистить.')
    parser_cleanup.add_argument('--no-backup', action='store_true', help='Эта команда не создает бэкапы, флаг для совместимости.')
    parser_cleanup.set_defaults(process_func=process_cleanup_backups)
    
    args = parser.parse_args()
    
    # --- Оркестрация с обработкой ошибок ---
    try:
        # Шаг 1: Бэкап (по умолчанию, кроме команды очистки)
        if not args.no_backup and args.command != 'cleanup-backups':
            create_backup(args.file, command=args.command)
        
        # Шаг 2: Выполнение команды
        # Некоторые обработчики (управление логами, очистка) могут работать с файлами напрямую
        if args.command in ['archive-log', 'bundle-log', 'detach-log', 'cleanup-backups']:
            args.process_func(args)
        else:
            # Для остальных команд нужен полный транзакционный цикл
            original_content, graph_data = load_graph(args.file)
            updated_graph, changeset, recipe_name = args.process_func(graph_data, args)
            
            # Шаг 3: Коммит транзакции и сохранение (если были изменения)
            if changeset:
                lsg_filepath = get_lsg_filepath(args.file)
                yaml_header = load_yaml_header(original_content)
                parent_sg_muid = yaml_header.get('muid', 'UNKNOWN_PARENT_SG')
                has_real_title = 'title' in yaml_header
                filename_without_ext = os.path.splitext(os.path.basename(args.file))[0]
                parent_sg_title = yaml_header.get('title', filename_without_ext)
                
                tm = TransactionManager(recipe_name, lsg_filepath, args.file, parent_sg_muid, parent_sg_title, has_real_title)
                tm.add_changes(changeset)
                tm.commit_and_save(updated_graph, original_content)
                print(f"\nТранзакция успешно зафиксирована.")
            else:
                print(f"\nНет изменений для фиксации.")

        print(f"\nОперация '{args.command}' успешно завершена для файла: {args.file}")

    except (FileNotFoundError, ValueError, FileExistsError) as e:
        # Ловим ожидаемые ошибки и выводим чистое сообщение
        print(f"\n[ОШИБКА ОПЕРАЦИИ]: {e}", file=sys.stderr)
        sys.exit(1) # Завершаем программу с кодом ошибки
    except Exception as e:
        # Для всех остальных, непредвиденных ошибок, показываем полный traceback для отладки
        print(f"\n[КРИТИЧЕСКАЯ ОШИБКА]: Произошла непредвиденная ошибка.", file=sys.stderr)
        raise # Показываем полный traceback

if __name__ == '__main__':
    main()