# ASRP Media Documents Knowledge Hub

This repository is an English-language navigation hub for migrated ASRP media, SMM, and publication materials. Article bodies are preserved only for English and Russian source content; other languages from the exports are intentionally not migrated.

## Entry Points

- [Documents catalog](documents/README.md)
- [Topics index](topics/README.md)
- [Migration skip report](migration-skipped.md)

## Repository Rules

- Each migrated document lives in its own `documents/<slug>/` folder.
- `README.md` files are summary cards, not full article bodies.
- Full bodies are stored as `content.en.md` and/or `content.ru.md`.
- `metadata.yaml` files preserve source traceability.
- Image binaries were not present in the export; image folders contain metadata for source paths and usage context.

## Current Snapshot

- Migrated documents: 29
- Migrated languages: English and Russian only
- Source exports: `documents_202606241032.json`, `documents_content_202606241032.json`, `document_draft_contents_202606241032.json`
