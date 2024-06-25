# This module contains a list of all the races DndBeyond has for character creation.

import modules.names as names

displayed_races = ["Hill Dwarf", "Mountain Dwarf", "High Elf", "Wood Elf", "Lightfoot Halfling", "Stout Halfling", "Human"]

races = ["hill dwarf", "mountain dwarf", "high elf", "wood elf", "lightfoot halfling", "stout halfling", "human"]

def display_races():
    for race in displayed_races:
        print(race)
    return

def define_hill_dwarf(tool_proficiency):
    print("What is your dwarf's gender? (male/female)")
    gender = input("> ")
    while gender.lower() not in ["male", "female"]:
        print("Please enter only male or female.")
        print("What is your dwarf's gender? (male/female)")
        gender = input("> ")
    name = names.get_dwarf_name(gender)
    hill_dwarf = Race(name, gender, "Dwarf", "Hill Dwarf", "Medium", 25, "Common, Dwarvish", "Constitution: 2, Wisdom: 1", "Darkvision, Dwarven Resilience, Dwarven Combat Training, Stonecunning, Tool Proficiency, Dwarven Toughness", "Battleaxe, Handaxe, Light Hammer, Warhammer")
    hill_dwarf.proficiencies += f", {tool_proficiency}"
    return hill_dwarf

def define_mountain_dwarf(tool_proficiency):
    print("What is your dwarf's gender? (male/female)")
    gender = input("> ")
    while gender.lower() not in ["male", "female"]:
        print("Please enter only male or female.")
        print("What is your dwarf's gender? (male/female)")
        gender = input("> ")
    name = names.get_dwarf_name(gender)
    mountain_dwarf = Race(name, gender, "Dwarf", "Mountain Dwarf", "Medium", 25, "Common, Dwarvish", "Constitution: 2, Strength: 2", "Darkvision, Dwarven Resilience, Dwarven Combat Training, Stonecunning, Tool Proficiency, Dwarven Armor Training", "Battleaxe, Handaxe, Light Hammer, Warhammer, Light Armor, Medium Armor")
    mountain_dwarf.proficiencies += f", {tool_proficiency}"
    return mountain_dwarf

def define_high_elf(language):
    print("What is your elf's gender? (male/female)")
    gender = input("> ")
    while gender.lower() not in ["male", "female"]:
        print("Please enter only male or female.")
        print("What is your elf's gender? (male/female)")
        gender = input("> ")
    name = names.get_elf_name(gender)
    high_elf = Race(name, gender, "Elf", "High Elf", "Medium", 30, "Common, Elvish", "Dexterity: 2, Intelligence: 1", "Darkvision, Keen Senses, Fey Ancestry, Trance, Elf Weapon Training, Cantrip, Extra Language", "Longsword, Shortsword, Longbow, Shortbow")
    high_elf.languages += f", {language}"
    return high_elf

def define_wood_elf():
    print("What is your elf's gender? (male/female)")
    gender = input("> ")
    while gender.lower() not in ["male", "female"]:
        print("Please enter only male or female.")
        print("What is your elf's gender? (male/female)")
        gender = input("> ")
    name = names.get_elf_name(gender)
    wood_elf = Race(name, gender, "Elf", "Wood Elf", "Medium", 35, "Common, Elvish", "Dexterity: 2, Wisdom: 1", "Darkvision, Keen Senses, Fey Ancestry, Trance, Elf Weapon Training, Fleet of Foot, Mask of the Wild", "Longsword, Shortsword, Longbow, Shortbow")
    return wood_elf

def define_lightfoot_halfling():
    print("What is your halfling's gender? (male/female)")
    gender = input("> ")
    while gender.lower() not in ["male", "female"]:
        print("Please enter only male or female.")
        print("What is your halfling's gender? (male/female)")
        gender = input("> ")
    name = names.get_halfling_name(gender)
    lightfoot_halfling = Race(name, gender, "Halfling", "Lightfoot Halfling", "Small", 25, "Common, Halfling", "Dexterity: 2, Charisma: 1", "Lucky, Brave, Halfling Nimbleness, Naturally Stealthy", "None")
    return lightfoot_halfling

def define_stout_halfling():
    print("What is your halfling's gender? (male/female)")
    gender = input("> ")
    while gender.lower() not in ["male", "female"]:
        print("Please enter only male or female.")
        print("What is your halfling's gender? (male/female)")
        gender = input("> ")
    name = names.get_halfling_name(gender)
    stout_halfling = Race(name, gender, "Halfling", "Stout Halfling", "Small", 25, "Common, Halfling", "Dexterity: 2, Constitution: 1", "Lucky, Brave, Halfling Nimbleness, Stout Resilience", "None")
    return stout_halfling

def define_human():
    print("What is your human's gender? (male/female)")
    gender = input("> ")
    while gender.lower() not in ["male", "female"]:
        print("Please enter only male or female.")
        print("What is your human's gender? (male/female)")
        gender = input("> ")
    name = names.get_human_name()
    human = Race(name, gender, "Human", "Human", "Medium", 30, "Common", "All ability scores: 1", "None", "None")
    return human

def test_races():
    print("Testing Races...")
    display_races()
    print("Testing Hill Dwarf... ")
    hill_dwarf_test = define_hill_dwarf("Pickaxe")
    print(hill_dwarf_test.get_info())
    print("Testing Mountain Dwarf... ")
    mountain_dwarf_test = define_mountain_dwarf("Pickaxe")
    print(mountain_dwarf_test.get_info())
    print("Testing High Elf... ")
    high_elf_test = define_high_elf("Sylvan")
    print(high_elf_test.get_info())
    print("Testing Wood Elf... ")
    wood_elf_test = define_wood_elf()
    print(wood_elf_test.get_info())
    print("Testing Lightfoot Halfling... ")
    lightfoot_halfling_test = define_lightfoot_halfling()
    print(lightfoot_halfling_test.get_info())
    print("Testing Stout Halfling... ")
    stout_halfling_test = define_stout_halfling()
    print(stout_halfling_test.get_info())
    print("Testing Human... ")
    human_test = define_human()
    print(human_test.get_info())
    print("Race Tests Completed...")
    print("Please report any bugs or errors.")
    return 

class Race:
    def __init__(self, name, gender, race, subrace, size, speed, languages, ability_score_increase, traits, proficiencies):
        self.name = name
        self.gender = gender
        self.race = race
        self.subrace = subrace
        self.size = size
        self.speed = speed
        self.languages = languages
        self.ability_score_increase = ability_score_increase
        self.traits = traits
        self.proficiencies = proficiencies
    
    def get_info(self):
        return f"{self.name} is a {self.size} {self.race}, in the {self.subrace} subrace. They have a speed of {self.speed} and can speak {self.languages}. They have the following ability score increases: {self.ability_score_increase}. They have the following traits: {self.traits}. They hold the following proficiencies: {self.proficiencies}."