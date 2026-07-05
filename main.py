from wellcome_screen import wellcome_screen
from main_menu import MAIN_MENU, show_main_menu
from user_choice import user_choice


def game():
    wellcome_screen()
    show_main_menu()
    user_choice(MAIN_MENU)


if __name__ == "__main__":
    game()