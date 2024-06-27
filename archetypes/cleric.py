# We still need to create methods for Clerics for the following:
# - update_spells_known
# - update_cantrips_known
# - update_spell_slots
# - level_up
# - proficiency_bonus
# - spell_save_dc
# - spell_attack_bonus
# - ritual_casting
# - spellcasting_focus

# Do clerics start with all spells and just "prepare" them? How does that work? Figure this out

import modules.starting_equipment as starting_equipment
import modules.skills as skills
import modules.spells as spells
import modules.cantrips as cantrips

displayed_cleric_skills, cleric_skills = skills.get_cleric_skills()
displayed_cleric_cantrips, cleric_cantrips = cantrips.get_cleric_cantrips()
displayed_cleric_spells, cleric_spells = spells.get_cleric_spells()
potential_starting_equipment = starting_equipment.get_starting_equipment("Cleric")

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
            player.increase_ability_score(2)
            self.cantrips_known = 4
            self.spell_slots_level_2 = 3
        if level == 5:
            self.special_abilities.append("Destroy Undead (CR 1/2)")
            self.special_abilities.append("Beacon of Hope", "Revivify")
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
            player.increase_ability_score(2)
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
            player.increase_ability_score(2)
        if level == 13:
            self.spell_slots_level_7 = 1
        if level == 14:
            self.special_abilities.append("Destroy Undead (CR 3)")
            self.special_abilities.append("Divine Strike (2d8)")
        if level == 15:
            self.spell_slots_level_8 = 1
        if level == 16:
            self.special_abilities.append("Ability Score Improvement 16th Level")
            player.increase_ability_score(2)
        if level == 17:
            self.special_abilities.append("Destroy Undead (CR 4)")
            self.special_abilities.append("Supreme Healing")
            self.spell_slots_level_9 = 1
        if level == 18:
            self.special_abilities.append("Channel Divinity 3/rest")
            self.spell_slots_level_5 = 3
        if level == 19:
            self.special_abilities.append("Ability Score Improvement 19th Level")
            player.increase_ability_score(2)
            self.spell_slots_level_6 = 2
        if level == 20:
            self.special_abilities.append("Divine Intervention Improvement")
            self.spell_slots_level_7 = 2
        return self

