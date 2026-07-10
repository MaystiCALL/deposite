# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: BudgetLeaf
def show_entry(entry):
    """Compact single-entry view."""
    print(f"ID: {entry.id}")
    print(f"Date:  {entry.date.strftime('%Y-%m-%d')}")
    print(f"Category: {entry.category.name if entry.category else 'None'}")
    print(f"Amount: {'+' if entry.amount >= 0 else '-'}{abs(entry.amount):.2f} RUB")
    print(f"Note: {entry.note or '(empty)'}")

show_entry(record1)
