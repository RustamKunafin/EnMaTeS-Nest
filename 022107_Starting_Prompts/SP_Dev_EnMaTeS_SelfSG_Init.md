---
yamlTemplate: membraArt
muid: 3d9a80a9-fea2-4f1f-9970-43ad70e70844
title: SP_Dev_EnMaTeS_SelfSG_Init v1.0
entityType: artifact
artifactType: chat_initialization_prompt
description: "Стартовый промпт для инициализации ИИ-чата, посвященного СОЗДАНИЮ и РАЗВИТИЮ семантического графа самой системы/методологии EnMaTeS."
version: "1.0"
status: active
tags: Membra, EnMaTeS
publish: true
---

# SP_Dev_EnMaTeS_SelfSG_Init v1.0 (Starting Prompt - EnMaTeS Self Semantic Graph Development Initiation)

Привет, ИИ-Ассистент!

Мы начинаем новую сессию разработки, сфокусированную на создании и развитии Семантического Графа (SG) для самой системы/методологии EnMaTeS. Цели и задачи этой сессии подробно описаны в PIC (Purpose and Introductory Context), который является частью твоей системной инструкции.

**Твоя Системная Инструкция для этого чата собрана из следующих компонентов:**
1.  `SMF_v2.2.md`
2.  `FPM-Dev_v1.1.md`
3.  `FPS_EnMaTeSArchitect_v1.0.md`
4.  `PIC_EnMaTeS_SelfSG_Dev_v1.0.md`

Пожалуйста, подтверди, что ты работаешь в соответствии с этой полной Системной Инструкцией.

**Начальные данные и первая задача:**

1.  **Семантический Граф Проекта:** Мы будем создавать и наполнять `SG_EnMaTeS_SystemMethodology_v0.1.md`. На данный момент он может быть пустым или содержать только базовые узлы, которые мы определим. Если у тебя есть предыдущая версия этого графа из нашей сессии, пожалуйста, используй `context_restoration_protocol` для его загрузки. Если нет, мы начнем с нуля.
2.  **Исходные Документы/Артефакты (SDA):** В качестве SDA для построения `SG_EnMaTeS_SystemMethodology_v0.1.md` мы будем использовать тексты уже существующих артефактов EnMaTeS (например, `SMF_v2.2.md`, `FPM-Dev_v1.1.md`, `FPM-Use_v1.1.md`, `FPS_EnMaTeSArchitect_v1.0.md`, `FPS_DomainExpert_v1.0.md`, `PIC_...` (различные), `EnMaTeS_NDF_v1.1.md`, `EnMaTeS_Overview_v1.0.md`, `FP-ArchimatePUML_v1.4.md` и другие по мере их появления или обсуждения). Я буду предоставлять тебе их содержимое или ссылки на них по мере необходимости. Ты можешь использовать команду `RAG_procedure_for_development` для их анализа.
3.  **Наша первая задача:** Давай начнем с моделирования самого верхнего уровня EnMaTeS. Предложи, пожалуйста, какие ключевые узлы (согласно SMF) должны представлять основные категории артефактов, которые мы только что согласовали в нашей структуре репозитория (например, "Semantic Modeling Framework", "Framework Prompt Modes", "Framework Prompt Specialization", "Purpose and Introductory Context", "Semantic Graph", "Source Documents/Artifacts", "User Manual", "Specific Task Framework Prompt", "System Overview & Naming Docs", "Chat Initialization Prompt", "Chat Configuration"). Для каждого, если уже не указан в артефакте, предложи `MUID` (пока просто уникальный текстовый идентификатор, я заменю на UUID), `type`, `content`, `role`, `context` и краткое `description`. Используй команду `propose_graph_updates`.

Жду твоих предложений по начальной структуре `SG_EnMaTeS_SystemMethodology_v0.1.md`.