---
muid: 456599f0-c0d6-4f12-97d3-3e7a7058481a
title: EnMaTeS Overview v1.2
entityType: system
tier: system_level
description: "Высокоуровневый обзор системы EnMaTeS: философия, цели, ключевые архитектурные компоненты и принципы работы. Версия 1.2 добавляет ссылку на MethodologyGuide."
version: "1.2"
status: revised
tags: Membra, EnMaTeS
publish: true
---

# EnMaTeS (Entrepreneurial-Management-Technological System) - Обзор v1.2

## 1. Философия и Назначение Системы

**EnMaTeS** – это интегрированная, ИИ-ассистируемая система, предназначенная для структурированного управления корпоративными знаниями, поддержки процессов проектирования и повышения эффективности операционной деятельности предприятия.

**Основная цель EnMaTeS:** Создание динамичного, контекстно-осведомленного "цифрового двойника" или "коллективного разума" бизнеса. Это достигается через построение сети взаимосвязанных ИИ-ассистентов (реализованных как чаты или специализированные агенты/микросервисы), каждый из которых обладает глубокими знаниями в своем специфическом бизнес-домене. Основой этих знаний служат формализованные семантические графы.

**Для детального изучения практических воркфлоу и лучших практик применения системы обратитесь к `EnMaTeS_MethodologyGuide.md`.**

**Ключевые принципы EnMaTeS:**
-   **Модульность:** Система состоит из четко определенных, переиспользуемых компонентов (фреймворков, семантических графов, конфигураций).
-   **Семантическое Моделирование:** Знания представляются в виде семантических графов, обеспечивая глубокое понимание контекста и взаимосвязей.
-   **Управляемость Контекста ИИ:** Через структурированные фреймворк-промпты и конфигурации достигается предсказуемое и целенаправленное поведение ИИ-ассистентов.
-   **Итеративность:** Система и ее компоненты развиваются итерационно, от MVP к более сложным решениям.
-   **RAG (Retrieval Augmented Generation):** ИИ-ассистенты используют семантические графы для навигации и осмысленного извлечения деталей из больших объемов исходных текстовых документов.

## 2. Ключевые Архитектурные Компоненты EnMaTeS

Система EnMaTeS строится на основе иерархии артефактов, обеспечивающих ее функционирование и развитие:

1.  **`SMF (Semantic Modeling Framework)`**:
    *   Фундаментальный фреймворк, определяющий единый стандарт для структуры данных всех семантических графов.

2.  **`FPM (Framework Prompt Modes)`**:
    *   Определяют общие инструкции и набор команд для ИИ в зависимости от основного режима его работы (`Dev` или `Use`).

3.  **`FPS (Framework Prompt Specialization)`**:
    *   Описывают типовую роль и специфические компетенции ИИ-ассистента (например, "Архитектор EnMaTeS").

4.  **`PIC (Purpose and Introductory Context)`**:
    *   Задают специфический контекст для конкретной сессии ИИ-чата: цели, задачи, используемые данные.

5.  **`SI (System Instruction)`**:
    *   Набор компонентов (SMF, FPM, FPS, PIC), из которых собирается полная **Системная Инструкция (SI)** для ИИ-чата.

6.  **`SG (Semantic Graph)`**:
    *   Структурированные базы знаний по конкретным бизнес-доменам, созданные согласно SMF.

7.  **`SDA (Source Documents/Artifacts)`**:
    *   Исходные текстовые документы, которые служат источником деталей для RAG-механизма.

8.  **`SP (Starting Prompt)`**:
    *   Шаблоны стартовых промптов для инициализации ИИ-чатов.

9.  **`UM (User Manual)`**:
    *   Руководства для конечных пользователей, объясняющие, как взаимодействовать с ИИ-агентом.

10. **`IP (Initiation Package)`**:
    *   Набор компонентов (SG, SDA, SP, UM), который подготавливается для первоначального запуска чата в режиме `Use`.

11. **`ChatConfig (Chat Configuration)`**:
    *   Файл, описывающий, из каких компонентов собирается **SI** и **IP** для каждого конкретного ИИ-чата.

12. **`EnMaTeS NDF (Naming and Description Framework)`**:
    *   Стандарт именования и описания всех артефактов системы.

13. **`FP-Task (Specific Task Framework Prompt)`**:
    *   Специализированные фреймворк-промпты для выполнения ИИ конкретных узких задач.

14. **`EnMaTeS_MethodologyGuide.md`**: **(Новое)**
    *   Основное руководство по методологии, детализирующее воркфлоу, лучшие практики и принципы работы с компонентами.

15. **`EnMaTeS_ImprovementRoadmap.md`**: **(Новое)**
    *   "Живой" документ для отслеживания планов по развитию и усилению системы.

## 3. Принцип Работы (Высокоуровнево)

1.  **Разработка (с использованием FPM-Dev):** Архитектор EnMaTeS совместно с ИИ-ассистентом разработчика создает и развивает компоненты системы, включая семантические графы для бизнес-доменов.
2.  **Конфигурация Агента:** Для каждого бизнес-домена создается конфигурация (`ChatConfig`), объединяющая SMF, FPM-Use и другие необходимые компоненты.
3.  **Инициализация Агента:** При запуске ИИ-агент загружает свою Системную инструкцию (SI) и Пакет инициализации (IP).
4.  **Взаимодействие с Пользователем:** Конечный пользователь взаимодействует с агентом, который использует SG для понимания запроса и SDA для детализации ответов (RAG).

## 4. Потенциал и Развитие

EnMaTeS нацелена на создание экосистемы ИИ-ассистентов, которые могут обмениваться знаниями (через связанные семантические графы) и коллективно поддерживать различные аспекты деятельности предприятия. В будущем планируется развитие ИИ-оркестратора для управления взаимодействием между различными специализированными ИИ-агентами.