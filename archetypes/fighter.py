import modules.equipment as equipment
import modules.skills as skills

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
    
    def sync_level(self, level, player):
        if level == 1:
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
        if level == 2:
            self.special_abilities.append("Action Surge (1/rest)")
        if level == 3:
            self.marital_archetype = "Champion"
            self.special_abilities.append("Improved Critical (crit range 19-20)")
        if level == 4:
            self.special_abilities.append("Ability Score Improvement 4th Level")
            player.update_ability_points(2)
        if level == 5:
            self.special_abilities.append("Extra Attack (1 extra attack)")
        if level == 6:
            self.special_abilities.append("Ability Score Improvement 6th Level")
            player.update_ability_points(2)
        if level == 7:
            self.special_abilities.append("Remarkable Athlete")
        if level == 8:
            self.special_abilities.append("Ability Score Improvement 8th Level")
            player.update_ability_points(2)
        if level == 9:
            self.special_abilities.append("Indomitable (1/rest)")
        if level == 10:
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
        if level == 11:
            self.special_abilities.append("Extra Attack (2 extra attacks)")
        if level == 12:
            self.special_abilities.append("Ability Score Improvement 12th Level")
            player.update_ability_points(2)
        if level == 13:
            self.special_abilities.append("Indomitable (2/rest)")
        if level == 14:
            self.special_abilities.append("Ability Score Improvement 14th Level")
            player.update_ability_points(2)
        if level == 15:
            self.special_abilities.append("Superior Critical (crit range 18-20)")
        if level == 16:
            self.special_abilities.append("Ability Score Improvement 16th Level")
            player.update_ability_points(2)
        if level == 17:
            self.special_abilities.append("Action Surge (2/rest)")
            self.special_abilities.append("Indomitable (3/rest)")
        if level == 18:
            self.special_abilities.append("Survivor")
        if level == 19:
            self.special_abilities.append("Ability Score Improvement 19th Level")
            player.update_ability_points(2)
        if level == 20:
            self.special_abilities.append("Extra Attack (3 extra attacks)")
        return self
    
def define_fighter():
    fighter = Fighter()

    ### Equipment Choices ###
    first_equipment_choice = equipment.weapon_choices(["Chain Mail", "Leather Armor and Longbow"])
    if first_equipment_choice == "Chain Mail":
        fighter.starting_equipment.append(equipment.chain_mail_heavy_armor)
    else:
        fighter.starting_equipment.append(equipment.leather_light_armor)
        fighter.starting_equipment.append(equipment.longbow)

    second_equipment_choice = equipment.weapon_choices(["Martial Weapon and Shield", "Two Martial Weapons"])
    if second_equipment_choice == "Martial Weapon and Shield":
        fighter.starting_equipment.append(equipment.shield)
        fighter.starting_equipment.append(equipment.get_weapons_from_category("Martial Weapons"))
    else:
        fighter.starting_equipment.append(equipment.get_weapons_from_category("Martial Weapons"))
        fighter.starting_equipment.append(equipment.get_weapons_from_category("Martial Weapons"))

    third_equipment_choice = equipment.weapon_choices(["Light Crossbow", "Two Handaxes"])
    if third_equipment_choice == "Light Crossbow":
        fighter.starting_equipment.append(equipment.light_crossbow)
    else:
        fighter.starting_equipment.append(equipment.hand_axe)
        fighter.starting_equipment.append(equipment.hand_axe)

    fourth_equipment_choice = equipment.weapon_choices(["Dungeoneer's Pack", "Explorer's Pack"])
    if fourth_equipment_choice == "Priest's Pack":
        fighter.starting_equipment.append(equipment.dungeoneers_pack)
    else:
        fighter.starting_equipment.append(equipment.explorers_pack)

    ### Skill Choices ###
    for i in range(2):
        skill = skills.select_skill_proficiencies("Fighter")
        fighter.skill_proficiencies.append(skill)

    return fighter
