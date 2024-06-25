import modules.equipment as equipment

displayed_monk_skills = ["Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"]
monk_skills = ["acrobatics", "athletics", "history", "insight", "religion", "stealth"]

potential_starting_equipment = ["A Shortsword or any simple weapon", "A Dungeoneer's Pack or an Explorer's Pack", "10 Darts"]
        
class Monk:
    
    def __init__(self):
        name = "Monk"
        bio = "A master of martial arts, harnessing the power of the body in pursuit of physical and spiritual perfection."
        hit_die = "1d8 for first level, then 1d8 (or 5, whichever is higher) per level after 1 + your Constitution modifier."
        primary_ability = "Dexterity, Wisdom"
        saving_throw_proficiencies = "Strength, Dexterity"
        armor_proficiencies = "None"
        weapon_proficiencies = "Simple weapons, Shortswords"
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
        self.monastic_tradition = ""
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
            self.special_abilities.append("Unarmored Defense")
            self.special_abilities.append("Martial Arts")
        if level >= 2:
            self.special_abilities.append("Ki")
            self.special_abilities.append("Unarmored Movement")
        if level >= 3:
            self.monastic_tradition = "Way of the Open Hand"
            self.special_abilities.append("Open Hand Technique")
            self.special_abilities.append("Deflect Missiles")
        if level >= 4:
            self.special_abilities.append("Ability Score Improvement 4th Level")
            self.special_abilities.append("Slow Fall")
        if level >= 5:
            self.special_abilities.append("Extra Attack")
            self.special_abilities.append("Stunning Strike")
        if level >= 6:
            self.special_abilities.append("Ki-Empowered Strikes")
            self.special_abilities.append("Wholeness of Body")
        if level >= 7:
            self.special_abilities.append("Evasion")
            self.special_abilities.append("Stillness of Mind")
        if level >= 8:
            self.special_abilities.append("Ability Score Improvement 8th Level")
        if level >= 9:
            self.special_abilities.append("Unarmored Movement Improvement")
        if level >= 10:
            self.special_abilities.append("Purity of Body")
        if level >= 11:
            self.special_abilities.append("Tranquility")
        if level >= 12:
            self.special_abilities.append("Ability Score Improvement 12th Level")
        if level >= 13:
            self.special_abilities.append("Tongue of the Sun and Moon")
        if level >= 14:
            self.special_abilities.append("Diamond Soul")
        if level >= 15:
            self.special_abilities.append("Timeless Body")
        if level >= 16:
            self.special_abilities.append("Ability Score Improvement 16th Level")
        if level >= 17:
            self.special_abilities.append("Quivering Palm")
        if level >= 18:
            self.special_abilities.append("Empty Body")
        if level >= 19:
            self.special_abilities.append("Ability Score Improvement 19th Level")
        if level >= 20:
            self.special_abilities.append("Perfect Self")

