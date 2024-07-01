import modules.equipment as equipment
import modules.skills as skills

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

    def sync_level(self, level, player):
        if level == 1:
            self.special_abilities.append("Expertise")
            self.special_abilities.append("Sneak Attack")
            self.special_abilities.append("Thieves' Cant")
        if level == 2:
            self.special_abilities.append("Cunning Action")
        if level == 3:
            self.roguish_archetype = "Thief"
            self.special_abilities.append("Fast Hands")
            self.special_abilities.append("Second-Story Work")
            self.sneak_attack_die = "2d6"
        if level == 4:
            self.special_abilities.append("Ability Score Improvement 4th Level")
            player.update_ability_points(2)
        if level == 5:
            self.special_abilities.append("Uncanny Dodge")
            self.sneak_attack_die = "3d6"
        if level == 6:
            self.special_abilities.append("Expertise")
        if level == 7:
            self.special_abilities.append("Evasion")
            self.sneak_attack_die = "4d6"
        if level == 8:
            self.special_abilities.append("Ability Score Improvement 8th Level")
            player.update_ability_points(2)
        if level == 9:
            self.special_abilities.append("Supreme Sneak")
            self.sneak_attack_die = "5d6"
        if level == 10:
            self.special_abilities.append("Ability Score Improvement 10th Level")
            player.update_ability_points(2)
        if level == 11:
            self.special_abilities.append("Reliable Talent")
            self.sneak_attack_die = "6d6"
        if level == 12:
            self.special_abilities.append("Ability Score Improvement 12th Level")
            player.update_ability_points(2)
        if level == 13:
            self.special_abilities.append("Use Magic Device")
            self.sneak_attack_die = "7d6"
        if level == 14:
            self.special_abilities.append("Blindsense")
        if level == 15:
            self.special_abilities.append("Slippery Mind")
            self.sneak_attack_die = "8d6"
        if level == 16:
            self.special_abilities.append("Ability Score Improvement 16th Level")
            player.update_ability_points(2)
        if level == 17:
            self.special_abilities.append("Thief's Reflexes")
            self.sneak_attack_die = "9d6"
        if level == 18:
            self.special_abilities.append("Elusive")
        if level == 19:
            self.special_abilities.append("Ability Score Improvement 19th Level")
            player.update_ability_points(2)
            self.sneak_attack_die = "10d6"
        if level == 20:
            self.special_abilities.append("Stroke of Luck")
        return self
    
def define_rogue():
    rogue = Rogue()

    ### Equipment Choices ###
    first_equipment_choice = equipment.weapon_choices(["Rapier", "Short Sword"])
    if first_equipment_choice == "Rapier":
        rogue.starting_equipment.append(equipment.rapier)
    elif first_equipment_choice == "Short Sword":
        rogue.starting_equipment.append(equipment.short_sword)

    second_equipment_choice = equipment.weapon_choices(["Short Bow", "Short Sword"])
    if second_equipment_choice == "Short Bow":
        rogue.starting_equipment.append(equipment.short_bow)
    elif second_equipment_choice == "Short Sword":
        rogue.starting_equipment.append(equipment.short_sword)

    third_equipment_choice = equipment.weapon_choices(["Burglar's Pack", "Dungeoneer's Pack", "Explorer's Pack"])
    if third_equipment_choice == "Burglar's Pack":
        rogue.starting_equipment.append(equipment.burglars_pack)
    elif third_equipment_choice == "Dungeoneer's Pack":
        rogue.starting_equipment.append(equipment.dungeoneers_pack)
    elif third_equipment_choice == "Explorer's Pack":
        rogue.starting_equipment.append(equipment.explorers_pack)

    rogue.starting_equipment.append(equipment.leather_light_armor)
    rogue.starting_equipment.append(equipment.dagger)
    rogue.starting_equipment.append(equipment.dagger)
    rogue.starting_equipment.append(equipment.thieves_tools)

    ### Skill Choices ###
    for i in range(2):
        skill = skills.select_skill_proficiencies("Rogue")
        rogue.skill_proficiencies.append(skill)

    return rogue
