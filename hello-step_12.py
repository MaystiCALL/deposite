# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: BudgetLeaf
import json, os

def load_budget_data(filepath):
    if not os.path.exists(filepath):
        print(f"Файл {filepath} не найден.")
        return []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            return [dict(item) for item in data]
        print("Неверный формат JSON (ожидался список).")
        return []
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        return []
    except Exception as e:
        print(f"Произошла неизвестная ошибка при чтении файла: {e}")
        return []
