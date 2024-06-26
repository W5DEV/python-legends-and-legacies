import modules.starting_equipment as starting_equipment
import modules.skills as skills

displayed_fighter_skills, fighter_skills = skills.get_fighter_skills()
potential_starting_equipment = starting_equipment.get_starting_equipment("Fighter")
     
class Fighter:
    
    def __init__(self):
        name = "Fighter"
        bio = "A master of martial combat, skilled with a variety of weapons and armor."
        hit_die = "1d10"
        primary_ability = "Strength or Dexterity"
        saving_throw_proficiencies = "Strength, Constitution"
        armor_proficiencies = "All Armor, Shields"
        weapon_proficiencies = "All Simple Weapons and Martial Weapons"
        tool_proficiencies = "None"
        self.name = name
        self.bio = bio
        self.hit_die = hit_die
        self.base_hp = 10
        self.primary_ability = primary_ability
        self.saving_throw_proficiencies = saving_throw_proficiencies
        self.armor_proficiencies = armor_proficiencies
        self.weapon_proficiencies = weapon_proficiencies
        self.tool_proficiencies = tool_proficiencies
        self.skill_proficiencies = []
        self.starting_equipment = []
        self.fighting_style = []
        self.marital_archetype = ""
        self.special_abilities = []

    def get_info(self):
        print(f"The {self.name}: {self.bio}")
        print(f"Hit Die: {self.hit_die}")
        print(f"Primary Ability: {self.primary_ability}")
        print(f"Saving Throw Proficiencies: {self.saving_throw_proficiencies}")
        print(f"Armor Proficiencies: {self.armor_proficiencies}")
        print(f"Weapon Proficiencies: {self.weapon_proficiencies}")
        print(f"Tool Proficiencies: {self.tool_proficiencies}")
        print(f"Skill Proficiencies:")
        for skill in self.skill_proficiencies:
            print(skill)
        print(f"Starting Equipment:")
        for item in self.starting_equipment:
            print(item.name)
        print(f"Special Abilities:")
        for ability in self.special_abilities:
            print(ability)
        return
    
    def sync_level(self, level):
        if level >= 1:
            print("You have reached level 1 and now have the following fighting styles:")
            for style in ["Archery", "Defense", "Dueling", "Great Weapon Fighting", "Protection", "Two-Weapon Fighting"]:
                print(style)
            print("Please enter your choice of fighting style:")
            fighting_style_choice = input("> ")
            while fighting_style_choice.lower() not in ["archery", "defense", "dueling", "great weapon fighting", "protection", "two-weapon fighting"]:
                print("That is not a valid choice. Please choose from the list.")
                fighting_style_choice = input("> ")
            self.fighting_style.append(fighting_style_choice)
            print(f"You have chosen the {fighting_style_choice} fighting style.")
            print("You cannot specialize in this fighting style in the future.")
            print("You have also gained the following special abilities:")
            self.special_abilities.append("Second Wind")
        if level >= 2:
            self.special_abilities.append("Action Surge (1/rest)")
        if level >= 3:
            self.marital_archetype = "Champion"
            self.special_abilities.append("Improved Critical (crit range 19-20)")
        if level >= 4:
            self.special_abilities.append("Ability Score Improvement 4th Level")
        if level >= 5:
            self.special_abilities.append("Extra Attack (1 extra attack)")
        if level >= 6:
            self.special_abilities.append("Ability Score Improvement 6th Level")
        if level >= 7:
            self.special_abilities.append("Remarkable Athlete")
        if level >= 8:
            self.special_abilities.append("Ability Score Improvement 8th Level")
        if level >= 9:
            self.special_abilities.append("Indomitable (1/rest)")
        if level >= 10:
            self.special_abilities.append("Additional Fighting Style")
            print("You have reached level 10 and now have the following fighting styles:")
            for style in ["Archery", "Defense", "Dueling", "Great Weapon Fighting", "Protection", "Two-Weapon Fighting"]:
                print(style)
            print("Please enter your choice of fighting style:")
            fighting_style_choice = input("> ")
            while (fighting_style_choice.lower() not in ["archery", "defense", "dueling", "great weapon fighting", "protection", "two-weapon fighting"]) and (fighting_style_choice not in self.fighting_style):
                print("That is not a valid choice. Please choose an unused style from the list.")
                print("Your current fighting styles are:")
                for style in self.fighting_style:
                    print(style)
                fighting_style_choice = input("> ")
            self.fighting_style.append(fighting_style_choice)
            print(f"You have chosen the {fighting_style_choice} fighting style.")
        if level >= 11:
            self.special_abilities.append("Extra Attack (2 extra attacks)")
        if level >= 12:
            self.special_abilities.append("Ability Score Improvement 12th Level")
        if level >= 13:
            self.special_abilities.append("Indomitable (2/rest)")
        if level >= 14:
            self.special_abilities.append("Ability Score Improvement 14th Level")
        if level >= 15:
            self.special_abilities.append("Superior Critical (crit range 18-20)")
        if level >= 16:
            self.special_abilities.append("Ability Score Improvement 16th Level")
        if level >= 17:
            self.special_abilities.append("Action Surge (2/rest)")
            self.special_abilities.append("Indomitable (3/rest)")
        if level >= 18:
            self.special_abilities.append("Survivor")
        if level >= 19:
            self.special_abilities.append("Ability Score Improvement 19th Level")
        if level >= 20:
            self.special_abilities.append("Extra Attack (3 extra attacks)")

