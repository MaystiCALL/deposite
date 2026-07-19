# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: BudgetLeaf
APP_CONFIG = {
    "app_name": "BudgetLeaf",
    "version": "0.1.29",
    "language": "ru",
    "currency_symbol": "₽",
    "default_categories": [
        {"id": 1, "name": "Продукты", "color": "#4CAF50"},
        {"id": 2, "name": "Транспорт", "color": "#2196F3"},
        {"id": 3, "name": "Развлечения", "color": "#FF9800"},
        {"id": 4, "name": "Прочее", "color": "#9E9E9E"},
    ],
    "default_monthly_limit": 50000,
    "budget_period_days": 30,
    "daily_spend_threshold": 2000,
    "notification_sound": True,
    "data_file": "budget_leaf.dat",
}

def get_config(key=None):
    if key is None:
        return dict(APP_CONFIG)
    return APP_CONFIG.get(key, APP_CONFIG["default_categories"][0])
