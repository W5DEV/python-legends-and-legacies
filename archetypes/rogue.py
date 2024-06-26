import modules.starting_equipment as starting_equipment
import modules.skills as skills

displayed_rogue_skills, rogue_skills = skills.get_rogue_skills()
potential_starting_equipment = starting_equipment.get_starting_equipment("Rogue")
      
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
            print(skill)
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
    equipment_choice_1 = starting_equipment.starting_equipment_choice("Rapier", "Shortsword")
    if equipment_choice_1.lower() == "rapier":
        weapon_choice = starting_equipment.starting_equipment("Rapier")
    else:
        weapon_choice = starting_equipment.starting_equipment("Short Sword") 
    print(f"One {weapon_choice.name} has been added to your starting equipment.") 
    rogue.starting_equipment.append(weapon_choice)

    equipment_choice_2 = starting_equipment.starting_equipment_choice("Shortbow and Quiver of 20 Arrows", "Shortsword")
    if equipment_choice_2.lower() == "shortbow and quiver of 20 arrows":
        weapon_choice = starting_equipment.starting_equipment("Short Bow")
    else:
        weapon_choice = starting_equipment.starting_equipment("Short Sword")
    print(f"One {weapon_choice.name} has been added to your starting equipment.")
    rogue.starting_equipment.append(weapon_choice)
    # Add a Quiver of 20 Arrows to the starting equipment if selected

    equipment_choice_3 = starting_equipment.starting_equipment_choice_three("Burglar's Pack", "Dungeoneer's Pack", "Explorer's Pack")
    if equipment_choice_3.lower() == "burglar's pack":
        pack_choice = starting_equipment.starting_equipment("Burglar's Pack")
    elif equipment_choice_3.lower() == "dungeoneer's pack":
        pack_choice = starting_equipment.starting_equipment("Dungeoneer's Pack")
    else:
        pack_choice = starting_equipment.starting_equipment("Explorer's Pack")
    print(f"One {pack_choice.name} has been added to your starting equipment.")
    rogue.starting_equipment.append(pack_choice)

    leather_armor = starting_equipment.starting_equipment("Leather Light Armor")
    dagger = starting_equipment.starting_equipment("Dagger")
    thieves_tools = starting_equipment.starting_equipment("Thieves' Tools")
    print("Leather Armor, Two Daggers, and Thieves' Tools have been added to your starting equipment.")
    rogue.starting_equipment.append(leather_armor)
    rogue.starting_equipment.append(dagger)
    rogue.starting_equipment.append(dagger)
    rogue.starting_equipment.append(thieves_tools)

    return rogue