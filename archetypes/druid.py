# We still need to create methods for druids for the following:
# - update_spells_known
# - update_cantrips_known
# - update_spell_slots
# - level_up
# - proficiency_bonus
# - spell_save_dc
# - spell_attack_bonus
# - ritual_casting
# - spellcasting_focus

import modules.starting_equipment as starting_equipment
import modules.skills as skills
import modules.spells as spells
import modules.cantrips as cantrips

displayed_druid_skills, druid_skills = skills.get_druid_skills()
displayed_druid_spells, druid_spells = spells.get_druid_spells()
displayed_druid_cantrips, druid_cantrips = cantrips.get_druid_cantrips()
potential_starting_equipment = starting_equipment.get_starting_equipment("Druid")

class Druid:
    def __init__(self):
        name = "Druid"
        bio = "A priest of the Old Faith, wielding the powers of nature — moonlight and plant growth, fire and lightning — and adopting animal forms."
        hit_die = "1d8"
        primary_ability = "Wisdom"
        saving_throw_proficiencies = "Intelligence, Wisdom"
        armor_proficiencies = "Non-metal Light Armor, Non-metal Medium Armor, Non-metal Shields"
        weapon_proficiencies = "Clubs, Daggers, Darts, Javelins, Maces, Quarterstaffs, Scimitars, Sickles, Slings, Spears"
        tool_proficiencies = "Herbalism Kit"
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
        self.special_abilities = []
        self.circle = ""
        self.cantrips = []
        self.spells = []
        self.cantrips_known = 2
        self.spell_slots_level_1 = 2
        self.spell_slots_level_2 = 0
        self.spell_slots_level_3 = 0
        self.spell_slots_level_4 = 0
        self.spell_slots_level_5 = 0
        self.spell_slots_level_6 = 0
        self.spell_slots_level_7 = 0
        self.spell_slots_level_8 = 0
        self.spell_slots_level_9 = 0

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
        if level == 1:
            self.special_abilities.append("Druidic")
            self.special_abilities.append("Spellcasting")
        if level == 2:
            self.circle = "Circle of the Land"
            self.special_abilities.append("Wild Shape - No flying or swimming speed (1/4 CR)")
            self.special_abilities.append("Bonus Cantrip")
            self.special_abilities.append("Natural Recovery")
            self.spell_slots_level_1 = 3
        if level == 3:
            self.special_abilities.append("3rd Level Circle Spells")
            self.spell_slots_level_1 = 4
            self.spell_slots_level_2 = 2
        if level == 4:
            self.special_abilities.append("Wild Shape Improvement 4th Level - No flying speed (1/2 CR)")
            self.special_abilities.append("Ability Score Improvement 4th Level")
            self.spell_slots_level_2 = 3
        if level == 5:
            self.special_abilities.append("5th Level Circle Spells")
            self.spell_slots_level_3 = 2
        if level == 6:
            self.special_abilities.append("Land's Stride")
            self.spell_slots_level_3 = 3
        if level == 7:
            self.special_abilities.append("7th Level Circle Spells")
            self.spell_slots_level_4 = 1
        if level == 8:
            self.special_abilities.append("Wild Shape Improvement 8th Level (1 CR)")
            self.special_abilities.append("Ability Score Improvement 8th Level")
            self.spell_slots_level_4 = 2
        if level == 9:
            self.special_abilities.append("9th Level Circle Spells")
            self.spell_slots_level_4 = 3
            self.spell_slots_level_5 = 1
        if level == 10:
            self.special_abilities.append("Nature's Ward")
            self.spell_slots_level_5 = 2
        if level == 11:
            self.spell_slots_level_6 = 1
        if level == 12:
            self.special_abilities.append("Ability Score Improvement 12th Level")
        if level == 13:
            self.spell_slots_level_7 = 1
        if level == 14:
            self.special_abilities.append("Nature's Sanctuary")
        if level == 15:
            self.spell_slots_level_8 = 1
        if level == 16:
            self.special_abilities.append("Ability Score Improvement 16th Level")
        if level == 17:
            self.spell_slots_level_9 = 1
        if level == 18:
            self.special_abilities.append("Timeless Body")
            self.special_abilities.append("Beast Spells")
            self.spell_slots_level_5 = 3
        if level == 19:
            self.special_abilities.append("Ability Score Improvement 19th Level")
            self.spell_slots_level_6 = 2
        if level == 20:
            self.special_abilities.append("Archdruid")
            self.spell_slots_level_7 = 2
        return self
    
