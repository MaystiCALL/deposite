# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: BudgetLeaf
def monthly_report(transactions, categories):
    """Generate a compact monthly budget report with key metrics."""
    if not transactions:
        return {"summary": "No data"}

    total_income = sum(t for t in transactions if t.get("type") == "income")
    total_expense = sum(t for t in transactions if t.get("type") == "expense")
    balance = total_income - total_expense

    category_totals = {}
    for t in transactions:
        cat = t["category"]
        amount = t["amount"]
        category_totals[cat] = category_totals.get(cat, 0) + amount

    category_breakdown = {k: f"{v:.2f}" for k, v in sorted(category_totals.items(), key=lambda x: -x[1])}

    return {
        "period": "monthly",
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance,
        "savings_rate": f"{(abs(balance) / (total_income + 0.01)) * 100:.2f}%" if total_income else "N/A",
        "top_categories": category_breakdown,
    }
