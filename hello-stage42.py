# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: BudgetLeaf
class Color:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    WHITE = "\033[97m"
    BOLD = "\033[1m"
    DIM = "\033[2m"

    @staticmethod
    def enabled():
        return os.environ.get("BUDGETLEAF_COLOR", "1") == "1"

    @classmethod
    def text(cls, text, color=None):
        if not cls.enabled():
            return text
        prefix = color or cls.WHITE
        return f"{prefix}{text}{cls.RESET}"

    @classmethod
    def money(cls, amount):
        if amount >= 0:
            return cls.text(f"+{amount:.2f}", cls.GREEN)
        return cls.text(f"{amount:.2f}", cls.RED)

    @classmethod
    def category(cls, name):
        return cls.text(name, cls.CYAN)

    @classmethod
    def limit(cls, value):
        return cls.text(f"{value:.2f}", cls.MAGENTA)

    @classmethod
    def title(cls, text):
        return cls.text(text, cls.BOLD + cls.WHITE)

    @classmethod
    def dim(cls, text):
        return cls.text(text, cls.DIM)

    @classmethod
    def warning(cls, text):
        return cls.text(text, cls.YELLOW)

    @classmethod
    def error(cls, text):
        return cls.text(text, cls.RED)
