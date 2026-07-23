# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: BudgetLeaf
def switch_profile(new_name):
    """Переключить активный профиль по имени."""
    global active_profile
    if new_name not in profiles:
        print(f"Профиль '{new_name}' не найден.")
        return False
    active_profile = new_name
    print(f"Активный профиль: {active_profile}")
    return True
