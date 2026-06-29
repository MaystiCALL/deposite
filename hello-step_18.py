# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: BudgetLeaf
class TagManager:
    def __init__(self, db):
        self.db = db
        self.tags = {}
        self.load_tags()

    def load_tags(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT id, name FROM tags")
        for row in cursor.fetchall():
            self.tags[row[0]] = row[1]
        cursor.close()

    def add_tag(self, name: str) -> int:
        if name in self.tags:
            return self.tags[name]
        cursor = self.db.cursor()
        try:
            cursor.execute("INSERT INTO tags (name) VALUES (%s)", (name,))
            tag_id = cursor.lastrowid
            self.tags[tag_id] = name
            return tag_id
        finally:
            cursor.close()

    def remove_tag(self, tag_id: int):
        if tag_id not in self.tags:
            return False
        cursor = self.db.cursor()
        try:
            # Удаляем операции с этим тегом перед удалением тега
            cursor.execute("DELETE FROM transactions WHERE tag_id = %s", (tag_id,))
            cursor.execute("DELETE FROM tags WHERE id = %s", (tag_id,))
            self.tags.pop(tag_id)
            return True
        finally:
            cursor.close()

    def get_tag(self, tag_id: int):
        return self.tags.get(tag_id)
