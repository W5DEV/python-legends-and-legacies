import gui_modules.equipment as equipment
import gui_modules.skills as skills
import gui_modules.spells as spells
import gui_modules.cantrips as cantrips

class Wizard:

    def __init__(self):
        name = "Wizard"
        bio = "A scholarly magic-user capable of manipulating the structures of reality."
        hit_die = "1d6"
        primary_ability = "Intelligence"
        saving_throw_proficiencies = "Intelligence, Wisdom"
        armor_proficiencies = "None"
        weapon_proficiencies = "Daggers, Darts, Slings, Quarterstaffs, Light Crossbows"
        tool_proficiencies = "None"
        self.name = name
        self.bio = bio
        self.hit_die = hit_die
        self.base_hp = 6
        self.primary_ability = primary_ability
        self.saving_throw_proficiencies = saving_throw_proficiencies
        self.armor_proficiencies = armor_proficiencies
        self.weapon_proficiencies = weapon_proficiencies
        self.tool_proficiencies = tool_proficiencies
        self.skill_proficiencies = []
        self.starting_equipment = []
        self.special_abilities = []
        self.arcane_tradition = ""
        self.cantrips = []
        self.spells = []
        self.cantrips_known = 3
        self.spell_slots_level_1 = 2
        self.spell_slots_level_2 = 0
        self.spell_slots_level_3 = 0
        self.spell_slots_level_4 = 0
        self.spell_slots_level_5 = 0
        self.spell_slots_level_6 = 0
        self.spell_slots_level_7 = 0
        self.spell_slots_level_8 = 0
        self.spell_slots_level_9 = 0

    def sync_level(self, level, player):
        if level == 1:
            self.special_abilities.append("Spellcasting")
            self.special_abilities.append("Arcane Recovery")
        if level == 2:
            self.arcane_tradition = "School of Evocation"
            self.special_abilities.append("Evocation Savant")
            self.special_abilities.append("Sculpt Spells")
            self.spell_slots_level_1 = 3
        if level == 3:
            self.spell_slots_level_1 = 4
            self.spell_slots_level_2 = 2
        if level == 4:
            self.special_abilities.append("Ability Score Improvement 4th Level")
            player.increase_ability_score(2)
            self.cantrips_known = 4
            self.spell_slots_level_2 = 3
        if level == 5:
            self.spell_slots_level_3 = 2
        if level == 6:
            self.special_abilities.append("Potent Cantrip")
            self.spell_slots_level_3 = 3
        if level == 7:
            self.spell_slots_level_4 = 1
        if level == 8:
            self.special_abilities.append("Ability Score Improvement 8th Level")
            player.increase_ability_score(2)
            self.spell_slots_level_4 = 2
        if level == 9:
            self.spell_slots_level_4 = 3
            self.spell_slots_level_5 = 1
        if level == 10:
            self.special_abilities.append("Empowered Evocation")
            self.cantrips_known = 5
            self.spell_slots_level_5 = 2
        if level == 11:
            self.spell_slots_level_6 = 1
        if level == 12:
            self.special_abilities.append("Ability Score Improvement 12th Level")
            player.increase_ability_score(2)
        if level == 13:
            self.spell_slots_level_7 = 1
        if level == 14:
            self.special_abilities.append("Overchannel")
        if level == 15:
            self.spell_slots_level_8 = 1
        if level == 16:
            self.special_abilities.append("Ability Score Improvement 16th Level")
            player.increase_ability_score(2)
        if level == 17:
            self.spell_slots_level_9 = 1
        if level == 18:
            self.special_abilities.append("Spell Mastery")
            self.spell_slots_level_5 = 3
        if level == 19:
            self.special_abilities.append("Ability Score Improvement 19th Level")
            player.increase_ability_score(2)
            self.spell_slots_level_6 = 2
        if level == 20:
            self.special_abilities.append("Signature Spells")
            self.spell_slots_level_7 = 2
        return self
    
def define_wizard():
    wizard = Wizard()

    ### Equipment Choices ###
    first_equipment_choice = equipment.weapon_choices(["Mace", "Warhammer"])
    if first_equipment_choice == "Mace":
        wizard.starting_equipment.append(equipment.mace)
    elif first_equipment_choice == "Warhammer":
        wizard.starting_equipment.append(equipment.war_hammer)

    second_equipment_choice = equipment.weapon_choices(["Scale Mail", "Leather Armor", "Chain Mail"])
    if second_equipment_choice == "Scale Mail":
        wizard.starting_equipment.append(equipment.scale_mail_medium_armor)
    elif second_equipment_choice == "Leather Armor":
        wizard.starting_equipment.append(equipment.leather_light_armor)
    elif second_equipment_choice == "Chain Mail":
        wizard.starting_equipment.append(equipment.chain_mail_heavy_armor)

    third_equipment_choice = equipment.weapon_choices(["Light Crossbow", "Any Simple Weapon"])
    if third_equipment_choice == "Light Crossbow":
        wizard.starting_equipment.append(equipment.light_crossbow)
    else:
        wizard.starting_equipment.append(equipment.get_weapons_from_category("Simple Weapons"))

        third_equipment_choice = equipment.weapon_choices(["Priest's Pack", "Explorer's Pack"])
    if third_equipment_choice == "Priest's Pack":
        wizard.starting_equipment.append(equipment.priests_pack)
    else:
        wizard.starting_equipment.append(equipment.explorers_pack)

    wizard.starting_equipment.append(equipment.shield)
    wizard.starting_equipment.append(equipment.holy_symbol_emblem)

    ### Skill Choices ###
    for i in range(2):
        skill = skills.select_skill_proficiencies("wizard")
        wizard.skill_proficiencies.append(skill)

    ### Spell Choices ###
    for i in range(1):
        spell = spells.select_spells("wizard")
        wizard.spells.append(spell)

    ### Cantrip Choices ###
    for i in range(3):
        cantrip = cantrips.select_cantrips("wizard")
        wizard.cantrips.append(cantrip)

    return wizard
    