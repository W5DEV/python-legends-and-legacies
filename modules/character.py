import modules.utils as utils

class Character:
    def __init__(self, name, race, archetype, bio, equipment, abilities, xp, gp, hp=0, max_hp=0, equipped_armor=None, equipped_weapon=None, readied_weapon=None):
        self.name = name
        self.race = race
        self.archetype = archetype
        self.bio = bio
        self.equipment = equipment
        self.abilities = abilities
        self.xp = xp
        self.gp = gp
        self.hp = hp
        self.max_hp = max_hp
        self.player_level = 0
        self.equipped_armor = equipped_armor
        self.equippped_weapon = equipped_weapon
        self.readied_weapon = readied_weapon
        self.proficincy_bonus = 0

    def calculate_level(self):
        level = utils.calculate_level(self.xp)
        self.player_level = level
        return 

    def calculate_proficiency_bonus(self):
        self.calculate_level()
        level = self.player_level
        proficiency_bonus = (-(-level // 4)) + 1
        self.proficiency_bonus = proficiency_bonus
        return
    
    def get_level(self):
        return self.player_level
    
    def get_proficiency_bonus(self):
        return self.proficiency_bonus

    def sync_level(self, level):
        self.archetype.sync_level(level)

    def sync_equipment(self):
        self.equipment = self.archetype.starting_equipment
        return

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

