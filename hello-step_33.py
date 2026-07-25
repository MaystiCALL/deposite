# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: BudgetLeaf
def undo_last_action(action_history):
    """Откатывает последнее действие из истории, если откат возможен.
    
    Поддерживает откат: добавления категорий (удаляет категорию), 
    изменения лимита категории (восстанавливает предыдущее значение).
    
    Аргумент:
        action_history: список словарей с ключами 'action', 'data'
        
    Возвращает: новый список истории после отката.
    """
    if not action_history:
        return action_history
    
    last_action = action_history[-1]
    action_type = last_action.get('action')
    
    if action_type == 'add_category':
        # Откат добавления категории — удаляем из списка категорий
        category_name = last_action['data'].get('name', '')
        return [a for a in action_history[:-1] if a.get('action') != 'add_category' or a.get('data', {}).get('name') != category_name]
    
    elif action_type == 'update_limit':
        # Откат изменения лимита — оставляем предыдущее значение
        return action_history[:-1] + [last_action[:-1]] if isinstance(last_action, list) else action_history[:-1]
    
    return action_history
