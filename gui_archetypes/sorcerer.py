import gui_modules.equipment as equipment
import gui_modules.skills as skills
import gui_modules.spells as spells
import gui_modules.cantrips as cantrips

class Sorcerer:

    def __init__(self):
        name = "Sorcerer"
        bio = "A spellcaster who draws on inherent magic from a gift or bloodline."
        hit_die = "1d6"
        primary_ability = "Charisma"
        saving_throw_proficiencies = "Constitution, Charisma"
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
        self.sorcerous_origin = ""
        self.cantrips = []
        self.spells = []
        self.sorcery_points = 0
        self.cantrips_known = 4
        self.spells_known = 2
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
            self.sorcerous_origin = "Dragon Bloodline"
            self.special_abilities.append("Dragon Ancestor")
            self.special_abilities.append("Dracoic Resilience")
        if level == 2:
            self.special_abilities.append("Font of Magic")
            self.sorcery_points = 2
            self.spells_known = 3
            self.spell_slots_level_1 = 3
        if level == 3:
            self.special_abilities.append("Metamagic")
            self.sorcery_points = 3
            self.spells_known = 4
            self.spell_slots_level_1 = 4
            self.spell_slots_level_2 = 2
        if level == 4:
            self.special_abilities.append("Ability Score Improvement 4th Level")
            player.increase_ability_score(2)
            self.sorcery_points = 4
            self.cantrips_known = 5
            self.spell_slots_level_2 = 3
        if level == 5:
            self.sorcery_points = 5
            self.spells_known = 6
            self.spell_slots_level_3 = 2
        if level == 6:
            self.special_abilities.append("Elemental Affinity")
            self.sorcery_points = 6
            self.spells_known = 7
            self.spell_slots_level_3 = 3
        if level == 7:
            self.sorcery_points = 7
            self.spells_known = 8
            self.spell_slots_level_4 = 1
        if level == 8:
            self.special_abilities.append("Ability Score Improvement 8th Level")
            player.increase_ability_score(2)
            self.sorcery_points = 8
            self.spells_known = 9
            self.spell_slots_level_4 = 2
        if level == 9:
            self.sorcery_points = 9
            self.spells_known = 10
            self.spell_slots_level_4 = 3
            self.spell_slots_level_5 = 1
        if level == 10:
            self.special_abilities.append("Metamagic")
            self.sorcery_points = 10
            self.cantrips_known = 6
            self.spells_known = 11
            self.spell_slots_level_5 = 2
        if level == 11:
            self.sorcery_points = 11
            self.spells_known = 12
            self.spell_slots_level_6 = 1
        if level == 12:
            self.special_abilities.append("Ability Score Improvement 12th Level")
            player.increase_ability_score(2)
            self.sorcery_points = 12
        if level == 13:
            self.sorcery_points = 13
            self.spells_known = 13
            self.spell_slots_level_7 = 1
        if level == 14:
            self.special_abilities.append("Dragon Wings")
            self.sorcery_points = 14
        if level == 15:
            self.sorcery_points = 15
            self.spells_known = 14
            self.spell_slots_level_8 = 1
        if level == 16:
            self.special_abilities.append("Ability Score Improvement 16th Level")
            player.increase_ability_score(2)
            self.sorcery_points = 16
        if level == 17:
            self.special_abilities.append("Metamagic")
            self.sorcery_points = 17
            self.spells_known = 15
            self.spell_slots_level_9 = 1
        if level == 18:
            self.special_abilities.append("Draconic Presence")
            self.sorcery_points = 18
            self.spell_slots_level_5 = 3
        if level == 19:
            self.special_abilities.append("Ability Score Improvement 19th Level")
            player.increase_ability_score(2)
            self.sorcery_points = 19
            self.spell_slots_level_6 = 2
        if level == 20:
            self.special_abilities.append("Sorcerous Restoration")
            self.sorcery_points = 20
            self.spell_slots_level_7 = 2
        return self
    
def define_sorcerer():
    sorcerer = Sorcerer()

    ### Equipment Choices ###
    first_equipment_choice = equipment.weapon_choices(["Mace", "Warhammer"])
    if first_equipment_choice == "Mace":
        sorcerer.starting_equipment.append(equipment.mace)
    elif first_equipment_choice == "Warhammer":
        sorcerer.starting_equipment.append(equipment.war_hammer)

    second_equipment_choice = equipment.weapon_choices(["Scale Mail", "Leather Armor", "Chain Mail"])
    if second_equipment_choice == "Scale Mail":
        sorcerer.starting_equipment.append(equipment.scale_mail_medium_armor)
    elif second_equipment_choice == "Leather Armor":
        sorcerer.starting_equipment.append(equipment.leather_light_armor)
    elif second_equipment_choice == "Chain Mail":
        sorcerer.starting_equipment.append(equipment.chain_mail_heavy_armor)

    third_equipment_choice = equipment.weapon_choices(["Light Crossbow", "Any Simple Weapon"])
    if third_equipment_choice == "Light Crossbow":
        sorcerer.starting_equipment.append(equipment.light_crossbow)
    else:
        sorcerer.starting_equipment.append(equipment.get_weapons_from_category("Simple Weapons"))

        third_equipment_choice = equipment.weapon_choices(["Priest's Pack", "Explorer's Pack"])
    if third_equipment_choice == "Priest's Pack":
        sorcerer.starting_equipment.append(equipment.priests_pack)
    else:
        sorcerer.starting_equipment.append(equipment.explorers_pack)

    sorcerer.starting_equipment.append(equipment.shield)
    sorcerer.starting_equipment.append(equipment.holy_symbol_emblem)

    ### Skill Choices ###
    for i in range(2):
        skill = skills.select_skill_proficiencies("sorcerer")
        sorcerer.skill_proficiencies.append(skill)

    ### Spell Choices ###
    for i in range(1):
        spell = spells.select_spells("sorcerer")
        sorcerer.spells.append(spell)

    ### Cantrip Choices ###
    for i in range(3):
        cantrip = cantrips.select_cantrips("sorcerer")
        sorcerer.cantrips.append(cantrip)

    return sorcerer