def define_monk():
    monk = Monk()
    print("You have chosen the Monk class.")
    print(monk.bio)

    # Skill Proficiencies
    print("Choose two skills from the following list:")
    for skill in displayed_monk_skills:
        print(skill)
    print("Please enter your first skill choice:")
    skill_choice1 = input("> ")
    while skill_choice1.lower() not in monk_skills:
        print("That is not a valid choice. Please choose from the list.")
        skill_choice1 = input("> ")
    monk.skill_proficiencies.append(skill_choice1)

    print("Please enter your second skill choice:")
    skill_choice2 = input("> ")
    while skill_choice2.lower() not in monk_skills:
        print("That is not a valid choice. Please choose from the list.")
        skill_choice2 = input("> ")
    monk.skill_proficiencies.append(skill_choice2)

    print("You have chosen the following skills:")
    for skill in monk.skill_proficiencies:
        print(skill)

    # Starting Equipment
    equipment_choice1 = ""
    equipment_choice2 = ""
    print("Choose your starting equipment:")
    for item in potential_starting_equipment:
        print(item)

    print("Please enter your choice of a 'Shortsword' or 'any Simple Weapon':")
    equipment_choice1 = input("> ")
    while equipment_choice1.lower() not in ["shortsword", "any simple weapon"]:
        print("That is not a valid choice. Please choose from the list.")
        equipment_choice1 = input("> ")
    if equipment_choice1.lower() == "shortsword":
        print("You have chosen Shortsword.")
        print("One Shortsword has been added to your starting equipment.")
        monk.starting_equipment.append(equipment.short_sword)
    else:
        for weapon in equipment.simple_weapons:
            print(weapon.name)
        print("Please enter your choice of simple weapon:")
        weapon_choice = input("> ")
        while weapon_choice.lower() not in [weapon.name.lower() for weapon in equipment.simple_weapons]:
            print("That is not a valid choice. Please choose from the list.")
            weapon_choice = input("> ")
        for weapon in equipment.simple_weapons:
            if weapon_choice.lower() == weapon.name.lower():
                print(f"You have chosen {weapon.name}.")
                print(f"{weapon.name} has been added to your starting equipment.")
                monk.starting_equipment.append(weapon)
                break

    print("Please enter your choice of a 'Dungeoneer's Pack' or an 'Explorer's Pack':")
    equipment_choice2 = input("> ")
    while equipment_choice2.lower() not in ["dungeoneer's pack", "explorer's pack"]:
        print("That is not a valid choice. Please choose from the list.")
        equipment_choice2 = input("> ")
    if equipment_choice2.lower() == "dungeoneer's pack":
        print("You have chosen a Dungeoneer's Pack.")
        print("A Dungeoneer's Pack has been added to your starting equipment.")
        monk.starting_equipment.append(equipment.dungeoneers_pack)
    elif equipment_choice2.lower() == "explorer's pack":
        print("You have chosen an Explorer's Pack.")
        print("An Explorer's Pack has been added to your starting equipment.")
        monk.starting_equipment.append(equipment.explorers_pack)

    print("You also start with 10 Darts.")
    print("10 Darts have been added to your starting equipment.")
    # Add darts to starting equipment

    # Starting Tools
    tool_choice = ""
    print("You can choose one type of artisan's tools or one musical instrument.")
    print("Please enter either 'Artisan's Tools' or 'Musical Instrument':")
    tool_choice= input("> ")
    while tool_choice.lower() not in ["artisan's tools", "musical instrument"]:
        print("That is not a valid choice. Please choose from the list.")
        tool_choice = input("> ")
    if tool_choice.lower() == "artisan's tools":
        print("You have chosen Artisan's Tools.")
        print("Please choose one type of Artisan's Tools from the following list:")
        valid_choices = []
        for tool in equipment.artisans_tools:
            valid_choices.append(tool.name.lower())
            print(tool.name)
        print("Please enter your choice:")
        chosen_tool = input("> ")
        while chosen_tool.lower() not in valid_choices:
            print("That is not a valid choice. Please choose from the list.")
            chosen_tool = input("> ")
        for tool in equipment.artisans_tools:
            if chosen_tool.lower() == tool.name.lower():
                print(f"You have chosen {tool.name}.")
                print(f"{tool.name} has been added to your starting equipment.")
                monk.tool_proficiencies.append(tool)
                break
    elif tool_choice.lower() == "musical instrument":
        print("You have chosen a musical instrument.")
        print("Please choose one musical instrument from the following list:")
        valid_choices = []
        for instrument in equipment.musical_instruments:
            valid_choices.append(instrument.name.lower())
            print(instrument.name)
        print("Please enter your choice:")
        chosen_instrument = input("> ")
        while chosen_instrument.lower() not in valid_choices:
            print("That is not a valid choice. Please choose from the list.")
            chosen_instrument = input("> ")
        for instrument in equipment.musical_instruments:
            if chosen_instrument.lower() == instrument.name.lower():
                print(f"You have chosen {instrument.name}.")
                print(f"{instrument.name} has been added to your starting equipment.")
                monk.tool_proficiencies.append(instrument)
                break
    
    print(f"You have chosen the following starting equipment:")
    for item in monk.starting_equipment:
        print(item.name)
    
    return monk