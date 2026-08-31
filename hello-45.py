# === Stage 45: Добавь восстановление из резервной копии ===
# Project: BudgetLeaf
def load_backup(backup_path, categories, budgets, transactions):
    """Restores data from a JSON backup file."""
    import json
    if not backup_path:
        return categories, budgets, transactions
    try:
        with open(backup_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, dict):
            data = {k: data.get(k, []) for k in ['categories', 'budgets', 'transactions']}
        if isinstance(data, list):
            data = {'categories': data, 'budgets': [], 'transactions': []}
        if 'categories' in data:
            categories.extend(data['categories'])
        if 'budgets' in data:
            budgets.extend(data['budgets'])
        if 'transactions' in data:
            transactions.extend(data['transactions'])
        print(f"[BudgetLeaf] Restored {len(data.get('categories',[]))} categories, "
              f"{len(data.get('budgets',[]))} budgets, "
              f"{len(data.get('transactions',[]))} transactions from backup.")
        return categories, budgets, transactions
    except Exception as e:
        print(f"[BudgetLeaf] Backup restore failed: {e}")
        return categories, budgets, transactions