def define_druid():
    druid = Druid()
    print("You have chosen the Druid class.")
    print(druid.bio)

    # Skill Proficiencies
    print("Choose two skills from the following:")
    for skill in displayed_druid_skills:
        print(skill)
    print("Please enter your first skill choice:")
    skill_choice_1 = input("> ")
    while skill_choice_1.lower() not in druid_skills:
        print("Please enter a valid skill choice:")
        skill_choice_1 = input("> ")

    print("Please enter your second skill choice:")
    skill_choice_2 = input("> ")
    while skill_choice_2.lower() not in druid_skills:
        print("Please enter a valid skill choice:")
        skill_choice_2 = input("> ")
    
    selected_skills = [skill_choice_1, skill_choice_2]
    print(f"You have chosen proficiency in {selected_skills[0]} and {selected_skills[1]}.")
    druid.skill_proficiencies = selected_skills

     # Starting Cantrips
    print("Druids start with 2 Cantrips. Choose 2 Cantrips from the following list:")
    for cantrip in displayed_druid_cantrips:
        print(cantrip)
    print("Please choose your first Cantrip:")
    cantrip_choice1 = input("> ")
    while (cantrip_choice1.lower() not in druid_cantrips):
        print("Please enter a valid Cantrip choice:")
        cantrip_choice1 = input("> ")
    for cantrip in displayed_druid_cantrips:
        if cantrip.lower() == cantrip_choice1.lower():
            druid.cantrips.append(cantrip)
            break
    print("Please choose your second Cantrip:")
    cantrip_choice2 = input("> ")
    while (cantrip_choice2.lower() not in druid_cantrips) or (cantrip_choice2.lower() in [cantrip_choice1.lower()]):
        print("You should not choose the same Cantrip twice.")
        print("Please enter a valid Cantrip choice:")
        cantrip_choice2 = input("> ")
    for cantrip in displayed_druid_cantrips:
        if cantrip.lower() == cantrip_choice2.lower():
            druid.cantrips.append(cantrip)
            break
    print(f"You have chosen the following Cantrips:")
    for cantrip in druid.cantrips:
        print(cantrip)

    # Starting Spells
    print("Druids can prepare 1 spell. Choose 1 spell from the following list:")
    for spell in displayed_druid_spells:
        print(spell)
    print("Please choose your spell:")
    spell_choice = input("> ")
    while spell_choice.lower() not in druid_spells:
        print("Please enter a valid spell choice:")
        spell_choice = input("> ")
    for spell in displayed_druid_spells:
        if spell.lower() == spell_choice.lower():
            druid.spells.append(spell)
            break
    print(f"You have chosen the following Spell:")
    for spell in druid.spells:
        print(spell)

    # Starting Equipment
    equipment_choice_1 = starting_equipment.starting_equipment_choice("Shield", "Any Simple Weapon")
    if equipment_choice_1.lower() == "shield":
        starting_weapon = starting_equipment.starting_equipment("Shield")
    else:
        starting_weapon = starting_equipment.select_equipment_from_category("Simple Weapons")
    print(f"One {starting_weapon.name} has been added to your starting equipment.")
    druid.starting_equipment.append(starting_weapon)

    equipment_choice_2 = starting_equipment.starting_equipment_choice("Scimitar", "Any Simple Melee Weapon")
    if equipment_choice_2.lower() == "scimitar":
        starting_weapon = starting_equipment.starting_equipment("Scimitar")
    else:
        starting_weapon = starting_equipment.select_equipment_from_category("Simple Melee Weapons")
    print(f"One {starting_weapon.name} has been added to your starting equipment.")
    druid.starting_equipment.append(starting_weapon)

    leather_armor = starting_equipment.starting_equipment("Leather Light Armor")
    explorers_pack = starting_equipment.starting_equipment("Explorer's Pack")
    druidic_focus = starting_equipment.starting_equipment("Druidic Focus")
    print("Leather Armor, an Explorer's Pack, and a Druidic Focus have been added to your starting equipment.")
    druid.starting_equipment.append(leather_armor)
    druid.starting_equipment.append(explorers_pack)
    druid.starting_equipment.append(druidic_focus)

    return druid