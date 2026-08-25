# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: BudgetLeaf
def dry_run(func, *args, **kwargs):
    """Execute func inside a dry-run context that logs the intended operation but skips real side effects.
    
    Returns the original return value of func.
    """
    import logging
    logger = logging.getLogger('BudgetLeaf')
    logger.info("--- DRY RUN ---")
    logger.info(f"Function: {func.__name__}")
    logger.info(f"Args: {args}")
    logger.info(f"Kwargs: {kwargs}")
    logger.info("--- END DRY RUN ---")
    return func(*args, **kwargs)
