# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: BudgetLeaf
def run_cli():
    print("=== BudgetLeaf CLI ===")
    while True:
        cmd = input("\nКоманда (1-5): ").strip()
        if not cmd: continue
        try:
            n = int(cmd)
        except ValueError: continue
        if n == 1:
            cat_name = input("Название категории: ")
            limit = float(input("Лимит: "))
            BudgetLeaf.add_category(cat_name, limit)
            print(f"Категория '{cat_name}' добавлена.")
        elif n == 2:
            amount = float(input("Сумма транзакции: "))
            desc = input("Описание (опционально): ") or ""
            BudgetLeaf.add_transaction(amount, desc)
            print(f"Транзакция '{desc}' записана.")
        elif n == 3:
            cat_name = input("Фильтр по категории ('все' для всех): ") or "все"
            BudgetLeaf.list_transactions(cat_name)
        elif n == 4:
            month = int(input("Месяц (1-12): "))
            year = int(input("Год: "))
            print("\n--- Отчёт за %d.%02d ---" % (year, month))
            BudgetLeaf.generate_report(month, year)
        elif n == 5:
            print("Выход.")
            break
