# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: BudgetLeaf
def check_expired_reminders(reminders, today):
    """Проверяет напоминания, чей срок уже прошёл, и возвращает список просроченных."""
    overdue = []
    for r in reminders:
        if isinstance(r, dict) and r.get("type") == "deadline":
            deadline_str = r["date"]
            try:
                deadline_date = datetime.strptime(deadline_str, "%Y-%m-%d").date()
                if today > deadline_date:
                    overdue.append({**r, "status": "overdue", "days_late": (today - deadline_date).days})
            except ValueError:
                pass
    return overdue

def print_overdue_report(overdue):
    """Выводит отчёт о просроченных напоминаниях."""
    if not overdue:
        print("✅ Все напоминания в срок!")
        return
    print("\n⚠️  Просроченные напоминания:")
    for item in overdue:
        name = item.get("name", "Без имени")
        deadline_str = item["date"]
        days_late = item.get("days_late", "?")
        print(f"  • {name} — срок был {deadline_str}, просрочено на {days_late} дней")
