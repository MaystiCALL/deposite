# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: BudgetLeaf
def self_check():
    print("=" * 60)
    print("BudgetLeaf — Самопроверка приложения")
    print("=" * 60)
    try:
        assert hasattr(self, "categories"), "Категории не определены"
        assert hasattr(self, "budgets"), "Бюджеты не определены"
        assert hasattr(self, "transactions"), "Транзакции не определены"
        assert hasattr(self, "add_category"), "Метод add_category отсутствует"
        assert hasattr(self, "add_budget"), "Метод add_budget отсутствует"
        assert hasattr(self, "add_transaction"), "Метод add_transaction отсутствует"
        assert hasattr(self, "get_summary"), "Метод get_summary отсутствует"
        assert hasattr(self, "generate_report"), "Метод generate_report отсутствует"
        assert hasattr(self, "display_dashboard"), "Метод display_dashboard отсутствует"
        print("✓ Все ключевые методы и атрибуты на месте")
    except AssertionError as e:
        print(f"✗ Ошибка: {e}")
        return False

    try:
        # Тест с нуля
        self.categories = {}
        self.budgets = {}
        self.transactions = []
        self.add_category("Еда", 5000)
        self.add_category("Транспорт", 2000)
        self.add_budget("Январь 2025", 10000)
        self.add_transaction("Еда", 1500, "2025-01-05")
        self.add_transaction("Транспорт", 500, "2025-01-10")
        summary = self.get_summary()
        assert summary["food"] == 1500
        assert summary["transport"] == 500
        report = self.generate_report()
        assert "Еда" in report
        assert "Транспорт" in report
        self.display_dashboard()
        print("✓ Тестовый сценарий прошёл успешно")
    except Exception as e:
        print(f"✗ Тестовый сценарий провалился: {e}")
        return False

    print("=" * 60)
    print("BudgetLeaf готов к использованию! 🎉")
    print("=" * 60)
    return True
