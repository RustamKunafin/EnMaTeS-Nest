"""
Обработчик команды 'validate'. Выполняет аудит графа и записывает отчет в сам файл графа.

Membra Open Development License (MODL) v1.0
Copyright (c) Rustam Kunafin 2025. All rights reserved.
Licensed under MODL v1.0. See LICENSE or https://cyberries.org/04_Resources/0440_Agreements/MODL.
"""
from core.operations import VALIDATION_CHECKS

def process_validation(graph_data: dict, args) -> tuple[dict, list, str]:
    """
    Выполняет все проверки валидации, выводит отчет в консоль 
    и добавляет/обновляет блок validation_issues в графе.
    """
    recipe_name = "validation_run"
    print(f"\nЗапуск полной валидации графа...")
    
    all_issues = []
    
    # Выполняем все проверки из карты VALIDATION_CHECKS
    for check_name, check_func in VALIDATION_CHECKS.items():
        issues = check_func(graph_data)
        if issues:
            print(f"Проверка '{check_name}' обнаружила проблемы.")
            # Гарантируем, что мы всегда добавляем список
            if isinstance(issues, list):
                all_issues.extend(issues)
            else: # Для find_duplicate_nodes, который возвращает dict
                all_issues.append({"issue_type": "duplicate_nodes", "duplicates": issues})
        else:
            print(f"Проверка '{check_name}': проблем не найдено.")
            
    # Формируем и выводим итоговый отчет
    if all_issues:
        print("\n--- ИТОГОВЫЙ ОТЧЕТ ВАЛИДАЦИИ ---")
        for issue in all_issues:
            print(f"  - {issue}")
        print("---------------------------------")
    else:
        print("\nИТОГ: Валидация прошла успешно. Проблем не обнаружено.")

    # Создаем запись об изменении (добавление/обновление блока ошибок)
    old_issues = graph_data.get("validation_issues")
    # Клонируем, чтобы избежать циклических ссылок при записи в лог
    graph_data_copy = graph_data.copy()
    graph_data_copy["validation_issues"] = all_issues
    
    changeset = [{
        "action": "validate_graph",
        "entity_id": "graph_meta",
        "entity_type": "graph",
        "details": {"issues_found": len(all_issues)},
        "old_state": {"validation_issues": old_issues},
        "new_state": {"validation_issues": all_issues}
    }]
    
    return graph_data_copy, changeset, recipe_name
