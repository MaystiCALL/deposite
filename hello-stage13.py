# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: BudgetLeaf
class BudgetSearch:
    def __init__(self, db):
        self.db = db
    
    def search(self, query=None, category=None, limit=None):
        if not any([query, category, limit]):
            return []
        
        results = list(self.db.entries)
        
        if query:
            q = query.lower()
            results = [e for e in results if q in e.get('description', '').lower()]
        
        if category:
            c = category.lower()
            results = [e for e in results if e.get('category', '').lower().startswith(c)]
        
        if limit is not None:
            results = results[:limit]
            
        return results
