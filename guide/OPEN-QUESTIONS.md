# Open questions

[Guide](README.md) · [Русский](OPEN-QUESTIONS.ru.md) · [Front page](../README.md)

Inconsistencies and gaps found while reading. Source files were not changed.

1. **Classification vs visibility.** `metadata.yaml` has `data_classification: INTERNAL` and the old README passport line says "classification `INTERNAL`"; the README says article bodies are **PUBLIC**; the repository is public. Which applies?
2. **What does `todo` mean?** 25 of 29 records carry `source_status: todo`, yet all have a publication date, bodies in two languages and `active: true`. The repository does not define the status.
3. **Missing export files.** `metadata.yaml` names three export files; they are not in the repository (`.gitignore`), so traceability cannot be checked against them.
4. **Epoch value in `deleted_at`.** All 29 records have `deleted_at: '1969-12-31T23:00:00.000Z'` while `active: true`; probably an empty date, not stated.
5. **Duplicate publication dates.** Two records share `publication_date: '2023-03-10T07:25:06.805Z'`; 20 of 29 dates are in 2023. Whether these are real dates is not stated.
6. **Statements without documents.** Patent, trademark and health statements inside articles have no backing document here ([CLAIMS.md](CLAIMS.md)); the patent applications listed in the README have no status and no named applicants.
7. **Spelling variants.** One surname is transliterated in several ways across the article bodies; the repository has no style rule.
