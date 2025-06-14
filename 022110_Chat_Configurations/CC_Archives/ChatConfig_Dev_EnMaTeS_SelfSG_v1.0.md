---
yamlTemplate: membraArt
muid: 18a115c6-3b69-4930-aed3-a3090316fea1
title: ChatConfig_Dev_EnMaTeS_SelfSG
entityType: artifact
artifactType: ai_chat_configuration
description: "Конфигурация Системной Инструкции (SI) для ИИ-чата разработчика, посвященного созданию и развитию Семантического Графа (SG) самой системы/методологии EnMaTeS."
version: "1.0"
status: active
tags: Membra, EnMaTeS
publish: true
---

# ChatConfig_Dev_EnMaTeS_SelfSG v1.0 (AI-Chat Configuration for EnMaTeS Self Semantic Graph Development)

version: 1.0 (ChatConfig_Dev_EnMaTeS_SelfSG)  
format: markdown  
usage: "Описывает компоненты, из которых собирается полная Системная Инструкция (SI) для ИИ-чата разработчика, работающего над Семантическим Графом (SG) системы EnMaTeS."

Название ИИ-чата: `AI-Chat_Dev_Architector_EnMaTeS_SelfSG_v0.1`

## 1. Назначение Чата / Агента:
-   **Режим работы ИИ:** Разработка (Development)
-   **Специализация ИИ:** Архитектор Системы EnMaTeS
-   **Основная цель сессии:** Создание и итерационное развитие `SG_EnMaTeS_SystemMethodology_vX.Y.md`.

## 2. Компоненты для Сборки Системной Инструкции (SI):

1.  **SMF (Semantic Modeling Framework):**
    *   Файл: `SMF_v2.2.md`
    *   Версия: 2.2
2.  **FPM (Framework Prompt Mode):**
    *   Файл: `FPM-Dev_v1.1.md`
    *   Версия: 1.1
3.  **FPS (Framework Prompt Specialization):**
    *   Файл: `FPS_EnMaTeSArchitect_v1.0.md`
    *   Версия: 1.0
4.  **PIC (Purpose and Introductory Context):**
    *   Файл: `PIC_EnMaTeS_SelfSG_Dev_v1.0.md`
    *   Версия: 1.0

## 3. Порядок Объединения Компонентов в SI:
Содержимое указанных выше файлов объединяется последовательно в следующем порядке для формирования полной Системной Инструкции, передаваемой ИИ:
1.  Содержимое `SMF_v2.2.md`
2.  Содержимое `FPM-Dev_v1.1.md`
3.  Содержимое `FPS_EnMaTeSArchitect_v1.0.md`
4.  Содержимое `PIC_EnMaTeS_SelfSG_Dev_v1.0.md`

## 4. Стартовый Промпт (SP) для Инициализации Чата:
-   Файл: `SP_Dev_EnMaTeS_SelfSG_Init_v1.0.md`
-   Версия: 1.0

## 5. Основной Рабочий Артефакт (Данные):
-   Семантический Граф: `SG_EnMaTeS_SystemMethodology_vX.Y.md` (создается и развивается в ходе сессии)
-   Исходные Документы (SDA): Тексты артефактов EnMaTeS (SMF, FPM, FPS, PIC, NDF, Overview и т.д.)