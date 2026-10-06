def init_game_state():
    return {
        "energy": 6,
        "fixed_errors": [False, False, False], #A, B, C
        "moves_left": 6,
        "clue_obtained": False, # Улика "Код доступа: EKEB"
        "has_charger": False, # Зарядка в инвентаре
        "charger_used": False # Была ли зарядка уже использована
    }


def print_header(title):
    print("=" * 50)
    print(f" {title}")
    print("=" * 50)


def print_status(state):
    print_header("СОСТОЯНИЕ И СТАТУС")
    print(f" Энергия: {state['energy']} / 6")
    print(f" Осталось ходов: {state['moves_left']}")

    fixed_count = sum(state['fixed_errors'])
    print(f" Исправлено ошибок: {fixed_count} из 3")
    print(f"   - Ошибка A (Код доступа): {'[ИСПРАВЛЕНО]' if state['fixed_errors'][0] else '[АКТИВНА]'}")
    print(f"   - Ошибка B (Минуты):       {'[ИСПРАВЛЕНО]' if state['fixed_errors'][1] else '[АКТИВНА]'}")
    print(f"   - Ошибка C (Нижний регистр):{'[ИСПРАВЛЕНО]' if state['fixed_errors'][2] else '[АКТИВНА]'}")

    # Инвентарь и улики
    inventory = []
    if state['has_charger']:
        inventory.append("Зарядка")

    clues = []
    if state['clue_obtained']:
        clues.append("Код доступа: EKEB")

    print(f" Инвентарь: {', '.join(inventory) if inventory else 'Пусто'}")
    print(f" Улики:     {', '.join(clues) if clues else 'Нет улик'}")
    print("-" * 50)