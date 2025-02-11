'''
This class holds main and general information for all subclasses, like name and max health.
'''
class Character:
    def __init__(self, name, max_health):
        try:
            self.name = name
            self.max_health = int(max_health)
        except:
            raise ValueError('Max health must be a numerical value.')

'''
This class holds only warrior traits.
'''
class WarriorTraits:
    def __init__(self):
        self.strength = 20
        
'''
This class only holds mage traits.
'''
class MageTraits:
    def __init__(self):
        self.mana = 50

'''
This class holds all the general information needed to create a Battle Mage, and also requires name
and max health.
'''
class BattleMage(Character, WarriorTraits, MageTraits):
    def __init__(self, name, max_health):
        super().__init__(name, max_health)
        WarriorTraits.__init__(self)
        MageTraits.__init__(self)

player_1 = BattleMage('Jovan', '90')

print(player_1.strength)
print(player_1.max_health)