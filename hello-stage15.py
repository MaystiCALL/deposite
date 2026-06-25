# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: BudgetLeaf
def get_weekly_stats(transactions: list[dict], start_date: str) -> dict[str, float]:
    from datetime import datetime, timedelta
    week_start = datetime.strptime(start_date, "%Y-%m-%d")
    current_week = week_start.replace(day=1) + timedelta(days=week_start.weekday())
    weekly_data = {}
    for i in range(52):  # Максимум недель в году
        w_start = current_week + timedelta(weeks=i)
        w_end = w_start + timedelta(days=6)
        week_range = (w_start.strftime("%Y-%m-%d"), min(w_end, datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)).strftime("%Y-%m-%d"))
        weekly_data[week_range] = {"income": 0.0, "expense": 0.0}
    for t in transactions:
        date_str = t["date"]
        if not (w_start <= datetime.strptime(date_str, "%Y-%m-%d") < w_end):
            continue
        amount = float(t["amount"])
        category = t.get("category", "other")
        weekly_data[week_range][t["type"]] += abs(amount)
    return weekly_data
