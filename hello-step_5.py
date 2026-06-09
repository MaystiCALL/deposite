# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: BudgetLeaf
def delete_record(record_id, records):
    """Удаление записи по ID с безопасной обработкой отсутствия."""
    if record_id not in records:
        print(f"Запись с ID {record_id} не найдена.")
        return records
    
    del records[record_id]
    print(f"Запись с ID {record_id} успешно удалена.")
    return records

def get_monthly_report(records, current_month):
    """Формирование отчёта за текущий месяц."""
    monthly_income = 0
    monthly_expense = 0
    
    for record in records.values():
        if record['date'].startswith(current_month):
            amount = float(record['amount'])
            if record['type'] == 'income':
                monthly_income += amount
            else:
                monthly_expense += amount
                
    print(f"\nОтчёт за {current_month}:")
    print(f"Доход: {monthly_income:.2f}")
    print(f"Расход: {monthly_expense:.2f}")
    return monthly_income, monthly_expense