def define_cleric():
    cleric = Cleric()
    print(f"You have chosen the Cleric class.")
    print(cleric.bio)

    # Skill Proficiencies
    print("A Cleric is proficient in 2 skills. Choose two skills from the following:")
    for skill in displayed_cleric_skills:
        print(skill)
    print("Please enter your first skill choice:")
    skill_choice_1 = input("> ")
    while skill_choice_1.lower() not in cleric_skills:
        print("Please enter a valid skill choice:")
        skill_choice_1 = input("> ")

    print("Please enter your second skill choice:")
    skill_choice_2 = input("> ")
    while skill_choice_2.lower() not in cleric_skills:
        print("Please enter a valid skill choice:")
        skill_choice_2 = input("> ")
    
    selected_skills = [skill_choice_1, skill_choice_2]
    print(f"You have chosen proficiency in {selected_skills[0]} and {selected_skills[1]}.")
    cleric.skill_proficiencies = selected_skills

     # Starting Cantrips
    print("Clerics start with 3 Cantrips. Choose 3 Cantrips from the following list:")
    for cantrip in displayed_cleric_cantrips:
        print(cantrip)
    print("Please choose your first Cantrip:")
    cantrip_choice1 = input("> ")
    while (cantrip_choice1.lower() not in cleric_cantrips):
        print("Please enter a valid Cantrip choice:")
        cantrip_choice1 = input("> ")
    for cantrip in displayed_cleric_cantrips:
        if cantrip.lower() == cantrip_choice1.lower():
            cleric.cantrips.append(cantrip)
            break
    print("Please choose your second Cantrip:")
    cantrip_choice2 = input("> ")
    while (cantrip_choice2.lower() not in cleric_cantrips) or (cantrip_choice2.lower() in [cantrip_choice1.lower()]):
        print("You should not choose the same Cantrip twice.")
        print("Please enter a valid Cantrip choice:")
        cantrip_choice2 = input("> ")
    for cantrip in displayed_cleric_cantrips:
        if cantrip.lower() == cantrip_choice2.lower():
            cleric.cantrips.append(cantrip)
            break
    print("Please choose your third Cantrip:")
    cantrip_choice3 = input("> ")
    while (cantrip_choice3.lower() not in cleric_cantrips) or (cantrip_choice3.lower() in [cantrip_choice1.lower(), cantrip_choice2.lower()]):
        print("You should not choose the same Cantrip twice.")
        print("Please enter a valid Cantrip choice:")
        cantrip_choice3 = input("> ")
    for cantrip in displayed_cleric_cantrips:
        if cantrip.lower() == cantrip_choice3.lower():
            cleric.cantrips.append(cantrip)
            break
    print(f"You have chosen the following Cantrips:")
    for cantrip in cleric.cantrips:
        print(cantrip)

    # Starting Spells
    print("Clerics can prepare 1 spell. Choose 1 spell from the following list:")
    for spell in displayed_cleric_spells:
        print(spell)
    print("Please choose your spell:")
    spell_choice = input("> ")
    while spell_choice.lower() not in cleric_spells:
        print("Please enter a valid spell choice:")
        spell_choice = input("> ")
    for spell in displayed_cleric_spells:
        if spell.lower() == spell_choice.lower():
            cleric.spells.append(spell)
            break
    print(f"You have chosen the following Spell:")
    for spell in cleric.spells:
        print(spell)

    # Starting Equipment
    equipment_choice_1 = starting_equipment.starting_equipment_choice("Mace", "Warhammer")
    if equipment_choice_1.lower() == "mace":
        starting_weapon = starting_equipment.starting_equipment("Mace")
    else:
        starting_weapon = starting_equipment.starting_equipment("Warhammer")
    print(f"One {starting_weapon.name} has been added to your starting equipment.")
    cleric.starting_equipment.append(starting_weapon)

    equipment_choice_2 = starting_equipment.starting_equipment_choice_three("Scale Mail", "Leather Armor", "Chain Mail")
    if equipment_choice_2.lower() == "scale mail":
        starting_armor = starting_equipment.starting_equipment("Scale Mail Medium Armor")
    elif equipment_choice_2.lower() == "leather armor":
        starting_armor = starting_equipment.starting_equipment("Leather Light Armor")
    else:
        starting_armor = starting_equipment.starting_equipment("Chain Mail Heavy Armor")
    print(f"One {starting_armor.name} has been added to your starting equipment.")
    cleric.starting_equipment.append(starting_armor)

    equipment_choice_3 = starting_equipment.starting_equipment_choice("Light Crossbow and 20 bolts", "Any Simple Weapon")
    if equipment_choice_3.lower() == "light crossbow and 20 bolts":
        starting_weapon = starting_equipment.starting_equipment("Light Crossbow")
    else:
        starting_weapon = starting_equipment.select_equipment_from_category("Simple Weapons")
    print(f"One {starting_weapon.name} has been added to your starting equipment.")
    cleric.starting_equipment.append(starting_weapon)
        
    equipment_choice_4 = starting_equipment.starting_equipment_choice("Priest's Pack", "Explorer's Pack")
    if equipment_choice_4.lower() == "priest's pack":
        starting_pack = starting_equipment.starting_equipment("Priest's Pack")
    else:
        starting_pack = starting_equipment.starting_equipment("Explorer's Pack")
    print(f"One {starting_pack.name} has been added to your starting equipment.")
    cleric.starting_equipment.append(starting_pack)

    shield = starting_equipment.starting_equipment("Shield")
    holy_symbol = starting_equipment.starting_equipment("Holy Symbol Emblem")
    print("A Shield and a Holy Symbol Emblem have been added to your starting equipment.")
    cleric.starting_equipment.append(shield)
    cleric.starting_equipment.append(holy_symbol)

    return cleric




