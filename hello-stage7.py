# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: BudgetLeaf
def sort_transactions(transactions, key='date'):
    if not transactions: return []
    reverse = False
    if key == 'priority': reverse = True
    elif key == 'name': key = lambda x: (x['amount'], x.get('category', ''), x['id'])
    else: key = lambda x: x.get(key, 0)
    return sorted(transactions, key=key, reverse=reverse)
