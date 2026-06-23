# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: BudgetLeaf
def generate_summary():
    total_income = sum(t['amount'] for t in transactions if t['type'] == 'income')
    total_expense = sum(t['amount'] for t in transactions if t['type'] == 'expense')
    balance = total_income - total_expense
    category_totals = {}
    for t in transactions:
        cat = t.get('category', 'Other')
        category_totals[cat] = category_totals.get(cat, 0) + (t['amount'] if t['type'] == 'expense' else 0)
    print(f"=== Monthly Budget Summary ===")
    print(f"Income: {total_income:.2f} | Expenses: {total_expense:.2f} | Balance: {balance:.2f}")
    for cat, spent in sorted(category_totals.items(), key=lambda x: x[1], reverse=True):
        pct = (spent / total_expense * 100) if total_expense > 0 else 0
        print(f"{cat}: {spent:.2f} ({pct:.1f}%)")
