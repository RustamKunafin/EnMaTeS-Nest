"""
Обработчик команды 'promote-relation'. Отвечает за логику 'продвижения' связи link до bind.

Membra Open Development License (MODL) v1.0
Copyright (c) Rustam Kunafin 2025. All rights reserved.
Licensed under MODL v1.0. See LICENSE or https://cyberries.org/04_Resources/0440_Agreements/MODL.
"""
from core.operations import promote_relation_op

def process_promote_relation(graph_data: dict, args) -> tuple[dict, list, str]:
    """
    Обрабатывает команду promote-relation и возвращает (измененный_граф, набор_изменений, имя_рецепта).
    """
    lid = args.lid
    recipe_name = f"promote_cmd_{lid}"
    print(f"\nОбработка команды promote-relation для LID: {lid}")
    
    params = {"lid": lid}
    updated_graph, change_record = promote_relation_op(graph_data, params)
    
    changeset = []
    if change_record:
        changeset.append(change_record)
        
    return updated_graph, changeset, recipe_name
