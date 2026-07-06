class Character:
    # Константы для баланса игры
    DEFAULT_STAT = 1
    MIN_STAT = 1
    MAX_STAT = 20

    MIN_LVL = 1
    MAX_LVL = 100


    def __init__(self, name, strength=None, agility=None, constitution=None,
                 intelligence=None, wisdom=None, luck=None, level :int=1, race=None):
        self.name = name
        self.race = race

        # Если значение не передано, используем DEFAULT_STAT.
        # Метод _stat_validate гарантирует, что стат будет в диапазоне [MIN_STAT, MAX_STAT]
        self.strength = self._stat_validate(strength or self.DEFAULT_STAT)
        self.agility = self._stat_validate(agility or self.DEFAULT_STAT)
        self.constitution = self._stat_validate(constitution or self.DEFAULT_STAT)
        self.intelligence = self._stat_validate(intelligence or self.DEFAULT_STAT)
        self.wisdom = self._stat_validate(wisdom or self.DEFAULT_STAT)
        self.luck = self._stat_validate(luck or self.DEFAULT_STAT)

        self.level = self._level_validate(level) or 1

        # Логика применения бонусов расы перемещена из __post_init__ (только в @dataclass) в __init__
        if self.race:
            for stat, modifier in self.race.stat_modifiers.items():
                # Применяем модификатор, но убеждаемся, что результат остается в допустимых пределах
                current_stat_value = getattr(self, stat)
                setattr(self, stat, self._stat_validate(current_stat_value + modifier))


    def _stat_validate(self, value):
        """Вспомогательный метод, чтобы значение не выходило за границы."""
        # Логика работы: min() ограничивает значение сверху на MAX_STAT,
        # а max() ограничивает результат снизу на MIN_STAT.
        # Результат: значение гарантированно в диапазоне [MIN_STAT, MAX_STAT]
        return max(self.MIN_STAT, min(self.MAX_STAT, value))

    def _level_validate(self, value):
        """Вспомогательный метод, чтобы значение уровня не выходило за границы."""
        return max(self.MIN_LVL, min(self.MAX_LVL, value))




class Race:
    def __init__(self, name, stat_modifiers=None):
        self.name = name
        self.stat_modifiers = stat_modifiers or {}


class Human(Race):
    def __init__(self):
        super().__init__(name="Человек", stat_modifiers={
            "luck": 1
        })

class Elf(Race):
    def __init__(self):
        super().__init__(name="Эльф", stat_modifiers={
            "agility": 1
        })


class Orc(Race):
    def __init__(self):
        super().__init__(name="Орк", stat_modifiers={
            "strength": 1
        })

RACES = (Human, Elf, Orc)