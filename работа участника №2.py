# ==============================================================================
# ЗОНА ОТВЕТСТВЕННОСТИ УЧАСТНИКА 2: Загадки, ошибки и проверка ответов
# ==============================================================================

def normalize_input(text):


    return text.strip().lower()


def check_answer(error_index, user_answer):



    ans = normalize_input(user_answer)
    if error_index == 0:
        return ans == "ekeb"
    elif error_index == 1:
        return ans == "120"
    elif error_index == 2:
        return ans == "almaty"
    return False


def handle_fix_error(state):

    print_header("УСТРАНЕНИЕ ОШИБОК СТЕНДА")
    print(f"Текущие ошибки:")
    print(f"1. Ошибка A (Требуется улика) - {'[Уже исправлена]' if state['fixed_errors'][0] else '[Активна]'}")
    print(f"2. Ошибка B (Расчет времени) - {'[Уже исправлена]' if state['fixed_errors'][1] else '[Активна]'}")
    print(f"3. Ошибка C (Форматирование)  - {'[Уже исправлена]' if state['fixed_errors'][2] else '[Активна]'}")
    print("0. Назад в меню действий")

    choice = input("\nВыберите номер ошибки для исправления (1-3): ").strip()

    if choice == "0":
        return False

    if choice not in ["1", "2", "3"]:
        print("\n [!] Неверный номер ошибки! Ресурсы не потрачены.")
        return False

    idx = int(choice) - 1


    if state['fixed_errors'][idx]:
        print("\n [!] Эта ошибка уже была успешно исправлена ранее! Выберите другую.")
        return False


    if state['energy'] < 2:
        print("\n [!] Недостаточно энергии! Для попытки исправления нужно минимум 2 units энергии.")
        return False


    if idx == 0 and not state['clue_obtained']:
        print("\n [!] Вы не знаете код доступа! Сначала осмотрите стенд, чтобы получить улику.")
        return False


    print("\n--- Задание ---")
    if idx == 0:
        user_ans = input("Введите код доступа к стенду: ")
    elif idx == 1:
        user_ans = input("Сколько минут в 2 часах?: ")
    elif idx == 2:
        user_ans = input("Приведите строку ' Almaty ' к нижнему регистру без пробелов по краям: ")


    state['moves_left'] -= 1
    state['energy'] -= 2

    if check_answer(idx, user_ans):
        state['fixed_errors'][idx] = True
        print("\n [УСПЕХ] Ошибка успешно устранена!")
    else:
        print("\n [ОШИБКА] Неверный ответ! Ресурсы потрачены, но ошибка осталась.")

    return True
