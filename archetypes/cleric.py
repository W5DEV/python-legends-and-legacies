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
        return self

    def sync_level(self, level):
        if level >= 1:
            self.divine_domain = "Life Domain"
            self.armor_proficiencies.append("Heavy Armor")
            self.special_abilities = ["Spellcasting", "Divine Domain"]
            self.special_abilities.append("Bless")
            self.special_abilities.append("Cure Wounds")
            self.special_abilities.append("Disciple of Life")
        if level >= 2:
            self.special_abilities.append("Channel Divinity 2/rest")
            self.special_abilities.append("Channel Divinity: Preserve Life")
            self.spell_slots_level_1 = 3
        if level >= 3:
            self.special_abilities.append("Lesser Restoration")
            self.special_abilities.append("Spiritual Weapon")
            self.spell_slots_level_1 = 4
            self.spell_slots_level_2 = 2
        if level >= 4:
            self.special_abilities.append("Ability Score Improvement 4th Level")
            self.cantrips_known = 4
            self.spell_slots_level_2 = 3
        if level >= 5:
            self.special_abilities.append("Destroy Undead (CR 1/2)")
            self.special_abilities.append("Beacon of Hope", "Revivify")
            self.spell_slots_level_3 = 2
        if level >= 6:
            self.special_abilities.append("Channel Divinity 2/rest")
            self.special_abilities.append("Blessed Healer")
            self.spell_slots_level_3 = 3
        if level >= 7:
            self.special_abilities.append("Death Ward")
            self.special_abilities.append("Guardian of Faith")
            self.spell_slots_level_4 = 1
        if level >= 8:
            self.special_abilities.append("Ability Score Improvement 8th Level")
            self.special_abilities.append("Destroy Undead (CR 1)")
            self.special_abilities.append("Divine Strike (1d8)")
            self.spell_slots_level_4 = 2
        if level >= 9:
            self.special_abilities.append("Mass Cure Wounds")
            self.special_abilities.append("Raise Dead")
            self.spell_slots_level_4 = 3
            self.spell_slots_level_5 = 1
        if level >= 10:
            self.special_abilities.append("Divine Intervention")
            self.spell_slots_level_5 = 2
        if level >= 11:
            self.special_abilities.append("Destroy Undead (CR 2)")
            self.spell_slots_level_6 = 1
        if level >= 12:
            self.special_abilities.append("Ability Score Improvement 12th Level")
        if level >= 13:
            self.spell_slots_level_7 = 1
        if level >= 14:
            self.special_abilities.append("Destroy Undead (CR 3)")
            self.special_abilities.append("Divine Strike (2d8)")
        if level >= 15:
            self.spell_slots_level_8 = 1
        if level >= 16:
            self.special_abilities.append("Ability Score Improvement 16th Level")
        if level >= 17:
            self.special_abilities.append("Destroy Undead (CR 4)")
            self.special_abilities.append("Supreme Healing")
            self.spell_slots_level_9 = 1
        if level >= 18:
            self.special_abilities.append("Channel Divinity 3/rest")
            self.spell_slots_level_5 = 3
        if level >= 19:
            self.special_abilities.append("Ability Score Improvement 19th Level")
            self.spell_slots_level_6 = 2
        if level >= 20:
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
    weapon_choice1 = ""
    armor_choice = ""
    weapon_choice2 = ""
    pack_choice = ""
    print("Clerics are able to choose from the following starting equipment:")
    for item in potential_starting_equipment:
        print(item)
    
    print("Please choose between a Mace or a Warhammer:")
    weapon_choice1 = input("> ")
    while weapon_choice1.lower() not in ["mace", "warhammer"]:
        print("Please enter a valid weapon choice:")
        weapon_choice1 = input("> ")
    if weapon_choice1.lower() == "mace":
        print("You have chosen a Mace.")
        print("A Mace has been added to your starting equipment.")
        cleric.starting_equipment.append(equipment.mace)
    elif weapon_choice1.lower() == "warhammer":
        print("You have chosen a Warhammer.")
        print("A Warhammer has been added to your starting equipment.")
        cleric.starting_equipment.append(equipment.warhammer)

    print("Please choose between Scale Mail, Leather Armor, or Chain Mail:")
    armor_choice = input("> ")
    while armor_choice.lower() not in ["scale mail", "leather Armor", "chain mail"]:
        print("Please enter a valid armor choice:")
        armor_choice = input("> ")
    if armor_choice.lower() == "scale mail":
        print("You have chosen Scale Mail.")
        print("Scale Mail has been added to your starting equipment.")
        cleric.starting_equipment.append(equipment.scale_mail_medium_armor)
    elif armor_choice.lower() == "leather armor":
        print("You have chosen Leather Armor.")
        print("Leather Armor has been added to your starting equipment.")
        cleric.starting_equipment.append(equipment.leather_light_armor)
    elif armor_choice.lower() == "chain mail":
        print("You have chosen Chain Mail.")
        print("Chain Mail has been added to your starting equipment.")
        cleric.starting_equipment.append(equipment.chain_mail_heavy_armor)
    
    print("Please choose between a Light Crossbow and 20 bolts or any simple weapon:")
    print("Please enter either 'Light Crossbow' or 'Other Simple Weapon'")
    weapon_choice2 = input("> ")
    while weapon_choice2.lower() not in ["light crossbow", "other simple weapon"]:
        print("Please enter a valid weapon choice:")
        weapon_choice2 = input()
    if weapon_choice2.lower() == "light crossbow":
        print("You have chosen a Light Crossbow and 20 bolts.")
        print("A Light Crossbow and 20 bolts have been added to your starting equipment.")
        cleric.starting_equipment.append(equipment.light_crossbow)
    elif weapon_choice2.lower() == "other simple weapon":
        valid_weapons = []
        print("Please choose a simple weapon from the list below:")
        for weapon in equipment.simple_weapons:
            valid_weapons.append(weapon.name.lower())
            print(weapon.name)
        other_weapon = input("> ")
        while other_weapon.lower() not in valid_weapons:
            print("Please enter a valid weapon choice")
            other_weapon = input("> ")
        for weapon in equipment.simple_weapons:
            if other_weapon.lower() == weapon.name.lower():
                print(f"You have chosen a {weapon.name}.")
                print(f"A {weapon.name} has been added to your starting equipment.")
                cleric.starting_equipment.append(weapon)
                break
    
    print("Please choose between a Priest's Pack or an Explorer's Pack:")
    pack_choice = input("> ")
    while pack_choice.lower() not in ["priest's pack", "explorer's pack"]:
        print("Please enter a valid pack choice:")
        pack_choice = input("> ")
    if pack_choice.lower() == "priest's pack":
        print("You have chosen a Priest's Pack.")
        print("A Priest's Pack has been added to your starting equipment.")
        cleric.starting_equipment.append(equipment.priests_pack)
    elif pack_choice.lower() == "explorer's pack":
        print("You have chosen an Explorer's Pack.")
        print("An Explorer's Pack has been added to your starting equipment.")
        cleric.starting_equipment.append(equipment.explorers_pack)

    print("You will also receive a Shield and a Holy Symbol Emblem.")
    print("A Shield and a Holy Symbol Emblem have been added to your starting equipment.")
    cleric.starting_equipment.append(equipment.shield)
    cleric.starting_equipment.append(equipment.holy_symbol_emblem)

    print("You will start with the following equipment:")
    for item in cleric.starting_equipment:
        print(item.name)

    return cleric




