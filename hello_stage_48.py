# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: BudgetLeaf
class BudgetLeafApp:
    def __init__(self):
        self.categories = {}
        self.monthly_report = {}
        self.transactions = []

    def add_category(self, name, limit):
        self.categories[name] = {"limit": limit, "used": 0}
        return self.categories[name]

    def add_transaction(self, category, amount):
        if category in self.categories:
            self.categories[category]["used"] += amount
            self.transactions.append({"category": category, "amount": amount})
            return True
        return False

    def get_balance(self, category):
        if category in self.categories:
            return self.categories[category]["limit"] - self.categories[category]["used"]
        return None

    def get_report(self):
        return {cat: {"used": data["used"], "limit": data["limit"], "balance": self.get_balance(cat)}
                for cat, data in self.categories.items()}

    def reset_month(self):
        for cat in self.categories:
            self.categories[cat]["used"] = 0
        self.transactions = []

    def print_status(self):
        print("=== Бюджет ===")
        for cat, data in self.categories.items():
            print(f"{cat}: израсходовано {data['used']}, лимит {data['limit']}, остаток {self.get_balance(cat)}")


app = BudgetLeafApp()
app.add_category("Еда", 300)
app.add_category("Транспорт", 100)
app.add_transaction("Еда", 150)
app.add_transaction("Транспорт", 50)
app.print_status()
print(app.get_report())
