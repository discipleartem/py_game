


class Character:
    # Константы для баланса игры
    DEFAULT_STAT = 1
    MIN_STAT = 1
    MAX_STAT = 20

    def __init__(self, name, strength=None, agility=None, constitution=None,
                 intelligence=None, wisdom=None,  luck=None):
        self.name = name
        
        # Если значение не передано, используем DEFAULT_STAT.
        # Метод _clamp гарантирует, что стат будет в диапазоне [MIN_STAT, MAX_STAT]
        self.strength = self._clamp(strength or self.DEFAULT_STAT)
        self.agility = self._clamp(agility or self.DEFAULT_STAT)
        self.constitution = self._clamp(constitution or self.DEFAULT_STAT)
        self.intelligence = self._clamp(intelligence or self.DEFAULT_STAT)
        self.wisdom = self._clamp(wisdom or self.DEFAULT_STAT)
        self.luck = self._clamp(luck or self.DEFAULT_STAT)



    def _clamp(self, value):
        """Вспомогательный метод, чтобы значение не выходило за границы."""
        # Логика работы: min() ограничивает значение сверху на MAX_STAT,
        # а max() ограничивает результат снизу на MIN_STAT.
        # Результат: значение гарантированно в диапазоне [MIN_STAT, MAX_STAT]
        return max(self.MIN_STAT, min(self.MAX_STAT, value))





def create_character():
    print("Создание персонажа:")
    name = input("Введите имя вашего героя: ")
    character = Character(name)
    print(f"Персонаж {character.name} успешно создан!")
    return character
