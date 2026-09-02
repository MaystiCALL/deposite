# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: BudgetLeaf
def migrate():
    """Миграция структуры данных: добавление поля 'last_sync' в конфигурацию."""
    config = load_config()
    if 'last_sync' not in config:
        config['last_sync'] = str(datetime.now().isoformat())
        save_config(config)
        print("Миграция выполнена: добавлено поле 'last_sync'")
    else:
        print("Миграция не требуется: поле 'last_sync' уже существует")
