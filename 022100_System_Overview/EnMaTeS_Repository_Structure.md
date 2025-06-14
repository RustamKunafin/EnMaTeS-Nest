---
yamlTemplate: membraArt
muid: a308a937-d5bd-4408-8fa6-1bc181cc038c
title: EnMaTeS Repository Structure v1.2
entityType: artifact
artifactType: documentation
description: "Описание стандартной структуры папок и файлов для репозитория системы EnMaTeS. Обеспечивает консистентность и легкую навигацию по компонентам. Версия 1.1 добавляет расположение для новых системных и тестовых артефактов."
version: "1.2"
status: revised
tags: Membra, EnMaTeS
publish: true
---

# EnMaTeS Repository Structure v1.1

## 1. Назначение

Данный документ описывает стандартную иерархическую структуру папок для хранения всех артефактов системы EnMaTeS. Соблюдение этой структуры является обязательным для поддержания порядка, облегчения навигации, автоматизации процессов и обеспечения общего понимания расположения компонентов всеми участниками разработки.

## 2. Структура Репозитория

.  
├── 022100_System_Overview/ # Высокоуровневые документы, описывающие систему в целом  
│ ├── EnMaTeS NDF.md # Naming and Description Framework - правила именования  
│ ├── EnMaTeS Overview.md # Обзор философии, целей и компонентов системы  
│ ├── EnMaTeS_MethodologyGuide.md # (Новое) Детальное руководство по методологии и воркфлоу  
│ ├── EnMaTeS_ImprovementRoadmap.md # (Новое) Дорожная карта развития системы  
│ └── EnMaTeS_Repository_Structure.md # Этот самый документ  
│  
├── 022101_Semantic_Modeling_Framework/ # Основа основ - SMF  
│ └── SMF.md  
│  
├── 022102_Framework_Prompt_Modes/ # Режимы работы ИИ (Dev, Use)  
│ ├── FPM-Dev.md  
│ └── FPM-Use.md  
│  
├── 022103_Framework_Prompt_Specializations/ # Специализации (роли) ИИ  
│ ├── FPS_DomainExpert.md # Базовый FPS для эксперта по домену  
│ ├── FPS_EnMaTeSArchitect.md # FPS для ИИ-помощника архитектора EnMaTeS  
│ ├── FPS_AgentDeveloper.md # (Новое) FPS для ИИ-помощника разработчика агентов
│ ├── FPS_TesterAI.md # (Новое) FPS для ИИ-тестировщика  
│ └── Role_Addons/ # Дополнения к базовым ролям  
│    └── FPS-Addon_LegalAdvisor.md  
│  
├── 022104_Purposes_Introductory_Contexts/ # Контексты и цели для конкретных сессий (PIC)  
│ ├── PIC_Client_v01_Legal.md  
│ ├── PIC_EnMaTeS_AgentDevFirebase.md  
│ ├── PIC_Dev_t01_LegalDev.md # PIC для Dev-сессии по проекту t01
│ ├── PIC_EnMaTeS_SelfSG_Dev.md  
│ └── PIC_EnMaTeS_SelfSG_Use.md  
│  
├── 022105_Semantic_Graphs/ # Хранилище семантических графов (SG)  
│ ├── Project_EnMaTeS_Development/ # SG, относящиеся к разработке самой EnMaTeS  
│ │ └── SG_EnMaTeS_SystemMethodology.md  
│ └── Project_v01/ # SG, относящиеся к проекту v01  
│    └── SG_v01_Legal.md  
│  
├── 022106_Source_Documents_Artifacts/ # Хранилище исходных документов (SDA) для RAG  
│ └── Project_v01/  
│    └── Legal_Subsystem/ # Пример вложенной структуры для документов проекта  
│  
├── 022107_Starting_Prompts/ # Шаблоны стартовых промптов (SP)  
│ └── SP_Dev_EnMaTeS_SelfSG_Init.md  
│  
├── 022108_User_Manuals/ # Руководства для конечных пользователей (UM)  
│ └── UM_Example_Template.md # (Пример)  
│  
├── 022109_Specific_Task_Framework_Prompts/ # Промпты для выполнения узких, специфических задач  
│ ├── FPTask_AgentEvaluation.md # (Новое) FP-Task для оценки ответа агента  
│ └── FPTask_ArchimatePUML.md # (Пример)  
│  
└── 022110_Chat_Configurations/ # Конфигурации сборок ИИ-агентов  
   └── ChatConfig_Dev_EnMaTeS_SelfSG.md