# Since the word "class" is reserved in Python, we will use the term "archetype" to refer to the D&D classes.
# This module contains a list of all the archetypes DndBeyond has for character creation.
# We will eventually expand the archetypes to be full-fledged classes, but for now, we will keep them simple.

import modules.equipment as equipment

displayed_archetypes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]

archetypes = ["barbarian", "bard", "cleric", "druid", "fighter", "monk", "paladin", "ranger", "rogue", "sorcerer", "warlock", "wizard"]

def display_archetypes():
    for archetype in displayed_archetypes:
        print(archetype)

class Archetype:
    def __init__(self, name, description, hit_die, primary_ability, saving_throw_proficiencies, armor_proficiencies, weapon_proficiencies, tool_proficiencies, skill_proficiencies, starting_equipment):
        self.name = name
        self.description = description
        self.hit_die = hit_die
        self.primary_ability = primary_ability
        self.saving_throw_proficiencies = saving_throw_proficiencies
        self.armor_proficiencies = armor_proficiencies
        self.weapon_proficiencies = weapon_proficiencies
        self.tool_proficiencies = tool_proficiencies
        self.skill_proficiencies = skill_proficiencies
        self.starting_equipment = starting_equipment
    
    def get_info(self):
        return f"{self.name} is a {self.hit_die} archetype that uses {self.primary_ability} as their primary ability."
    
def define_barbarian():
    name = "Barbarian"
    description = "A fierce warrior of primitive background who can enter a battle rage"
    hit_die = "d12"
    primary_ability = "Strength"
    saving_throw_proficiencies = "Strength, Constitution"
    armor_proficiencies = "Light Armor, Medium Armor, Shields"
    weapon_proficiencies = "Simple Weapons, Martial Weapons"
    tool_proficiencies = "None"
    displayed_skill_proficiencies = ["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"]
    skill_proficiencies = ["animal handling", "athletics", "intimidation", "nature", "perception", "survival"]
    starting_equipment = ["Greataxe or any martial melee weapon", "Two Handaxes or Any Simple Weapon", "Explorer's Pack", "Four Javelins"]
    print(f'You have chosen the {name} class.')
    print(description)

    # Skill Proficiencies
    print("Choose 2 skills from the following list, which you will be proficient in:")
    for skill in displayed_skill_proficiencies:
        print(skill)
    print("Please enter your first skill choice:")
    skill_choice1 = input("> ")
    while skill_choice1.lower() not in skill_proficiencies:
        print("That is not a valid choice. Please choose from the list.")
        skill_choice1 = input("> ")
    print("Please enter your second skill choice:")
    skill_choice2 = input("> ")
    while skill_choice2.lower() not in skill_proficiencies:
        print("That is not a valid choice. Please choose from the list.")
        skill_choice2 = input("> ")
    selected_skill_proficiencies = [skill_choice1, skill_choice2]
    print(f"You have chosen {selected_skill_proficiencies[0]} and {selected_skill_proficiencies[1]} as your skill proficiencies.")
    
    # Starting Equipment
    first_weapon = ""
    second_weapon = ""
    print(f"{name}'s are able to choose between a few different starting equipment options.")
    print(f'You will start with the following equipment: {starting_equipment}')
    print("Would you like to start with a Greataxe or any martial melee weapon?")
    print("Please enter your either 'Greataxe' or 'Other Weapon':")
    first_weapon_preference = input("> ")
    while first_weapon_preference.lower() not in ["greataxe", "other weapon"]:
        print("That is not a valid choice. Please choose from the list.")
        first_weapon_preference = input("> ")
    if first_weapon_preference.lower() == "greataxe":
        first_weapon = equipment.great_axe
    else:
        print("Please choose a martial melee weapon from the following list:")
        valid_weapons = []
        for weapon in equipment.martial_melee_weapons:
            valid_weapons.append(weapon.name.lower())
            print(weapon.name)
        first_weapon_choice = input("> ")
        while first_weapon_choice.lower() not in valid_weapons:
            print("That is not a valid choice. Please choose from the list.")
            first_weapon_choice = input("> ")
        for weapon in equipment.martial_melee_weapons:
            if first_weapon_choice.lower() == weapon.name.lower():
                first_weapon = weapon
                break
    print(f"You have chosen {first_weapon.name} as your first weapon.")
    print(f"One {first_weapon.name} has been added to your starting equipment.")

    print("Would you like to start with Two Handaxes or any Other Simple Weapon?")
    print("Please enter your either 'Two Handaxes' or 'Other Simple Weapon':")
    second_weapon_preference = input("> ")
    while second_weapon_preference.lower() not in ["two handaxes", "other weapon"]:
        print("That is not a valid choice. Please choose from the list.")
        second_weapon_preference = input("> ")
    if second_weapon_preference.lower() == "two handaxes":
        second_weapon = equipment.hand_axe
    else:
        print("Please choose a martial melee weapon from the following list:")
        valid_weapons = []
        for weapon in equipment.simple_weapons:
            valid_weapons.append(weapon.name.lower())
            print(weapon.name)
        second_weapon_choice = input("> ")
        while second_weapon_choice.lower() not in valid_weapons:
                print("That is not a valid choice. Please choose from the list.")
                second_weapon_choice = input("> ")
        for weapon in equipment.simple_weapons:
            if second_weapon_choice.lower() == weapon.name.lower():
                second_weapon = weapon
                break
   
    if second_weapon == equipment.hand_axe:
        print("You have also chosen Two Handaxes as your secon weapon.")
        print("You will have two handaxes in your inventory, which can be dual weilded or used individually for melee or throwing attacks.")
        print("Two Handaxes have been added to your starting equipment.")
    else:
         print(f"You have chosen one {second_weapon.name} as your second weapon.")
         print(f"One {second_weapon.name} has been added to your starting equipment.")

    selected_starting_equipment = [first_weapon, second_weapon, second_weapon, equipment.explorers_pack, equipment.javelin, equipment.javelin, equipment.javelin, equipment.javelin]

    barbarian = Archetype(name, description, hit_die, primary_ability, saving_throw_proficiencies, armor_proficiencies, weapon_proficiencies, tool_proficiencies, selected_skill_proficiencies, selected_starting_equipment)

    return barbarian
        


