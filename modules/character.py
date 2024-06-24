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
        self.equipped_armor = equipped_armor
        self.equippped_weapon = equipped_weapon
        self.readied_weapon = readied_weapon

    def sync_level(self, level):
        self.archetype.sync_level(level)

    def add_armor(self, armor):
        self.armor = armor

    def greet(self):
        return f"Hello, {self.name}!"
    
    def get_info(self):
        return f"{self.name} is a {self.race.subrace} {self.archetype.name}"
    
    def get_bio(self):
        return self.bio
    
    def get_equipment(self):
        return self.equipment
    
    def get_abilities(self):
        return self.abilities
    
    def get_gp(self):
        return self.gp
    
    def get_xp(self):
        level = utils.calculate_level(self.xp)
        return f"{self.name} has {self.xp} xp, so they are level {level}."

    def award_xp(self, xp):
        self.xp += xp
        level = utils.calculate_level(self.xp)
        return f"{self.name} has received {xp} XP and now has a total of {self.xp} XP, making them level {level}."
    
    def get_level(self):
        level = utils.calculate_level(self.xp)
        return level
    
    def xp_needed_for_next_level(self):
        xp_needed = utils.calculate_xp_needed(self.xp)
        return f"{self.name} needs {xp_needed} XP to reach the next level."
    
    def calculate_max_hp(self, hp):
        self.max_hp = hp
        return f"{self.name} has a max HP of {self.max_hp}."

