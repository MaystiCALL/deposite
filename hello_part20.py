# === Stage 20: Добавь восстановление записей из архива ===
# Project: BudgetLeaf
import json, os, datetime as dt

def restore_from_archive(archive_path: str) -> None:
    if not os.path.exists(archive_path):
        return
    try:
        with open(archive_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for record in data.get('transactions', []):
            rec_id = record.pop('id', None)
            if not rec_id:
                continue
            try:
                dt.datetime.fromisoformat(record['date'])
            except ValueError:
                record['date'] = dt.datetime.now().strftime('%Y-%m-%d')
        with open('budget.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception:
        pass
