# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: BudgetLeaf
import json, os

DATA_FILE = "budget_leaf.json"

def save_data(data):
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except IOError as e:
        print(f"[ERROR] Не удалось сохранить данные в {DATA_FILE}: {e}")
        return False

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"transactions": [], "categories": {}, "limits": {}, "settings": {"currency": "RUB"}}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print("[ERROR] Файл данных повреждён или недоступен. Используется пустой набор.")
        return {"transactions": [], "categories": {}, "limits": {}, "settings": {"currency": "RUB"}}

def get_data():
    data = load_data()
    if not os.path.exists(DATA_FILE):
        save_data(data)
    return data
