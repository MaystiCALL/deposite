# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: BudgetLeaf
class BudgetModel:
    def __init__(self):
        self.categories = {}
        self.monthly_limits = {}
        self.transactions = []

    def add_category(self, name, limit=None):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Категория должна быть непустой строкой")
        if limit is not None and (not isinstance(limit, (int, float)) or limit < 0):
            raise ValueError("Лимит должен быть неотрицательным числом")
        self.categories[name] = limit

    def set_monthly_limit(self, category_name, limit):
        if category_name not in self.categories:
            raise KeyError(f"Категория '{category_name}' не найдена")
        if limit is not None and (not isinstance(limit, (int, float)) or limit < 0):
            raise ValueError("Лимит должен быть неотрицательным числом")
        self.monthly_limits[category_name] = limit

    def add_transaction(self, category, amount, description=""):
        if not isinstance(category, str) or not category.strip():
            raise ValueError("Категория транзакции должна быть непустой строкой")
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Сумма транзакции должна быть положительным числом")
        if description != "" and (not isinstance(description, str) or len(description) > 100):
            raise ValueError("Описание должно быть строкой длиной до 100 символов")
        self.transactions.append({
            "category": category,
            "amount": amount,
            "description": description
        })

    def get_category_balance(self, category_name):
        if category_name not in self.categories:
            return None
        total = sum(t["amount"] for t in self.transactions if t["category"] == category_name)
        limit = self.monthly_limits.get(category_name)
        return {"total": total, "limit": limit, "remaining": limit - total if limit else None}
