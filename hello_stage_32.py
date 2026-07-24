# === Stage 32: Добавь журнал действий пользователя ===
# Project: BudgetLeaf
class ActionLog:
    def __init__(self):
        self._entries = []

    def log(self, action_type, description=None, amount=None, category=None, timestamp=None):
        entry = {"type": action_type, "description": description or "", "amount": amount, "category": category}
        if timestamp is None:
            import datetime
            timestamp = datetime.datetime.now()
        entry["timestamp"] = timestamp.isoformat()
        self._entries.append(entry)

    @property
    def entries(self):
        return list(self._entries)

    def get_recent(self, count=10):
        return self._entries[-count:]

    def clear(self):
        self._entries.clear()
