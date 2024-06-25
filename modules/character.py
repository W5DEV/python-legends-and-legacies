import modules.utils as utils
import modules.dice_rolls as dice_rolls
class Character:
    def __init__(self, name, race, archetype, bio, equipment, abilities, xp, gp, hp=0, max_hp=0, equipped_armor=None, equipped_weapon=None, readied_weapon=None):
        self.name = name
        self.race = race
        self.archetype = archetype
        self.bio = bio
        self.equipment = equipment
        self.xp = xp
        self.gp = gp
        self.hp = hp
        self.max_hp = max_hp
        self.level = 0
        self.equipped_armor = equipped_armor
        self.equippped_weapon = equipped_weapon
        self.readied_weapon = readied_weapon
        self.proficincy_bonus = 0
        self.strength = 0
        self.strength_mod = 0
        self.dexterity = 0
        self.dexterity_mod = 0
        self.constitution = 0
        self.constitution_mod = 0
        self.intelligence = 0
        self.intelligence_mod = 0
        self.wisdom = 0
        self.wisdom_mod = 0
        self.charisma = 0
        self.charisma_mod = 0

    def initialize_player(self):
        self.calculate_level()
        self.calculate_modifiers()
        self.sync_max_hp()
        self.calculate_proficiency_bonus()
        return self

    def level_up(self):
        self.level += 1
        self.sync_level(self.level)
        self.sync_max_hp()
        self.hp = self.max_hp
        self.calculate_proficiency_bonus()
        return f"{self.name} has leveled up to level {self.level}!"
    
    def calculate_modifiers(self):
        self.strength_mod = (self.strength - 10) // 2
        self.dexterity_mod = (self.dexterity - 10) // 2
        self.constitution_mod = (self.constitution - 10) // 2
        self.intelligence_mod = (self.intelligence - 10) // 2
        self.wisdom_mod = (self.wisdom - 10) // 2
        self.charisma_mod = (self.charisma - 10) // 2
        return

    def sync_max_hp(self):
        if self.level == 1:
            self.max_hp = self.archetype.base_hp + self.constitution_mod
        else:
            if self.archetype.hit_die == "d6":
                self.max_hp += dice_rolls.roll_6_sided_dice() + self.constitution_mod
            elif self.archetype.hit_die == "d8":
                self.max_hp += dice_rolls.roll_8_sided_dice() + self.constitution_mod
            elif self.archetype.hit_die == "d10":
                self.max_hp += dice_rolls.roll_10_sided_dice() + self.constitution_mod
            elif self.archetype.hit_die == "d12":
                self.max_hp += dice_rolls.roll_12_sided_dice() + self.constitution_mod

    def calculate_level(self):
        level = utils.calculate_level(self.xp)
        self.level = level
        return 

    def calculate_proficiency_bonus(self):
        self.calculate_level()
        level = self.level
        proficiency_bonus = (-(-level // 4)) + 1
        self.proficiency_bonus = proficiency_bonus
        return
    
    def get_level(self):
        return self.level
    
    def get_proficiency_bonus(self):
        return self.proficiency_bonus

    def sync_level(self, level):
        self.archetype.sync_level(level)

    def sync_equipment(self):
        self.equipment = self.archetype.starting_equipment

    def award_xp(self, xp):
        self.xp += xp
        level = utils.calculate_level(self.xp)
        return f"{self.name} has received {xp} XP and now has a total of {self.xp} XP, making them level {level}."
    
    def xp_needed_for_next_level(self):
        xp_needed = utils.calculate_xp_needed(self.xp)
        return f"{self.name} needs {xp_needed} XP to reach the next level."
    
    def calculate_max_hp(self, hp):
        self.max_hp = hp
        return f"{self.name} has a max HP of {self.max_hp}."

