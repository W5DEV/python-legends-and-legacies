import modules.equipment as equipment
import modules.skills as skills
import modules.spells as spells
import modules.cantrips as cantrips

class Cleric:

    def __init__(self):
        name = "Cleric"
        bio = "A priestly champion who wields divine magic in service of a higher power."
        hit_die = "1d8"
        primary_ability = "Wisdom"
        saving_throw_proficiencies = "Wisdom, Charisma"
        armor_proficiencies = "Light Armor, Medium Armor, Shields"
        weapon_proficiencies = "Simple Weapons"
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
        self.special_abilities = []
        self.divine_domain = ""
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
            self.divine_domain = "Life Domain"
            self.special_abilities = ["Spellcasting", "Divine Domain"]
            self.special_abilities.append("Bless")
            self.special_abilities.append("Cure Wounds")
            self.special_abilities.append("Disciple of Life")
        if level == 2:
            self.special_abilities.append("Channel Divinity 2/rest")
            self.special_abilities.append("Channel Divinity: Preserve Life")
            self.spell_slots_level_1 = 3
        if level == 3:
            self.special_abilities.append("Lesser Restoration")
            self.special_abilities.append("Spiritual Weapon")
            self.spell_slots_level_1 = 4
            self.spell_slots_level_2 = 2
        if level == 4:
            self.special_abilities.append("Ability Score Improvement 4th Level")
            player.update_ability_points(2)
            self.cantrips_known = 4
            self.spell_slots_level_2 = 3
        if level == 5:
            self.special_abilities.append("Destroy Undead (CR 1/2)")
            self.special_abilities.append("Beacon of Hope")
            self.special_abilities.append("Revivify")
            self.spell_slots_level_3 = 2
        if level == 6:
            self.special_abilities.append("Channel Divinity 2/rest")
            self.special_abilities.append("Blessed Healer")
            self.spell_slots_level_3 = 3
        if level == 7:
            self.special_abilities.append("Death Ward")
            self.special_abilities.append("Guardian of Faith")
            self.spell_slots_level_4 = 1
        if level == 8:
            self.special_abilities.append("Ability Score Improvement 8th Level")
            player.update_ability_points(2)
            self.special_abilities.append("Destroy Undead (CR 1)")
            self.special_abilities.append("Divine Strike (1d8)")
            self.spell_slots_level_4 = 2
        if level == 9:
            self.special_abilities.append("Mass Cure Wounds")
            self.special_abilities.append("Raise Dead")
            self.spell_slots_level_4 = 3
            self.spell_slots_level_5 = 1
        if level == 10:
            self.special_abilities.append("Divine Intervention")
            self.spell_slots_level_5 = 2
        if level == 11:
            self.special_abilities.append("Destroy Undead (CR 2)")
            self.spell_slots_level_6 = 1
        if level == 12:
            self.special_abilities.append("Ability Score Improvement 12th Level")
            player.update_ability_points(2)
        if level == 13:
            self.spell_slots_level_7 = 1
        if level == 14:
            self.special_abilities.append("Destroy Undead (CR 3)")
            self.special_abilities.append("Divine Strike (2d8)")
        if level == 15:
            self.spell_slots_level_8 = 1
        if level == 16:
            self.special_abilities.append("Ability Score Improvement 16th Level")
            player.update_ability_points(2)
        if level == 17:
            self.special_abilities.append("Destroy Undead (CR 4)")
            self.special_abilities.append("Supreme Healing")
            self.spell_slots_level_9 = 1
        if level == 18:
            self.special_abilities.append("Channel Divinity 3/rest")
            self.spell_slots_level_5 = 3
        if level == 19:
            self.special_abilities.append("Ability Score Improvement 19th Level")
            player.update_ability_points(2)
            self.spell_slots_level_6 = 2
        if level == 20:
            self.special_abilities.append("Divine Intervention Improvement")
            self.spell_slots_level_7 = 2
        return self
    
def define_cleric():
    cleric = Cleric()

    ### Equipment Choices ###
    first_equipment_choice = equipment.weapon_choices(["Mace", "Warhammer"])
    if first_equipment_choice == "Mace":
        cleric.starting_equipment.append(equipment.mace)
    elif first_equipment_choice == "Warhammer":
        cleric.starting_equipment.append(equipment.war_hammer)

    second_equipment_choice = equipment.weapon_choices(["Scale Mail", "Leather Armor", "Chain Mail"])
    if second_equipment_choice == "Scale Mail":
        cleric.starting_equipment.append(equipment.scale_mail_medium_armor)
    elif second_equipment_choice == "Leather Armor":
        cleric.starting_equipment.append(equipment.leather_light_armor)
    elif second_equipment_choice == "Chain Mail":
        cleric.starting_equipment.append(equipment.chain_mail_heavy_armor)

    third_equipment_choice = equipment.weapon_choices(["Light Crossbow", "Any Simple Weapon"])
    if third_equipment_choice == "Light Crossbow":
        cleric.starting_equipment.append(equipment.light_crossbow)
    else:
        cleric.starting_equipment.append(equipment.get_weapons_from_category("Simple Weapons"))

    fourth_equipment_choice = equipment.weapon_choices(["Priest's Pack", "Explorer's Pack"])
    if fourth_equipment_choice == "Priest's Pack":
        cleric.starting_equipment.append(equipment.priests_pack)
    else:
        cleric.starting_equipment.append(equipment.explorers_pack)

    cleric.starting_equipment.append(equipment.shield)
    cleric.starting_equipment.append(equipment.holy_symbol_emblem)

    ### Skill Choices ###
    for i in range(2):
        skill = skills.select_skill_proficiencies("Cleric")
        cleric.skill_proficiencies.append(skill)

    ### Spell Choices ###
    for i in range(1):
        spell = spells.select_spells("Cleric")
        cleric.spells.append(spell)

    ### Cantrip Choices ###
    for i in range(3):
        cantrip = cantrips.select_cantrips("Cleric")
        cleric.cantrips.append(cantrip)

    return cleric
