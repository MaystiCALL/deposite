# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: BudgetLeaf
def print_budget_report(month):
    """Выводит отчёт по бюджету за указанный месяц в виде таблицы."""
    total_income = 0
    total_expense = 0
    
    for category in categories:
        if category.month == month:
            income = sum(amt[1] for amt in category.income)
            expense = sum(amt[1] for amt in category.expense)
            balance = income - expense
            
            print(f"{category.name:<20} | {income:>8.2f} | {expense:>8.2f} | {balance:>8.2f}")
            
            total_income += income
            total_expense += expense
    
    print("-" * 56)
    print(f"{'TOTAL':<20} | {total_income:>8.2f} | {total_expense:>8.2f} | {total_income - total_expense:>8.2f}")

print_budget_report(1)
