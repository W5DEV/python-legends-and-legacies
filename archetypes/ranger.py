import modules.starting_equipment as starting_equipment
import modules.skills as skills

displayed_ranger_skills, ranger_skills = skills.get_ranger_skills()
potential_starting_equipment = starting_equipment.get_starting_equipment("Ranger")       

class Ranger:
    
    def __init__(self):
        name = "Ranger"
        bio = "A warrior who uses martial prowess and nature magic to combat threats on the edges of civilization"
        hit_die = "1d10"
        primary_ability = "Dexterity, Wisdom"
        saving_throw_proficiencies = "Strength, Dexterity"
        armor_proficiencies = "Light Armor, Medium Armor, Shields"
        weapon_proficiencies = "Simple Weapons, Martial Weapons"
        self.name = name
        self.bio = bio
        self.hit_die = hit_die
        self.base_hp = 10
        self.primary_ability = primary_ability
        self.saving_throw_proficiencies = saving_throw_proficiencies
        self.armor_proficiencies = armor_proficiencies
        self.weapon_proficiencies = weapon_proficiencies
        self.tool_proficiencies = []
        self.skill_proficiencies = []
        self.starting_equipment = []
        self.fighting_style = ""
        self.ranger_archetype = ""
        self.special_abilities = []
        self.spells_known = 0
        self.spell_slots_level_1 = 0
        self.spell_slots_level_2 = 0
        self.spell_slots_level_3 = 0
        self.spell_slots_level_4 = 0
        self.spell_slots_level_5 = 0

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
            self.special_abilities.append("Favored Enemy")
            self.special_abilities.append("Natural Explorer")
        if level >= 2:
            print("You have reached level 1 and now have the following fighting styles:")
            for style in ["Archery", "Defense", "Dueling", "Two-Weapon Fighting"]:
                print(style)
            print("Please enter your choice of fighting style:")
            fighting_style_choice = input("> ")
            while fighting_style_choice.lower() not in ["archery", "defense", "dueling", "two-weapon fighting"]:
                print("That is not a valid choice. Please choose from the list.")
                fighting_style_choice = input("> ")
            self.fighting_style.append(fighting_style_choice)
            print(f"You have chosen the {fighting_style_choice} fighting style.")
            print("You cannot specialize in this fighting style in the future.")
            print("You have also gained the following special abilities:")
            self.special_abilities.append("Spellcasting")
            self.spells_known = 2
            self.spell_slots_level_1 = 2
        if level >= 3:
            self.ranger_archetype = "Hunter"
            self.special_abilities.append("Hunter's Prey")
            self.special_abilities.append("Primeval Awareness")
            self.spells_known = 3
            self.spell_slots_level_1 = 3
        if level >= 4:
            self.special_abilities.append("Ability Score Improvement 4th Level")
        if level >= 5:
            self.special_abilities.append("Extra Attack")
            self.spells_known = 4
            self.spell_slots_level_1 = 4
            self.spell_slots_level_2 = 2
        if level >= 6:
            self.special_abilities.append("Favorite Enemy Improvement")
            self.special_abilities.append("Natural Explorer Improvement")
        if level >= 7:
            self.special_abilities.append("Defensive Tactics")
            self.spells_known = 5
            self.spell_slots_level_3 = 3
        if level >= 8:
            self.special_abilities.append("Ability Score Improvement 8th Level")
            self.special_abilities.append("Land's Stride")
        if level >= 9:
            self.spells_known = 6
            self.spell_slots_level_3 = 2
        if level >= 10:
            self.special_abilities.append("Natural Explorer Improvement")
            self.special_abilities.append("Hide in Plain Sight")
        if level >= 11:
            self.special_abilities.append("Multiattack")
            self.spells_known = 7
            self.spell_slots_level_3 = 3
        if level >= 12:
            self.special_abilities.append("Ability Score Improvement 12th Level")
        if level >= 13:
            self.spells_known = 8
            self.spell_slots_level_4 = 1
        if level >= 14:
            self.special_abilities.append("Favored Enemy Improvement")
            self.special_abilities.append("Vanish")
        if level >= 15:
            self.special_abilities.append("Superior Hunter's Defense")
            self.spells_known = 9
            self.spell_slots_level_4 = 2
        if level >= 16:
            self.special_abilities.append("Ability Score Improvement 16th Level")
        if level >= 17:
            self.spells_known = 10
            self.spell_slots_level_4 = 3
            self.spell_slots_level_5 = 1
        if level >= 18:
            self.special_abilities.append("Fereal Senses")
        if level >= 19:
            self.special_abilities.append("Ability Score Improvement 19th Level")
            self.spells_known = 11
            self.spell_slots_level_5 = 2
        if level >= 20:
            self.special_abilities.append("Foe Slayer")

