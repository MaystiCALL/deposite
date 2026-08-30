# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: BudgetLeaf
import os
import shutil
from datetime import datetime

def backup_data_file(path: str) -> str:
    """Create a timestamped backup of the data file."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Data file not found: {path}")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = f"{path}.{timestamp}.bak"
    shutil.copy2(path, backup_path)
    return backup_path
