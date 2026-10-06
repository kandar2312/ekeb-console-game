def handle_command(raw_input):
    """
    Функция Участника 4: Обработка команд игрока и проверка ввода.
    """
    # Очищаем от пробелов по краям
    if raw_input is None:
        cmd = ""
    else:
        cmd = raw_input.strip()

    # Проверка на пустой ввод
    if cmd == "":
        print("\n[!] Вы ничего не ввели. Попробуйте еще раз.")
        return None

    # Валидация введенных пунктов меню
    if cmd == "1":
        print("\n-> Выбрано: Осмотреть стенд")
        return "1"
    elif cmd == "2":
        print("\n-> Выбрано: Забрать зарядку")
        return "2"
    elif cmd == "3":
        print("\n-> Выбрано: Использовать зарядку")
        return "3"
    elif cmd == "4":
        print("\n-> Выбрано: Исправить ошибку")
        return "4"
    elif cmd == "5":
        print("\n-> Выбрано: Статус / инвентарь")
        return "5"
    elif cmd == "0":
        print("\n-> Выбрано: Возврат в меню")
        return "0"
    else:
        print(f"\n[!] Неизвестная команда '{cmd}'. Попробуйте еще раз.")
        return None