---
muid: c5e2daef-7ab8-4b24-886c-a6bab452fb93
title: EnMaTeS NDF v1.2
entityType: artifact
artifactType: standard_procedure 
description: "Определяет стандарты и шаблоны для именования файлов, папок и описаний сущностей в рамках системы EnMaTeS. Версия 1.2 добавляет правила для новых типов артефактов (MethodologyGuide, ImprovementRoadmap, FPS_TesterAI, FPTask_AgentEvaluation) и уточняет существующие."
version: "1.2"
status: revised
tags: Membra, EnMaTeS
publish: true
---

# EnMaTeS Naming and Description Framework (NDF) v1.2

## 1. Общие Принципы Нейминга и Описаний

- **Ясность и Однозначность:** Названия должны быть понятны и не допускать множественных толкований.
- **Консистентность:** Использовать единые шаблоны и терминологию для однотипных сущностей во всем репозитории.
- **Краткость (для названий):** Названия файлов и ключевых идентификаторов должны быть достаточно короткими для удобства, но информативными.
- **Информативность (для описаний):** Внутренние описания артефактов (например, поле `description` или `usage` в YAML/Markdown заголовках) должны давать достаточно контекста о назначении сущности.
- **Версионирование:** Явно указывать версию (`v{{X}}.{{Y}}`) для артефактов, которые могут изменяться и развиваться (фреймворки, графы, конфигурации, мануалы). Версия указывается внутри документа, а не в имени файла.
- **Префиксы/Суффиксы:** Активно использовать префиксы для обозначения типа артефакта (например, `SMF_`, `FPM-`, `FPS_`, `PIC_`, `SG_`, `UM_`, `SP_`, `ChatConfig_`, `FPTask_`) и части имени для указания специфики (проект, домен, режим).
- **Структура Папок:** Следовать согласованной структуре папок репозитория (см. `EnMaTeS_Repository_Structure.md`).

## 2. Шаблоны для Ключевых Артефактов EnMaTeS

### 2.1. Semantic Modeling Framework (SMF)
-   **Название файла:** `SMF.md`
-   **Пример:** `SMF.md`
-   **Описание (`usage`):** "Semantic Modeling Framework. Определяет структуру узлов, связей, атрибутов для ВСЕХ семантических графов EnMaTeS."

### 2.2. Framework Prompt Mode (FPM)
-   **Название файла:** `FPM-{{Dev|Use}}.md`
-   **Примеры:**
    -   `FPM-Dev.md`
    -   `FPM-Use.md`
-   **Описание (`usage`):** "Framework Prompt Mode - `{{Development|Usage}}`. Содержит специфичные для режима `{{разработки|использования}}` ИИ инструкции: набор команд и общее поведение."

### 2.3. Framework Prompt Specialization (FPS)
-   **Общий шаблон:**
    -   Название файла: `FPS_{{RoleConcept}}.md`
    -   Примеры: `FPS_DomainExpert.md`, `FPS_EnMaTeSArchitect.md`, `FPS_TesterAI.md`
-   **Конкретная специализация (например, для проекта):**
    -   Название файла: `FPS_{{RoleName}}_{{Project/Context}}.md`
    -   Пример: `FPS_LegalAdvisor_ClientX.md`
-   **Дополнения (Addons):**
    -   Название файла: `FPS-Addon_{{AddonName}}.md`
    -   Пример: `FPS-Addon_LegalAdvisor.md`
-   **Описание (`usage`):** "Framework Prompt Specialization - `{{Описание Роли}}`. Определяет типовую роль ИИ и общие компетенции в этой специализации."

### 2.4. Purpose and Introductory Context (PIC)
-   **Название файла:** `PIC_{{Project/System}}_{{Purpose/Domain}}.md`
-   **Примеры:**
    -   `PIC_EnMaTeS_AgentDevFirebase.md`
    -   `PIC_ClientX_Legal.md`
-   **Описание (`usage` или `description`):** "Purpose and Introductory Context - `{{Описание}}`. Определяет специфику текущей задачи, проекта или конфигурации конкретного ИИ-агента/чата."

