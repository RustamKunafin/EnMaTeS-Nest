---
title: ChatConfig_Dev_t01_FrameworkAgreementGen v1.0
entityType: artifact
artifactType: ai_chat_configuration
description: Конфигурация для запуска Dev-чата, предназначенного для разработки ИИ-агента-генератора рамочных договоров для клиента t01. Использует роль AgentDeveloper и PIC с методом реверс-инжиниринга.
version: "1.0"
status: proposed
tags: Membra, EnMaTeS, ChatConfig, Development, t01, Generator
publish: true
muid: 00e3f4f6-277e-426e-994c-46fa5529795a
---

# ChatConfig_Dev_t01_FrameworkAgreementGen v1.0

## 1. Назначение Чата / Агента:
- **Название ИИ-чата:** AI-Chat_Dev_AgentDeveloper_t01_FrameworkAgreementGen_v0.1
- **Режим работы ИИ:** Разработка (Development)
- **Специализация ИИ:** Помощник Разработчика ИИ-Агентов (Agent Developer)
- **Основная цель сессии:** Создание ИИ-агента FrameworkAgreementGen для клиента t01 методом реверс-инжиниринга существующего РД.

## 2. Компоненты для Сборки Системной Инструкции (SI):
1. **SMF (Semantic Modeling Framework):**
    - Файл: SMF.md
    - Версия: 2.2
2. **FPM (Framework Prompt Mode):**
    - Файл: FPM-Dev.md
    - Версия: 1.2
3. **FPS (Framework Prompt Specialization):**
    - Файл: FPS_AgentDeveloper.md
    - Версия: 1.0
4. **PIC (Purpose and Introductory Context):**
    - Файл: PIC_Dev_t01_FrameworkAgreementGen_v1.1.md **(уточненная версия)**

## 3. Порядок Объединения Компонентов в SI:
Содержимое указанных выше файлов объединяется последовательно для формирования полной Системной Инструкции, которая будет передана новому Dev-чату.

## 4. Пакет Инициализации (IP) для Данного Dev-чата:
- **Семантические Графы (SG):**
    1. SG_EnMaTeS_SystemMethodology.md (актуальная версия): Загружается как **мета-база знаний** о методологии EnMaTeS.
    2. SG_t01_FrameworkAgreementGen.md: Будет создан и развиваться в ходе сессии как **основная рабочая область**.
- **Исходные Документы (SDA):**
    - **Основной SDA:** Actual_FrameworkAgreement_ExistingClient.docx (или .md) - **актуальный РД**, который мы будем декомпозировать.
    - **Дополнительный SDA:** NewClient_Requisites.txt - реквизиты нового клиента для Фазы I.
- **Стартовый Промпт (SP):**
    - Рекомендуется создать SP_Dev_t01_FrameworkAgreementGen_Init.md, который будет содержать приветствие, ссылку на PIC и первую задачу, например: "Привет! Начинаем работу по PIC_Dev_t01_FrameworkAgreementGen_v1.1. Пожалуйста, проанализируй прикрепленный Actual_FrameworkAgreement_ExistingClient.docx и предложи список переменных для замены (Фаза I)".