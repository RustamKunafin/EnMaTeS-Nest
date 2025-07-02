"""
Обработчик команды 'cleanup-backups'. Отвечает за удаление временных бэкапов.

Membra Open Development License (MODL) v1.0
Copyright (c) Rustam Kunafin 2025. All rights reserved.
Licensed under MODL v1.0. See LICENSE or https://cyberries.org/04_Resources/0440_Agreements/MODL.
"""
import os
import glob
import re

def process_cleanup_backups(args):
    """
    Находит и удаляет все временные страховочные бэкапы для указанного файла,
    используя точное совпадение по шаблону.
    """
    sg_filepath = args.file
    directory, filename_with_ext = os.path.split(sg_filepath)
    filename, ext = os.path.splitext(filename_with_ext)

    # Шаблон для поиска всех потенциальных бэкапов
    search_pattern = os.path.join(directory, f"{filename}.backup_*")
    
    # ИСПОЛЬЗУЕМ РЕГУЛЯРНОЕ ВЫРАЖЕНИЕ ДЛЯ ТОЧНОГО ПОИСКА
    # Оно ищет файлы, которые точно соответствуют нашему формату:
    # ИмяФайла.backup_имякоманды_ГГГГММДД_ЧЧММСС.md
    backup_regex = re.compile(
        re.escape(filename) + r"\.backup_[a-zA-Z-]+\_\d{8}_\d{6}" + re.escape(ext)
    )

    print(f"Поиск временных бэкапов для '{filename_with_ext}'...")
    
    # Сначала находим всех кандидатов, потом фильтруем по точному шаблону
    all_files = glob.glob(search_pattern)
    backup_files_to_delete = [f for f in all_files if backup_regex.search(os.path.basename(f))]
    
    if not backup_files_to_delete:
        print("Временные страховочные бэкапы для этого файла не найдены.")
        return None, [], None

    print("\nНайдены следующие бэкапы для удаления:")
    for f in backup_files_to_delete:
        print(f"  - {os.path.basename(f)}")
        
    # Запрос подтверждения у пользователя
    confirm = input("\nВы уверены, что хотите удалить эти файлы? (y/n): ").lower()
    
    if confirm == 'y':
        deleted_count = 0
        for f in backup_files_to_delete:
            try:
                os.remove(f)
                print(f"Удален: {os.path.basename(f)}")
                deleted_count += 1
            except Exception as e:
                print(f"Ошибка при удалении файла {f}: {e}")
        print(f"\nОчистка завершена. Удалено файлов: {deleted_count}.")
    else:
        print("\nОперация отменена пользователем.")

    # Эта команда не возвращает данные для транзакции
    return None, [], None
