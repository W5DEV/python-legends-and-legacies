import modules.starting_equipment as starting_equipment
import modules.skills as skills

displayed_monk_skills, monk_skills = skills.get_monk_skills()
potential_starting_equipment = starting_equipment.get_starting_equipment("Monk")

class Monk:
    
    def __init__(self):
        name = "Monk"
        bio = "A master of martial arts, harnessing the power of the body in pursuit of physical and spiritual perfection."
        hit_die = "1d8"
        primary_ability = "Dexterity, Wisdom"
        saving_throw_proficiencies = "Strength, Dexterity"
        armor_proficiencies = "None"
        weapon_proficiencies = "Simple weapons, Shortswords"
        self.name = name
        self.bio = bio
        self.hit_die = hit_die
        self.base_hp = 8
        self.primary_ability = primary_ability
        self.saving_throw_proficiencies = saving_throw_proficiencies
        self.armor_proficiencies = armor_proficiencies
        self.weapon_proficiencies = weapon_proficiencies
        self.tool_proficiencies = []
        self.skill_proficiencies = []
        self.starting_equipment = []
        self.monastic_tradition = ""
        self.special_abilities = []
        self.martial_arts_die = "1d4"
        self.ki_points = 0
        self.unarmored_movement = 0

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
            self.special_abilities.append("Unarmored Defense")
            self.special_abilities.append("Martial Arts")
        if level >= 2:
            self.special_abilities.append("Ki")
            self.special_abilities.append("Unarmored Movement")
            self.ki_points = 2
            self.unarmored_movement = 10
        if level >= 3:
            self.monastic_tradition = "Way of the Open Hand"
            self.special_abilities.append("Open Hand Technique")
            self.special_abilities.append("Deflect Missiles")
            self.ki_points = 3
        if level >= 4:
            self.special_abilities.append("Ability Score Improvement 4th Level")
            self.special_abilities.append("Slow Fall")
            self.ki_points = 4
        if level >= 5:
            self.special_abilities.append("Extra Attack")
            self.special_abilities.append("Stunning Strike")
            self.ki_points = 5
            self.martial_arts_die = "1d6"
        if level >= 6:
            self.special_abilities.append("Ki-Empowered Strikes")
            self.special_abilities.append("Wholeness of Body")
            self.ki_points = 6
            self.unarmored_movement = 15
        if level >= 7:
            self.special_abilities.append("Evasion")
            self.special_abilities.append("Stillness of Mind")
            self.ki_points = 7
        if level >= 8:
            self.special_abilities.append("Ability Score Improvement 8th Level")
            self.ki_points = 8
        if level >= 9:
            self.special_abilities.append("Unarmored Movement Improvement")
            self.ki_points = 9
        if level >= 10:
            self.special_abilities.append("Purity of Body")
            self.ki_points = 10
            self.unarmored_movement = 20
        if level >= 11:
            self.special_abilities.append("Tranquility")
            self.ki_points = 11
            self.martial_arts_die = "1d8"
        if level >= 12:
            self.special_abilities.append("Ability Score Improvement 12th Level")
            self.ki_points = 12
        if level >= 13:
            self.special_abilities.append("Tongue of the Sun and Moon")
            self.ki_points = 13
        if level >= 14:
            self.special_abilities.append("Diamond Soul")
            self.ki_points = 14
            self.unarmored_movement = 25
        if level >= 15:
            self.special_abilities.append("Timeless Body")
            self.ki_points = 15
        if level >= 16:
            self.special_abilities.append("Ability Score Improvement 16th Level")
            self.ki_points = 16
        if level >= 17:
            self.special_abilities.append("Quivering Palm")
            self.ki_points = 17
            self.martial_arts_die = "1d10"
        if level >= 18:
            self.special_abilities.append("Empty Body")
            self.ki_points = 18
            self.unarmored_movement = 30
        if level >= 19:
            self.special_abilities.append("Ability Score Improvement 19th Level")
            self.ki_points = 19
        if level >= 20:
            self.special_abilities.append("Perfect Self")
            self.ki_points = 20

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
    equipment_choice_1 = starting_equipment.starting_equipment_choice("Shortsword", "Any Simple Weapon")
    if equipment_choice_1.lower() == "shortsword":
        weapon_choice = starting_equipment.starting_equipment("Short Sword")
    else:
        weapon_choice = starting_equipment.select_equipment_from_category("Simple Weapons")
    print(f"One {weapon_choice.name} has been added to your starting equipment.")
    monk.starting_equipment.append(weapon_choice)

    equipment_choice_2 = starting_equipment.starting_equipment_choice("Dungeoneer's Pack", "Explorer's Pack")
    if equipment_choice_2.lower() == "dungeoneer's pack":
        pack_choice = starting_equipment.starting_equipment("Dungeoneer's Pack")
    else:
        pack_choice = starting_equipment.starting_equipment("Explorer's Pack")
    print(f"One {pack_choice.name} has been added to your starting equipment.")
    monk.starting_equipment.append(pack_choice)

    print("10 Darts have been added to your starting equipment.")
    # Add darts to starting equipment

    # Tool Proficiencies
    print("You can choose proficiency in one type of artisan's tools or one musical instrument.")
    tool_proficiency = starting_equipment.starting_equipment_choice("Artisan's Tools", "Musical Instrument")
    if tool_proficiency.lower() == "artisan's tools":
        tool_choice = starting_equipment.select_equipment_from_category("Artisan's Tools")
    else:
        tool_choice = starting_equipment.select_equipment_from_category("Instruments")
    print(f"You have chosen proficiency in {tool_choice.name}.")
    monk.tool_proficiencies.append(tool_choice.name)
    
    return monk