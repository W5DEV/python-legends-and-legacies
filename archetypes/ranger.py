import modules.equipment as equipment

displayed_ranger_skills = ["Animal Handling", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth", "Survival"]
ranger_skills = ["animal handling", "athletics", "insight", "investigation", "nature", "perception", "stealth", "survival"]

potential_starting_equipment = ["Scale Mail or Leather Armor", "Two Shortswords or Two Simple Melee Weapons" "A Dungeoneer's Pack or an Explorer's Pack", "A Longbow and a quiver of 20 arrows"]
        
class Ranger:
    
    def __init__(self):
        name = "Ranger"
        bio = "A warrior who uses martial prowess and nature magic to combat threats on the edges of civilization"
        hit_die = "1d10 for first level, then 1d10 (or 6, whichever is higher) per level after 1 + your Constitution modifier."
        primary_ability = "Dexterity, Wisdom"
        saving_throw_proficiencies = "Strength, Dexterity"
        armor_proficiencies = "Light Armor, Medium Armor, Shields"
        weapon_proficiencies = "Simple Weapons, Martial Weapons"
        self.name = name
        self.bio = bio
        self.hit_die = hit_die
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
        self.proficiency_bonus = 2

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
            print(skill.name)
        print(f"Starting Equipment:")
        for item in self.starting_equipment:
            print(item.name)
        print(f"Special Abilities:")
        for ability in self.special_abilities:
            print(ability)
        return self
    
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
        if level >= 3:
            self.ranger_archetype = "Hunter"
            self.special_abilities.append("Hunter's Prey")
            self.special_abilities.append("Primeval Awareness")
        if level >= 4:
            self.special_abilities.append("Ability Score Improvement 4th Level")
        if level >= 5:
            self.special_abilities.append("Extra Attack")
        if level >= 6:
            self.special_abilities.append("Favorite Enemy Improvement")
            self.special_abilities.append("Natural Explorer Improvement")
        if level >= 7:
            self.special_abilities.append("Defensive Tactics")
        if level >= 8:
            self.special_abilities.append("Ability Score Improvement 8th Level")
            self.special_abilities.append("Land's Stride")
        if level >= 9:
            pass
        if level >= 10:
            self.special_abilities.append("Natural Explorer Improvement")
            self.special_abilities.append("Hide in Plain Sight")
        if level >= 11:
            self.special_abilities.append("Multiattack")
        if level >= 12:
            self.special_abilities.append("Ability Score Improvement 12th Level")
        if level >= 13:
            pass
        if level >= 14:
            self.special_abilities.append("Favored Enemy Improvement")
            self.special_abilities.append("Vanish")
        if level >= 15:
            self.special_abilities.append("Superior Hunter's Defense")
        if level >= 16:
            self.special_abilities.append("Ability Score Improvement 16th Level")
        if level >= 17:
            pass
        if level >= 18:
            self.special_abilities.append("Fereal Senses")
        if level >= 19:
            self.special_abilities.append("Ability Score Improvement 19th Level")
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
    equipment_choice1 = ""
    equipment_choice2 = ""
    equipment_choice3 = ""
    print("Choose your starting equipment:")
    for item in potential_starting_equipment:
        print(item)

    print("Please enter your choice of a 'Scale Mail' or 'Leather Armor':")
    equipment_choice1 = input("> ")
    while equipment_choice1.lower() not in ["scale mail", "leather armor"]:
        print("That is not a valid choice. Please choose from the list.")
        equipment_choice1 = input("> ")
    if equipment_choice1.lower() == "scale mail":
        print("You have chosen Scale Mail.")
        print("Scale Mail has been added to your starting equipment.")
        ranger.starting_equipment.append(equipment.scale_mail_medium_armor)
    elif equipment_choice1.lower() == "leather armor":
        print("You have chosen Leather Armor.")
        print("Leather Armor has been added to your starting equipment.")
        ranger.starting_equipment.append(equipment.leather_light_armor)

    print("Please enter your choice of a 'Two Shortswords' or 'Two Simple Melee Weapons':")
    equipment_choice2 = input("> ")
    while equipment_choice2.lower() not in ["two shortswords", "two simple melee weapons"]:
        print("That is not a valid choice. Please choose from the list.")
        equipment_choice2 = input("> ")
    if equipment_choice2.lower() == "two shortswords":
        print("You have chosen Two Shortswords.")
        print("Two Shortswords has been added to your starting equipment.")
        ranger.starting_equipment.append(equipment.short_sword)
        ranger.starting_equipment.append(equipment.short_sword)
    elif equipment_choice2.lower() == "two simple melee weapons":
        print("You have chosen Two Simple Melee Weapons.")
        print("Please choose two Simple Melee Weapons from the following list:")
        valid_choices = []
        for weapon in equipment.simple_melee_weapons:
            valid_choices.append(weapon.name.lower())
            print(weapon.name)
        print("Please enter your first choice:")
        chosen_weapon1 = input("> ")
        while chosen_weapon1.lower() not in valid_choices:
            print("That is not a valid choice. Please choose from the list.")
            chosen_weapon1 = input("> ")
        for weapon in equipment.simple_melee_weapons:
            if chosen_weapon1.lower() == weapon.name.lower():
                print(f"You have chosen {weapon.name}.")
                print(f"{weapon.name} has been added to your starting equipment.")
                ranger.starting_equipment.append(weapon)
                break
        print("Please enter your second choice:")
        chosen_weapon2 = input("> ")
        while chosen_weapon2.lower() not in valid_choices:
            print("That is not a valid choice. Please choose from the list.")
            chosen_weapon2 = input("> ")
        for weapon in equipment.simple_melee_weapons:
            if chosen_weapon2.lower() == weapon.name.lower():
                print(f"You have chosen {weapon.name}.")
                print(f"{weapon.name} has been added to your starting equipment.")
                ranger.starting_equipment.append(weapon)
                break

    print("Please enter your choice of a 'Dungeoneer's Pack' or an 'Explorer's Pack':")
    equipment_choice3 = input("> ")
    while equipment_choice3.lower() not in ["dungeoneer's pack", "explorer's pack"]:
        print("That is not a valid choice. Please choose from the list.")
        equipment_choice3 = input("> ")
    if equipment_choice3.lower() == "dungeoneer's pack":
        print("You have chosen a Dungeoneer's Pack.")
        print("A Dungeoneer's Pack has been added to your starting equipment.")
        ranger.starting_equipment.append(equipment.dungeoneers_pack)
    elif equipment_choice3.lower() == "explorer's pack":
        print("You have chosen an Explorer's Pack.")
        print("An Explorer's Pack has been added to your starting equipment.")
        ranger.starting_equipment.append(equipment.explorers_pack)

    print("You also start with a Longbow and a quiver of 20 arrows.")
    print("A Longbow and a quiver of 20 arrows. have been added to your starting equipment.")
    ranger.starting_equipment.append(equipment.longbow)
    # Add quiver of 20 arrows to starting equipment
    
    print(f"You have chosen the following starting equipment:")
    for item in ranger.starting_equipment:
        print(item.name)
    
    return ranger