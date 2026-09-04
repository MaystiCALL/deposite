# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: BudgetLeaf
def demo():
    print("=" * 50)
    print("BudgetLeaf — демо-сценарий")
    print("=" * 50)

    categories = ["Продукты", "Транспорт", "Развлечения", "Жильё"]
    limits = [5000, 3000, 2000, 15000]

    print("\n📋 Категории и лимиты:")
    for cat, lim in zip(categories, limits):
        print(f"  • {cat}: {lim} ₽")

    transactions = [
        ("Продукты", 1200,  "2024-03-01", "Покупка в супермаркете"),
        ("Транспорт", 350,   "2024-03-02", "Такси до работы"),
        ("Развлечения", 800, "2024-03-05", "Кино и кофе"),
        ("Продукты", 4500,  "2024-03-10", "Большая закупка"),
        ("Транспорт", 200,   "2024-03-12", "Бензин"),
        ("Развлечения", 300, "2024-03-15", "Спортивный зал"),
    ]

    print("\n💰 Транзакции:")
    for desc, amount, date, note in transactions:
        print(f"  [{date}] {desc}: {amount} ₽ — {note}")

    print("\n📊 Итоги по категориям:")
    cat_sum = {}
    for desc, amount, date, note in transactions:
        cat_sum[desc] = cat_sum.get(desc, 0) + amount
    for cat, total in cat_sum.items():
        lim = next(l for l, c in zip(limits, categories) if c == cat)
        usage = f"{total / lim * 100:.1f}%" if lim else "—"
        status = "⚠️ почти лимит" if usage > 90 else "✓ в норме"
        print(f"  • {cat}: {total} ₽ / {lim} ₽ ({usage}) — {status}")

    print("\n🏁 Демо завершено. Спасибо за использование BudgetLeaf!")
