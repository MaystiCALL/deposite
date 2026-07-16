# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: BudgetLeaf
def reset_demo_data():
    """Сбросить демо-данные в категории, лимиты и историю трат."""
    global categories, monthly_limits, transactions, balance
    categories = {
        "Продукты": {"limit": 3000},
        "Транспорт": {"limit": 1500},
        "Развлечения": {"limit": 2000},
        "Жилище": {"limit": 5000},
    }
    monthly_limits = {cat["name"]: cat["limit"] for cat in categories.values()}
    transactions = []
    balance = 0.0
    print("Демо-данные сброшены.")


def clear_state():
    """Полная очистка: все данные, баланс и история."""
    global categories, monthly_limits, transactions, balance
    categories.clear()
    monthly_limits.clear()
    transactions.clear()
    balance = 0.0
    print("Состояние полностью очищено.")
