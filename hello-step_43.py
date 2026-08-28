# === Stage 43: Добавь пагинацию длинных списков ===
# Project: BudgetLeaf
class Paginator:
    def __init__(self, items, page_size=10):
        self.items = list(items)
        self.page_size = page_size
        self.total_pages = max(1, len(self.items) // self.page_size + bool(self.items) % self.page_size)

    def paginate(self, page=1):
        if page < 1 or page > self.total_pages:
            page = self.total_pages
        start = (page - 1) * self.page_size
        return {
            "page": page,
            "total_pages": self.total_pages,
            "items": self.items[start:start + self.page_size],
            "total": len(self.items),
        }
