import modules.starting_equipment as starting_equipment

displayed_barbarian_skills = ["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"]
barbarian_skills = ["animal handling", "athletics", "intimidation", "nature", "perception", "survival"]

potential_starting_equipment = ["Greataxe or any martial melee weapon", "Two Handaxes or Any Simple Weapon", "Explorer's Pack", "Four Javelins"]
        
class Barbarian:
    
    def __init__(self):
        name = "Barbarian"
        bio = "A fierce warrior of primitive background who can enter a battle rage."
        hit_die = "1d12"
        primary_ability = "Strength"
        saving_throw_proficiencies = "Strength, Constitution"
        armor_proficiencies = "Light Armor, Medium Armor, Shields"
        weapon_proficiencies = "Simple Weapons, Martial Weapons"
        tool_proficiencies = "None"
        self.name = name
        self.bio = bio
        self.hit_die = hit_die
        self.base_hp = 12
        self.primary_ability = primary_ability
        self.saving_throw_proficiencies = saving_throw_proficiencies
        self.armor_proficiencies = armor_proficiencies
        self.weapon_proficiencies = weapon_proficiencies
        self.tool_proficiencies = tool_proficiencies
        self.skill_proficiencies = []
        self.starting_equipment = []
        self.special_abilities = []
        self.primal_path = ""
        self.rages = 0
        self.rage_damage_bonus = 0

    
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
            self.special_abilities.append("Rage")
            self.special_abilities.append("Unarmored Defense")
            self.rages = 1
            self.rage_damage_bonus = 2
        if level >= 2:
            self.special_abilities.append("Reckless Attack")
            self.special_abilities.append("Danger Sense")
        if level >= 3:
            print("You have reached level 3 and can now choose your Primal Path: Path of the Berserker")
            self.primal_path = "Path of the Berserker"
            self.special_abilities.append("Frenzy")
            self.rages = 3
        if level >= 4:
            self.special_abilities.append("Ability Score Improvement 4th Level")
        if level >= 5:
            self.special_abilities.append("Extra Attack")
            self.special_abilities.append("Fast Movement")
        if level >= 6:
            self.special_abilities.append("Mindless Rage")
            self.rages = 4
        if level >= 7:
            self.special_abilities.append("Feral Instinct")
        if level >= 8:
            self.special_abilities.append("Ability Score Improvement 8th Level")
        if level >= 9:
            self.special_abilities.append("Brutal Critical")
            self.rage_damage_bonus = 3
        if level >= 10:
            self.special_abilities.append("Intimidating Presence")
        if level >= 11:
            self.special_abilities.append("Reliable Talent")
            self.special_abilities.append("Relentless Rage")
        if level >= 12:
            self.special_abilities.append("Ability Score Improvement 12th Level")
            self.rages = 5
        if level >= 13:
            self.special_abilities.append("Bear Totem")
        if level >= 14:
            self.special_abilities.append("Retaliation")
        if level >= 15:
            self.special_abilities.append("Persistent Rage")
        if level >= 16:
            self.special_abilities.append("Ability Score Improvement 16th Level")
            self.rage_damage_bonus = 4
        if level >= 17:
            self.rages = 6
        if level >= 18:
            self.special_abilities.append("Indomitable Might")
        if level >= 19:
            self.special_abilities.append("Ability Score Improvement 19th Level")
        if level >= 20:
            self.special_abilities.append("Primal Champion")
            self.rages = 9999
        print(f"Special Abilities for level {level}:")
        i = 1
        for ability in self.special_abilities:
            print(f"{i}: {ability}")
            i += 1
        return self

def define_barbarian():
    barbarian = Barbarian()
    print(f'You have chosen the Barbarian class.')
    print(barbarian.bio)

    # Skill Proficiencies
    print("Choose 2 skills from the following list, which you will be proficient in:")
    for skill in displayed_barbarian_skills:
        print(skill)
    print("Please enter your first skill choice:")
    skill_choice1 = input("> ")
    while skill_choice1.lower() not in barbarian_skills:
        print("That is not a valid choice. Please choose from the list.")
        skill_choice1 = input("> ")
    print("Please enter your second skill choice:")
    skill_choice2 = input("> ")
    while skill_choice2.lower() not in barbarian_skills:
        print("That is not a valid choice. Please choose from the list.")
        skill_choice2 = input("> ")
    selected_skill_proficiencies = [skill_choice1, skill_choice2]
    print(f"You have chosen {selected_skill_proficiencies[0]} and {selected_skill_proficiencies[1]} as your skill proficiencies.")
    barbarian.skill_proficiencies = selected_skill_proficiencies
    
    # Starting Equipment
    weapon_choice_1 = starting_equipment.starting_equipment_choice("Greataxe", "Any Martial Melee Weapon")
    if weapon_choice_1.lower() == "greataxe":
        starting_weapon = starting_equipment.starting_equipment("Great Axe")
    else:
        starting_weapon = starting_equipment.select_equipment_from_category("Martial Melee Weapons")
    print(f"One {starting_weapon.name} has been added to your starting equipment.")
    barbarian.starting_equipment.append(starting_weapon)

    weapon_choice_2 = starting_equipment.starting_equipment_choice("Two Handaxes", "Any Simple Weapon")
    if weapon_choice_2.lower() == "two handaxes":
        starting_weapon = starting_equipment.starting_equipment("Hand Axe")
        print(f"Two {starting_weapon.name}'s have been added to your starting equipment.")
        barbarian.starting_equipment.append(starting_weapon)
        barbarian.starting_equipment.append(starting_weapon)
    else:
        starting_weapon = starting_equipment.select_equipment_from_category("Simple Weapons")
        print(f"One {starting_weapon.name} has been added to your starting equipment.")
        barbarian.starting_equipment.append(starting_weapon)
    
    explorer_pack = starting_equipment.starting_equipment("Explorer's Pack")
    print(f"An {explorer_pack.name} has been added to your starting equipment.")
    barbarian.starting_equipment.append(explorer_pack)

    javelin = starting_equipment.starting_equipment("Javelin")
    print(f"Four {javelin.name}'s have been added to your starting equipment.")
    barbarian.starting_equipment.append(javelin)
    barbarian.starting_equipment.append(javelin)
    barbarian.starting_equipment.append(javelin)
    barbarian.starting_equipment.append(javelin)
    return barbarian
        


