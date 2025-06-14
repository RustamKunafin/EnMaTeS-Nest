---
muid: 18a115c6-3b69-4930-aed3-a3090316fea1
title: ChatConfig_Dev_EnMaTeS_SelfSG v1.1
entityType: artifact
artifactType: ai_chat_configuration
description: "Конфигурация Системной Инструкции (SI) для ИИ-чата разработчика ('мастер-чата'), посвященного созданию и развитию Семантического Графа (SG) самой системы/методологии EnMaTeS. Использует актуальные версии компонентов."
version: "1.1"
status: revised
tags: Membra, EnMaTeS
publish: true
---

# ChatConfig_Dev_EnMaTeS_SelfSG v1.1

version: 1.1 (ChatConfig_Dev_EnMaTeS_SelfSG)  
format: markdown  
usage: "Описывает компоненты, из которых собирается полная Системная Инструкция (SI) для 'мастер' Dev-чата, работающего над Семантическим Графом (SG) системы EnMaTeS."

Название ИИ-чата: `AI-Chat_Dev_Architector_EnMaTeS_SelfSG_v0.2` **(Изменено)**

## 1. Назначение Чата / Агента:
-   **Режим работы ИИ:** Разработка (Development)
-   **Специализация ИИ:** Архитектор Системы EnMaTeS
-   **Основная цель сессии:** Создание и итерационное развитие `SG_EnMaTeS_SystemMethodology_vX.Y.md`.

## 2. Компоненты для Сборки Системной Инструкции (SI):

1.  **SMF (Semantic Modeling Framework):**
    *   Файл: `SMF.md`
    *   Версия: 2.2
2.  **FPM (Framework Prompt Mode):**
    *   Файл: `FPM-Dev.md`
    *   Версия: 1.2 **(Обновлено)**
3.  **FPS (Framework Prompt Specialization):**
    *   Файл: `FPS_EnMaTeSArchitect.md`
    *   Версия: 1.0
4.  **PIC (Purpose and Introductory Context):**
    *   Файл: `PIC_EnMaTeS_SelfSG_Dev.md`
    *   Версия: 1.0

## 3. Порядок Объединения Компонентов в SI:
Содержимое указанных выше файлов объединяется последовательно для формирования полной Системной Инструкции, передаваемой ИИ.

## 4. Стартовый Промпт (SP) для Инициализации Чата:
-   Файл: `SP_Dev_EnMaTeS_SelfSG_Init_Restore.md`
-   Версия: 1.0
-   **Примечание:** Рекомендуется использовать новую форму стартового промпта, которая включает прикрепление файла с последним слепком SG и команду на его восстановление через `context_restoration_protocol`.

## 5. Основной Рабочий Артефакт (Данные):
-   Семантический Граф: `SG_EnMaTeS_SystemMethodology_vX.Y.md` (создается и развивается в ходе сессии)
-   Исходные Документы (SDA): Тексты всех актуальных артефактов EnMaTeS.