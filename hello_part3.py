# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: BudgetLeaf
class BudgetState:
    def __init__(self):
        self.records = []
        self.categories = {}
        self.monthly_limits = {}

    def add_record(self, date, category, amount, type_="expense"):
        record = {
            "date": date,
            "category": category,
            "amount": float(amount),
            "type": type_
        }
        self.records.append(record)
        if category not in self.categories:
            self.categories[category] = {"income": 0.0, "expense": 0.0}
        if type_ == "income":
            self.categories[category]["income"] += float(amount)
        else:
            self.categories[category]["expense"] += float(amount)

    def set_limit(self, category, limit):
        self.monthly_limits[category] = float(limit)

    def get_monthly_report(self, month_year):
        report = {}
        for cat in self.categories:
            total_income = self.categories[cat]["income"]
            total_expense = self.categories[cat]["expense"]
            limit = self.monthly_limits.get(cat, 0.0)
            report[cat] = {
                "income": total_income,
                "expense": total_expense,
                "limit": limit,
                "remaining": limit - total_expense if limit else None
            }
        return report

state = BudgetState()
