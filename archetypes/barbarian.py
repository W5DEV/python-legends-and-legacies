import modules.equipment as equipment

class Barbarian:
    
    def __init__(self):
        name = "Barbarian"
        description = "A fierce warrior of primitive background who can enter a battle rage"
        hit_die = "1d12 per Barbarian level"
        primary_ability = "Strength"
        saving_throw_proficiencies = "Strength, Constitution"
        armor_proficiencies = "Light Armor, Medium Armor, Shields"
        weapon_proficiencies = "Simple Weapons, Martial Weapons"
        tool_proficiencies = "None"
        displayed_skill_proficiencies = ["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"]
        available_skill_proficiencies = ["animal handling", "athletics", "intimidation", "nature", "perception", "survival"]
        skill_proficiencies = []
        potential_starting_equipment = ["Greataxe or any martial melee weapon", "Two Handaxes or Any Simple Weapon", "Explorer's Pack", "Four Javelins"]
        special_abilities = []
        self.name = name
        self.description = description
        self.hit_die = hit_die
        self.primary_ability = primary_ability
        self.saving_throw_proficiencies = saving_throw_proficiencies
        self.armor_proficiencies = armor_proficiencies
        self.weapon_proficiencies = weapon_proficiencies
        self.tool_proficiencies = tool_proficiencies
        self.displayed_skill_proficiencies = displayed_skill_proficiencies
        self.available_skill_proficiencies = available_skill_proficiencies
        self.skill_proficiencies = skill_proficiencies
        self.potential_starting_equipment = potential_starting_equipment
        self.starting_equipment = []
        self.special_abilities = special_abilities
        self.primal_path = ""
    
    def get_info(self):
        print(f"The {self.name}: {self.description}")
        print(f"Hit Die: {self.hit_die}")
        print(f"Primary Ability: {self.primary_ability}")
        print(f"Saving Throw Proficiencies: {self.saving_throw_proficiencies}")
        print(f"Armor Proficiencies: {self.armor_proficiencies}")
        print(f"Weapon Proficiencies: {self.weapon_proficiencies}")
        print(f"Tool Proficiencies: {self.tool_proficiencies}")
        print(f"Skill Proficiencies: {self.displayed_skill_proficiencies}")
        print(f"Starting Equipment: {self.potential_starting_equipment}")
        print(f"Special Abilities: {self.special_abilities}")
        return self
    
    def update_special_abilities(self, level):
        if level >= 1:
            self.special_abilities.append("Rage")
            self.special_abilities.append("Unarmored Defense")
        if level >= 2:
            self.special_abilities.append("Reckless Attack")
            self.special_abilities.append("Danger Sense")
        if level >= 3:
            print("You have reached level 3 and can now choose your Primal Path: Path of the Berserker")
            self.primal_path = "Path of the Berserker"
            self.special_abilities.append("Frenzy")
        if level >= 4:
            self.special_abilities.append("Ability Score Improvement 4th Level")
        if level >= 5:
            self.special_abilities.append("Extra Attack")
            self.special_abilities.append("Fast Movement")
        if level >= 6:
            self.special_abilities.append("Mindless Rage")
        if level >= 7:
            self.special_abilities.append("Feral Instinct")
        if level >= 8:
            self.special_abilities.append("Ability Score Improvement 8th Level")
        if level >= 9:
            self.special_abilities.append("Brutal Critical")
        if level >= 10:
            self.special_abilities.append("Intimidating Presence")
        if level >= 11:
            self.special_abilities.append("Reliable Talent")
            self.special_abilities.append("Relentless Rage")
        if level >= 12:
            self.special_abilities.append("Ability Score Improvement 12th Level")
        if level >= 13:
            self.special_abilities.append("Bear Totem")
        if level >= 14:
            self.special_abilities.append("Retaliation")
        if level >= 15:
            self.special_abilities.append("Persistent Rage")
        if level >= 16:
            self.special_abilities.append("Ability Score Improvement 16th Level")
        if level >= 18:
            self.special_abilities.append("Indomitable Might")
        if level >= 19:
            self.special_abilities.append("Ability Score Improvement 19th Level")
        if level >= 20:
            self.special_abilities.append("Primal Champion")
        print(f"Special Abilities for level {level}:")
        i = 1
        for ability in self.special_abilities:
            print(f"{i}: {ability}")
            i += 1
        return self

def define_barbarian():
    barbarian = Barbarian()
    print(f'You have chosen the Barbarian class.')
    print(barbarian.description)

    # Skill Proficiencies
    print("Choose 2 skills from the following list, which you will be proficient in:")
    for skill in barbarian.displayed_skill_proficiencies:
        print(skill)
    print("Please enter your first skill choice:")
    skill_choice1 = input("> ")
    while skill_choice1.lower() not in barbarian.available_skill_proficiencies:
        print("That is not a valid choice. Please choose from the list.")
        skill_choice1 = input("> ")
    print("Please enter your second skill choice:")
    skill_choice2 = input("> ")
    while skill_choice2.lower() not in barbarian.available_skill_proficiencies:
        print("That is not a valid choice. Please choose from the list.")
        skill_choice2 = input("> ")
    selected_skill_proficiencies = [skill_choice1, skill_choice2]
    print(f"You have chosen {selected_skill_proficiencies[0]} and {selected_skill_proficiencies[1]} as your skill proficiencies.")
    barbarian.skill_proficiencies = selected_skill_proficiencies
    
    # Starting Equipment
    first_weapon = ""
    second_weapon = ""
    print(f"Barbarian's are able to choose between a few different starting equipment options.")
    print(f'You will start with the following equipment: {barbarian.starting_equipment}')
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
    barbarian.starting_equipment = selected_starting_equipment

    return barbarian
        


