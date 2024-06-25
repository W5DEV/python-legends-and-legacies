import modules.equipment as equipment

displayed_rogue_skills = ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight of Hand", "Stealth"]
rogue_skills = ["acrobatics", "athletics", "deception", "insight", "intimidation", "investigation", "perception", "performance", "persuasion", "sleight of hand", "stealth"]

potential_starting_equipment = ["A Rapier or a Shortsword", "A Shortbow and Quiver of 20 Arrows or a Shortsword", "A Burglar's Pack, a Dungeoneer's Pack or an Explorer's Pack", "Leather Armor, Two Daggers, and Thieves' Tools"]
        
class Rogue:
    
    def __init__(self):
        name = "Rogue"
        bio = "A scoundrel who uses stealth and trickery to overcome obstacles and enemies."
        hit_die = "1d8"
        primary_ability = "Dexterity"
        saving_throw_proficiencies = "Dexterity, Intelligence"
        armor_proficiencies = "Light Armor"
        weapon_proficiencies = "Simple weapons, Hand Crossbows, Longswords, Rapiers, Shortswords"
        tool_proficiencies = "Thieves' Tools"
        self.name = name
        self.bio = bio
        self.hit_die = hit_die
        self.base_hp = 8
        self.primary_ability = primary_ability
        self.saving_throw_proficiencies = saving_throw_proficiencies
        self.armor_proficiencies = armor_proficiencies
        self.weapon_proficiencies = weapon_proficiencies
        self.tool_proficiencies = tool_proficiencies
        self.skill_proficiencies = []
        self.starting_equipment = []
        self.roguish_archetype = ""
        self.special_abilities = []
        self.sneak_attack_die = "1d6"

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
            self.special_abilities.append("Expertise")
            self.special_abilities.append("Sneak Attack")
            self.special_abilities.append("Thieves' Cant")
        if level >= 2:
            self.special_abilities.append("Cunning Action")
        if level >= 3:
            self.roguish_archetype = "Thief"
            self.special_abilities.append("Fast Hands")
            self.special_abilities.append("Second-Story Work")
            self.sneak_attack_die = "2d6"
        if level >= 4:
            self.special_abilities.append("Ability Score Improvement 4th Level")
        if level >= 5:
            self.special_abilities.append("Uncanny Dodge")
            self.sneak_attack_die = "3d6"
        if level >= 6:
            self.special_abilities.append("Expertise")
        if level >= 7:
            self.special_abilities.append("Evasion")
            self.sneak_attack_die = "4d6"
        if level >= 8:
            self.special_abilities.append("Ability Score Improvement 8th Level")
        if level >= 9:
            self.special_abilities.append("Supreme Sneak")
            self.sneak_attack_die = "5d6"
        if level >= 10:
            self.special_abilities.append("Ability Score Improvement 10th Level")
        if level >= 11:
            self.special_abilities.append("Reliable Talent")
            self.sneak_attack_die = "6d6"
        if level >= 12:
            self.special_abilities.append("Ability Score Improvement 12th Level")
        if level >= 13:
            self.special_abilities.append("Use Magic Device")
            self.sneak_attack_die = "7d6"
        if level >= 14:
            self.special_abilities.append("Blindsense")
        if level >= 15:
            self.special_abilities.append("Slippery Mind")
            self.sneak_attack_die = "8d6"
        if level >= 16:
            self.special_abilities.append("Ability Score Improvement 16th Level")
        if level >= 17:
            self.special_abilities.append("Thief's Reflexes")
            self.sneak_attack_die = "9d6"
        if level >= 18:
            self.special_abilities.append("Elusive")
        if level >= 19:
            self.special_abilities.append("Ability Score Improvement 19th Level")
            self.sneak_attack_die = "10d6"
        if level >= 20:
            self.special_abilities.append("Stroke of Luck")

