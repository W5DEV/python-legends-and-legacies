import modules.equipment as equipment
import modules.skills as skills
import modules.spells as spells
import modules.cantrips as cantrips

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

    def sync_level(self, level, player):
        if level == 1:
            self.special_abilities.append("Rage")
            self.special_abilities.append("Unarmored Defense")
            self.rages = 1
            self.rage_damage_bonus = 2
        if level == 2:
            self.special_abilities.append("Reckless Attack")
            self.special_abilities.append("Danger Sense")
        if level == 3:
            self.primal_path = "Path of the Berserker"
            self.special_abilities.append("Frenzy")
            self.rages = 3
        if level == 4:
            self.special_abilities.append("Ability Score Improvement 4th Level")
            player.update_ability_points(2)
        if level == 5:
            self.special_abilities.append("Extra Attack")
            self.special_abilities.append("Fast Movement")
        if level == 6:
            self.special_abilities.append("Mindless Rage")
            self.rages = 4
        if level == 7:
            self.special_abilities.append("Feral Instinct")
        if level == 8:
            self.special_abilities.append("Ability Score Improvement 8th Level")
            player.update_ability_points(2)
        if level == 9:
            self.special_abilities.append("Brutal Critical")
            self.rage_damage_bonus = 3
        if level == 10:
            self.special_abilities.append("Intimidating Presence")
        if level == 11:
            self.special_abilities.append("Reliable Talent")
            self.special_abilities.append("Relentless Rage")
        if level == 12:
            self.special_abilities.append("Ability Score Improvement 12th Level")
            player.update_ability_points(2)
            self.rages = 5
        if level == 13:
            self.special_abilities.append("Bear Totem")
        if level == 14:
            self.special_abilities.append("Retaliation")
        if level == 15:
            self.special_abilities.append("Persistent Rage")
        if level == 16:
            self.special_abilities.append("Ability Score Improvement 16th Level")
            player.update_ability_points(2)
            self.rage_damage_bonus = 4
        if level == 17:
            self.rages = 6
        if level == 18:
            self.special_abilities.append("Indomitable Might")
        if level == 19:
            self.special_abilities.append("Ability Score Improvement 19th Level")
            player.update_ability_points(2)
        if level == 20:
            self.special_abilities.append("Primal Champion")
            self.rages = 9999
        return
    
def define_barbarian():
    barbarian = Barbarian()

    ### Equipment Choices ###
    first_equipment_choice = equipment.weapon_choices(["Great Axe", "Any Martial Melee Weapon"])
    if first_equipment_choice == "Great Axe":
        barbarian.starting_equipment.append(equipment.great_axe)
    else:
        barbarian.starting_equipment.append(equipment.get_weapons_from_category("Martial Melee Weapons"))

    second_equipment_choice = equipment.weapon_choices(["Two Hand Axes", "Any Simple Weapon"])
    if second_equipment_choice == "Two Hand Axes":
        barbarian.starting_equipment.append(equipment.hand_axe)
        barbarian.starting_equipment.append(equipment.hand_axe)
    else:
        barbarian.starting_equipment.append(equipment.get_weapons_from_category("Simple Weapons"))
    
    barbarian.starting_equipment.append(equipment.explorers_pack)

    barbarian.starting_equipment.append(equipment.javelin)
    barbarian.starting_equipment.append(equipment.javelin)
    barbarian.starting_equipment.append(equipment.javelin)
    barbarian.starting_equipment.append(equipment.javelin)

    ### Skill Choices ###
    for i in range(2):
        skill = skills.select_skill_proficiencies("Barbarian")
        barbarian.skill_proficiencies.append(skill)

    return barbarian
