from character import Character
from character import RACES # tuple с объектами классов


def display_character(character):
    print(f"Имя: {character.name}")
    print()

    print(f"Уровень: {character.level} ")
    print()

    print("Ваши характеристики:")
    print(f"Сила: {character.strength}")
    print(f"Ловкость: {character.agility}")
    print(f"Выносливость: {character.constitution}")
    print(f"Интеллект: {character.intelligence}")
    print(f"Мудрость: {character.wisdom}")
    print(f"Удача: {character.luck}")
    print()


def set_race(races):
    print()
    print("Выберите расу вашего персонажа:")
    for i, race in enumerate(races, start=1):
        print(f"{i}. {race().name}")

    choice = input("Введите номер расы: ")

    try:
        choice = int(choice)
    except ValueError:
        print("Ошибка: Введите корректный номер расы.")
        return set_race(races)

    return races[choice - 1]()



def create_character():
    print("Создание персонажа:")
    print()
    name = input("Введите имя вашего героя: ")
    print()

    race = set_race(races=RACES)
    character = Character(name=name, level=1, race=race)
    display_character(character=character)
    print(f"Персонаж {character.name} успешно создан!")

    return character