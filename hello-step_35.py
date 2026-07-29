# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: BudgetLeaf
def suggest_next_action(state):
    """Simple heuristic-based next action recommendation."""
    if not state.get("transactions"):
        return "Start by adding a transaction."
    
    total_spent = sum(t["amount"] for t in state["transactions"])
    categories = state.get("categories", {})
    cat_totals = {}
    for t in state["transactions"]:
        cat = t.get("category", "Uncategorized")
        cat_totals[cat] = cat_totals.get(cat, 0) + t["amount"]
    
    if not cat_totals:
        return "Add a category before logging expenses."
    
    # Check which categories have exceeded their limits
    exceeded = []
    for cat, spent in cat_totals.items():
        limit = categories.get(cat, {}).get("limit", float('inf'))
        if spent > limit:
            exceeded.append(f"{cat} ({spent:.2f}/{limit:.2f})")
    
    if exceeded:
        return f"Warning: {', '.join(exceeded)} have exceeded their limits! Consider reducing spending."
    
    # Check if budget is empty (no categories defined)
    if not categories and state["transactions"]:
        return "Define categories to better track your spending."
    
    # Check for most active category
    if cat_totals:
        top_cat = max(cat_totals, key=cat_totals.get)
        return f"Tip: {top_cat} is your biggest expense. Consider setting a limit for it."
    
    return "All looks good! Continue adding transactions to build your budget."
