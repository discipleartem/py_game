from wellcome_screen import wellcome_screen
from main_menu import MAIN_MENU, show_main_menu
from user_choice import user_choice
from create_character import create_character


def game():
    wellcome_screen()
    show_main_menu()

    # Обработка выбора пользователя с использованием конструкции match-case (доступно в Python 3.10+).
    match user_choice(MAIN_MENU):
        # Если пользователь выбрал пункт с индексом 1 ("Новая Игра").
        case 1:
            create_character()
        # Если пользователь выбрал пункт с индексом 0 ("Выйти").
        case 0:
            print("Выход из игры. До встречи!")
            # Завершаем выполнение программы.
            exit()
        case _:
            # Обработка любого другого значения (на случай ошибок в user_choice)
            print("Произошла системная ошибка выбора.")


if __name__ == "__main__":
    game()