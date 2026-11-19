#!/usr/bin/env python3
"""Generates the showcase visuals of asrp.media-documents (never hand-edit the SVG output; edit this file).

    python3 tools/build_visuals.py

Output (English and Russian twin for every picture)
    guide/assets/banner/hero-banner.{en,ru}.svg           generated illustration, not a screenshot
    guide/assets/diagrams/topics-map.{en,ru}.svg          documents per topic (computed)
    guide/assets/diagrams/hub-flow.{en,ru}.svg            export -> migration -> document folders -> topics/catalog
    guide/assets/diagrams/evidence-layers.{en,ru}.svg     what the repository shows / what articles say / what is not here
    guide/assets/diagrams/doc-anatomy.{en,ru}.svg         the files of one documents/<slug>/ folder
    guide/assets/icons/*.svg                              navigation icons

Every number comes from tools/facts.py (computed from the repository). Text is measured and must fit
(the build aborts otherwise); a status is a word paired with a shape, never colour alone.
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svgkit import *  # noqa: E402,F401,F403
import facts as factsmod  # noqa: E402

F = factsmod.facts()

TOPIC_NAMES = {
    "lucid-dreaming": ("Lucid Dreaming", "Осознанные сновидения"),
    "technology-and-ai": ("Technology and AI", "Технологии и ИИ"),
    "history-and-philosophy": ("History and Philosophy", "История и философия"),
    "health-and-sleep": ("Health and Sleep", "Здоровье и сон"),
    "blockjam-2025": ("BlockJam 2025", "BlockJam 2025"),
    "uap-and-cosmology": ("UAP and Cosmology", "UAP и космология"),
    "art-and-culture": ("Art and Culture", "Искусство и культура"),
    "markets-and-web3": ("Markets and Web3", "Рынки и Web3"),
    "research-methods": ("Research Methods", "Методы исследований"),
}

L = {"en": 0, "ru": 1}


def lang_pick(pair, lang):
    return pair[L[lang]]


def foot(cv, text_, bottom, color=MUTED):
    lines = wrap(text_, FS_SMALL, cv.w - 48)
    y = bottom - 20 * (len(lines) - 1)
    for i, ln in enumerate(lines):
        cv.label(24, y + 20 * i, ln, FS_SMALL, color, box=cv.w - 48)


# --- hero banner -----------------------------------------------------------------------------
def banner(lang):
    t = {
        "en": ("ASRP Media Documents", "KNOWLEDGE HUB", "PUBLIC REPOSITORY · A CATALOG, NOT A STUDY",
               ["Migrated media, SMM and publication", "articles, by topic, in EN and RU"],
               ["{docs} documents · {topics} topics", "EN + RU bodies", "{image_meta} image records, no binaries"],
               "dot = documents of one topic"),
        "ru": ("Медиа-документы ASRP", "ХАБ ЗНАНИЙ", "ПУБЛИЧНЫЙ РЕПОЗИТОРИЙ · КАТАЛОГ, НЕ ИССЛЕДОВАНИЕ",
               ["Мигрированные медиа-, SMM- и публикационные", "статьи по темам, на EN и RU"],
               ["{docs} документов · {topics} тем", "тексты EN + RU", "{image_meta} записей об изображениях"],
               "точка = документ темы"),
    }[lang]
    desc = {
        "en": "Generated illustration, not a screenshot. A hub ring with {topics} topic nodes whose dots count the documents of each topic "
              "({counts}), the title, and three figures computed from the repository: {docs} documents in {topics} topics, English and "
              "Russian bodies, {image_meta} image metadata records without binaries.",
        "ru": "Сгенерированная иллюстрация, не скриншот. Кольцо хаба с {topics} узлами-темами, точки показывают число документов темы "
              "({counts}), заголовок и три числа, посчитанные по репозиторию: {docs} документов в {topics} темах, тексты на английском и "
              "русском, {image_meta} записей о метаданных изображений без бинарных файлов.",
    }[lang]
    items = list(F["topics_by_slug"].items())
    desc = desc.format(counts=", ".join(str(n) for _, n in items), **F)
    W, H = 1200, 330
    o = [svg_open(W, H, t[0], desc)]
    cx, cy, R = 270, 165, 110
    cols = [GOLD, TEAL, VIOLET, GREEN, BLUE, AMBER, GOLD, TEAL, VIOLET]
    o.append("<circle cx='%d' cy='%d' r='%d' fill='none' stroke='%s' stroke-opacity='0.55'/>" % (cx, cy, R, LINE))
    for i, (slug, n) in enumerate(items):
        a = math.radians(-90 + 360 * i / len(items))
        x, y = cx + R * math.cos(a), cy + R * math.sin(a)
        o.append("<line x1='%d' y1='%d' x2='%.1f' y2='%.1f' stroke='%s' stroke-width='1.4' stroke-opacity='0.7' stroke-dasharray='5 7'>"
                 "<animate attributeName='stroke-dashoffset' from='24' to='0' dur='%.1fs' repeatCount='indefinite'/></line>"
                 % (cx, cy, x, y, cols[i], 2.2 + 0.2 * i))
        o.append("<circle cx='%.1f' cy='%.1f' r='%d' fill='%s' stroke='%s' stroke-width='2.4'/>" % (x, y, 7 + 2 * n if n < 6 else 19, BG0, cols[i]))
        o.append(text("%.1f" % x, "%.1f" % (y + 5), str(n), FS_SMALL, INK, "middle", 700))
    o.append("<circle cx='%d' cy='%d' r='34' fill='%s' stroke='%s' stroke-width='2' filter='url(#glow)'/>" % (cx, cy, PANEL, TEAL))
    o.append(text(cx, cy + 6, "%d" % F["docs"], 20, INK, "middle", 800))
    tx = 520
    box = W - tx - 36
    o.append(text(tx, 66, t[1], FS_KICKER, TEAL, "start", 700, 2, box))
    o.append(text(W - 36, 36, t[2], FS_SMALL, MUTED, "end", 700, 1, 620))
    o.append(text(tx, 128, t[0], 46, INK, "start", 800, 0, box))
    for i, line in enumerate(t[3]):
        o.append(text(tx, 170 + 28 * i, line, 21, MUTED, "start", 400, 0, box))
    x = tx
    for i, chip in enumerate(t[4]):
        chip = chip.format(**F)
        w = text_width(chip, FS_KICKER, True) + 28
        if x + w > W - 30:
            raise SystemExit("chips overflow the banner: %r" % chip)
        col = [GOLD, TEAL, GREEN][i]
        o.append("<rect x='%.1f' y='246' width='%.1f' height='38' rx='19' fill='%s' fill-opacity='0.08' stroke='%s'/>" % (x, w, col, col))
        o.append(text("%.1f" % (x + w / 2), 271, chip, FS_KICKER, INK, "middle", 700))
        x += w + 12
    o.append(text(24, H - 14, t[5], FS_SMALL, MUTED, "start", 400, 0, 460))
    o.append("</svg>\n")
    return "\n".join(o)


# --- topics map ------------------------------------------------------------------------------
def topics_map(lang):
    title = {"en": "Documents per topic", "ru": "Документов по темам"}[lang]
    sub = {"en": "Bar length = number of documents in the topic", "ru": "Длина полосы = число документов темы"}[lang]
    items = list(F["topics_by_slug"].items())
    desc = {"en": "Horizontal bars, one per topic, counted from documents/*/metadata.yaml: %s. Total %d documents."
                  % ("; ".join("%s %d" % (TOPIC_NAMES[s][0], n) for s, n in items), F["docs"]),
            "ru": "Горизонтальные полосы по темам, посчитаны по documents/*/metadata.yaml: %s. Всего %d документов."
                  % ("; ".join("%s %d" % (TOPIC_NAMES[s][1], n) for s, n in items), F["docs"])}[lang]
    W = 1000
    H = 120 + 42 * len(items) + 70
    cv = Canvas(W, H, title, desc, title, sub, {"en": "TOPICS", "ru": "ТЕМЫ"}[lang])
    maxn = max(n for _, n in items)
    x0, bw = 290, 560
    cols = [GOLD, TEAL, VIOLET, GREEN, BLUE, AMBER, GOLD, TEAL, VIOLET]
    for i, (slug, n) in enumerate(items):
        y = 100 + 42 * i
        cv.label(24, y + 22, lang_pick(TOPIC_NAMES[slug], lang), FS_BODY, INK, weight=600, box=250)
        w = bw * n / maxn
        cv.add("<rect x='%d' y='%d' width='%.1f' height='28' rx='8' fill='%s' fill-opacity='0.85'/>" % (x0, y, w, cols[i]))
        cv.label(x0 + w + 12, y + 21, str(n), FS_BODY, INK, weight=700)
    foot(cv, {"en": "Total: %d documents in %d topics. Source: documents/*/metadata.yaml (topic_slug)." % (F["docs"], F["topics"]),
              "ru": "Всего: %d документов в %d темах. Источник: documents/*/metadata.yaml (topic_slug)." % (F["docs"], F["topics"])}[lang], H - 18)
    return "\n".join(cv.o + ["</svg>\n"])


# --- hub flow --------------------------------------------------------------------------------
def hub_flow(lang):
    en = lang == "en"
    title = "How the hub was made" if en else "Как собран хаб"
    sub = "From the platform exports to the pages you read" if en else "От экспортов платформы к страницам, которые вы читаете"
    desc = ("Four stages left to right. Stage 1: three source export files named in metadata.yaml, not stored in this repository (listed "
            "in .gitignore). Stage 2: migration filter, English and Russian bodies only, image metadata only. Stage 3: %d documents/<slug>/ folders. "
            "Stage 4: %d topic pages and the documents catalog, entered from README.md." % (F["docs"], F["topic_pages"])
            if en else
            "Четыре этапа слева направо. Этап 1: три файла экспорта из metadata.yaml, в репозитории не хранятся (перечислены в .gitignore). "
            "Этап 2: фильтр миграции, только тексты на английском и русском, для изображений только метаданные. Этап 3: %d папок documents/<slug>/. "
            "Этап 4: %d страниц тем и каталог документов, вход из README.md." % (F["docs"], F["topic_pages"]))
    W, H = 1180, 400
    cv = Canvas(W, H, title, desc, title, sub, "FLOW" if en else "ПОТОК")
    bw, gap, y = 260, 40, 110
    xs = [24 + i * (bw + gap) for i in range(4)]
    st = {"absent": ("✕ NOT IN THIS REPOSITORY", AMBER) if en else ("✕ НЕТ В РЕПОЗИТОРИИ", AMBER),
          "avail": ("✓ IN THIS REPOSITORY", GREEN) if en else ("✓ ЕСТЬ В РЕПОЗИТОРИИ", GREEN)}
    boxes = [
        (("1 · Source exports", ["3 JSON files named in metadata.yaml", "documents, contents, drafts (export stamp 202606241032)"], st["absent"], VIOLET) if en else
         ("1 · Экспорты источника", ["3 JSON-файла из metadata.yaml", "документы, тексты, черновики (метка 202606241032)"], st["absent"], VIOLET)),
        (("2 · Migration filter", ["EN and RU bodies only", "image records: metadata only, no binaries"], st["avail"], TEAL) if en else
         ("2 · Фильтр миграции", ["только тексты EN и RU", "изображения: только метаданные, без бинарных файлов"], st["avail"], TEAL)),
        (("3 · documents/<slug>/", ["%d folders: card, bodies, index, metadata, images" % F["docs"], "traceability to the source id"], st["avail"], GOLD) if en else
         ("3 · documents/<slug>/", ["%d папок: карточка, тексты, index, метаданные, изображения" % F["docs"], "трассировка к исходному id"], st["avail"], GOLD)),
        (("4 · Topics and catalog", ["%d topic pages + documents/README.md" % F["topic_pages"], "entered from README.md"], st["avail"], GREEN) if en else
         ("4 · Темы и каталог", ["%d страниц тем + documents/README.md" % F["topic_pages"], "вход из README.md"], st["avail"], GREEN)),
    ]
    for x, (ttl, lines, status, col) in zip(xs, boxes):
        cv.box(x, y, bw, ttl, lines, [status], stroke=col, h=190, valign="top")
    for i in range(3):
        cv.arrow([(xs[i] + bw, y + 95), (xs[i + 1], y + 95)], color=TEAL)
    foot(cv, "The exports are named in metadata.yaml (source_exports); the repository does not contain them, so the migration cannot be re-run from here."
         if en else "Экспорты названы в metadata.yaml (source_exports); в репозитории их нет, поэтому миграцию отсюда повторить нельзя.", H - 18)
    return "\n".join(cv.o + ["</svg>\n"])


# --- evidence layers -------------------------------------------------------------------------
def evidence(lang):
    en = lang == "en"
    title = "Three layers, never blended" if en else "Три слоя, которые не смешиваются"
    sub = "What the repository shows, what articles say, what is not here" if en else "Что показывает репозиторий, что говорят статьи, чего здесь нет"
    desc = ("Three columns. Left, shown by the repository: %d document folders, %d topics, %d interviews, %d articles, %d research pieces, "
            "traceability metadata. Middle, said inside articles and attributed to their authors: patent, trademark, health and classified-archive "
            "statements, none backed by a document here. Right, not in the repository: the export files, image binaries, patent and trademark documents."
            % (F["docs"], F["topics"], F["interview"], F["article"], F["research"]) if en else
            "Три колонки. Слева показано репозиторием: %d папок документов, %d тем, %d интервью, %d статей, %d исследовательских текстов, "
            "метаданные трассировки. В центре сказано внутри статей и приписано их авторам: заявления о патенте, товарном знаке, здоровье и "
            "засекреченном архиве, ни одно не подтверждено документом здесь. Справа чего нет в репозитории: файлов экспорта, изображений, "
            "документов о патентах и товарном знаке." % (F["docs"], F["topics"], F["interview"], F["article"], F["research"]))
    W, H = 1180, 440
    cv = Canvas(W, H, title, desc, title, sub, "EVIDENCE" if en else "ДОКАЗАТЕЛЬСТВА")
    bw, gap, y = 350, 40, 105
    xs = [24 + i * (bw + gap) for i in range(3)]
    cols = [GREEN, GOLD, AMBER]
    if en:
        data = [("✓ Shown by the repository", ["%d document folders in %d topics" % (F["docs"], F["topics"]),
                 "%d interviews · %d articles · %d research pieces" % (F["interview"], F["article"], F["research"]),
                 "EN and RU bodies for every document", "source id and timestamps per document (metadata.yaml)"]),
                ("◇ Said inside articles", ["a patent application was submitted; something was \"patented\"",
                 "a trademark certificate is claimed", "health benefit of a method; classified archives",
                 "each statement is the author's; no document backs it here"]),
                ("✕ Not in the repository", ["the 3 source export files", "image binaries (%d records, 0 files)" % F["image_meta"],
                 "patent and trademark documents or status", "any result, dataset or protocol"])]
    else:
        data = [("✓ Показано репозиторием", ["%d папок документов в %d темах" % (F["docs"], F["topics"]),
                 "%d интервью · %d статей · %d исследовательских текстов" % (F["interview"], F["article"], F["research"]),
                 "тексты EN и RU для каждого документа", "исходный id и даты на документ (metadata.yaml)"]),
                ("◇ Сказано внутри статей", ["подана заявка на патент; что-то «запатентовано»",
                 "заявлено свидетельство на товарный знак", "польза метода для здоровья; засекреченные архивы",
                 "каждое утверждение принадлежит автору; документа в репозитории нет"]),
                ("✕ Нет в репозитории", ["3 файла экспорта источника", "бинарных изображений (%d записей, 0 файлов)" % F["image_meta"],
                 "документов и статуса по патентам и товарному знаку", "результатов, данных и протоколов"])]
    for x, (ttl, lines), col in zip(xs, data, cols):
        cv.box(x, y, bw, ttl, lines, [], stroke=col, h=250, valign="top", title_size=17)
    foot(cv, "Articles are published media texts: they report views of their authors and are not verified scientific claims (README disclaimer)."
         if en else "Статьи это опубликованные медиатексты: они передают позиции авторов и не являются проверенными научными утверждениями (отказ от ответственности в README).", H - 18)
    return "\n".join(cv.o + ["</svg>\n"])


# --- anatomy of one document folder -----------------------------------------------------------
def anatomy(lang):
    en = lang == "en"
    title = "One document folder" if en else "Одна папка документа"
    sub = "documents/<slug>/ - the same five parts, %d times" % F["docs"] if en else "documents/<slug>/ - одни и те же пять частей, %d раз" % F["docs"]
    desc = ("A folder documents/<slug>/ with five parts: README.md summary card, content.en.md English body, content.ru.md Russian body, "
            "index.md both languages in one page, metadata.yaml source traceability, and images/<name>/metadata.yaml image records. "
            "Counts: %d cards, %d English bodies, %d Russian bodies, %d index pages, %d image records." % (
                F["doc_readmes"], F["en_bodies"], F["ru_bodies"], F["index_md"], F["image_meta"]) if en else
            "Папка documents/<slug>/ из пяти частей: README.md карточка, content.en.md английский текст, content.ru.md русский текст, "
            "index.md оба языка на одной странице, metadata.yaml трассировка источника, images/<имя>/metadata.yaml записи об изображениях. "
            "Количество: %d карточек, %d английских текстов, %d русских текстов, %d страниц index, %d записей об изображениях." % (
                F["doc_readmes"], F["en_bodies"], F["ru_bodies"], F["index_md"], F["image_meta"]))
    W, H = 1180, 330
    cv = Canvas(W, H, title, desc, title, sub, "ANATOMY" if en else "УСТРОЙСТВО")
    parts = ([("README.md", "summary card", "%d" % F["doc_readmes"], GOLD), ("content.en.md", "English body", "%d" % F["en_bodies"], TEAL),
              ("content.ru.md", "Russian body", "%d" % F["ru_bodies"], TEAL), ("index.md", "EN + RU on one page", "%d" % F["index_md"], VIOLET),
              ("metadata.yaml", "source traceability", "%d" % F["docs"], GREEN)] if en else
             [("README.md", "карточка-сводка", "%d" % F["doc_readmes"], GOLD), ("content.en.md", "английский текст", "%d" % F["en_bodies"], TEAL),
              ("content.ru.md", "русский текст", "%d" % F["ru_bodies"], TEAL), ("index.md", "EN + RU на одной странице", "%d" % F["index_md"], VIOLET),
              ("metadata.yaml", "трассировка источника", "%d" % F["docs"], GREEN)])
    bw, gap = 200, 20
    for i, (name, what, n, col) in enumerate(parts):
        x = 24 + i * (bw + gap)
        cv.box(x, 105, bw, name, [what], [("%s %s" % (n, "files" if en else "файлов"), col)], stroke=col, h=110, center=True)
    cv.box(24, 235, 1132 - 0, ("images/<name>/metadata.yaml - %d image records, 0 binaries" % F["image_meta"]) if en else
           ("images/<имя>/metadata.yaml: %d записей, 0 файлов изображений" % F["image_meta"]), [], [], stroke=AMBER, h=48, center=True)
    foot(cv, "README.md is a card, not the article: full text is in content.en.md / content.ru.md." if en else
         "README.md это карточка, не статья: полный текст в content.en.md / content.ru.md.", H - 14)
    return "\n".join(cv.o + ["</svg>\n"])


# --- icons -----------------------------------------------------------------------------------
def icon(col, body, title):
    return ("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 64 64\" width=\"64\" height=\"64\" role=\"img\">\n"
            "<title>%s</title>\n<desc>Navigation icon: %s.</desc>\n<rect x=\"2\" y=\"2\" width=\"60\" height=\"60\" rx=\"12\" fill=\"#101826\" "
            "stroke=\"%s\" stroke-width=\"3\"/>\n<g fill='none' stroke='%s' stroke-width='2.6' stroke-linecap='round' "
            "stroke-linejoin='round'>%s</g>\n</svg>\n" % (title, title, col, col, body))


ICONS = {
    "hub": (TEAL, "<circle cx='32' cy='32' r='6'/><circle cx='32' cy='14' r='4'/><circle cx='49' cy='26' r='4'/><circle cx='43' cy='47' r='4'/>"
                  "<circle cx='21' cy='47' r='4'/><circle cx='15' cy='26' r='4'/><path d='M32 26V18M38 30l8-3M36 37l5 7M28 37l-5 7M26 30l-8-3'/>", "the hub"),
    "topics": (GOLD, "<rect x='13' y='14' width='16' height='16' rx='3'/><rect x='35' y='14' width='16' height='16' rx='3'/>"
                     "<rect x='13' y='36' width='16' height='14' rx='3'/><rect x='35' y='36' width='16' height='14' rx='3'/>", "topics"),
    "documents": (VIOLET, "<rect x='16' y='12' width='32' height='40' rx='4'/><path d='M23 22h18M23 30h18M23 38h10'/>", "documents"),
    "navigation": (GREEN, "<path d='M20 14v36M20 22h10M20 34h10M20 46h10'/><rect x='30' y='17' width='20' height='10' rx='2'/>"
                          "<rect x='30' y='29' width='20' height='10' rx='2'/><rect x='30' y='41' width='20' height='10' rx='2'/>", "navigation"),
    "evidence": (AMBER, "<circle cx='28' cy='28' r='13'/><path d='M38 38l12 12M23 28l4 4 7-8'/>", "claims and evidence"),
    "ecosystem": (BLUE, "<circle cx='32' cy='32' r='6'/><circle cx='32' cy='14' r='4'/><circle cx='48' cy='41' r='4'/>"
                        "<circle cx='16' cy='41' r='4'/><path d='M32 26V18M37 35l8 4M27 35l-8 4'/>", "ecosystem and IP"),
    "open": (GOLD, "<circle cx='32' cy='32' r='18'/><path d='M26 27a6 6 0 1 1 9 5c-2 1-3 2-3 4M32 43v2'/>", "open questions"),
    "figures": (TEAL, "<rect x='12' y='16' width='40' height='32' rx='4'/><path d='M12 38l11-10 9 8 7-6 13 10'/><circle cx='42' cy='25' r='3'/>", "figures"),
    "archive": (MUTED, "<rect x='12' y='14' width='40' height='11' rx='3'/><path d='M16 25v25h32V25M26 34h12'/>", "archive"),
}


def main():
    for lang in ("en", "ru"):
        write("guide/assets/banner/hero-banner.%s.svg" % lang, banner(lang))
        write("guide/assets/diagrams/topics-map.%s.svg" % lang, topics_map(lang))
        write("guide/assets/diagrams/hub-flow.%s.svg" % lang, hub_flow(lang))
        write("guide/assets/diagrams/evidence-layers.%s.svg" % lang, evidence(lang))
        write("guide/assets/diagrams/doc-anatomy.%s.svg" % lang, anatomy(lang))
    for name, (col, body, title) in ICONS.items():
        write("guide/assets/icons/%s.svg" % name, icon(col, body, title))


if __name__ == "__main__":
    main()