### 2.5. Semantic Graphs (SG)
-   **Название файла:** `SG_{{ProjectName}}_{{SubsystemName}}.md`
-   **Примеры:**
    -   `SG_ClientX_Legal.md`
    -   `SG_EnMaTeS_SystemMethodology.md`
-   **Атрибут `summary` внутри графа:** "Семантический граф, моделирующий `{{что моделирует}}` для проекта `{{Название Проекта}}` (`{{Подсистема, если применимо}}`), версия `{{X}}.{{Y}}`. Включает `{{ключевые типы информации}}`."

### 2.6. Source Documents/Artifacts (SDA)
-   **Название файла:** `{{DocTypePrefix}}_{{MeaningfulName}}.md` (или другой релевантный суффикс типа файла)
-   **Префиксы:** `ContractTmpl_`, `AppendixTmpl_`, `AddAgreementTmpl_`, `BlockTmpl_`, `Spec_`, `Guide_`, `Policy_`, `ProcessDesc_` и т.д.
-   **Примеры:**
    -   `ContractTmpl_MainProductManufacturing.md`
    -   `Spec_ContractPackage_List.md`

### 2.7. User Manuals (UM)
-   **Название файла:** `UM_ClientX_{{ProjectName}}_{{SubsystemName}}.md`
-   **Пример:** `UM_ClientX_Legal.md`
-   **Заголовок внутри документа:** "Руководство пользователя: Ваш ИИ-Ассистент по `{{чему}}` проекта '`{{Название Проекта}}`' (v{{X}}.{{Y}})"

### 2.8. Specific Task Framework Prompts (FP-Task)
-   **Название файла:** `FPTask_{{TaskName}}.md`
-   **Пример:** `FPTask_AgentEvaluation.md`, `FPTask_ArchimatePUML.md`
-   **Описание (`usage`):** "Framework Prompt - `{{Описание Задачи}}`. Системная инструкция для ИИ для выполнения конкретной узкоспециализированной задачи генерации или анализа."

### 2.9. System Overview & Methodology
-   **`EnMaTeS_Overview.md`**: Общее описание системы EnMaTeS.
-   **`EnMaTeS_NDF.md`**: Данный документ (Naming and Description Framework).
-   **`EnMaTeS_Repository_Structure.md`**: Описание структуры репозитория.
-   **`EnMaTeS_MethodologyGuide.md`**: **(Новое)** Детальное руководство по методологии.
-   **`EnMaTeS_ImprovementRoadmap.md`**: **(Новое)** Дорожная карта развития системы.

### 2.10. Starting Prompt (SP)
-   **Название файла:** `SP_{{TargetAudience}}_{{Project/System}}_{{Purpose/Step}}.md`
-   **Примеры:**
    -   `SP_Dev_EnMaTeS_SelfSG_Init.md`
    -   `SP_ClientX_Legal_Welcome.md`
-   **Описание (внутреннее, для разработчика):** "Starting Prompt - `{{Описание}}`. Шаблон стартового промпта для инициализации чата `{{с кем}}` по проекту `{{какому}}` для цели `{{какой}}`."

### 2.11. Chat Configurations (ChatConfig)
-   **Название файла:** `ChatConfig_{{Audience/Mode}}_{{Project/System}}_{{Purpose/Domain}}.md`
-   **Примеры:**
    -   `ChatConfig_Dev_EnMaTeS_AgentDevFirebase.md`
    -   `ChatConfig_ClientX_Legal.md`
-   **Описание (внутреннее):** "Chat Configuration - `{{Описание}}`. Описывает, из каких компонентов (SMF, FPM, FPS, PIC) собирается полная Системная Инструкция, а также из каких компонентов (SG, SDA, SP, UM) подготавливается **Пакет инициализации** (IP) для каждого конкретного ИИ-чата/агента.

## 3. Структура Папок Репозитория
См. документ `EnMaTeS_Repository_Structure.md`.

## 4. Применение NDF
-   **При создании нового артефакта/чата/промпта:** Обращаться к NDF для выбора корректного шаблона имени и структуры описания.
-   **При обновлении версий:** Отражать изменения во внутренних версиях артефактов.
-   **Для навигации и автоматизации:** Консистентные имена и структура облегчают поиск, управление и потенциальную автоматизацию работы с артефактами.