import modules.equipment as equipment
import modules.skills as skills
import modules.spells as spells
import modules.cantrips as cantrips

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
            player.update_ability_points(2)
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
            player.update_ability_points(2)
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
            player.update_ability_points(2)
        if level == 13:
            self.spell_slots_level_7 = 1
        if level == 14:
            self.special_abilities.append("Overchannel")
        if level == 15:
            self.spell_slots_level_8 = 1
        if level == 16:
            self.special_abilities.append("Ability Score Improvement 16th Level")
            player.update_ability_points(2)
        if level == 17:
            self.spell_slots_level_9 = 1
        if level == 18:
            self.special_abilities.append("Spell Mastery")
            self.spell_slots_level_5 = 3
        if level == 19:
            self.special_abilities.append("Ability Score Improvement 19th Level")
            player.update_ability_points(2)
            self.spell_slots_level_6 = 2
        if level == 20:
            self.special_abilities.append("Signature Spells")
            self.spell_slots_level_7 = 2
        return self
    
def define_wizard():
    wizard = Wizard()

    ### Equipment Choices ###
    first_equipment_choice = equipment.weapon_choices(["Quarterstaff", "Dagger"])
    if first_equipment_choice == "Quarterstaff":
        wizard.starting_equipment.append(equipment.quarter_staff)
    elif first_equipment_choice == "dagger":
        wizard.starting_equipment.append(equipment.dagger)

    second_equipment_choice = equipment.weapon_choices(["Component Pouch", "Arcane Focus"])
    if second_equipment_choice == "Component Pouch":
        wizard.starting_equipment.append(equipment.component_pouch)
    elif second_equipment_choice == "Arcane Focus":
        wizard.starting_equipment.append(equipment.arcane_focus_crystal)

    third_equipment_choice = equipment.weapon_choices(["Scholar's Pack", "Explorer's Pack"])
    if third_equipment_choice == "Scholar's Pack":
        wizard.starting_equipment.append(equipment.scholars_pack)
    else:
        wizard.starting_equipment.append(equipment.explorers_pack)

    wizard.starting_equipment.append(equipment.spellbook)

    ### Skill Choices ###
    for i in range(2):
        skill = skills.select_skill_proficiencies("Wizard")
        wizard.skill_proficiencies.append(skill)

    ### Spell Choices ###
    for i in range(2):
        spell = spells.select_spells("Wizard")
        wizard.spells.append(spell)

    ### Cantrip Choices ###
    for i in range(3):
        cantrip = cantrips.select_cantrips("Wizard")
        wizard.cantrips.append(cantrip)

    return wizard
    