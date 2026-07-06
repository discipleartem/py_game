


class Character:
    def __init__(self, name):
        self.name = name



def create_character():
    print("Создание персонажа:")
    name = input("Введите имя вашего героя: ")
    character = Character(name)
    print(f"Персонаж {character.name} успешно создан!")
    return character
