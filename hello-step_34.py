# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: BudgetLeaf
TEMPLATE_CATEGORIES = {
    'food': ['groceries', 'restaurant'],
    'transport': ['fuel', 'public_transit', 'taxi'],
    'shopping': ['clothes', 'electronics', 'household'],
}

def add_from_template(template_name, amount):
    if template_name not in TEMPLATE_CATEGORIES:
        print(f'Unknown template: {template_name}')
        return False
    cat = random.choice(TEMPLATE_CATEGORIES[template_name])
    desc = f'{cat} (from {template_name})'
    return add_entry(cat, amount, desc)

def setup_templates():
    TEMPLATE_CATEGORIES['health'] = ['gym', 'medicine', 'vitamins']