def define_ranger():
    ranger = Ranger()
    print("You have chosen the ranger class.")
    print(ranger.bio)

    # Skill Proficiencies
    print("Choose two skills from the following list:")
    for skill in displayed_ranger_skills:
        print(skill)
    print("Please enter your first skill choice:")
    skill_choice1 = input("> ")
    while skill_choice1.lower() not in ranger_skills:
        print("That is not a valid choice. Please choose from the list.")
        skill_choice1 = input("> ")
    ranger.skill_proficiencies.append(skill_choice1)

    print("Please enter your second skill choice:")
    skill_choice2 = input("> ")
    while skill_choice2.lower() not in ranger_skills:
        print("That is not a valid choice. Please choose from the list.")
        skill_choice2 = input("> ")
    ranger.skill_proficiencies.append(skill_choice2)

    print("You have chosen the following skills:")
    for skill in ranger.skill_proficiencies:
        print(skill)

    # Starting Equipment
    equipment_choice_1 = starting_equipment.starting_equipment_choice("Scale Mail", "Leather Armor")
    if equipment_choice_1.lower() == "scale mail":
        armor_choice = starting_equipment.starting_equipment("Scale Mail Medium Armor")
    elif equipment_choice_1.lower() == "leather armor":
        armor_choice = starting_equipment.starting_equipment("Leather Light Armor")
    print(f"{armor_choice.name} has been added to your starting equipment.")
    ranger.starting_equipment.append(armor_choice)

    equipment_choice_2 = starting_equipment.starting_equipment_choice("Two Shortswords", "Two Simple Melee Weapons")
    if equipment_choice_2.lower() == "two shortswords":
        weapon_choice = starting_equipment.starting_equipment("Short Sword")
        print(f"Two {weapon_choice.name}'s have been added to your starting equipment.")
        ranger.starting_equipment.append(weapon_choice)
        ranger.starting_equipment.append(weapon_choice)
    else:
        weapon_choice = starting_equipment.select_equipment_from_category("Simple Melee Weapons")
        print(f"One {weapon_choice.name}'s have been added to your starting equipment.")
        ranger.starting_equipment.append(weapon_choice)
        weapon_choice = starting_equipment.select_equipment_from_category("Simple Melee Weapons")
        print(f"One {weapon_choice.name}'s have been added to your starting equipment.")
        ranger.starting_equipment.append(weapon_choice)

    equipment_choice_3 = starting_equipment.starting_equipment_choice("Dungeoneer's Pack", "Explorer's Pack")
    if equipment_choice_3.lower() == "dungeoneer's pack":
        pack_choice = starting_equipment.starting_equipment("Dungeoneer's Pack")
    else:
        pack_choice = starting_equipment.starting_equipment("Explorer's Pack")
    print(f"One {pack_choice.name} has been added to your starting equipment.")
    ranger.starting_equipment.append(pack_choice)

    longbow = starting_equipment.starting_equipment("Longbow")
    print("A Longbow and a quiver of 20 arrows. have been added to your starting equipment.")
    ranger.starting_equipment.append(longbow)
    # Add quiver of 20 arrows to starting equipment

    return ranger