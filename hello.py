


# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: BudgetLeaf
import json
from datetime import datetime

DATA_FILE = "budget_data.json"

def load_data():
      try:
                with open(DATA_FILE, "r", encoding="utf-8") as f:
                              return json.load(f)
      except FileNotFoundError:
                return {"categories": {}, "transactions": [], "limits": {}}

  def save_data(data):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
                  json.dump(data, f, ensure_ascii=False, indent=2)

    def init_demo_data():
          data = load_data()
          if not data["transactions"]:
                    demo = [
                                  {"id": 1, "date": "2023-10-01", "category": "food", "amount": -1500, "description": "Продукты"},
                                  {"id": 2, "date": "2023-10-05", "category": "salary", "amount": 50000, "description": "Зарплата"},
                                  {"id": 3, "date": "2023-10-10", "category": "utilities", "amount": -3000, "description": "Коммуналка"},
                    ]
                    data["transactions"] = demo
                    data["categories"] = {"food": "Еда", "salary": "Доход", "utilities": "Коммуналка"}
                    data["limits"] = {"food": 5000, "utilities": 5000}
                    save_data(data)
                return data

def get_balance():
      data = load_data()
    total = sum(t["amount"] for t in data["transactions"])
    return total

def main():
      print("=== BudgetLeaf ===")
    print(f"Текущий баланс: {get_balance()} руб.")
    data = init_demo_data()
    print(f"Категории: {', '.join(data['categories'].values())}")
    print("Данные загружены из файла.")

if __name__ == "__main__":
      main()
