import modules.equipment as equipment
import modules.skills as skills

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

    def sync_level(self, level, player):
        if level == 1:
            self.special_abilities.append("Unarmored Defense")
            self.special_abilities.append("Martial Arts")
        if level == 2:
            self.special_abilities.append("Ki")
            self.special_abilities.append("Unarmored Movement")
            self.ki_points = 2
            self.unarmored_movement = 10
        if level == 3:
            self.monastic_tradition = "Way of the Open Hand"
            self.special_abilities.append("Open Hand Technique")
            self.special_abilities.append("Deflect Missiles")
            self.ki_points = 3
        if level == 4:
            self.special_abilities.append("Ability Score Improvement 4th Level")
            player.update_ability_points(2)
            self.special_abilities.append("Slow Fall")
            self.ki_points = 4
        if level == 5:
            self.special_abilities.append("Extra Attack")
            self.special_abilities.append("Stunning Strike")
            self.ki_points = 5
            self.martial_arts_die = "1d6"
        if level == 6:
            self.special_abilities.append("Ki-Empowered Strikes")
            self.special_abilities.append("Wholeness of Body")
            self.ki_points = 6
            self.unarmored_movement = 15
        if level == 7:
            self.special_abilities.append("Evasion")
            self.special_abilities.append("Stillness of Mind")
            self.ki_points = 7
        if level == 8:
            self.special_abilities.append("Ability Score Improvement 8th Level")
            player.update_ability_points(2)
            self.ki_points = 8
        if level == 9:
            self.special_abilities.append("Unarmored Movement Improvement")
            self.ki_points = 9
        if level == 10:
            self.special_abilities.append("Purity of Body")
            self.ki_points = 10
            self.unarmored_movement = 20
        if level == 11:
            self.special_abilities.append("Tranquility")
            self.ki_points = 11
            self.martial_arts_die = "1d8"
        if level == 12:
            self.special_abilities.append("Ability Score Improvement 12th Level")
            player.update_ability_points(2)
            self.ki_points = 12
        if level == 13:
            self.special_abilities.append("Tongue of the Sun and Moon")
            self.ki_points = 13
        if level == 14:
            self.special_abilities.append("Diamond Soul")
            self.ki_points = 14
            self.unarmored_movement = 25
        if level == 15:
            self.special_abilities.append("Timeless Body")
            self.ki_points = 15
        if level == 16:
            self.special_abilities.append("Ability Score Improvement 16th Level")
            player.update_ability_points(2)
            self.ki_points = 16
        if level == 17:
            self.special_abilities.append("Quivering Palm")
            self.ki_points = 17
            self.martial_arts_die = "1d10"
        if level == 18:
            self.special_abilities.append("Empty Body")
            self.ki_points = 18
            self.unarmored_movement = 30
        if level == 19:
            self.special_abilities.append("Ability Score Improvement 19th Level")
            player.update_ability_points(2)
            self.ki_points = 19
        if level == 20:
            self.special_abilities.append("Perfect Self")
            self.ki_points = 20
        return self

def define_monk():
    monk = Monk()

    ### Equipment Choices ###
    first_equipment_choice = equipment.weapon_choices(["Short Sword", "Any Simple Weapon"])
    if first_equipment_choice == "Short Sword":
        monk.starting_equipment.append(equipment.mace)
    elif first_equipment_choice == "Any Simple Weapon":
        monk.starting_equipment.append(equipment.get_weapons_from_category("Simple Weapons"))

    second_equipment_choice = equipment.weapon_choices(["Dungeoneer's Pack", "Explorer's Pack"])
    if second_equipment_choice == "Dungeoneer's Pack":
        monk.starting_equipment.append(equipment.dungeoneers_pack)
    elif second_equipment_choice == "Explorer's Pack":
        monk.starting_equipment.append(equipment.explorers_pack)

    # Add 10 Darts

    third_equipment_choice = equipment.weapon_choices(["Artisan's Tools", "Musical Instrument"])
    if third_equipment_choice == "Artisan's Tools":
        monk.starting_equipment.append(equipment.get_weapons_from_category("Artisan's Tools"))
    else:
        monk.starting_equipment.append(equipment.get_weapons_from_category("Instruments"))

    ### Skill Choices ###
    for i in range(2):
        skill = skills.select_skill_proficiencies("Monk")
        monk.skill_proficiencies.append(skill)

    return monk
