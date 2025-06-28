"""
Набор общих, переиспользуемых утилит, таких как создание бэкапов.

Membra Open Development License (MODL) v1.0
Copyright (c) Rustam Kunafin 2025. All rights reserved.
Licensed under MODL v1.0. See LICENSE or https://cyberries.org/04_Resources/0440_Agreements/MODL.
"""
import shutil
import os
from datetime import datetime

def create_backup(filepath: str):
    """
    Создает бэкап файла с временной меткой.
    """
    directory, filename_with_ext = os.path.split(filepath)
    filename, ext = os.path.splitext(filename_with_ext)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_filename = f"{filename}.backup.{timestamp}{ext}"
    backup_filepath = os.path.join(directory, backup_filename)

    print(f"Создание бэкапа: {backup_filepath}")
    
    try:
        shutil.copy(filepath, backup_filepath)
        print("Бэкап успешно создан.")
    except Exception as e:
        print(f"ОШИБКА при создании бэкапа: {e}")
        raise
