# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: BudgetLeaf
class BudgetError(Exception):
    pass


def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise BudgetError(f"Некорректная дата '{date_str}'. Используйте формат YYYY-MM-DD.")


def validate_amount(amount_str):
    try:
        amount = float(amount_str)
        if amount <= 0:
            raise BudgetError("Сумма должна быть положительной.")
        return amount
    except ValueError:
        raise BudgetError(f"Некорректная сумма '{amount_str}'. Введите число, например 150.50.")


def validate_category(category):
    if not category or len(category.strip()) == 0:
        raise BudgetError("Категория не может быть пустой.")
    return category.strip()
