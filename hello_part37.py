# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: BudgetLeaf
import unittest
from budget_leaf import Category, BudgetRecord

class TestCategory(unittest.TestCase):
    def test_create_category(self):
        c = Category("Food", 500)
        self.assertEqual(c.name, "Food")
        self.assertEqual(c.limit, 500)

    def test_add_record(self):
        c = Category("Transport", 300)
        record = BudgetRecord(1709620800, 45, "Bus pass")
        c.add(record)
        self.assertEqual(len(c.records), 1)
        self.assertAlmostEqual(c.spent(), 45.0)

    def test_limit_exceeded(self):
        c = Category("Entertainment", 50)
        record = BudgetRecord(1709620800, 60, "Movie")
        with self.assertRaises(ValueError):
            c.add(record)

class TestBudgetRecord(unittest.TestCase):
    def test_record(self):
        r = BudgetRecord(1709620800, -30, "Coffee refund")
        self.assertEqual(r.amount, -30.0)
        self.assertFalse(r.is_income())

if __name__ == "__main__":
    unittest.main()
