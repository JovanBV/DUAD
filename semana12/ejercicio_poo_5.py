class Character:
    def __init__(self, name, max_health):
        self.name = name
        self.max_health = max_health

class WarriorTraits:
    def __init__(self):
        self.strength = 20

class MageTraits:
    def __init__(self):
        self.mana = 50

class BattleMage(Character, WarriorTraits, MageTraits):
    def __init__(self, name, max_health):
        Character.__init__(self, name, max_health)
        WarriorTraits.__init__(self)
        MageTraits.__init__(self)

player_1 = BattleMage('Jovan', 30)

print(player_1.strength)
print(player_1.max_health)