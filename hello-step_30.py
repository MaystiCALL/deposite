# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: BudgetLeaf
class Profile:
    def __init__(self, name):
        self.name = name
        self.budgets = {}

    def add_budget(self, category, limit):
        if category in self.budgets:
            raise ValueError(f"Budget for {category} already exists")
        self.budgets[category] = {"limit": limit, "spent": 0.0}

    def get_spent(self, category):
        return self.budgets.get(category, {}).get("spent", 0.0)

    def reset_month(self):
        for budget in self.budgets.values():
            budget["spent"] = 0.0


class BudgetLeaf:
    profiles = {}

    @staticmethod
    def create_profile(name):
        p = Profile(name)
        BudgetLeaf.profiles[name] = p
        return p

    @staticmethod
    def get_profile(name):
        return BudgetLeaf.profiles.get(name)

    @staticmethod
    def set_active_profile(name):
        if name not in BudgetLeaf.profiles:
            raise ValueError(f"Profile {name} does not exist")
        BudgetLeaf.active_profile = BudgetLeaf.profiles[name]

    active_profile = None
