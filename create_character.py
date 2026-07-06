


class Character:
    # Константы для баланса игры
    DEFAULT_STAT = 1
    MIN_STAT = 1
    MAX_STAT = 20

    MIN_LVL = 1
    MAX_LVL = 100


    def __init__(self, name, strength=None, agility=None, constitution=None,
                 intelligence=None, wisdom=None, luck=None, level :int=1):
        self.name = name
        
        # Если значение не передано, используем DEFAULT_STAT.
        # Метод _stat_validate гарантирует, что стат будет в диапазоне [MIN_STAT, MAX_STAT]
        self.strength = self._stat_validate(strength or self.DEFAULT_STAT)
        self.agility = self._stat_validate(agility or self.DEFAULT_STAT)
        self.constitution = self._stat_validate(constitution or self.DEFAULT_STAT)
        self.intelligence = self._stat_validate(intelligence or self.DEFAULT_STAT)
        self.wisdom = self._stat_validate(wisdom or self.DEFAULT_STAT)
        self.luck = self._stat_validate(luck or self.DEFAULT_STAT)

        self.level = self._level_validate(level) or 1



    def _stat_validate(self, value):
        """Вспомогательный метод, чтобы значение не выходило за границы."""
        # Логика работы: min() ограничивает значение сверху на MAX_STAT,
        # а max() ограничивает результат снизу на MIN_STAT.
        # Результат: значение гарантированно в диапазоне [MIN_STAT, MAX_STAT]
        return max(self.MIN_STAT, min(self.MAX_STAT, value))

    def _level_validate(self, value):
        """Вспомогательный метод, чтобы значение уровня не выходило за границы."""
        return max(self.MIN_LVL, min(self.MAX_LVL, value))




def create_character():
    print("Создание персонажа:")
    name = input("Введите имя вашего героя: ")
    character = Character(name=name, level=1)
    print()
    print(f"Персонаж {character.name} успешно создан!")
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

    return character
