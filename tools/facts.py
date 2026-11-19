#!/usr/bin/env python3
"""Facts computed from the repository itself (standard library only).

    python3 tools/facts.py        # prints all facts as JSON

Everything that a showcase page or picture says as a number comes from here: documents, topics, source types and
statuses, languages, image metadata files, sizes. Content files are only read, never written.
"""
import glob
import json
import os
import re
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TAG = "pre-showcase-2026-11"


def read(p):
    return open(os.path.join(ROOT, p), encoding="utf-8").read()


def scalar(text, key):
    m = re.search(r"^%s: (.*)$" % re.escape(key), text, re.M)
    return m.group(1).strip().strip("'\"") if m else None


def pre_files():
    """Tracked files at the base tag (falls back to the working tree when the tag is absent)."""
    r = subprocess.run(["git", "ls-tree", "-r", "--name-only", TAG], cwd=ROOT, capture_output=True, text=True)
    if r.returncode == 0 and r.stdout.strip():
        return r.stdout.split("\n")[:-1]
    out = []
    for top in ("documents", "topics"):
        for dp, _, fs in os.walk(os.path.join(ROOT, top)):
            out += [os.path.relpath(os.path.join(dp, f), ROOT) for f in fs]
    return out + ["README.md", "metadata.yaml", ".gitignore"]


def facts():
    F = {}
    slugs = sorted(d for d in os.listdir(os.path.join(ROOT, "documents")) if os.path.isdir(os.path.join(ROOT, "documents", d)))
    F["docs"] = len(slugs)
    types, status, topics, free = {}, {}, {}, 0
    en = ru = both = 0
    for s in slugs:
        m = read("documents/%s/metadata.yaml" % s)
        types[scalar(m, "source_type")] = types.get(scalar(m, "source_type"), 0) + 1
        status[scalar(m, "source_status")] = status.get(scalar(m, "source_status"), 0) + 1
        topics[scalar(m, "topic_slug")] = topics.get(scalar(m, "topic_slug"), 0) + 1
        free += scalar(m, "free") == "true"
        has_en = os.path.exists(os.path.join(ROOT, "documents", s, "content.en.md"))
        has_ru = os.path.exists(os.path.join(ROOT, "documents", s, "content.ru.md"))
        en += has_en
        ru += has_ru
        both += has_en and has_ru
    F["types"], F["status"], F["topics_by_slug"] = types, status, dict(sorted(topics.items(), key=lambda kv: (-kv[1], kv[0])))
    F["interview"], F["article"], F["research"] = types.get("interview", 0), types.get("article", 0), types.get("research", 0)
    F["published"], F["todo"] = status.get("published", 0), status.get("todo", 0)
    F["topics"] = len(topics)
    F["free_true"] = free
    F["en_bodies"], F["ru_bodies"], F["both_langs"] = en, ru, both
    F["index_md"] = len(glob.glob(os.path.join(ROOT, "documents", "*", "index.md")))
    F["doc_readmes"] = len(glob.glob(os.path.join(ROOT, "documents", "*", "README.md")))
    F["image_meta"] = len(glob.glob(os.path.join(ROOT, "documents", "*", "images", "*", "metadata.yaml")))
    F["image_no_binary"] = sum("binary_in_export: false" in open(p, encoding="utf-8").read()
                               for p in glob.glob(os.path.join(ROOT, "documents", "*", "images", "*", "metadata.yaml")))
    F["topic_pages"] = len([f for f in os.listdir(os.path.join(ROOT, "topics")) if f.endswith(".md") and f != "README.md"])
    words = {"en": 0, "ru": 0}
    for lang in words:
        for p in glob.glob(os.path.join(ROOT, "documents", "*", "content.%s.md" % lang)):
            words[lang] += len(open(p, encoding="utf-8").read().split())
    F["words_en"], F["words_ru"] = words["en"], words["ru"]
    pf = pre_files()
    F["files_pre"] = len(pf)
    F["md_pre"] = sum(f.endswith(".md") for f in pf)
    F["yaml_pre"] = sum(f.endswith(".yaml") for f in pf)
    F["binaries_pre"] = sum(not f.endswith((".md", ".yaml", ".gitignore")) for f in pf)
    F["commits_pre"] = int(subprocess.run(["git", "rev-list", "--count", TAG], cwd=ROOT, capture_output=True, text=True).stdout.strip() or 0)
    meta = read("metadata.yaml")
    F["metadata_docs"] = int(scalar(meta, "migrated_documents_count"))
    F["metadata_topics"] = int(scalar(meta, "topics_count"))
    return F


if __name__ == "__main__":
    print(json.dumps(facts(), ensure_ascii=False, indent=1))
