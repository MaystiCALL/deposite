# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: BudgetLeaf
def _pretty_report(monthly: dict[str, dict[str, float]]) -> str:
    """Формирует отчёт за месяц в читаемом виде."""
    lines: list[str] = []
    lines.append(f"📊 Отчёт за {month_name(monthly)}")
    lines.append("=" * 30)
    for cat, data in sorted(monthly.items()):
        spent = data["spent"]
        limit = data.get("limit", 0)
        status = "✅" if limit == 0 else "⚠️" if spent > limit else "✅"
        lines.append(f"  {status} {cat}: {spent:.2f} / {limit:.2f}")
    return "\n".join(lines)
