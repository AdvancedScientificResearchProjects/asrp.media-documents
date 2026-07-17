# ASRP MEDIA DOCUMENTS KNOWLEDGE HUB
# ХАБ МЕДИА-ДОКУМЕНТОВ ASRP

**Bilingual navigation hub for migrated ASRP media, SMM, and publication articles (EN / RU)**
**Двуязычный навигационный хаб мигрированных медиа-, SMM- и публикационных статей ASRP (EN / RU)**

---

<div align="center">

| Repository / Репозиторий | Status / Статус |
|-------------------------|----------------|
| `asrp.media-documents` | ACTIVE / АКТИВЕН |

**Organization / Организация:** Advanced Scientific Research Projects (ASRP)

[![ASRP](https://img.shields.io/badge/ASRP-Research-blue)](https://github.com/AdvancedScientificResearchProjects)
[![Language](https://img.shields.io/badge/Language-EN%2F%2FRU-brightgreen)]()
[![Status](https://img.shields.io/badge/Status-Active-success)]()
[![Mode](https://img.shields.io/badge/Mode-Hub-informational)]()

**Part of Advanced Scientific Research Projects (ASRP) Ecosystem / Часть Экосистемы Advanced Scientific Research Projects (ASRP)**

</div>

---

<div align="center">

[![💛 Support our work / Поддержать](https://img.shields.io/badge/💛%20Support%20our%20work-asrp.tech%2Fpatrons-FBBF24?style=for-the-badge)](https://asrp.tech/en/patrons)

> **EN:** **If this work is valuable to you — support us.** 7 patron tiers from Principal Philanthropist to Individual Contributor.
> **RU:** **Если эта работа вам полезна — поддержите нас.** 7 уровней меценатства — от Главного Филантропа до Индивидуального Вкладчика.
>
> **Support / Поддержать:** <https://asrp.tech/en/patrons>
> **Investment inquiries / Инвестиционные запросы:** _pending — provide URL when available / в ожидании — добавляется при предоставлении_

</div>

---

## QUICK NAVIGATION / БЫСТРАЯ НАВИГАЦИЯ

| Section / Раздел | Description / Описание | Status / Статус |
|------------------|------------------------|-----------------|
| [Overview / Обзор](#overview--обзор) | What this hub is and how it is organized / Что это за хаб и как он устроен | Available / Доступно |
| [Documents by Topic / Документы по темам](#documents-by-topic--документы-по-темам) | 29 articles across 9 topics / 29 статей по 9 темам | Available / Доступно |
| [Documents Catalog / Каталог документов](#documents-catalog--каталог-документов) | Full per-document catalog (EN / RU) / Полный каталог по документам (EN / RU) | Available / Доступно |
| [Structure / Структура](#structure--структура) | Repository folder tree / Дерево папок репозитория | Available / Доступно |
| [Security / Безопасность](#security--безопасность) | Data classification / Классификация данных | Standard / Стандартно |
| [ASRP Ecosystem / Экосистема ASRP](#asrp-ecosystem--экосистема-asrp) | Related repos + patents / Связанные репозитории и патенты | Available / Доступно |
| [Contact / Контакты](#contact-information--контактная-информация) | Org contact block / Корпоративные контакты | Available / Доступно |

---

## OVERVIEW / ОБЗОР

### ENGLISH

This repository is a **bilingual (EN / RU) navigation hub** for **29 migrated ASRP media, SMM, and publication articles**. It is a media/knowledge catalog, **not** an experimental study — there are no protocols or experimental-design sections here.

Each migrated article lives in its own `documents/<slug>/` folder with a summary-card `README.md`, full bodies as `content.en.md` and/or `content.ru.md`, a traceability `metadata.yaml`, and image-metadata folders. Article bodies are preserved only for English and Russian source content; other languages from the original exports were intentionally not migrated. Image binaries were not present in the export, so image folders record metadata only (source paths and usage context).

Navigation is topic-first: the **Topics index** and the **Documents catalog** are the central entry points. The hub groups the 29 documents across 9 practical themes — from lucid dreaming and sleep physiology to BlockJam 2025, Web3/markets, and UAP/cosmology.

### РУССКИЙ

Этот репозиторий — **двуязычный (EN / RU) навигационный хаб** для **29 мигрированных медиа-, SMM- и публикационных статей ASRP**. Это медиа-/знаниевый каталог, **а не** экспериментальное исследование — здесь нет протоколов или разделов с планом экспериментов.

Каждая мигрированная статья находится в собственной папке `documents/<slug>/` с карточкой-сводкой `README.md`, полными текстами `content.en.md` и/или `content.ru.md`, файлом трассировки `metadata.yaml` и папками с метаданными изображений. Тексты статей сохранены только для англо- и русскоязычного исходного контента; прочие языки из исходных экспортов намеренно не мигрировались. Бинарные файлы изображений отсутствовали в экспорте, поэтому папки изображений содержат только метаданные (исходные пути и контекст использования).

Навигация построена от тем: **Индекс тем** и **Каталог документов** — центральные точки входа. Хаб распределяет 29 документов по 9 практическим темам — от осознанных сновидений и физиологии сна до BlockJam 2025, Web3/рынков и UAP/космологии.

---

## DOCUMENTS BY TOPIC / ДОКУМЕНТЫ ПО ТЕМАМ

| Topic / Тема | Docs / Документов | Lead file / Главный файл |
|---|---:|---|
| Lucid Dreaming / Осознанные сновидения | 10 | [`topics/lucid-dreaming.md`](topics/lucid-dreaming.md) |
| Technology and AI / Технологии и ИИ | 5 | [`topics/technology-and-ai.md`](topics/technology-and-ai.md) |
| History and Philosophy / История и философия | 4 | [`topics/history-and-philosophy.md`](topics/history-and-philosophy.md) |
| Health and Sleep / Здоровье и сон | 3 | [`topics/health-and-sleep.md`](topics/health-and-sleep.md) |
| BlockJam 2025 / BlockJam 2025 | 2 | [`topics/blockjam-2025.md`](topics/blockjam-2025.md) |
| UAP and Cosmology / UAP и космология | 2 | [`topics/uap-and-cosmology.md`](topics/uap-and-cosmology.md) |
| Art and Culture / Искусство и культура | 1 | [`topics/art-and-culture.md`](topics/art-and-culture.md) |
| Markets and Web3 / Рынки и Web3 | 1 | [`topics/markets-and-web3.md`](topics/markets-and-web3.md) |
| Research Methods / Методы исследований | 1 | [`topics/research-methods.md`](topics/research-methods.md) |
| **Total / Всего** | **29** | [`topics/README.md`](topics/README.md) |

**EN:** Open any topic page for the list of articles in that theme, or use the full catalog below for the complete per-document index with source IDs, types, and status.

**RU:** Откройте страницу темы, чтобы увидеть список статей в ней, либо воспользуйтесь полным каталогом ниже для индекса по всем документам с исходными ID, типами и статусом.

---

## DOCUMENTS CATALOG / КАТАЛОГ ДОКУМЕНТОВ

**EN:** The complete catalog of all **29** migrated documents — each with a summary card and full EN / RU bodies — lives in [`documents/README.md`](documents/README.md). The catalog lists title, source type (`interview` / `article` / `research`), source status (`published` / `todo`), topic, available languages, and source ID.

- **Interviews / Интервью:** 18 · **Articles / Статьи:** 9 · **Research / Исследования:** 2
- **Source status `published` / Опубликовано в источнике:** 4 · **Source status `todo` / В работе в источнике:** 25
- **Available translations / Доступные переводы:** English (EN) and Russian (RU) for every document / Английский (EN) и русский (RU) для каждого документа

**RU:** Полный каталог всех **29** мигрированных документов — с карточкой-сводкой и полными текстами EN / RU — находится в [`documents/README.md`](documents/README.md). В каталоге указаны название, тип источника (`interview` / `article` / `research`), статус источника (`published` / `todo`), тема, доступные языки и исходный ID.

---

## STRUCTURE / СТРУКТУРА

```
asrp.media-documents/
├── README.md                     # This hub README / Этот хаб-README
├── metadata.yaml                 # Machine-readable hub metadata / Машинно-читаемые метаданные хаба
├── documents/
│   ├── README.md                 # Full documents catalog / Полный каталог документов
│   └── <slug>/                   # One folder per article / Папка на статью
│       ├── README.md             # Summary card / Карточка-сводка
│       ├── content.en.md         # English body (where migrated) / Английский текст
│       ├── content.ru.md         # Russian body (where migrated) / Русский текст
│       ├── metadata.yaml         # Source traceability / Трассировка источника
│       └── images/<slug>/
│           └── metadata.yaml     # Image metadata only (no binaries) / Только метаданные
└── topics/
    ├── README.md                 # Topics index / Индекс тем
    └── <topic>.md                # One page per topic / Страница на тему
```

**EN:** Each `documents/<slug>/` folder is self-contained. `README.md` files are summary cards, not full article bodies — full bodies live in `content.en.md` / `content.ru.md`. `metadata.yaml` files preserve source traceability (export filenames, source IDs, language rows). Source exports referenced by traceability: `documents_202606241032.json`, `documents_content_202606241032.json`, `document_draft_contents_202606241032.json`.

**RU:** Каждая папка `documents/<slug>/` самодостаточна. Файлы `README.md` — это карточки-сводки, а не полные тексты статей; полные тексты находятся в `content.en.md` / `content.ru.md`. Файлы `metadata.yaml` сохраняют трассировку источника (имена файлов экспорта, исходные ID, языковые строки). Экспорты-источники, на которые ссылается трассировка: `documents_202606241032.json`, `documents_content_202606241032.json`, `document_draft_contents_202606241032.json`.

---

## SECURITY / БЕЗОПАСНОСТЬ

### Data Classification / Классификация данных

| Level / Уровень | Access / Доступ | Marking / Маркировка | Description / Описание |
|----------------|-----------------|---------------------|----------------------|
| **PUBLIC / ПУБЛИЧНЫЙ** | Open / Открытый | GREEN / ЗЕЛЁНЫЙ | General information / Общая информация |
| **RESEARCH / ИССЛЕДОВАТЕЛЬСКИЙ** | Team Only / Только команда | YELLOW / ЖЁЛТЫЙ | Research data / Исследовательские данные |
| **RESTRICTED / ОГРАНИЧЕННЫЙ** | Core Team / Основная команда | RED / КРАСНЫЙ | Sensitive analysis / Конфиденциальный анализ |
| **INTERNAL / ВНУТРЕННИЙ** | Director Only / Только директор | BLACK / ЧЁРНЫЙ | Director-level review only / Только обзор уровня директора |

> **EN:** Migrated article bodies (`content.en.md` / `content.ru.md`) are **PUBLIC** — they are editorial/educational media content cleared for public reading. Source `metadata.yaml` records export traceability only; it contains no personal data beyond source IDs and publication timestamps.
> **RU:** Тексты статей (`content.en.md` / `content.ru.md`) имеют уровень **ПУБЛИЧНЫЙ** — это редакционный/образовательный медиаконтент, разрешённый для публичного чтения. Файлы `metadata.yaml` содержат только трассировку экспорта; в них нет персональных данных помимо исходных ID и временных меток публикации.

---

## ASRP ECOSYSTEM / ЭКОСИСТЕМА ASRP

<div align="center">

### Related Research Repositories / Связанные исследовательские репозитории

</div>

| Repository / Репозиторий | Direction / Направление | Link / Ссылка |
|-------------------------|------------------------|---------------|
| **ASRP.media (publication platform) / Платформа публикаций** | Media & SMM articles source / Источник медиа- и SMM-статей | _referenced via migrated `source_id` traceability in each `metadata.yaml` / ссылается через исходные `source_id` в каждом `metadata.yaml` |
| **Hyperbolic Field Agricultural Study / Сельскохозяйственное исследование** | Plant & seed growth / Рост растений и семян | [View / Просмотр](https://github.com/AdvancedScientificResearchProjects/Hyperbolic_Field_Agricultural_Study) |
| **UAP Reverse Engineering Study / Исследование по реверс-инжинирингу НАЯ** | Multi-track UAP research hub / Многотрековый хаб исследований НАЯ | [View / Просмотр](https://github.com/AdvancedScientificResearchProjects/UAP_Reverse_Engineering_Study) |
| **ASRP.art** | Art & consciousness / Искусство и сознание | [View / Просмотр](https://github.com/AdvancedScientificResearchProjects/Axionetic_Sensing_Reactions_Platform_in_Art) |

<div align="center">

### Patent Portfolio / Патентный портфель

</div>

> **EN:** This hub is a media/knowledge catalog and is **not itself** the IP basis for any filing. Several migrated articles cover ASRP research programs that **are** patent-grounded; their canonical patents are listed below. No patent filing directly grounds this catalog.
> **RU:** Этот хаб — медиа-/знаниевый каталог и **сам по себе** не является основанием какой-либо заявки. Ряд мигрированных статей освещает исследовательские программы ASRP, имеющие патентную основу; их канонические патенты приведены ниже. Патентная заявка не лежит в основе данного каталога.

| Patent / Патент | Application / Заявка | Link / Ссылка |
|----------------|---------------------|---------------|
| **ASRP.art / ПНИР.искусство** | KZ 2025/0592.1 + PCT | [View / Просмотр](https://github.com/denisbanchenko/Kazpatent_Axionetic_Sensing_Reactions_Platform_in_Art_Patent) |
| **ASRP.drift / ПНИР.дрифт** | KZ 413554 | [View / Просмотр](https://github.com/denisbanchenko/Kazpatent_Advanced_Synchro_Resonance_Platform_For_Deep_Resonant_Patent) |
| **Fractal Biomedical System / Фрактальная биомедицинская система** | KZ 2025/1095.1 | [View / Просмотр](https://github.com/denisbanchenko/Kazpatent_Fractal_Biomedical_System_Patent) |
| **Global Forecasting System (GFS) / Глобальная система прогнозирования** | KZ 2025/1096.1 | [View / Просмотр](https://github.com/denisbanchenko/Kazpatent_Global_Forecasting_System_Patent) |

---

> **Support / Поддержать:** if this work is valuable to you — https://asrp.tech/en/patrons

---

## CONTACT INFORMATION / КОНТАКТНАЯ ИНФОРМАЦИЯ

<div align="center">

### Corporate Contact / Корпоративные контакты

</div>

| Field / Поле | Value / Значение |
|--------------|------------------|
| **Organization / Организация** | ТОО "Перспективные Научно-Исследовательские Разработки" / Advanced Scientific Research Projects LLP |
| **Country / Страна** | Republic of Kazakhstan / Республика Казахстан |
| **Website / Веб-сайт** | [asrp.tech](https://asrp.tech) |
| **Email** | info@asrp.tech |

| Purpose / Цель | Contact / Контакт |
|---------------|------------------|
| **General Inquiries / Общие вопросы** | info@asrp.tech |
| **Research Collaboration / Научное сотрудничество** | info@asrp.tech |
| **Security Issues / Безопасность** | info@asrp.tech |

> **EN:** Contact uses the organization's registered address and `info@asrp.tech` only. No member's personal/home address or personal contact details are published here.
> **RU:** Для связи используются только зарегистрированный адрес организации и `info@asrp.tech`. Личные/домашние адреса или личные контакты участников здесь не публикуются.

---

## DISCLAIMER / ОТКАЗ ОТ ОТВЕТСТВЕННОСТИ

### ENGLISH

This repository is a media/knowledge catalog of migrated editorial articles. Article content reflects its original authors and publication context; it is presented for documentation and navigation, not as verified scientific claims.

### РУССКИЙ

Этот репозиторий — медиа-/знаниевый каталог мигрированных редакционных статей. Содержание статей отражает позиции их авторов и контекст публикации; оно представлено для документирования и навигации, а не как проверенные научные утверждения.

---

**Last Updated / Последнее обновление:** July 2026
**Status / Статус:** The hub actively catalogs 29 migrated bilingual articles across 9 topics / Хаб активно каталогизирует 29 мигрированных двуязычных статей по 9 темам.

---

**ASRP RESEARCH STANDARD v2.1**

---

## NAVIGATION INDEX / НАВИГАЦИОННЫЙ ИНДЕКС

[Overview / Обзор](#overview--обзор) · [Documents by Topic / Документы по темам](#documents-by-topic--документы-по-темам) · [Documents Catalog / Каталог](#documents-catalog--каталог-документов) · [Structure / Структура](#structure--структура) · [Security / Безопасность](#security--безопасность) · [ASRP Ecosystem / Экосистема](#asrp-ecosystem--экосистема-asrp) · [Contact / Контакты](#contact-information--контактная-информация) · [Disclaimer / Отказ](#disclaimer--отказ-от-ответственности)