def define_rogue():
    rogue = Rogue()
    print("You have chosen the rogue class.")
    print(rogue.bio)

    # Skill Proficiencies
    print("Choose two skills from the following list:")
    for skill in displayed_rogue_skills:
        print(skill)
    print("Please enter your first skill choice:")
    skill_choice1 = input("> ")
    while skill_choice1.lower() not in rogue_skills:
        print("That is not a valid choice. Please choose from the list.")
        skill_choice1 = input("> ")
    rogue.skill_proficiencies.append(skill_choice1)

    print("Please enter your second skill choice:")
    skill_choice2 = input("> ")
    while skill_choice2.lower() not in rogue_skills:
        print("That is not a valid choice. Please choose from the list.")
        skill_choice2 = input("> ")
    rogue.skill_proficiencies.append(skill_choice2)

    print("You have chosen the following skills:")
    for skill in rogue.skill_proficiencies:
        print(skill)

    # Starting Equipment
    equipment_choice1 = ""
    equipment_choice2 = ""
    equipment_choice3 = ""
    print("Choose your starting equipment:")
    for item in potential_starting_equipment:
        print(item)

    print("Please enter your choice of a 'Rapier' or a 'Shortsword':")
    equipment_choice1 = input("> ")
    while equipment_choice1.lower() not in ["rapier", "shortsword"]:
        print("That is not a valid choice. Please choose from the list.")
        equipment_choice1 = input("> ")
    if equipment_choice1.lower() == "rapier":
        print("You have chosen a Rapier.")
        print("One Rapier has been added to your starting equipment.")
        rogue.starting_equipment.append(equipment.rapier)
    else:
        print("You have chosen a Shortsword.")
        print("One Shortsword has been added to your starting equipment.")
        rogue.starting_equipment.append(equipment.short_sword)

    print("Please enter your choice of a 'Shortbow and Quiver of 20 Arrows' or a 'Shortsword':")
    equipment_choice2 = input("> ")
    while equipment_choice2.lower() not in ["shortbow and quiver of 20 arrows", "shortsword"]:
        print("That is not a valid choice. Please choose from the list.")
        equipment_choice2 = input("> ")
    if equipment_choice2.lower() == "shortbow and quiver of 20 arrows":
        print("You have chosen a Shortbow and Quiver of 20 Arrows.")
        print("One Shortbow has been added to your starting equipment, along with a Quiver of 20 Arrows.")
        rogue.starting_equipment.append(equipment.short_bow)
        # Add a Quiver of 20 Arrows to the starting equipment
    else:
        print("You have chosen a Shortsword.")
        print("One Shortsword has been added to your starting equipment.")
        rogue.starting_equipment.append(equipment.short_sword)

    print("Please enter your choice of a 'Burglar's Pack', 'Dungeoneer's Pack' or an 'Explorer's Pack':")
    equipment_choice3 = input("> ")
    while equipment_choice3.lower() not in ["burglar's pack", "dungeoneer's pack", "explorer's pack"]:
        print("That is not a valid choice. Please choose from the list.")
        equipment_choice3 = input("> ")
    if equipment_choice3.lower() == "burglar's pack":
        print("You have chosen a Burglar's Pack.")
        print("A Burglar's Pack has been added to your starting equipment.")
        rogue.starting_equipment.append(equipment.burglars_pack)
    elif equipment_choice3.lower() == "dungeoneer's pack":
        print("You have chosen a Dungeoneer's Pack.")
        print("A Dungeoneer's Pack has been added to your starting equipment.")
        rogue.starting_equipment.append(equipment.dungeoneers_pack)
    elif equipment_choice3.lower() == "explorer's pack":
        print("You have chosen an Explorer's Pack.")
        print("An Explorer's Pack has been added to your starting equipment.")
        rogue.starting_equipment.append(equipment.explorers_pack)

    print("You also start with Leather Armor, Two Daggers, and Thieves' Tools.")
    print("Leather Armor, Two Daggers, and Thieves' Tools have been added to your starting equipment.")
    rogue.starting_equipment.append(equipment.leather_light_armor)
    rogue.starting_equipment.append(equipment.dagger)
    rogue.starting_equipment.append(equipment.dagger)
    rogue.starting_equipment.append(equipment.thieves_tools)

    print(f"You have chosen the following starting equipment:")
    for item in rogue.starting_equipment:
        print(item.name)
    
    return rogue