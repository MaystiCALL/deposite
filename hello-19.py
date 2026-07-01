# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: BudgetLeaf
def archive_old_records(cutoff_date=None):
    if cutoff_date is None:
        import datetime
        cutoff_date = datetime.date.today() - datetime.timedelta(days=30)
    
    archived_count = 0
    for record in records:
        if isinstance(record, dict) and 'date' in record:
            try:
                rec_date = datetime.datetime.strptime(
                    record['date'], '%Y-%m-%d').date()
                if rec_date < cutoff_date:
                    record['_archived'] = True
                    archived_count += 1
            except ValueError:
                pass
    
    return archived_count
