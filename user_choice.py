def user_choice(menu):
    while True:
        choice = input("\nВыберите пункт меню: ")
        
        if choice.isdigit():
            choice_idx = int(choice) # Преобразуем строку в число
            if 0 <= choice_idx < len(menu):
                return choice_idx # Возвращаем число для match-case
        
        print(f"Ошибка: введите число от 0 до {len(menu) - 1}")