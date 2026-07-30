# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: BudgetLeaf
def integrity_check_and_repair():
    """Проверка целостности данных и ремонт простых проблем."""
    if not categories:
        print("Ошибка: список категорий пуст")
        return False
    
    issues = []
    
    # Проверка лимитов расходов
    total_spent = sum(category.spent for category in categories)
    total_limit = sum(category.limit for category in categories)
    
    if total_spent > total_limit:
        print(f"Предупреждение: потрачено {total_spent:.2f}, лимит {total_limit:.2f}")
        issues.append("Перерасход бюджета")
    
    # Проверка отрицательных сумм
    for category in categories:
        if category.spent < 0 or category.limit < 0:
            print(f"Ошибка: категория '{category.name}' имеет некорректные значения")
            issues.append(f"Некорректная категория: {category.name}")
    
    # Проверка баланса
    for category in categories:
        if category.balance < 0:
            print(f"Предупреждение: баланс категории '{category.name}' отрицательный")
            issues.append(f"Отрицательный баланс: {category.name}")
    
    if not issues:
        print("Все данные корректны")
        return True
    
    print(f"Найдено {len(issues)} проблем")
    return False

integrity_check_and_repair()
