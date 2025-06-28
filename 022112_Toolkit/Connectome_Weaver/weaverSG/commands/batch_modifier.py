"""
Обработчик команды 'batch-modify'. Читает рецепты и координирует выполнение пакетных операций.

Membra Open Development License (MODL) v1.0
Copyright (c) Rustam Kunafin 2025. All rights reserved.
Licensed under MODL v1.0. See LICENSE or https://cyberries.org/04_Resources/0440_Agreements/MODL.
"""
import yaml
import os
from core.operations import OPERATIONS_MAP

def process_batch_recipe(graph_data: dict, args) -> tuple[dict, list, str]:
    """
    Обрабатывает рецепт и возвращает (измененный_граф, набор_изменений, имя_рецепта).
    """
    recipe_path = args.recipe
    recipe_name = os.path.basename(recipe_path)
    print(f"\nОбработка рецепта: {recipe_path}")
    
    try:
        with open(recipe_path, 'r', encoding='utf-8') as f:
            recipe = yaml.safe_load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл рецепта не найден: {recipe_path}")

    print(f"Описание рецепта: {recipe.get('description', 'Без описания')}")
    
    changeset = []
    
    for step in recipe.get('steps', []):
        operation_name = step.get('operation')
        params = step.get('params', {})
        print(f"\nПрименение шага: '{operation_name}'")
        
        if operation_name in OPERATIONS_MAP:
            operation_func = OPERATIONS_MAP[operation_name]
            graph_data, change_record = operation_func(graph_data, params)
            if change_record:
                # Если операция возвращает список (как массовые операции), расширяем changeset
                if isinstance(change_record, list):
                    changeset.extend(change_record)
                else:
                    changeset.append(change_record)
        else:
            print(f"Предупреждение: Шаг '{operation_name}' неизвестен и будет пропущен.")

    return graph_data, changeset, recipe_name
