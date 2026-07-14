# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: BudgetLeaf
if __name__ == "__main__":
    demo = {
        "salary": {"category": "income", "amount": 5000},
        "freelance": {"category": "income", "amount": 3000},
        "food": {"category": "expenses", "amount": 1200},
        "rent": {"category": "expenses", "amount": 2500},
        "utilities": {"category": "expenses", "amount": 400},
    }

    for name, data in demo.items():
        if data["category"] == "income":
            add_income(name, data["amount"])
        else:
            add_expense(data["category"], data["amount"])

    print("=== Monthly Report ===")
    list_categories()
    list_budgets()
    list_transactions()
    show_summary(2024)
