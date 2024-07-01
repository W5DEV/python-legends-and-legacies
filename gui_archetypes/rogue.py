import gui_modules.equipment as equipment
import gui_modules.skills as skills
import gui_modules.spells as spells
import gui_modules.cantrips as cantrips

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
            player.increase_ability_score(2)
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
            player.increase_ability_score(2)
        if level == 9:
            self.special_abilities.append("Supreme Sneak")
            self.sneak_attack_die = "5d6"
        if level == 10:
            self.special_abilities.append("Ability Score Improvement 10th Level")
            player.increase_ability_score(2)
        if level == 11:
            self.special_abilities.append("Reliable Talent")
            self.sneak_attack_die = "6d6"
        if level == 12:
            self.special_abilities.append("Ability Score Improvement 12th Level")
            player.increase_ability_score(2)
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
            player.increase_ability_score(2)
        if level == 17:
            self.special_abilities.append("Thief's Reflexes")
            self.sneak_attack_die = "9d6"
        if level == 18:
            self.special_abilities.append("Elusive")
        if level == 19:
            self.special_abilities.append("Ability Score Improvement 19th Level")
            player.increase_ability_score(2)
            self.sneak_attack_die = "10d6"
        if level == 20:
            self.special_abilities.append("Stroke of Luck")
        return self
    
def define_rogue():
    rogue = Rogue()

    ### Equipment Choices ###
    first_equipment_choice = equipment.weapon_choices(["Mace", "Warhammer"])
    if first_equipment_choice == "Mace":
        rogue.starting_equipment.append(equipment.mace)
    elif first_equipment_choice == "Warhammer":
        rogue.starting_equipment.append(equipment.war_hammer)

    second_equipment_choice = equipment.weapon_choices(["Scale Mail", "Leather Armor", "Chain Mail"])
    if second_equipment_choice == "Scale Mail":
        rogue.starting_equipment.append(equipment.scale_mail_medium_armor)
    elif second_equipment_choice == "Leather Armor":
        rogue.starting_equipment.append(equipment.leather_light_armor)
    elif second_equipment_choice == "Chain Mail":
        rogue.starting_equipment.append(equipment.chain_mail_heavy_armor)

    third_equipment_choice = equipment.weapon_choices(["Light Crossbow", "Any Simple Weapon"])
    if third_equipment_choice == "Light Crossbow":
        rogue.starting_equipment.append(equipment.light_crossbow)
    else:
        rogue.starting_equipment.append(equipment.get_weapons_from_category("Simple Weapons"))

        third_equipment_choice = equipment.weapon_choices(["Priest's Pack", "Explorer's Pack"])
    if third_equipment_choice == "Priest's Pack":
        rogue.starting_equipment.append(equipment.priests_pack)
    else:
        rogue.starting_equipment.append(equipment.explorers_pack)

    rogue.starting_equipment.append(equipment.shield)
    rogue.starting_equipment.append(equipment.holy_symbol_emblem)

    ### Skill Choices ###
    for i in range(2):
        skill = skills.select_skill_proficiencies("rogue")
        rogue.skill_proficiencies.append(skill)

    ### Spell Choices ###
    for i in range(1):
        spell = spells.select_spells("rogue")
        rogue.spells.append(spell)

    ### Cantrip Choices ###
    for i in range(3):
        cantrip = cantrips.select_cantrips("rogue")
        rogue.cantrips.append(cantrip)

    return rogue
