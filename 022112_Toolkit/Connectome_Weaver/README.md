---
muid: fe91ce22-8e13-4114-96b2-128b7db64e98
---
# Connectome Weaver (`weaverSG`)

### 1. Краткое описание

`weaverSG` — это транзакционный CLI-инструмент для полного жизненного цикла Семантических Графов (SG) в экосистеме EnMaTeS: аудита, миграции схемы, безопасного редактирования и управления логами.

### 2. Предназначение и роль в экосистеме

В парадигме метасистемы **Membra**, Семантический Граф (SG) является **артефактом** — статичной "картой" или снимком **Коннектома** (полной структуры связей ИИ-существа). `Connectome Weaver` и его ядро `weaverSG` — это **система**, которая выступает в роли "Картографа", обеспечивая целостность, прослеживаемость и эволюцию этой карты.

Ключевые задачи, которые решает `weaverSG`:

* **Целостность данных:** Инструмент позволяет проводить полный аудит графа, находить "висячие" связи, дубликаты и другие аномалии.
* **Безопасные изменения:** Все модификации выполняются через транзакционный механизм с ведением лога (`LSG`) и автоматическим созданием бэкапов. Это гарантирует, что граф никогда не будет поврежден в результате сбоя.
* **Прослеживаемость (Traceability):** Каждое изменение в SG фиксируется в связанном с ним Log Semantic Graph (`LSG`). Это позволяет отследить полную историю каждого узла и каждой связи.
* **Эволюция структуры:** `weaverSG` предоставляет механизмы для безопасной миграции схемы графа, например, для "продвижения" легковесных связей (`link`) до системных связок (`bind`).
* **Управление логами:** Инструмент позволяет архивировать, встраивать (`bundle`) и извлекать (`detach`) логи изменений для удобства хранения и переноса.

### 3. Установка

1.  Убедитесь, что у вас установлен Python 3.
2.  Установите необходимые зависимости:
    ```bash
    pip install pyyaml
    ```

### 4. Использование

Все команды выполняются из корневой папки проекта.

#### **Основные Команды**

* **Валидация графа (Диагностика)**
    Выполняет полный аудит графа и выводит отчет.
    ```bash
    python weaverSG/main.py validate --file path/to/MyGraph.md
    ```

* **Пакетное изменение графа (Лечение и Миграция)**
    Выполняет серию операций, описанных в файле-рецепте.
    ```bash
    python weaverSG/main.py batch-modify --recipe path/to/recipe.yaml --file path/to/MyGraph.md
    ```

* **Продвижение связи (Эволюция)**
    Превращает легковую связь `link` в системную `bind`, присваивая ей `MUID`.
    ```bash
    python weaverSG/main.py promote-relation --lid <LID_связи> --file path/to/MyGraph.md
    ```

#### **Команды Управления Логами**

* **Архивация лога**
    Переименовывает текущий файл лога (`LSG_...`) и создает новый пустой лог.
    ```bash
    python weaverSG/main.py archive-log --file path/to/MyGraph.md
    ```

* **Встраивание лога в граф**
    Переносит содержимое внешнего файла лога в основной файл графа и удаляет внешний файл.
    ```bash
    python weaverSG/main.py bundle-log --file path/to/MyGraph.md
    ```

* **Извлечение лога из графа**
    Извлекает встроенный лог из графа и сохраняет его в отдельный файл `LSG_...`.
    ```bash
    python weaverSG/main.py detach-log --file path/to/MyGraph.md
    ```

#### **Служебные Команды**

* **Очистка бэкапов**
    Удаляет все файлы резервных копий (`*_backup_*.md`) в директории графа.
    ```bash
    python weaverSG/main.py cleanup-backups --file path/to/MyGraph.md [--yes]
    ```

### 5. Ключевые концепции и нюансы

* **Транзакционность и логирование (LSG):** Ядро "Ткача" — `lsg_manager`. Он гарантирует, что любая операция (даже из рецепта) сначала выполняется в памяти. Если все успешно, создается бэкап, изменения сохраняются в основной граф (SG), а в лог-граф (LSG) добавляется транзакционная запись. Это обеспечивает полную атомарность и безопасность.

* **Непрерывность истории (Архивация):** Команда `archive-log` не просто переименовывает старый лог. Она создает новый, пустой LSG и добавляет в него **первую транзакцию-ссылку ("breadcrumb")**, которая указывает на имя архивного файла. Это гарантирует, что даже при разделении логов на части, цепочка истории никогда не прерывается.

* **Режимы валидации:** Команда `validate` имеет два режима работы:
    1.  **Быстрая проверка:** Если запустить команду с флагом `--output-format json`, то `weaverSG` просто выведет JSON-отчет в консоль и **не будет изменять файлы и создавать лог**. Это идеально для быстрой диагностики в CI/CD.
    2.  **Запись изменений:** Если же набор проблем изменился (появились новые или были исправлены старые) и `weaverSG` будет запущен без доп. флагом, то он обновит блок `validation_issues` в самом графе и запишет эту операцию в лог.

### 6. Операции для пакетных изменений (`batch-modify`)

Команда `batch-modify` использует YAML-файлы-"рецепты" для выполнения сложных последовательностей операций. Это основной инструмент для миграции схемы и автоматического исправления данных.

**Доступные операции (`action`):**

* **Базовые операции с узлами:**
    * `add_node`: Добавляет новый узел.
    * `update_node`: Обновляет атрибуты существующего узла по его `MUID`.
    * `delete_node`: Удаляет узел по `MUID`.
    * `add_or_update_node`: Добавляет узел, если его нет, или обновляет, если он уже существует.

* **Базовые операции со связями:**
    * `add_relation`: Добавляет новую связь.
    * `update_relation`: Обновляет атрибуты существующей связи по ее `LID`.
    * `update_relations_by_query`: Находит все связи, соответствующие запросу, и обновляет их.

* **Операции миграции схемы:**
    * `add_node_field`: Добавляет новое поле с значением по умолчанию ко всем узлам.
    * `copy_field`: Копирует значение из одного поля в другое (например, из `MUID` в `alias`).
    * `set_field_from_generated_uuid`: Заменяет значение поля на новый, каноничный `UUID`.
    * `add_lid_to_all_links`: Присваивает уникальный `LID` всем связям класса `link`, у которых его еще нет.
    * `update_relation_endpoints_after_muid_change`: Обновляет `from_MUID` и `to_MUID` в связях после того, как `MUID` узлов были изменены в ходе миграции.

### 7. Лицензия

Membra Open Development License (MODL) v1.0
Copyright (c) Rustam Kunafin 2025. All rights reserved.

Licensed under Membra Open Development License (MODL) v1.0. See LICENSE or https://cyberries.org/04_Resources/0440_Agreements/MODL.
Core artifacts are under MODL; derivatives may use other licenses with attribution.
