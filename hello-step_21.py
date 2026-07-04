# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: BudgetLeaf
class Reminder:
    def __init__(self, title: str, date: datetime.date):
        self.title = title
        self.date = date
        self.done = False
    
    def is_due(self) -> bool:
        return not self.done and self.date <= datetime.date.today()
    
    def mark_done(self):
        self.done = True

def load_reminders(path: str) -> List[Reminder]:
    reminders = []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split('|')
                if len(parts) == 3:
                    title, date_str, done_str = parts
                    reminders.append(Reminder(title, datetime.strptime(date_str, '%Y-%m-%d')))
    except FileNotFoundError:
        pass
    return reminders

def save_reminders(path: str, reminders: List[Reminder]):
    with open(path, 'w', encoding='utf-8') as f:
        for r in reminders:
            done = 'yes' if r.done else 'no'
            f.write(f"{r.title}|{r.date.strftime('%Y-%m-%d')}|{done}\n")

def check_and_save_reminders(path: str):
    reminders = load_reminders(path)
    for r in reminders:
        print(f"[{'X' if r.done else '.'}] {r.title} ({r.date})")
    save_reminders(path, reminders)
