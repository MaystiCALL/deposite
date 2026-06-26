# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: BudgetLeaf
def generate_monthly_report(start_date, end_date):
    """Генерирует сводную статистику доходов/расходов за указанный период."""
    stats = {"income": 0, "expense": 0, "transactions_by_category": {}}
    
    for record in transactions:
        if start_date <= record["date"] <= end_date:
            amount = record.get("amount", 0)
            category = record.get("category", "Other")
            
            if category not in stats["transactions_by_category"]:
                stats["transactions_by_category"][category] = {"income": 0, "expense": 0}
            
            if amount > 0:
                stats["income"] += amount
                stats["transactions_by_category"][category]["income"] += amount
            else:
                stats["expense"] -= amount
                stats["transactions_by_category"][category]["expense"] -= amount
    
    return stats
