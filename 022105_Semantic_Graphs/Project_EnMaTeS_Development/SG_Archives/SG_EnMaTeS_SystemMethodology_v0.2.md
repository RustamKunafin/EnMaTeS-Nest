---
muid: 224a333f-9483-4f33-b822-4e7c83576b5b
graph_version: "0.2"
creation_timestamp: "2025-06-05T10:00:00Z" # Placeholder, actual creation of SG 0.1
last_update_timestamp: "YYYY-MM-DDTHH:MM:SSZ" # Placeholder, will be set by user/system
dialog_session_id: "CURRENT_SESSION_ID_PLACEHOLDER" # Placeholder
summary: "Семантический граф, моделирующий систему и методологию EnMaTeS, включая ее ключевые компоненты, принципы, воркфлоу и направления развития. Версия 0.2."
---

```json
{
  "nodes": [
    {
        "MUID": "ENMATES_SYSTEM_ROOT",
        "timestamp": "2025-06-05T10:00:00Z",
        "turn_id": 1,
        "source": "ai",
        "type": "concept",
        "content": "EnMaTeS System/Methodology",
        "role": "anchor, stable, critical, context_setter",
        "context": "meta, design, strategy",
        "explicitness": "explicit",
        "weight": "high",
        "status": "accepted",
        "description": "The overarching EnMaTeS (Entrepreneurial-Management-Technological System) system and methodology for AI-assisted semantic modeling, knowledge management, and agent-based task execution. This node represents the entire EnMaTeS concept as described in EnMaTeS Overview v1.1. Further detailed in EnMaTeS Methodology Guide (proposed)."
    },
    {
        "MUID": "SMF_CATEGORY", "timestamp": "2025-06-05T10:00:01Z", "turn_id": 1, "source": "ai", "type": "concept", "content": "Semantic Modeling Framework (SMF) Category", "role": "stable, critical, context_setter", "context": "meta, logic, design", "explicitness": "explicit", "weight": "high", "status": "accepted", "description": "Represents the category for Semantic Modeling Frameworks (SMF) within EnMaTeS. SMF defines the core structure for semantic graphs. Specific SMF versions are instances of this concept. Detailed application described in EnMaTeS Methodology Guide."
    },
    {
        "MUID": "FPM_CATEGORY", "timestamp": "2025-06-05T10:00:02Z", "turn_id": 1, "source": "ai", "type": "concept", "content": "Framework Prompt Modes (FPM) Category", "role": "stable, critical", "context": "meta, ai_logic", "explicitness": "explicit", "weight": "high", "status": "accepted", "description": "Represents the category for Framework Prompt Modes (FPM) within EnMaTeS, defining general AI operational modes (e.g., Dev, Use). Detailed application described in EnMaTeS Methodology Guide."
    },
    {
        "MUID": "FPS_CATEGORY", "timestamp": "2025-06-05T10:00:03Z", "turn_id": 1, "source": "ai", "type": "concept", "content": "Framework Prompt Specialization (FPS) Category", "role": "stable, critical", "context": "meta, ai_logic", "explicitness": "explicit", "weight": "high", "status": "accepted", "description": "Represents the category for Framework Prompt Specializations (FPS) within EnMaTeS, defining AI roles and competencies. Includes base FPS and FPS-Addons. Detailed application described in EnMaTeS Methodology Guide."
    },
    {
        "MUID": "PIC_CATEGORY", "timestamp": "2025-06-05T10:00:04Z", "turn_id": 1, "source": "ai", "type": "concept", "content": "Purpose and Introductory Context (PIC) Category", "role": "stable, context_setter", "context": "meta, planning", "explicitness": "explicit", "weight": "high", "status": "accepted", "description": "Represents the category for Purpose and Introductory Context (PIC) documents, setting goals and context for AI sessions/agents. Detailed application described in EnMaTeS Methodology Guide."
    },
    {
        "MUID": "SG_CATEGORY", "timestamp": "2025-06-05T10:00:05Z", "turn_id": 1, "source": "ai", "type": "concept", "content": "Semantic Graph (SG) Category", "role": "stable, critical", "context": "meta, logic, design, content_management", "explicitness": "explicit", "weight": "high", "status": "accepted", "description": "Represents the category for Semantic Graphs (SG), the core knowledge structures in EnMaTeS, built according to SMF. Detailed application described in EnMaTeS Methodology Guide."
    },
    {
        "MUID": "SDA_CATEGORY", "timestamp": "2025-06-05T10:00:06Z", "turn_id": 1, "source": "ai", "type": "concept", "content": "Source Documents/Artifacts (SDA) Category", "role": "stable", "context": "meta, content_management", "explicitness": "explicit", "weight": "medium", "status": "accepted", "description": "Represents the category for Source Documents/Artifacts (SDA), external inputs for knowledge extraction and RAG. Detailed application described in EnMaTeS Methodology Guide."
    },
    {
        "MUID": "UM_CATEGORY", "timestamp": "2025-06-05T10:00:07Z", "turn_id": 1, "source": "ai", "type": "concept", "content": "User Manual (UM) Category", "role": "stable", "context": "meta, content_management", "explicitness": "explicit", "weight": "medium", "status": "accepted", "description": "Represents the category for User Manuals (UM) for EnMaTeS agents. Detailed application described in EnMaTeS Methodology Guide."
    },
    {
        "MUID": "STFP_FP_TASK_CATEGORY", "timestamp": "2025-06-05T10:00:08Z", "turn_id": 1, "source": "ai", "type": "concept", "content": "Specific Task Framework Prompt (STFP/FP-Task) Category", "role": "stable", "context": "meta, ai_logic", "explicitness": "explicit", "weight": "medium", "status": "accepted", "description": "Represents the category for Specific Task Framework Prompts (STFP) or FP-Task, for narrow AI tasks. Detailed application described in EnMaTeS Methodology Guide."
    },
    {
        "MUID": "SYS_OVERVIEW_NAMING_CATEGORY", "timestamp": "2025-06-05T10:00:09Z", "turn_id": 1, "source": "ai", "type": "concept", "content": "System Overview & Naming Docs Category", "role": "stable, context_setter", "context": "meta, content_management", "explicitness": "explicit", "weight": "medium", "status": "accepted", "description": "Represents the category for high-level system descriptions (e.g., EnMaTeS Overview) and naming conventions (e.g., NDF)."
    },
    {
        "MUID": "CIP_SP_CATEGORY", "timestamp": "2025-06-05T10:00:10Z", "turn_id": 1, "source": "ai", "type": "concept", "content": "Chat Initialization Prompt (CIP/SP) Category", "role": "stable", "context": "meta, ai_logic, communication", "explicitness": "explicit", "weight": "medium", "status": "accepted", "description": "Represents the category for Chat Initialization Prompts (CIP) or Starting Prompts (SP). Detailed application described in EnMaTeS Methodology Guide."
    },
    {
        "MUID": "CHAT_CONFIG_CATEGORY", "timestamp": "2025-06-05T10:00:11Z", "turn_id": 1, "source": "ai", "type": "concept", "content": "Chat Configuration (ChatConfig) Category", "role": "stable, critical", "context": "meta, ai_logic, technical", "explicitness": "explicit", "weight": "high", "status": "accepted", "description": "Represents the category for Chat Configuration artifacts, defining AI System Instruction assembly. Detailed application described in EnMaTeS Methodology Guide."
    },
    {
        "MUID": "IP_CATEGORY", "timestamp": "2025-06-05T10:00:12Z", "turn_id": 2, "source": "ai", "type": "concept", "content": "Initiation Package (IP) Category", "role": "stable", "context": "meta, ai_logic, technical", "explicitness": "explicit", "weight": "medium", "status": "accepted", "description": "Represents the category for Initiation Packages (IP), a set of components (SG, SDA, SP, UM) for starting a user-facing chat. Mentioned in EnMaTeS Overview. Detailed application described in EnMaTeS Methodology Guide."
    },
    {
        "MUID": "SI_CONCEPT", "timestamp": "2025-06-05T10:00:13Z", "turn_id": 2, "source": "ai", "type": "concept", "content": "System Instruction (SI)", "role": "stable, critical", "context": "meta, ai_logic", "explicitness": "explicit", "weight": "high", "status": "accepted", "description": "The complete set of instructions (SMF, FPM, FPS, PIC) provided to an AI agent to define its behavior, knowledge base, and goals. Defined in EnMaTeS Overview and ChatConfig."
    },
    {
        "MUID": "456599f0-c0d6-4f12-97d3-3e7a7058481a", "timestamp": "2025-06-05T10:01:00Z", "turn_id": 2, "source": "user", "type": "artifact", "content": "Обзор системы EnMaTeS v1.1", "role": "stable, critical, context_setter", "context": "meta, design, strategy", "explicitness": "explicit", "weight": "high", "status": "accepted", "description": "Высокоуровневый обзор системы EnMaTeS: философия, цели, ключевые архитектурные компоненты и принципы работы. Дополняется `EnMaTeS_MethodologyGuide_v1.0.md` (proposed) для детальных описаний процессов и практик. (From EnMaTeS Overview.md)", "artifactType": "system_description", "version": "1.1"
    },
    {
        "MUID": "c5e2daef-7ab8-4b24-886c-a6bab452fb93", "timestamp": "2025-06-05T10:01:01Z", "turn_id": 2, "source": "user", "type": "artifact", "content": "EnMaTeS NDF v1.1", "role": "stable, critical", "context": "meta, content_management", "explicitness": "explicit", "weight": "high", "status": "accepted", "description": "Определяет стандарты и шаблоны для именования файлов, папок и описаний сущностей в рамках системы EnMaTeS. (From EnMaTeS NDF.md)", "artifactType": "standard_procedure", "version": "1.1"
    },
    {
        "MUID": "f5bef63a-23fc-4057-ac62-483a9e0530e6", "timestamp": "2025-06-05T10:01:02Z", "turn_id": 2, "source": "user", "type": "artifact", "content": "SMF v2.2", "role": "stable, critical, context_setter", "context": "meta, logic, design", "explicitness": "explicit", "weight": "high", "status": "accepted", "description": "Semantic Modeling Framework. Определяет структуру узлов, связей, атрибутов для ВСЕХ семантических графов EnMaTeS. (From SMF.md)", "artifactType": "framework_definition", "version": "2.2" 
    },
     {
        "MUID": "429fb2c2-86d4-4b28-ae88-f94443b483e4", "timestamp": "2025-06-05T10:01:03Z", "turn_id": 2, "source": "user", "type": "artifact", "content": "FPM-Dev v1.1", "role": "stable, critical", "context": "meta, ai_logic, development_tool", "explicitness": "explicit", "weight": "high", "status": "accepted", "description": "Режим Фреймворк-Промпта ИИ для разработки EnMaTeS. Включает команды для создания артефактов и процедуры для анализа пользовательского фидбэка с целью улучшения системы. (From FPM-Dev.md)", "artifactType": "framework_prompt_module", "version": "1.1"
    },
    {
        "MUID": "7969c80a-1efb-489d-8bfd-978472b5fcb7", "timestamp": "2025-06-05T10:01:04Z", "turn_id": 2, "source": "user", "type": "artifact", "content": "FPM-Use v1.1", "role": "stable, critical", "context": "meta, ai_logic", "explicitness": "explicit", "weight": "high", "status": "accepted", "description": "Режим Фреймворк-Промпта ИИ для использования (клиентский). Включает процедуры RAG и механизмы для сбора пользовательского фидбэка. (From FPM-Use.md)", "artifactType": "framework_prompt_module", "version": "1.1"
    },
    {
        "MUID": "a0920c09-159c-40fc-8e05-76204e9de728", "timestamp": "2025-06-05T10:01:05Z", "turn_id": 2, "source": "user", "type": "artifact", "content": "FPS_DomainExpert v1.0", "role": "stable", "context": "meta, ai_logic", "explicitness": "explicit", "weight": "medium", "status": "accepted", "description": "Общий Фреймворк-Промпт Специализации для ИИ-ассистента, выступающего в роли Эксперта по произвольному Бизнес-Домену. (From FPS_DomainExpert.md)", "artifactType": "framework_prompt_module", "version": "1.0"
    },
    {
        "MUID": "4102aa13-8418-4a5e-88e1-1ce98c67474f", "timestamp": "2025-06-05T10:01:06Z", "turn_id": 2, "source": "user", "type": "artifact", "content": "FPS_EnMaTeSArchitect v1.0", "role": "stable, critical", "context": "meta, ai_logic, development_tool", "explicitness": "explicit", "weight": "high", "status": "accepted", "description": "Модуль Фреймворк-Промпта, определяющий специализацию ИИ как Архитектора системы EnMaTeS. (From FPS_EnMaTeSArchitect.md)", "artifactType": "framework_prompt_module", "version": "1.0"
    },
    {
        "MUID": "3bb00c7e-3706-4213-b545-fb9f41e77c8c", "timestamp": "2025-06-05T10:01:07Z", "turn_id": 2, "source": "user", "type": "artifact", "content": "FPS-Addon_LegalAdvisor v1.0", "role": "stable", "context": "meta, ai_logic, legal", "explicitness": "explicit", "weight": "medium", "status": "accepted", "description": "Дополнение к FPS_DomainExpertAI, конкретизирующее роль ИИ-ассистента как Юридического Консультанта. (From FPS-Addon_LegalAdvisor.md)", "artifactType": "framework_prompt_module_addon", "version": "1.0"
    },
    {
        "MUID": "e2afe7f4-9bb5-40b3-8b3e-e05d53324799", "timestamp": "2025-06-05T10:01:08Z", "turn_id": 2, "source": "user", "type": "artifact", "content": "PIC_Client_v01_Legal v1.0", "role": "stable", "context": "meta, planning, legal", "explicitness": "explicit", "weight": "medium", "status": "accepted", "description": "Определяет цель, специализацию, базу знаний и контекст для ИИ-агента, обслуживающего клиента 'Мебельная фабрика v01' по вопросам правовой подсистемы. (From PIC_Client_v01_Legal.md)", "artifactType": "agent_configuration_context", "version": "1.0"
    },
    {
        "MUID": "480dd136-bdf3-4266-8771-169953190f08", "timestamp": "2025-06-05T10:01:09Z", "turn_id": 2, "source": "user", "type": "artifact", "content": "PIC_EnMaTeS_SelfSG_Dev v1.0", "role": "stable, context_setter", "context": "meta, planning, development_tool", "explicitness": "explicit", "weight": "high", "status": "accepted", "description": "Определяет цель, задачи и вводный контекст для сессии ИИ-чата, посвященной СОЗДАНИЮ и РАЗВИТИЮ семантического графа самой системы/методологии EnMaTeS. (From PIC_EnMaTeS_SelfSG_Dev.md)", "artifactType": "project_context_definition", "version": "1.0"
    },
    {
        "MUID": "80e82615-3aae-4c33-8874-20428a354b99", "timestamp": "2025-06-05T10:01:10Z", "turn_id": 2, "source": "user", "type": "artifact", "content": "PIC_EnMaTeS_SelfSG_Use v1.0", "role": "stable, context_setter", "context": "meta, planning", "explicitness": "explicit", "weight": "medium", "status": "accepted", "description": "Определяет цель, задачи и вводный контекст для сессии ИИ-чата, посвященной ИСПОЛЬЗОВАНИЮ семантического графа самой системы/методологии EnMaTeS. (From PIC_EnMaTeS_SelfSG_Use.md)", "artifactType": "project_context_definition", "version": "1.0"
    },
    {
        "MUID": "3d9a80a9-fea2-4f1f-9970-43ad70e70844", "timestamp": "2025-06-05T10:01:11Z", "turn_id": 2, "source": "user", "type": "artifact", "content": "SP_Dev_EnMaTeS_SelfSG_Init v1.0", "role": "stable", "context": "meta, ai_logic, communication", "explicitness": "explicit", "weight": "medium", "status": "accepted", "description": "Стартовый промпт для инициализации ИИ-чата, посвященного СОЗДАНИЮ и РАЗВИТИЮ семантического графа самой системы/методологии EnMaTeS. (From SP_Dev_EnMaTeS_SelfSG_Init.md)", "artifactType": "chat_initialization_prompt", "version": "1.0"
    },
    {
        "MUID": "18a115c6-3b69-4930-aed3-a3090316fea1", "timestamp": "2025-06-05T10:01:12Z", "turn_id": 2, "source": "user", "type": "artifact", "content": "ChatConfig_Dev_EnMaTeS_SelfSG v1.0", "role": "stable, critical", "context": "meta, ai_logic, technical", "explicitness": "explicit", "weight": "high", "status": "accepted", "description": "Конфигурация Системной Инструкции (SI) для ИИ-чата разработчика, посвященного созданию и развитию SG самой системы EnMaTeS. (From ChatConfig_Dev_EnMaTeS_SelfSG_v1.0.md)", "artifactType": "ai_chat_configuration", "version": "1.0"
    },
    {
        "MUID": "CONCEPT_SMF", "timestamp": "2025-06-05T10:02:00Z", "turn_id": 2, "source": "derived_from_MUID:456599f0-c0d6-4f12-97d3-3e7a7058481a", "type": "concept", "content": "SMF (Semantic Modeling Framework)", "role": "stable, critical", "context": "meta, logic, design", "explicitness": "explicit", "weight": "high", "status": "accepted", "description": "Ключевой компонент EnMaTeS: фреймворк, определяющий единый стандарт для структуры семантических графов."
    },
    {
        "MUID": "CONCEPT_FPM", "timestamp": "2025-06-05T10:02:01Z", "turn_id": 2, "source": "derived_from_MUID:456599f0-c0d6-4f12-97d3-3e7a7058481a", "type": "concept", "content": "FPM (Framework Prompt Modes)", "role": "stable, critical", "context": "meta, ai_logic", "explicitness": "explicit", "weight": "high", "status": "accepted", "description": "Ключевой компонент EnMaTeS: определяет общие инструкции и команды для ИИ в разных режимах работы (Dev, Use)."
    },
    {
        "MUID": "CONCEPT_FPS", "timestamp": "2025-06-05T10:02:02Z", "turn_id": 2, "source": "derived_from_MUID:456599f0-c0d6-4f12-97d3-3e7a7058481a", "type": "concept", "content": "FPS (Framework Prompt Specialization)", "role": "stable, critical", "context": "meta, ai_logic", "explicitness": "explicit", "weight": "high", "status": "accepted", "description": "Ключевой компонент EnMaTeS: описывает типовую роль и специфические компетенции ИИ-ассистента."
    },
    {
        "MUID": "CONCEPT_PIC", "timestamp": "2025-06-05T10:02:03Z", "turn_id": 2, "source": "derived_from_MUID:456599f0-c0d6-4f12-97d3-3e7a7058481a", "type": "concept", "content": "PIC (Purpose and Introductory Context)", "role": "stable, context_setter", "context": "meta, planning", "explicitness": "explicit", "weight": "high", "status": "accepted", "description": "Ключевой компонент EnMaTeS: задает специфический контекст для сессии ИИ-чата."
    },
    {
        "MUID": "CONCEPT_SG", "timestamp": "2025-06-05T10:02:04Z", "turn_id": 2, "source": "derived_from_MUID:456599f0-c0d6-4f12-97d3-3e7a7058481a", "type": "concept", "content": "SG (Semantic Graph)", "role": "stable, critical", "context": "meta, logic, design", "explicitness": "explicit", "weight": "high", "status": "accepted", "description": "Ключевой компонент EnMaTeS: структурированные базы знаний по доменам."
    },
    {
        "MUID": "CONCEPT_SDA", "timestamp": "2025-06-05T10:02:05Z", "turn_id": 2, "source": "derived_from_MUID:456599f0-c0d6-4f12-97d3-3e7a7058481a", "type": "concept", "content": "SDA (Source Documents/Artifacts)", "role": "stable", "context": "meta, content_management", "explicitness": "explicit", "weight": "medium", "status": "accepted", "description": "Ключевой компонент EnMaTeS: исходные текстовые документы для RAG."
    },
    {
        "MUID": "CONCEPT_SP_CIP", "timestamp": "2025-06-05T10:02:06Z", "turn_id": 2, "source": "derived_from_MUID:456599f0-c0d6-4f12-97d3-3e7a7058481a", "type": "concept", "content": "SP/CIP (Starting Prompt / Chat Initialization Prompt)", "role": "stable", "context": "meta, ai_logic, communication", "explicitness": "explicit", "weight": "medium", "status": "accepted", "description": "Ключевой компонент EnMaTeS: шаблоны стартовых промптов для инициализации ИИ-чатов."
    },
    {
        "MUID": "CONCEPT_UM", "timestamp": "2025-06-05T10:02:07Z", "turn_id": 2, "source": "derived_from_MUID:456599f0-c0d6-4f12-97d3-3e7a7058481a", "type": "concept", "content": "UM (User Manual)", "role": "stable", "context": "meta, content_management", "explicitness": "explicit", "weight": "medium", "status": "accepted", "description": "Ключевой компонент EnMaTeS: руководства для конечных пользователей."
    },
    {
        "MUID": "CONCEPT_IP", "timestamp": "2025-06-05T10:02:08Z", "turn_id": 2, "source": "derived_from_MUID:456599f0-c0d6-4f12-97d3-3e7a7058481a", "type": "concept", "content": "IP (Initiation Package)", "role": "stable", "context": "meta, ai_logic, technical", "explicitness": "explicit", "weight": "medium", "status": "accepted", "description": "Ключевой компонент EnMaTeS: набор компонентов (SG, SDA, SP, UM) для запуска чата в режиме MFP-Use."
    },
    {
        "MUID": "CONCEPT_CHAT_CONFIG", "timestamp": "2025-06-05T10:02:09Z", "turn_id": 2, "source": "derived_from_MUID:456599f0-c0d6-4f12-97d3-3e7a7058481a", "type": "concept", "content": "ChatConfig (Chat Configuration)", "role": "stable, critical", "context": "meta, ai_logic, technical", "explicitness": "explicit", "weight": "high", "status": "accepted", "description": "Ключевой компонент EnMaTeS: файл, описывающий сборку SI и IP для ИИ-чата."
    },
    {
        "MUID": "CONCEPT_ENMATES_NDF", "timestamp": "2025-06-05T10:02:10Z", "turn_id": 2, "source": "derived_from_MUID:456599f0-c0d6-4f12-97d3-3e7a7058481a", "type": "concept", "content": "EnMaTeS NDF (Naming and Description Framework)", "role": "stable, critical", "context": "meta, content_management", "explicitness": "explicit", "weight": "high", "status": "accepted", "description": "Ключевой компонент EnMaTeS: стандарт именования и описания артефактов."
    },
    {
        "MUID": "CONCEPT_FP_TASK", "timestamp": "2025-06-05T10:02:11Z", "turn_id": 2, "source": "derived_from_MUID:456599f0-c0d6-4f12-97d3-3e7a7058481a", "type": "concept", "content": "FP-Task (Specific Task Framework Prompt)", "role": "stable", "context": "meta, ai_logic", "explicitness": "explicit", "weight": "medium", "status": "accepted", "description": "Ключевой компонент EnMaTeS: специализированные фреймворк-промпты для узких задач."
    },
    {
        "MUID": "PHILOSOPHY_ENMATES", "timestamp": "2025-06-05T10:03:00Z", "turn_id": 2, "source": "derived_from_MUID:456599f0-c0d6-4f12-97d3-3e7a7058481a", "type": "concept", "content": "EnMaTeS Philosophy", "role": "stable, context_setter", "context": "meta, strategy", "explicitness": "explicit", "weight": "high", "status": "accepted", "description": "Интегрированная, ИИ-ассистируемая система для структурированного управления корпоративными знаниями, поддержки проектирования и повышения эффективности операционной деятельности."
    },
    {
        "MUID": "GOAL_ENMATES", "timestamp": "2025-06-05T10:03:01Z", "turn_id": 2, "source": "derived_from_MUID:456599f0-c0d6-4f12-97d3-3e7a7058481a", "type": "goal", "content": "Primary Goal of EnMaTeS", "role": "stable, critical", "context": "meta, strategy", "explicitness": "explicit", "weight": "high", "status": "accepted", "description": "Создание динамичного, контекстно-осведомленного 'цифрового двойника' или 'коллективного разума' бизнеса через сеть ИИ-ассистентов на основе семантических графов."
    },
    {
        "MUID": "PRINCIPLE_MODULARITY", "timestamp": "2025-06-05T10:03:02Z", "turn_id": 2, "source": "derived_from_MUID:456599f0-c0d6-4f12-97d3-3e7a7058481a", "type": "concept", "content": "EnMaTeS Principle: Modularity", "role": "stable", "context": "meta, design", "explicitness": "explicit", "weight": "medium", "status": "accepted", "description": "Система состоит из четко определенных, переиспользуемых компонентов."
    },
    {
        "MUID": "PRINCIPLE_SEMANTIC_MODELING", "timestamp": "2025-06-05T10:03:03Z", "turn_id": 2, "source": "derived_from_MUID:456599f0-c0d6-4f12-97d3-3e7a7058481a", "type": "concept", "content": "EnMaTeS Principle: Semantic Modeling", "role": "stable, critical", "context": "meta, logic, design", "explicitness": "explicit", "weight": "high", "status": "accepted", "description": "Знания представляются в виде семантических графов для глубокого понимания контекста."
    },
    {
        "MUID": "PRINCIPLE_CONTEXT_MANAGEMENT", "timestamp": "2025-06-05T10:03:04Z", "turn_id": 2, "source": "derived_from_MUID:456599f0-c0d6-4f12-97d3-3e7a7058481a", "type": "concept", "content": "EnMaTeS Principle: AI Context Management", "role": "stable, critical", "context": "meta, ai_logic", "explicitness": "explicit", "weight": "high", "status": "accepted", "description": "Управляемость контекста ИИ через структурированные фреймворк-промпты и конфигурации."
    },
    {
        "MUID": "PRINCIPLE_ITERATIVITY", "timestamp": "2025-06-05T10:03:05Z", "turn_id": 2, "source": "derived_from_MUID:456599f0-c0d6-4f12-97d3-3e7a7058481a", "type": "concept", "content": "EnMaTeS Principle: Iterativity", "role": "stable", "context": "meta, workflow, project_management", "explicitness": "explicit", "weight": "medium", "status": "accepted", "description": "Система и ее компоненты развиваются итерационно."
    },
    {
        "MUID": "PRINCIPLE_RAG", "timestamp": "2025-06-05T10:03:06Z", "turn_id": 2, "source": "derived_from_MUID:456599f0-c0d6-4f12-97d3-3e7a7058481a", "type": "concept", "content": "EnMaTeS Principle: RAG (Retrieval Augmented Generation)", "role": "stable", "context": "meta, ai_logic, technical", "explicitness": "explicit", "weight": "medium", "status": "accepted", "description": "ИИ-ассистенты используют СГ для навигации и извлечения деталей из исходных документов."
    },
    {
        "MUID": "SMF_NODE_DEF", "timestamp": "2025-06-05T10:04:00Z", "turn_id": 2, "source": "derived_from_MUID:f5bef63a-23fc-4057-ac62-483a9e0530e6", "type": "concept", "content": "SMF Node Definition", "role": "stable, critical", "context": "meta, logic, design", "explicitness": "explicit", "weight": "high", "status": "accepted", "description": "Defines the structure and attributes of nodes in EnMaTeS semantic graphs (MUID, timestamp, turn_id, source, type, content, role, context, explicitness, weight, status, description)."
    },
    {
        "MUID": "SMF_RELATION_DEF", "timestamp": "2025-06-05T10:04:01Z", "turn_id": 2, "source": "derived_from_MUID:f5bef63a-23fc-4057-ac62-483a9e0530e6", "type": "concept", "content": "SMF Relation Definition", "role": "stable, critical", "context": "meta, logic, design", "explicitness": "explicit", "weight": "high", "status": "accepted", "description": "Defines the structure and attributes of relations in EnMaTeS semantic graphs (from_MUID, to_MUID, type, weight, context, label)."
    },
    {
        "MUID": "SMF_NODE_TYPES_LIST", "timestamp": "2025-06-05T10:04:02Z", "turn_id": 2, "source": "derived_from_MUID:f5bef63a-23fc-4057-ac62-483a9e0530e6", "type": "concept", "content": "SMF Node Types", "role": "stable, critical", "context": "meta, logic, design", "explicitness": "explicit", "weight": "high", "status": "accepted", "description": "List of defined node types: concept, goal, problem, solution, actor, process, signal, artifact, hypothesis, metric, requirement, constraint, question, answer, finding, assumption, feature, placeholder, artifact_template_fragment, flow."
    },
    {
        "MUID": "SMF_RELATION_TYPES_LIST", "timestamp": "2025-06-05T10:04:03Z", "turn_id": 2, "source": "derived_from_MUID:f5bef63a-23fc-4057-ac62-483a9e0530e6", "type": "concept", "content": "SMF Relation Types", "role": "stable, critical", "context": "meta, logic, design", "explicitness": "explicit", "weight": "high", "status": "accepted", "description": "List of defined relation types (leads_to, depends_on, refines, etc.)."
    },
    {
        "MUID": "SMF_NODE_ROLES_LIST", "timestamp": "2025-06-05T10:04:04Z", "turn_id": 2, "source": "derived_from_MUID:f5bef63a-23fc-4057-ac62-483a9e0530e6", "type": "concept", "content": "SMF Node Roles", "role": "stable", "context": "meta, logic, design", "explicitness": "explicit", "weight": "medium", "status": "accepted", "description": "List of defined semantic node roles (anchor, volatile, stable, critical, etc.)."
    },
    {
        "MUID": "SMF_CONTEXTS_LIST", "timestamp": "2025-06-05T10:04:05Z", "turn_id": 2, "source": "derived_from_MUID:f5bef63a-23fc-4057-ac62-483a9e0530e6", "type": "concept", "content": "SMF Contexts of Attention", "role": "stable", "context": "meta, logic, design", "explicitness": "explicit", "weight": "medium", "status": "accepted", "description": "List of defined contexts of attention / semantic projections (logic, strategy, design, workflow, etc.)."
    },
    {
        "MUID": "SMF_GRAPH_METADATA_DEF", "timestamp": "2025-06-05T10:04:06Z", "turn_id": 2, "source": "derived_from_MUID:f5bef63a-23fc-4057-ac62-483a9e0530e6", "type": "concept", "content": "SMF Graph Metadata Definition", "role": "stable", "context": "meta, logic, design", "explicitness": "explicit", "weight": "medium", "status": "accepted", "description": "Defines metadata for graph snapshots (graph_version, creation_timestamp, etc.)."
    },
    {
        "MUID": "WF_CREATE_NEW_USER_CHAT", "timestamp": "2025-06-05T11:00:00Z", "turn_id": 5, "source": "ai", "type": "process", "content": "Workflow: Creating a New User-Facing Chat for a New Business Domain", "role": "stable, critical", "context": "workflow, meta, project_management, design", "explicitness": "explicit", "weight": "high", "status": "accepted", "description": "The overarching workflow for setting up a development environment and then developing and configuring a user-facing EnMaTeS chat agent for a new business domain. Consists of three main stages."
    },
    {
        "MUID": "WF_STAGE_I_DEV_SETUP", "timestamp": "2025-06-05T11:00:01Z", "turn_id": 5, "source": "ai", "type": "process", "content": "Stage I: Setup Dev Chat Environment for New Domain", "role": "stable", "context": "workflow, meta, project_management, development_tool", "explicitness": "explicit", "weight": "high", "status": "accepted", "description": "First stage of creating a new user chat: configuring and initializing a development (Dev) chat environment tailored for building components for the new business domain."
    },
    {
        "MUID": "WF_STEP_I_1_DEFINE_PIC_DEV", "timestamp": "2025-06-05T11:00:02Z", "turn_id": 5, "source": "ai", "type": "process", "content": "Step I.1: Define Goal & Context for Development (PIC_Dev)", "role": "stable", "context": "workflow, meta, planning", "explicitness": "explicit", "weight": "medium", "status": "accepted", "description": "Create a PIC_Dev artifact (e.g., PIC_Dev_{{NewDomainName}}_{{Purpose}}_vX.Y.md) specifying the Dev chat's purpose: to build SG and other artifacts for the future Use-chat of the new domain."
    },
    {
        "MUID": "WF_STEP_I_2_SELECT_FPS_DEV", "timestamp": "2025-06-05T11:00:03Z", "turn_id": 5, "source": "ai", "type": "process", "content": "Step I.2: Select/Adapt Specialization for Developer (FPS_Dev)", "role": "stable", "context": "workflow, meta, ai_logic", "explicitness": "explicit", "weight": "medium", "status": "accepted", "description": "Typically select FPS_EnMaTeSArchitect. If highly specialized development support is needed for the new domain (rare), a custom FPS_Dev could be considered."
    },
    {
        "MUID": "WF_STEP_I_3_CREATE_CHATCONFIG_DEV", "timestamp": "2025-06-05T11:00:04Z", "turn_id": 5, "source": "ai", "type": "process", "content": "Step I.3: Create Configuration for Dev-chat (ChatConfig_Dev)", "role": "stable", "context": "workflow, meta, technical, ai_logic", "explicitness": "explicit", "weight": "medium", "status": "accepted", "description": "Create a ChatConfig_Dev artifact specifying SMF, FPM-Dev, the selected FPS_Dev, and the created PIC_Dev to assemble the System Instruction for the Dev-chat."
    },
    {
        "MUID": "WF_STEP_I_4_INIT_DEV_CHAT", "timestamp": "2025-06-05T11:00:05Z", "turn_id": 5, "source": "ai", "type": "process", "content": "Step I.4: Initialize Dev-chat", "role": "stable", "context": "workflow, meta, communication, development_tool", "explicitness": "explicit", "weight": "medium", "status": "accepted", "description": "Use a Starting Prompt (SP_Dev) to launch the Dev-chat with the System Instruction assembled according to ChatConfig_Dev."
    },
    {
        "MUID": "WF_STAGE_II_USE_COMP_DEV", "timestamp": "2025-06-05T11:00:06Z", "turn_id": 5, "source": "ai", "type": "process", "content": "Stage II: Develop Use Chat Components (within Dev Chat)", "role": "stable", "context": "workflow, meta, project_management, design, content_management", "explicitness": "explicit", "weight": "high", "status": "accepted", "description": "Second stage, performed within the initialized Dev-chat: creating all necessary artifacts for the future user-facing (Use) chat agent."
    },
    {
        "MUID": "WF_STEP_II_5_DEV_SG", "timestamp": "2025-06-05T11:00:07Z", "turn_id": 5, "source": "ai", "type": "process", "content": "Step II.5: Develop Semantic Graph for Domain (SG)", "role": "stable", "context": "workflow, meta, logic, design", "explicitness": "explicit", "weight": "medium", "status": "accepted", "description": "With Dev-AI assistance, create SG_{{NewDomainName}}_{{SubsystemName}}_vX.Y.md. Analyze domain SDAs and model key concepts and relations in SG per SMF."
    },
    {
        "MUID": "WF_STEP_II_6_PREP_SDA", "timestamp": "2025-06-05T11:00:08Z", "turn_id": 5, "source": "ai", "type": "process", "content": "Step II.6: Prepare and Structure Source Documents (SDA)", "role": "stable", "context": "workflow, meta, content_management", "explicitness": "explicit", "weight": "medium", "status": "accepted", "description": "Collect, prepare, and organize source text documents for the new business domain. These will be used for RAG in the Use-chat. Register them as artifacts in the domain SG."
    },
    {
        "MUID": "WF_STEP_II_7_DEV_FPS_USE", "timestamp": "2025-06-05T11:00:09Z", "turn_id": 5, "source": "ai", "type": "process", "content": "Step II.7: Develop/Adapt Specialization for Use-chat (FPS_Use)", "role": "stable", "context": "workflow, meta, ai_logic", "explicitness": "explicit", "weight": "medium", "status": "accepted", "description": "Define the AI role for the end-user. Typically use FPS_DomainExpert. If needed, create a specific FPS-Addon or a new FPS_{{UserRole}} with Dev-AI assistance."
    },
    {
        "MUID": "WF_STEP_II_8_CREATE_PIC_USE", "timestamp": "2025-06-05T11:00:10Z", "turn_id": 5, "source": "ai", "type": "process", "content": "Step II.8: Create Context for Use-chat (PIC_Use)", "role": "stable", "context": "workflow, meta, planning", "explicitness": "explicit", "weight": "medium", "status": "accepted", "description": "With Dev-AI assistance, create PIC_Use_{{NewDomainName}}_{{Purpose}}_vX.Y.md. It links to the domain SG, lists key SDAs, and describes the domain context for the Use-chat AI."
    },
    {
        "MUID": "WF_STEP_II_9_CREATE_SP_USE", "timestamp": "2025-06-05T11:00:11Z", "turn_id": 5, "source": "ai", "type": "process", "content": "Step II.9: Create Starting Prompt for Use-chat (SP_Use)", "role": "stable", "context": "workflow, meta, communication", "explicitness": "explicit", "weight": "medium", "status": "accepted", "description": "With Dev-AI assistance, create SP_Use_{{TargetAudience}}_{{NewDomainName}}_Welcome_vX.Y.md to greet the user and provide initial guidance."
    },
    {
        "MUID": "WF_STEP_II_10_CREATE_UM_USE", "timestamp": "2025-06-05T11:00:12Z", "turn_id": 5, "source": "ai", "type": "process", "content": "Step II.10: Create User Manual for Use-chat (UM_Use)", "role": "stable", "context": "workflow, meta, content_management", "explicitness": "explicit", "weight": "medium", "status": "accepted", "description": "Recommended: With Dev-AI assistance, create UM_{{Client/Target}}_{{NewDomainName}}_vX.Y.md explaining how to use the AI assistant."
    },
    {
        "MUID": "WF_STAGE_III_USE_SETUP_LAUNCH", "timestamp": "2025-06-05T11:00:13Z", "turn_id": 5, "source": "ai", "type": "process", "content": "Stage III: Setup and Launch Use Chat", "role": "stable", "context": "workflow, meta, project_management, technical, ai_logic", "explicitness": "explicit", "weight": "high", "status": "accepted", "description": "Final stage: configuring, assembling components, and launching the user-facing (Use) chat agent."
    },
    {
        "MUID": "WF_STEP_III_11_CREATE_CHATCONFIG_USE", "timestamp": "2025-06-05T11:00:14Z", "turn_id": 5, "source": "ai", "type": "process", "content": "Step III.11: Create Configuration for Use-chat (ChatConfig_Use)", "role": "stable", "context": "workflow, meta, technical, ai_logic", "explicitness": "explicit", "weight": "medium", "status": "accepted", "description": "Create ChatConfig_Use_{{TargetAudience}}_{{NewDomainName}}_vX.Y.md. It specifies SMF, FPM-Use, the developed FPS_Use, and PIC_Use for the Use-chat's System Instruction."
    },
    {
        "MUID": "WF_STEP_III_12_ASSEMBLE_SI_IP_USE", "timestamp": "2025-06-05T11:00:15Z", "turn_id": 5, "source": "ai", "type": "process", "content": "Step III.12: Assemble System Instruction (SI) & Initiation Package (IP) for Use-chat", "role": "stable", "context": "workflow, meta, technical, ai_logic", "explicitness": "explicit", "weight": "medium", "status": "accepted", "description": "Assemble the SI (SMF, FPM-Use, FPS_Use, PIC_Use) and IP (Domain SG, SDAs, SP_Use, UM_Use) for the Use-chat."
    },
    {
        "MUID": "WF_STEP_III_13_DEPLOY_LAUNCH_USE_CHAT", "timestamp": "2025-06-05T11:00:16Z", "turn_id": 5, "source": "ai", "type": "process", "content": "Step III.13: Deploy and Launch Use-chat AI Agent", "role": "stable", "context": "workflow, meta, technical, platform", "explicitness": "explicit", "weight": "medium", "status": "accepted", "description": "Deploy the Use-chat AI agent on the chosen platform (e.g., Firebase Genkit, Latenode) with its SI and IP."
    },
    {
        "MUID": "ACTOR_ENMATES_DEVELOPER", "timestamp": "2025-06-05T11:00:17Z", "turn_id": 5, "source": "ai", "type": "actor", "content": "EnMaTeS Developer/Architect (Human)", "role": "stable", "context": "meta, workflow", "explicitness": "explicit", "weight": "medium", "status": "accepted", "description": "The human user responsible for designing, developing, and configuring EnMaTeS agents and their components."
    },
    {
        "MUID": "ACTOR_DEV_AI_ASSISTANT", "timestamp": "2025-06-05T11:00:18Z", "turn_id": 5, "source": "ai", "type": "actor", "content": "Dev-AI Assistant", "role": "stable", "context": "meta, workflow, ai_logic", "explicitness": "explicit", "weight": "medium", "status": "accepted", "description": "The AI assistant operating in FPM-Dev mode, assisting the EnMaTeS Developer in creating system components."
    },
    {
        "MUID": "ART_ENMATES_METHODOLOGY_GUIDE_V1", "timestamp": "2025-06-05T12:00:00Z", "turn_id": 7, "source": "ai", "type": "artifact", "content": "EnMaTeS Methodology Guide v1.0", "role": "stable, critical, context_setter", "context": "meta, design, workflow, project_management, content_management", "explicitness": "explicit", "weight": "high", "status": "proposed", "description": "Comprehensive guide to the EnMaTeS methodology, detailing workflows (like WF_CREATE_NEW_USER_CHAT), best practices for component design (SG, FPM, FPS, PIC), versioning principles, and SDA structuring for RAG. Complements EnMaTeS Overview.", "artifactType": "methodology_documentation", "version": "1.0"
    },
    {
        "MUID": "ART_ENMATES_IMPROVEMENT_ROADMAP_V1", "timestamp": "2025-06-05T12:00:01Z", "turn_id": 7, "source": "ai", "type": "artifact", "content": "EnMaTeS Improvement Roadmap v1.0", "role": "stable, volatile", "context": "meta, strategy, planning, project_management", "explicitness": "explicit", "weight": "medium", "status": "proposed", "description": "Living document tracking identified weaknesses in EnMaTeS, proposed solutions, enhancement initiatives (like FEATURE_CENTRAL_ARTIFACT_REGISTRY), their implementation status, and planned new features.", "artifactType": "planning_document", "version": "1.0"
    },
    {
        "MUID": "CONCEPT_AI_AGENT_TESTING", "timestamp": "2025-06-05T12:00:02Z", "turn_id": 7, "source": "ai", "type": "concept", "content": "AI Agent Testing within EnMaTeS", "role": "stable", "context": "meta, quality_control, workflow, ai_logic", "explicitness": "explicit", "weight": "medium", "status": "proposed", "description": "The concept of testing EnMaTeS AI agents, including methodologies, criteria, and supporting tools/artifacts like specialized FPS (FPSTmpl_TesterAI) or FP-Tasks (FPTaskTmpl_AgentEvaluation)."
    },
    {
        "MUID": "CONCEPT_TEST_SCENARIO_GENERATION", "timestamp": "2025-06-05T12:00:03Z", "turn_id": 7, "source": "ai", "type": "concept", "content": "Test Scenario Generation for AI Agents", "role": "stable", "context": "meta, quality_control, ai_logic", "explicitness": "explicit", "weight": "medium", "status": "proposed", "description": "The process or capability of generating test scenarios to evaluate the performance and correctness of EnMaTeS AI agents."
    },
    {
        "MUID": "ART_FPSTMPL_TESTER_AI_V1", "timestamp": "2025-06-05T12:00:04Z", "turn_id": 7, "source": "ai", "type": "artifact", "content": "FPSTmpl_TesterAI v1.0", "role": "stable", "context": "meta, ai_logic, quality_control", "explicitness": "explicit", "weight": "medium", "status": "proposed", "description": "Template for an FPS (Framework Prompt Specialization) designed for an AI agent whose role is to test other EnMaTeS AI agents.", "artifactType": "framework_prompt_template", "version": "1.0"
    },
    {
        "MUID": "ART_FPTASKTMPL_AGENT_EVAL_V1", "timestamp": "2025-06-05T12:00:05Z", "turn_id": 7, "source": "ai", "type": "artifact", "content": "FPTaskTmpl_AgentEvaluation v1.0", "role": "stable", "context": "meta, ai_logic, quality_control", "explicitness": "explicit", "weight": "medium", "status": "proposed", "description": "Template for an FP-Task (Specific Task Framework Prompt) designed for evaluating responses or behavior of an EnMaTeS AI agent against defined criteria.", "artifactType": "framework_prompt_template", "version": "1.0"
    },
    {
        "MUID": "FEATURE_CENTRAL_ARTIFACT_REGISTRY", "timestamp": "2025-06-05T12:00:06Z", "turn_id": 7, "source": "ai", "type": "feature", "content": "Centralized EnMaTeS Artifact Registry", "role": "stable", "context": "meta, design, technical, content_management", "explicitness": "explicit", "weight": "medium", "status": "proposed", "description": "A planned feature for a centralized system (beyond simple file storage) to manage, version, and track dependencies of EnMaTeS artifacts, improving scalability and discoverability."
    },
    {
        "MUID": "CONCEPT_USER_FEEDBACK_LOOP", "timestamp": "2025-06-05T12:00:07Z", "turn_id": 7, "source": "ai", "type": "concept", "content": "User Feedback Loop in EnMaTeS", "role": "stable, critical", "context": "meta, workflow, quality_control, ai_logic, communication", "explicitness": "explicit", "weight": "high", "status": "proposed", "description": "The process and mechanisms for collecting feedback from users (both developers in FPM-Dev and end-users in FPM-Use) and using this feedback to iteratively improve EnMaTeS components (SG, prompts, etc.)."
    }
  ],
  "relations": [
    {"from_MUID": "SMF_CATEGORY", "to_MUID": "ENMATES_SYSTEM_ROOT", "type": "part_of", "weight": "high", "context": "meta"},
    {"from_MUID": "FPM_CATEGORY", "to_MUID": "ENMATES_SYSTEM_ROOT", "type": "part_of", "weight": "high", "context": "meta"},
    {"from_MUID": "FPS_CATEGORY", "to_MUID": "ENMATES_SYSTEM_ROOT", "type": "part_of", "weight": "high", "context": "meta"},
    {"from_MUID": "PIC_CATEGORY", "to_MUID": "ENMATES_SYSTEM_ROOT", "type": "part_of", "weight": "high", "context": "meta"},
    {"from_MUID": "SG_CATEGORY", "to_MUID": "ENMATES_SYSTEM_ROOT", "type": "part_of", "weight": "high", "context": "meta"},
    {"from_MUID": "SDA_CATEGORY", "to_MUID": "ENMATES_SYSTEM_ROOT", "type": "part_of", "weight": "medium", "context": "meta"},
    {"from_MUID": "UM_CATEGORY", "to_MUID": "ENMATES_SYSTEM_ROOT", "type": "part_of", "weight": "medium", "context": "meta"},
    {"from_MUID": "STFP_FP_TASK_CATEGORY", "to_MUID": "ENMATES_SYSTEM_ROOT", "type": "part_of", "weight": "medium", "context": "meta"},
    {"from_MUID": "SYS_OVERVIEW_NAMING_CATEGORY", "to_MUID": "ENMATES_SYSTEM_ROOT", "type": "part_of", "weight": "medium", "context": "meta"},
    {"from_MUID": "CIP_SP_CATEGORY", "to_MUID": "ENMATES_SYSTEM_ROOT", "type": "part_of", "weight": "medium", "context": "meta"},
    {"from_MUID": "CHAT_CONFIG_CATEGORY", "to_MUID": "ENMATES_SYSTEM_ROOT", "type": "part_of", "weight": "high", "context": "meta"},
    {"from_MUID": "IP_CATEGORY", "to_MUID": "ENMATES_SYSTEM_ROOT", "type": "part_of", "weight": "medium", "context": "meta"},
    {"from_MUID": "SI_CONCEPT", "to_MUID": "ENMATES_SYSTEM_ROOT", "type": "part_of", "weight": "high", "context": "meta", "label": "SI is a key part of EnMaTeS operation"},
    {"from_MUID": "456599f0-c0d6-4f12-97d3-3e7a7058481a", "to_MUID": "SYS_OVERVIEW_NAMING_CATEGORY", "type": "instance_of", "weight": "high", "context": "meta"},
    {"from_MUID": "456599f0-c0d6-4f12-97d3-3e7a7058481a", "to_MUID": "ENMATES_SYSTEM_ROOT", "type": "describes", "weight": "high", "context": "meta"},
    {"from_MUID": "c5e2daef-7ab8-4b24-886c-a6bab452fb93", "to_MUID": "SYS_OVERVIEW_NAMING_CATEGORY", "type": "instance_of", "weight": "high", "context": "meta"},
    {"from_MUID": "c5e2daef-7ab8-4b24-886c-a6bab452fb93", "to_MUID": "CONCEPT_ENMATES_NDF", "type": "instance_of", "weight": "high", "context": "meta", "label": "Is the concrete NDF document"},
    {"from_MUID": "f5bef63a-23fc-4057-ac62-483a9e0530e6", "to_MUID": "SMF_CATEGORY", "type": "instance_of", "weight": "high", "context": "meta"},
    {"from_MUID": "f5bef63a-23fc-4057-ac62-483a9e0530e6", "to_MUID": "CONCEPT_SMF", "type": "defines", "weight": "high", "context": "meta", "label": "Specifies the SMF concept"},
    {"from_MUID": "429fb2c2-86d4-4b28-ae88-f94443b483e4", "to_MUID": "FPM_CATEGORY", "type": "instance_of", "weight": "high", "context": "meta"},
    {"from_MUID": "7969c80a-1efb-489d-8bfd-978472b5fcb7", "to_MUID": "FPM_CATEGORY", "type": "instance_of", "weight": "high", "context": "meta"},
    {"from_MUID": "a0920c09-159c-40fc-8e05-76204e9de728", "to_MUID": "FPS_CATEGORY", "type": "instance_of", "weight": "high", "context": "meta"},
    {"from_MUID": "4102aa13-8418-4a5e-88e1-1ce98c67474f", "to_MUID": "FPS_CATEGORY", "type": "instance_of", "weight": "high", "context": "meta"},
    {"from_MUID": "3bb00c7e-3706-4213-b545-fb9f41e77c8c", "to_MUID": "FPS_CATEGORY", "type": "instance_of", "weight": "medium", "context": "meta", "label": "Is an FPS Addon"},
    {"from_MUID": "3bb00c7e-3706-4213-b545-fb9f41e77c8c", "to_MUID": "a0920c09-159c-40fc-8e05-76204e9de728", "type": "refines", "weight": "high", "context": "meta, legal", "label": "Extends FPS_DomainExpert for LegalAdvisor role"},
    {"from_MUID": "e2afe7f4-9bb5-40b3-8b3e-e05d53324799", "to_MUID": "PIC_CATEGORY", "type": "instance_of", "weight": "high", "context": "meta"},
    {"from_MUID": "480dd136-bdf3-4266-8771-169953190f08", "to_MUID": "PIC_CATEGORY", "type": "instance_of", "weight": "high", "context": "meta"},
    {"from_MUID": "80e82615-3aae-4c33-8874-20428a354b99", "to_MUID": "PIC_CATEGORY", "type": "instance_of", "weight": "high", "context": "meta"},
    {"from_MUID": "3d9a80a9-fea2-4f1f-9970-43ad70e70844", "to_MUID": "CIP_SP_CATEGORY", "type": "instance_of", "weight": "high", "context": "meta"},
    {"from_MUID": "18a115c6-3b69-4930-aed3-a3090316fea1", "to_MUID": "CHAT_CONFIG_CATEGORY", "type": "instance_of", "weight": "high", "context": "meta"},
    {"from_MUID": "18a115c6-3b69-4930-aed3-a3090316fea1", "to_MUID": "CONCEPT_CHAT_CONFIG", "type": "instance_of", "weight": "high", "context": "meta", "label": "Is the concrete ChatConfig document"},
    {"from_MUID": "CONCEPT_SMF", "to_MUID": "SMF_CATEGORY", "type": "part_of", "weight": "high", "context": "meta"},
    {"from_MUID": "CONCEPT_FPM", "to_MUID": "FPM_CATEGORY", "type": "part_of", "weight": "high", "context": "meta"},
    {"from_MUID": "CONCEPT_FPS", "to_MUID": "FPS_CATEGORY", "type": "part_of", "weight": "high", "context": "meta"},
    {"from_MUID": "CONCEPT_PIC", "to_MUID": "PIC_CATEGORY", "type": "part_of", "weight": "high", "context": "meta"},
    {"from_MUID": "CONCEPT_SG", "to_MUID": "SG_CATEGORY", "type": "part_of", "weight": "high", "context": "meta"},
    {"from_MUID": "CONCEPT_SDA", "to_MUID": "SDA_CATEGORY", "type": "part_of", "weight": "high", "context": "meta"},
    {"from_MUID": "CONCEPT_SP_CIP", "to_MUID": "CIP_SP_CATEGORY", "type": "part_of", "weight": "high", "context": "meta"},
    {"from_MUID": "CONCEPT_UM", "to_MUID": "UM_CATEGORY", "type": "part_of", "weight": "high", "context": "meta"},
    {"from_MUID": "CONCEPT_IP", "to_MUID": "IP_CATEGORY", "type": "part_of", "weight": "high", "context": "meta"},
    {"from_MUID": "CONCEPT_CHAT_CONFIG", "to_MUID": "CHAT_CONFIG_CATEGORY", "type": "part_of", "weight": "high", "context": "meta"},
    {"from_MUID": "CONCEPT_ENMATES_NDF", "to_MUID": "SYS_OVERVIEW_NAMING_CATEGORY", "type": "part_of", "weight": "high", "context": "meta"},
    {"from_MUID": "CONCEPT_FP_TASK", "to_MUID": "STFP_FP_TASK_CATEGORY", "type": "part_of", "weight": "high", "context": "meta"},
    {"from_MUID": "PHILOSOPHY_ENMATES", "to_MUID": "ENMATES_SYSTEM_ROOT", "type": "defines", "weight": "high", "context": "meta, strategy"},
    {"from_MUID": "PHILOSOPHY_ENMATES", "to_MUID": "456599f0-c0d6-4f12-97d3-3e7a7058481a", "type": "described_in", "weight": "high", "context": "meta"},
    {"from_MUID": "GOAL_ENMATES", "to_MUID": "PHILOSOPHY_ENMATES", "type": "part_of", "weight": "high", "context": "meta, strategy"},
    {"from_MUID": "GOAL_ENMATES", "to_MUID": "456599f0-c0d6-4f12-97d3-3e7a7058481a", "type": "described_in", "weight": "high", "context": "meta"},
    {"from_MUID": "PRINCIPLE_MODULARITY", "to_MUID": "PHILOSOPHY_ENMATES", "type": "supports", "weight": "medium", "context": "meta, design"},
    {"from_MUID": "PRINCIPLE_SEMANTIC_MODELING", "to_MUID": "PHILOSOPHY_ENMATES", "type": "supports", "weight": "high", "context": "meta, logic"},
    {"from_MUID": "PRINCIPLE_CONTEXT_MANAGEMENT", "to_MUID": "PHILOSOPHY_ENMATES", "type": "supports", "weight": "high", "context": "meta, ai_logic"},
    {"from_MUID": "PRINCIPLE_ITERATIVITY", "to_MUID": "PHILOSOPHY_ENMATES", "type": "supports", "weight": "medium", "context": "meta, workflow"},
    {"from_MUID": "PRINCIPLE_RAG", "to_MUID": "PHILOSOPHY_ENMATES", "type": "supports", "weight": "medium", "context": "meta, ai_logic"},
    {"from_MUID": "SMF_NODE_DEF", "to_MUID": "f5bef63a-23fc-4057-ac62-483a9e0530e6", "type": "defined_by", "weight": "high", "context": "meta, design"},
    {"from_MUID": "SMF_RELATION_DEF", "to_MUID": "f5bef63a-23fc-4057-ac62-483a9e0530e6", "type": "defined_by", "weight": "high", "context": "meta, design"},
    {"from_MUID": "SMF_NODE_TYPES_LIST", "to_MUID": "f5bef63a-23fc-4057-ac62-483a9e0530e6", "type": "defined_by", "weight": "high", "context": "meta, design"},
    {"from_MUID": "SMF_RELATION_TYPES_LIST", "to_MUID": "f5bef63a-23fc-4057-ac62-483a9e0530e6", "type": "defined_by", "weight": "high", "context": "meta, design"},
    {"from_MUID": "SMF_NODE_ROLES_LIST", "to_MUID": "f5bef63a-23fc-4057-ac62-483a9e0530e6", "type": "defined_by", "weight": "high", "context": "meta, design"},
    {"from_MUID": "SMF_CONTEXTS_LIST", "to_MUID": "f5bef63a-23fc-4057-ac62-483a9e0530e6", "type": "defined_by", "weight": "high", "context": "meta, design"},
    {"from_MUID": "SMF_GRAPH_METADATA_DEF", "to_MUID": "f5bef63a-23fc-4057-ac62-483a9e0530e6", "type": "defined_by", "weight": "high", "context": "meta, design"},
    {"from_MUID": "18a115c6-3b69-4930-aed3-a3090316fea1", "to_MUID": "SI_CONCEPT", "type": "defines_assembly_for", "weight": "high", "context": "meta, ai_logic", "label": "Defines how SI is assembled"},
    {"from_MUID": "SI_CONCEPT", "to_MUID": "f5bef63a-23fc-4057-ac62-483a9e0530e6", "type": "composed_of", "weight": "high", "context": "meta, ai_logic", "label": "SI includes SMF"},
    {"from_MUID": "SI_CONCEPT", "to_MUID": "429fb2c2-86d4-4b28-ae88-f94443b483e4", "type": "composed_of", "weight": "high", "context": "meta, ai_logic", "label": "SI (for dev) includes FPM-Dev"},
    {"from_MUID": "SI_CONCEPT", "to_MUID": "4102aa13-8418-4a5e-88e1-1ce98c67474f", "type": "composed_of", "weight": "high", "context": "meta, ai_logic", "label": "SI (for dev) includes FPS_EnMaTeSArchitect"},
    {"from_MUID": "SI_CONCEPT", "to_MUID": "480dd136-bdf3-4266-8771-169953190f08", "type": "composed_of", "weight": "high", "context": "meta, ai_logic", "label": "SI (for dev) includes PIC_EnMaTeS_SelfSG_Dev"},
    {"from_MUID": "18a115c6-3b69-4930-aed3-a3090316fea1", "to_MUID": "3d9a80a9-fea2-4f1f-9970-43ad70e70844", "type": "references", "weight": "medium", "context": "meta, ai_logic", "label": "Specifies starting prompt"},
    {"from_MUID": "CONCEPT_FPM", "to_MUID": "CONCEPT_SMF", "type": "uses_concepts_from", "weight": "high", "context": "meta, ai_logic"},
    {"from_MUID": "CONCEPT_FPS", "to_MUID": "CONCEPT_FPM", "type": "refines", "weight": "high", "context": "meta, ai_logic", "label": "FPS refines behavior within an FPM"},
    {"from_MUID": "CONCEPT_PIC", "to_MUID": "CONCEPT_FPS", "type": "provides_input_for", "weight": "high", "context": "meta, ai_logic", "label": "PIC provides context for an FPS"},
    {"from_MUID": "CONCEPT_SG", "to_MUID": "CONCEPT_SMF", "type": "structured_by", "weight": "high", "context": "meta, logic"},
    {"from_MUID": "CONCEPT_SG", "to_MUID": "CONCEPT_SDA", "type": "derived_from", "weight": "medium", "context": "meta, content_management", "label": "SG can be derived from SDA content"},
    {"from_MUID": "PRINCIPLE_RAG", "to_MUID": "CONCEPT_SG", "type": "uses_artifact_concept", "weight": "high", "context": "meta, ai_logic"},
    {"from_MUID": "PRINCIPLE_RAG", "to_MUID": "CONCEPT_SDA", "type": "uses_artifact_concept", "weight": "high", "context": "meta, ai_logic"},
    {"from_MUID": "CONCEPT_ENMATES_NDF", "to_MUID": "ENMATES_SYSTEM_ROOT", "type": "governs", "weight": "high", "context": "meta, content_management", "label": "NDF governs naming for all EnMaTeS artifacts"},
    {"from_MUID": "WF_CREATE_NEW_USER_CHAT", "to_MUID": "ENMATES_SYSTEM_ROOT", "type": "defines", "weight": "high", "context": "workflow, meta", "label": "Defines a core process of EnMaTeS"},
    {"from_MUID": "WF_CREATE_NEW_USER_CHAT", "to_MUID": "456599f0-c0d6-4f12-97d3-3e7a7058481a", "type": "elaborates_on", "weight": "medium", "context": "workflow, meta", "label": "Elaborates on principle of work from Overview"},
    {"from_MUID": "WF_STAGE_I_DEV_SETUP", "to_MUID": "WF_CREATE_NEW_USER_CHAT", "type": "part_of", "weight": "high", "context": "workflow"},
    {"from_MUID": "WF_STAGE_II_USE_COMP_DEV", "to_MUID": "WF_CREATE_NEW_USER_CHAT", "type": "part_of", "weight": "high", "context": "workflow"},
    {"from_MUID": "WF_STAGE_III_USE_SETUP_LAUNCH", "to_MUID": "WF_CREATE_NEW_USER_CHAT", "type": "part_of", "weight": "high", "context": "workflow"},
    {"from_MUID": "WF_STAGE_I_DEV_SETUP", "to_MUID": "WF_STAGE_II_USE_COMP_DEV", "type": "precedes", "weight": "high", "context": "workflow"},
    {"from_MUID": "WF_STAGE_II_USE_COMP_DEV", "to_MUID": "WF_STAGE_III_USE_SETUP_LAUNCH", "type": "precedes", "weight": "high", "context": "workflow"},
    {"from_MUID": "WF_STEP_I_1_DEFINE_PIC_DEV", "to_MUID": "WF_STAGE_I_DEV_SETUP", "type": "part_of", "weight": "medium", "context": "workflow"},
    {"from_MUID": "WF_STEP_I_1_DEFINE_PIC_DEV", "to_MUID": "PIC_CATEGORY", "type": "produces_artifact_concept", "weight": "medium", "context": "workflow", "label": "Produces a PIC_Dev artifact"},
    {"from_MUID": "WF_STEP_I_1_DEFINE_PIC_DEV", "to_MUID": "ACTOR_ENMATES_DEVELOPER", "type": "responsible_for_action", "weight": "medium", "context": "workflow"},
    {"from_MUID": "WF_STEP_I_1_DEFINE_PIC_DEV", "to_MUID": "WF_STEP_I_2_SELECT_FPS_DEV", "type": "precedes", "weight": "high", "context": "workflow"},
    {"from_MUID": "WF_STEP_I_2_SELECT_FPS_DEV", "to_MUID": "WF_STAGE_I_DEV_SETUP", "type": "part_of", "weight": "medium", "context": "workflow"},
    {"from_MUID": "WF_STEP_I_2_SELECT_FPS_DEV", "to_MUID": "FPS_CATEGORY", "type": "uses_artifact_concept", "weight": "medium", "context": "workflow", "label": "Selects/references an FPS_Dev"},
    {"from_MUID": "WF_STEP_I_2_SELECT_FPS_DEV", "to_MUID": "4102aa13-8418-4a5e-88e1-1ce98c67474f", "type": "references", "weight": "medium", "context": "workflow", "label": "Typically FPS_EnMaTeSArchitect"},
    {"from_MUID": "WF_STEP_I_2_SELECT_FPS_DEV", "to_MUID": "ACTOR_ENMATES_DEVELOPER", "type": "responsible_for_action", "weight": "medium", "context": "workflow"},
    {"from_MUID": "WF_STEP_I_2_SELECT_FPS_DEV", "to_MUID": "WF_STEP_I_3_CREATE_CHATCONFIG_DEV", "type": "precedes", "weight": "high", "context": "workflow"},
    {"from_MUID": "WF_STEP_I_3_CREATE_CHATCONFIG_DEV", "to_MUID": "WF_STAGE_I_DEV_SETUP", "type": "part_of", "weight": "medium", "context": "workflow"},
    {"from_MUID": "WF_STEP_I_3_CREATE_CHATCONFIG_DEV", "to_MUID": "CHAT_CONFIG_CATEGORY", "type": "produces_artifact_concept", "weight": "medium", "context": "workflow", "label": "Produces a ChatConfig_Dev artifact"},
    {"from_MUID": "WF_STEP_I_3_CREATE_CHATCONFIG_DEV", "to_MUID": "ACTOR_ENMATES_DEVELOPER", "type": "responsible_for_action", "weight": "medium", "context": "workflow"},
    {"from_MUID": "WF_STEP_I_3_CREATE_CHATCONFIG_DEV", "to_MUID": "WF_STEP_I_4_INIT_DEV_CHAT", "type": "precedes", "weight": "high", "context": "workflow"},
    {"from_MUID": "WF_STEP_I_4_INIT_DEV_CHAT", "to_MUID": "WF_STAGE_I_DEV_SETUP", "type": "part_of", "weight": "medium", "context": "workflow"},
    {"from_MUID": "WF_STEP_I_4_INIT_DEV_CHAT", "to_MUID": "CIP_SP_CATEGORY", "type": "uses_artifact_concept", "weight": "medium", "context": "workflow", "label": "Uses an SP_Dev"},
    {"from_MUID": "WF_STEP_I_4_INIT_DEV_CHAT", "to_MUID": "ACTOR_ENMATES_DEVELOPER", "type": "initiates", "weight": "medium", "context": "workflow"},
    {"from_MUID": "WF_STEP_I_4_INIT_DEV_CHAT", "to_MUID": "ACTOR_DEV_AI_ASSISTANT", "type": "triggers", "weight": "medium", "context": "workflow", "label": "Activates Dev-AI Assistant"},
    {"from_MUID": "WF_STEP_II_5_DEV_SG", "to_MUID": "WF_STAGE_II_USE_COMP_DEV", "type": "part_of", "weight": "medium", "context": "workflow"},
    {"from_MUID": "WF_STEP_II_5_DEV_SG", "to_MUID": "SG_CATEGORY", "type": "produces_artifact_concept", "weight": "medium", "context": "workflow", "label": "Produces a Domain SG"},
    {"from_MUID": "WF_STEP_II_5_DEV_SG", "to_MUID": "ACTOR_ENMATES_DEVELOPER", "type": "participates_in", "weight": "medium", "context": "workflow"},
    {"from_MUID": "WF_STEP_II_5_DEV_SG", "to_MUID": "ACTOR_DEV_AI_ASSISTANT", "type": "participates_in", "weight": "medium", "context": "workflow"},
    {"from_MUID": "WF_STEP_II_5_DEV_SG", "to_MUID": "429fb2c2-86d4-4b28-ae88-f94443b483e4", "type": "uses_artifact", "weight": "high", "context": "workflow", "label": "Performed using FPM-Dev"},
    {"from_MUID": "WF_STEP_II_5_DEV_SG", "to_MUID": "WF_STEP_II_6_PREP_SDA", "type": "precedes", "weight": "high", "context": "workflow"},
    {"from_MUID": "WF_STEP_II_6_PREP_SDA", "to_MUID": "WF_STAGE_II_USE_COMP_DEV", "type": "part_of", "weight": "medium", "context": "workflow"},
    {"from_MUID": "WF_STEP_II_6_PREP_SDA", "to_MUID": "SDA_CATEGORY", "type": "produces_artifact_concept", "weight": "medium", "context": "workflow", "label": "Prepares/organizes SDAs"},
    {"from_MUID": "WF_STEP_II_6_PREP_SDA", "to_MUID": "ACTOR_ENMATES_DEVELOPER", "type": "participates_in", "weight": "medium", "context": "workflow"},
    {"from_MUID": "WF_STEP_II_6_PREP_SDA", "to_MUID": "ACTOR_DEV_AI_ASSISTANT", "type": "participates_in", "weight": "medium", "context": "workflow"},
    {"from_MUID": "WF_STEP_II_6_PREP_SDA", "to_MUID": "WF_STEP_II_7_DEV_FPS_USE", "type": "precedes", "weight": "high", "context": "workflow"},
    {"from_MUID": "WF_STEP_II_7_DEV_FPS_USE", "to_MUID": "WF_STAGE_II_USE_COMP_DEV", "type": "part_of", "weight": "medium", "context": "workflow"},
    {"from_MUID": "WF_STEP_II_7_DEV_FPS_USE", "to_MUID": "FPS_CATEGORY", "type": "produces_artifact_concept", "weight": "medium", "context": "workflow", "label": "Produces/adapts FPS_Use/Addon"},
    {"from_MUID": "WF_STEP_II_7_DEV_FPS_USE", "to_MUID": "a0920c09-159c-40fc-8e05-76204e9de728", "type": "references", "weight": "medium", "context": "workflow", "label": "Often FPS_DomainExpert"},
    {"from_MUID": "WF_STEP_II_7_DEV_FPS_USE", "to_MUID": "ACTOR_ENMATES_DEVELOPER", "type": "participates_in", "weight": "medium", "context": "workflow"},
    {"from_MUID": "WF_STEP_II_7_DEV_FPS_USE", "to_MUID": "ACTOR_DEV_AI_ASSISTANT", "type": "participates_in", "weight": "medium", "context": "workflow"},
    {"from_MUID": "WF_STEP_II_7_DEV_FPS_USE", "to_MUID": "WF_STEP_II_8_CREATE_PIC_USE", "type": "precedes", "weight": "high", "context": "workflow"},
    {"from_MUID": "WF_STEP_II_8_CREATE_PIC_USE", "to_MUID": "WF_STAGE_II_USE_COMP_DEV", "type": "part_of", "weight": "medium", "context": "workflow"},
    {"from_MUID": "WF_STEP_II_8_CREATE_PIC_USE", "to_MUID": "PIC_CATEGORY", "type": "produces_artifact_concept", "weight": "medium", "context": "workflow", "label": "Produces PIC_Use"},
    {"from_MUID": "WF_STEP_II_8_CREATE_PIC_USE", "to_MUID": "ACTOR_ENMATES_DEVELOPER", "type": "participates_in", "weight": "medium", "context": "workflow"},
    {"from_MUID": "WF_STEP_II_8_CREATE_PIC_USE", "to_MUID": "ACTOR_DEV_AI_ASSISTANT", "type": "participates_in", "weight": "medium", "context": "workflow"},
    {"from_MUID": "WF_STEP_II_8_CREATE_PIC_USE", "to_MUID": "WF_STEP_II_9_CREATE_SP_USE", "type": "precedes", "weight": "high", "context": "workflow"},
    {"from_MUID": "WF_STEP_II_9_CREATE_SP_USE", "to_MUID": "WF_STAGE_II_USE_COMP_DEV", "type": "part_of", "weight": "medium", "context": "workflow"},
    {"from_MUID": "WF_STEP_II_9_CREATE_SP_USE", "to_MUID": "CIP_SP_CATEGORY", "type": "produces_artifact_concept", "weight": "medium", "context": "workflow", "label": "Produces SP_Use"},
    {"from_MUID": "WF_STEP_II_9_CREATE_SP_USE", "to_MUID": "ACTOR_ENMATES_DEVELOPER", "type": "participates_in", "weight": "medium", "context": "workflow"},
    {"from_MUID": "WF_STEP_II_9_CREATE_SP_USE", "to_MUID": "ACTOR_DEV_AI_ASSISTANT", "type": "participates_in", "weight": "medium", "context": "workflow"},
    {"from_MUID": "WF_STEP_II_9_CREATE_SP_USE", "to_MUID": "WF_STEP_II_10_CREATE_UM_USE", "type": "precedes", "weight": "high", "context": "workflow"},
    {"from_MUID": "WF_STEP_II_10_CREATE_UM_USE", "to_MUID": "WF_STAGE_II_USE_COMP_DEV", "type": "part_of", "weight": "medium", "context": "workflow"},
    {"from_MUID": "WF_STEP_II_10_CREATE_UM_USE", "to_MUID": "UM_CATEGORY", "type": "produces_artifact_concept", "weight": "medium", "context": "workflow", "label": "Produces UM_Use"},
    {"from_MUID": "WF_STEP_II_10_CREATE_UM_USE", "to_MUID": "ACTOR_ENMATES_DEVELOPER", "type": "participates_in", "weight": "medium", "context": "workflow"},
    {"from_MUID": "WF_STEP_II_10_CREATE_UM_USE", "to_MUID": "ACTOR_DEV_AI_ASSISTANT", "type": "participates_in", "weight": "medium", "context": "workflow"},
    {"from_MUID": "WF_STEP_III_11_CREATE_CHATCONFIG_USE", "to_MUID": "WF_STAGE_III_USE_SETUP_LAUNCH", "type": "part_of", "weight": "medium", "context": "workflow"},
    {"from_MUID": "WF_STEP_III_11_CREATE_CHATCONFIG_USE", "to_MUID": "CHAT_CONFIG_CATEGORY", "type": "produces_artifact_concept", "weight": "medium", "context": "workflow", "label": "Produces ChatConfig_Use"},
    {"from_MUID": "WF_STEP_III_11_CREATE_CHATCONFIG_USE", "to_MUID": "ACTOR_ENMATES_DEVELOPER", "type": "responsible_for_action", "weight": "medium", "context": "workflow"},
    {"from_MUID": "WF_STEP_III_11_CREATE_CHATCONFIG_USE", "to_MUID": "WF_STEP_III_12_ASSEMBLE_SI_IP_USE", "type": "precedes", "weight": "high", "context": "workflow"},
    {"from_MUID": "WF_STEP_III_12_ASSEMBLE_SI_IP_USE", "to_MUID": "WF_STAGE_III_USE_SETUP_LAUNCH", "type": "part_of", "weight": "medium", "context": "workflow"},
    {"from_MUID": "WF_STEP_III_12_ASSEMBLE_SI_IP_USE", "to_MUID": "SI_CONCEPT", "type": "produces_artifact_concept", "weight": "medium", "context": "workflow", "label": "Assembles SI for Use-chat"},
    {"from_MUID": "WF_STEP_III_12_ASSEMBLE_SI_IP_USE", "to_MUID": "IP_CATEGORY", "type": "produces_artifact_concept", "weight": "medium", "context": "workflow", "label": "Assembles IP for Use-chat"},
    {"from_MUID": "WF_STEP_III_12_ASSEMBLE_SI_IP_USE", "to_MUID": "ACTOR_ENMATES_DEVELOPER", "type": "responsible_for_action", "weight": "medium", "context": "workflow"},
    {"from_MUID": "WF_STEP_III_12_ASSEMBLE_SI_IP_USE", "to_MUID": "WF_STEP_III_13_DEPLOY_LAUNCH_USE_CHAT", "type": "precedes", "weight": "high", "context": "workflow"},
    {"from_MUID": "WF_STEP_III_13_DEPLOY_LAUNCH_USE_CHAT", "to_MUID": "WF_STAGE_III_USE_SETUP_LAUNCH", "type": "part_of", "weight": "medium", "context": "workflow"},
    {"from_MUID": "WF_STEP_III_13_DEPLOY_LAUNCH_USE_CHAT", "to_MUID": "ACTOR_ENMATES_DEVELOPER", "type": "responsible_for_action", "weight": "medium", "context": "workflow"},
    {"from_MUID": "ART_ENMATES_METHODOLOGY_GUIDE_V1", "to_MUID": "SYS_OVERVIEW_NAMING_CATEGORY", "type": "instance_of", "weight": "high", "context": "meta, content_management"},
    {"from_MUID": "ART_ENMATES_METHODOLOGY_GUIDE_V1", "to_MUID": "456599f0-c0d6-4f12-97d3-3e7a7058481a", "type": "elaborates_on", "weight": "high", "context": "meta", "label": "Details and expands on Overview"},
    {"from_MUID": "WF_CREATE_NEW_USER_CHAT", "to_MUID": "ART_ENMATES_METHODOLOGY_GUIDE_V1", "type": "described_in", "weight": "high", "context": "workflow, meta", "label": "Workflow detailed in Methodology Guide"},
    {"from_MUID": "ART_ENMATES_IMPROVEMENT_ROADMAP_V1", "to_MUID": "SYS_OVERVIEW_NAMING_CATEGORY", "type": "instance_of", "weight": "high", "context": "meta, content_management"},
    {"from_MUID": "ART_ENMATES_IMPROVEMENT_ROADMAP_V1", "to_MUID": "ENMATES_SYSTEM_ROOT", "type": "tracks_development_of", "weight": "medium", "context": "meta, strategy"},
    {"from_MUID": "CONCEPT_AI_AGENT_TESTING", "to_MUID": "ENMATES_SYSTEM_ROOT", "type": "part_of", "weight": "medium", "context": "meta, quality_control"},
    {"from_MUID": "CONCEPT_AI_AGENT_TESTING", "to_MUID": "ART_ENMATES_METHODOLOGY_GUIDE_V1", "type": "described_in", "weight": "medium", "context": "meta, quality_control", "label": "Testing principles in Methodology Guide"},
    {"from_MUID": "CONCEPT_TEST_SCENARIO_GENERATION", "to_MUID": "CONCEPT_AI_AGENT_TESTING", "type": "supports", "weight": "medium", "context": "meta, quality_control"},
    {"from_MUID": "ART_FPSTMPL_TESTER_AI_V1", "to_MUID": "FPS_CATEGORY", "type": "instance_of", "weight": "medium", "context": "meta, ai_logic"},
    {"from_MUID": "ART_FPSTMPL_TESTER_AI_V1", "to_MUID": "CONCEPT_AI_AGENT_TESTING", "type": "supports", "weight": "medium", "context": "meta, quality_control"},
    {"from_MUID": "ART_FPTASKTMPL_AGENT_EVAL_V1", "to_MUID": "STFP_FP_TASK_CATEGORY", "type": "instance_of", "weight": "medium", "context": "meta, ai_logic"},
    {"from_MUID": "ART_FPTASKTMPL_AGENT_EVAL_V1", "to_MUID": "CONCEPT_AI_AGENT_TESTING", "type": "supports", "weight": "medium", "context": "meta, quality_control"},
    {"from_MUID": "FEATURE_CENTRAL_ARTIFACT_REGISTRY", "to_MUID": "ENMATES_SYSTEM_ROOT", "type": "enhancement_for", "weight": "medium", "context": "meta, technical"},
    {"from_MUID": "FEATURE_CENTRAL_ARTIFACT_REGISTRY", "to_MUID": "ART_ENMATES_IMPROVEMENT_ROADMAP_V1", "type": "documented_in", "weight": "medium", "context": "meta, planning", "label": "May be tracked in Roadmap"},
    {"from_MUID": "CONCEPT_USER_FEEDBACK_LOOP", "to_MUID": "ENMATES_SYSTEM_ROOT", "type": "part_of", "weight": "high", "context": "meta, workflow"},
    {"from_MUID": "CONCEPT_USER_FEEDBACK_LOOP", "to_MUID": "PRINCIPLE_ITERATIVITY", "type": "supports", "weight": "high", "context": "meta, workflow"},
    {"from_MUID": "CONCEPT_USER_FEEDBACK_LOOP", "to_MUID": "ART_ENMATES_METHODOLOGY_GUIDE_V1", "type": "described_in", "weight": "medium", "context": "meta, workflow", "label": "Feedback process in Methodology Guide"},
    {"from_MUID": "7969c80a-1efb-489d-8bfd-978472b5fcb7", "to_MUID": "CONCEPT_USER_FEEDBACK_LOOP", "type": "implements", "weight": "medium", "context": "meta, ai_logic", "label": "FPM-Use implements feedback collection"},
    {"from_MUID": "429fb2c2-86d4-4b28-ae88-f94443b483e4", "to_MUID": "CONCEPT_USER_FEEDBACK_LOOP", "type": "supports", "weight": "medium", "context": "meta, ai_logic", "label": "FPM-Dev supports feedback analysis"}
  ]
}