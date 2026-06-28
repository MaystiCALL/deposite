# === Stage 17: Добавь группировку записей по категориям ===
# Project: BudgetLeaf
def group_by_category(records):
    from collections import defaultdict
    grouped = defaultdict(list)
    for r in records:
        cat_name = r.get('category', 'Uncategorized')
        amount = float(r['amount'])
        is_income = r['type'] == 'income'
        key = (cat_name, is_income)
        grouped[key].append(amount)
    result = {}
    for (name, inc), amounts in grouped.items():
        total = sum(amounts)
        if inc:
            result[name] = {'balance': total, 'count': len(amounts)}
        else:
            result[name] = {'balance': -total, 'count': len(amounts)}
    return dict(sorted(result.items()))
