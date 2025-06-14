---
muid: e4f5a6b7-c8d9-e0f1-a2b3-c4d5e6f7g8h9
title: ChatConfig_Dev_t01_LegalDev v1.1
entityType: artifact
artifactType: ai_chat_configuration
description: "Конфигурация для запуска дочернего Dev-чата с ролью AgentDeveloper, предназначенного для разработки компонентов ИИ-агента LegalAdvisor для клиента t01."
version: "1.1"
status: revised
tags: Membra, EnMaTeS, ChatConfig, Development, t01, Legal
publish: true
---

# ChatConfig_Dev_t01_LegalDev v1.1

## 1. Назначение Чата / Агента:

-   **Название ИИ-чата:** `AI-Chat_Dev_AgentDeveloper_t01_Legal_v0.1` **(Изменено)**
-   **Режим работы ИИ:** Разработка (Development)
-   **Специализация ИИ:** Помощник Разработчика ИИ-Агентов (Agent Developer) **(Изменено)**
-   **Основная цель сессии:** Создание и итерационное развитие компонентов (SG, PIC_Use, SP_Use и т.д.) для Use-чата "LegalAdvisor" клиента t01.

## 2. Компоненты для Сборки Системной Инструкции (SI):

1.  **SMF (Semantic Modeling Framework):**
    *   Файл: `SMF.md` (v2.2)
2.  **FPM (Framework Prompt Mode):**
    *   Файл: `FPM-Dev.md` (v1.2)
3.  **FPS (Framework Prompt Specialization):**
    *   Файл: `FPS_AgentDeveloper.md` (v1.0) **(Изменено)**
4.  **PIC (Purpose and Introductory Context):**
    *   Файл: `PIC_Dev_t01_LegalDev.md` (v1.0)

## 3. Порядок Объединения Компонентов в SI:
Содержимое указанных выше файлов объединяется последовательно для формирования полной Системной Инструкции, передаваемой новому Dev-чату.

## 4. Пакет Инициализации (IP) для Данного Dev-чата:

-   **Семантические Графы (SG):**
    1.  `SG_EnMaTeS_SystemMethodology.md` (актуальная версия): Загружается как **мета-база знаний** о самой методологии.
    2.  (Опционально) `SG_t01_Legal.md`: Можно начать с пустого или базового графа как с **рабочей области** для разработки.
-   **Исходные Документы (SDA):**
    -   Все юридические документы клиента t01, которые будут служить основой для наполнения `SG_t01_Legal.md`.
-   **Стартовый Промпт (SP):**
    -   (Рекомендуется создать) `SP_Dev_t01_Legal_Init.md`: Стартовый промпт для инициализации этого дочернего Dev-чата.