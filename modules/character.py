import modules.utils as utils

class Character:
    def __init__(self, name, race, archetype, bio, equipment, abilities, xp, gp):
        self.name = name
        self.race = race
        self.archetype = archetype
        self.bio = bio
        self.equipment = equipment
        self.abilities = abilities
        self.xp = xp
        self.gp = gp

    def add_armor(self, armor):
        self.armor = armor

    def add_weapon(self, weapon):
        self.weapon = weapon

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
    
    def xp_needed_for_next_level(self):
        xp_needed = utils.calculate_xp_needed(self.xp)
        return f"{self.name} needs {xp_needed} XP to reach the next level."
