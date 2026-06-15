# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: BudgetLeaf
import json, sys, os
from pathlib import Path
DATA_FILE = "data.json"
def load_initial_data():
    if not os.path.exists(DATA_FILE):
        return {"categories": ["Зарплата", "Еда", "Транспорт"], "limits": {}, "transactions": []}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, dict):
            return {"categories": [], "limits": {}, "transactions": []}
        for key in ["categories", "limits", "transactions"]:
            if key not in data or not isinstance(data[key], list):
                data[key] = []
        return data
    except json.JSONDecodeError:
        return {"categories": [], "limits": {}, "transactions": []}

def init_budget():
    initial_data = load_initial_data()
    categories_set = set(initial_data.get("categories", []))
    for cat in ["Зарплата", "Еда", "Транспорт"]:
        if cat not in categories_set:
            initial_data["categories"].append(cat)
    limits_dict = {cat: 0.0 for cat in initial_data.get("categories", [])}
    for limit_str, value in (initial_data.get("limits", {}).items()):
        try:
            limits_dict[limit_str] = float(value)
        except ValueError:
            pass
    transactions_list = []
    for tx in initial_data.get("transactions", []):
        if isinstance(tx, dict) and "amount" in tx and "category" in tx:
            transactions_list.append({
                "id": tx.get("id"),
                "date": tx.get("date"),
                "description": tx.get("description", ""),
                "amount": float(tx["amount"]),
                "category": tx["category"],
                "type": tx.get("type", "expense")
            })
    return {
        "categories": list(categories_set),
        "limits": limits_dict,
        "transactions": transactions_list
    }

if __name__ == "__main__":
    budget = init_budget()
    print(f"Загружено категорий: {len(budget['categories'])}, транзакций: {len(budget['transactions'])}")