def define_fighter():
    fighter = Fighter()
    print("You have chosen the Fighter class.")
    print(fighter.bio)

    # Skill Proficiencies
    print("Choose two skills from the following list:")
    for skill in displayed_fighter_skills:
        print(skill)
    print("Please enter your first skill choice:")
    skill_choice1 = input("> ")
    while skill_choice1.lower() not in fighter_skills:
        print("That is not a valid choice. Please choose from the list.")
        skill_choice1 = input("> ")
    fighter.skill_proficiencies.append(skill_choice1)

    print("Please enter your second skill choice:")
    skill_choice2 = input("> ")
    while skill_choice2.lower() not in fighter_skills:
        print("That is not a valid choice. Please choose from the list.")
        skill_choice2 = input("> ")
    fighter.skill_proficiencies.append(skill_choice2)

    print("You have chosen the following skills:")
    for skill in fighter.skill_proficiencies:
        print(skill)

    # Starting Equipment
    equipment_choice_1 = starting_equipment.starting_equipment_choice("Chain Mail", "Leather Armor, Longbow, and 20 Arrows")
    if equipment_choice_1.lower() == "chain mail":
        starting_weapon = starting_equipment.starting_equipment("Chain Mail Heavy Armor")
        print(f"{starting_weapon.name} has been added to your starting equipment.")
        fighter.starting_equipment.append(starting_weapon)
    else:
        starting_weapon = starting_equipment.starting_equipment("Leather Light Armor")
        print(f"{starting_weapon.name} has been added to your starting equipment.")
        fighter.starting_equipment.append(starting_weapon)
        starting_weapon = starting_equipment.starting_equipment("Longbow")
        print(f"{starting_weapon.name} has been added to your starting equipment.")
        fighter.starting_equipment.append(starting_weapon)
        # Add 20 arrows here.

    equipment_choice_2 = starting_equipment.starting_equipment_choice("Any Martial Weapon and a Shield", "Two Martial Weapons")
    if equipment_choice_2.lower() == "any martial weapon and a shield":
        starting_weapon = starting_equipment.select_equipment_from_category("Martial Weapons")
        print(f"{starting_weapon.name} has been added to your starting equipment.")
        fighter.starting_equipment.append(starting_weapon)
        starting_weapon = starting_equipment.starting_equipment("Shield")
        print(f"{starting_weapon.name} has been added to your starting equipment.")
        fighter.starting_equipment.append(starting_weapon)
    else:
        starting_weapon = starting_equipment.select_equipment_from_category("Martial Weapons")
        print(f"{starting_weapon.name} has been added to your starting equipment.")
        fighter.starting_equipment.append(starting_weapon)
        starting_weapon = starting_equipment.select_equipment_from_category("Martial Weapons")
        print(f"{starting_weapon.name} has been added to your starting equipment.")
        fighter.starting_equipment.append(starting_weapon)

    equipment_choice_3 = starting_equipment.starting_equipment_choice("Light Crossbow and 20 Bolts", "Two Handaxes")
    if equipment_choice_3.lower() == "light crossbow and 20 bolts":
        starting_weapon = starting_equipment.starting_equipment("Light Crossbow")
        print(f"{starting_weapon.name} has been added to your starting equipment.")
        fighter.starting_equipment.append(starting_weapon)
        # Add 20 bolts here.
    else:
        starting_weapon = starting_equipment.starting_equipment("Hand Axe")
        print(f"Two {starting_weapon.name}'s have been added to your starting equipment.")
        fighter.starting_equipment.append(starting_weapon)
        fighter.starting_equipment.append(starting_weapon)

    equipment_choice_3 = starting_equipment.starting_equipment_choice("Dungeoneer's Pack", "Explorer's Pack")
    if equipment_choice_3.lower() == "dungeoneer's pack":
        starting_pack = starting_equipment.starting_equipment("Dungeoneer's Pack")
    else:
        starting_pack = starting_equipment.starting_equipment("Explorer's Pack")
    print(f"{starting_pack.name} has been added to your starting equipment.")
    fighter.starting_equipment.append(starting_pack)

    return fighter