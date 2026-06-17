# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: BudgetLeaf
def export_to_json():
    import json
    from datetime import datetime
    state = {
        "timestamp": datetime.utcnow().isoformat(),
        "categories": list(categories.items()),
        "transactions": transactions,
        "limits": limits,
        "summary": calculate_summary()
    }
    return json.dumps(state, indent=2)
