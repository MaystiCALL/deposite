# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: BudgetLeaf
def filter_transactions(records, status=None, category=None, tags=None):
    """Фильтрует записи по статусу, категории или тегам."""
    filtered = []
    for r in records:
        if status and r.get('status') != status:
            continue
        if category and r.get('category') != category:
            continue
        if tags:
            record_tags = r.get('tags', [])
            if not any(tags in record_tags for tags in tags):
                continue
        filtered.append(r)
    return filtered
