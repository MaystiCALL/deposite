# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: BudgetLeaf
def edit_transaction(txn_id, new_data):
    """Редактирует запись по ID. Возвращает обновлённую запись или None."""
    if txn_id not in transactions:
        return None
    
    # Разрешаем менять только указанные поля, остальные оставляем без изменений
    updated_txn = {
        'id': txn_id,
        'date': new_data.get('date', transactions[txn_id]['date']),
        'description': new_data.get('description', transactions[txn_id]['description']),
        'amount': new_data.get('amount', transactions[txn_id]['amount']),
        'category': new_data.get('category', transactions[txn_id]['category']),
        'type': new_data.get('type', transactions[txn_id]['type']),
    }
    
    # Проверка на корректность данных (опционально, можно расширить)
    if updated_txn['amount'] < 0:
        print(f"Ошибка: сумма транзакции {txn_id} не может быть отрицательной.")
        return None
    
    transactions[txn_id] = updated_txn
    return updated_txn
