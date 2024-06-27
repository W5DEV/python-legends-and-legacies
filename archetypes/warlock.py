# We still need to create methods for warlocks for the following:
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

displayed_warlock_skills, warlock_skills = skills.get_warlock_skills()
displayed_warlock_spells, warlock_spells = spells.get_warlock_spells()
displayed_warlock_cantrips, warlock_cantrips = cantrips.get_warlock_cantrips()
potential_starting_equipment = starting_equipment.get_starting_equipment("Warlock")

class Warlock:
    def __init__(self):
        name = "Warlock"
        bio = "A wielder of magic that is derived from a bargain with an extraplanar entity."
        hit_die = "1d8"
        primary_ability = "Charisma"
        saving_throw_proficiencies = "Wisdom, Charisma"
        armor_proficiencies = "Light Armor"
        weapon_proficiencies = "Simple Weapons"
        tool_proficiencies = "None"
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
        self.otherworldly_patrons = ""
        self.cantrips = []
        self.spells = []
        self.cantrips_known = 2
        self.spells_known = 2
        self.spell_slots = 1
        self.spell_slot_level = 1
        self.invocations_known = 0
    
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
            self.otherworldly_patrons = "The Fiend"
            self.special_abilities.append("Fiend Expanded Spells Level 1")
            self.special_abilities.append("Pact Magic")
            self.special_abilities.append("Dark One's Blessing")
        if level == 2:
            self.special_abilities.append("Eldritch Invocations")
            self.special_abilities.append("Fiend Expanded Spells Level 2")
            self.spells_known = 3
            self.spell_slots = 2
            self.invocations_known = 2
        if level == 3:
            self.special_abilities.append("Pact Boom")
            self.special_abilities.append("Fiend Expanded Spells Level 3")
            self.spells_known = 4
            self.spell_slot_level = 2
        if level == 4:
            self.special_abilities.append("Ability Score Improvement 4th Level")
            player.increase_ability_score(2)
            self.special_abilities.append("Fiend Expanded Spells Level 4")
            self.cantrips_known = 3
            self.spells_known = 5
        if level == 5:
            self.special_abilities.append("Fiend Expanded Spells Level 5")
            self.spells_known = 6
            self.spell_slot_level = 3
            self.invocations_known = 3
        if level == 6:
            self.special_abilities.append("Dark One's Own Luck")
            self.spells_known = 7
        if level == 7:
            self.spells_known = 8
            self.spell_slot_level = 4
            self.invocations_known = 4
        if level == 8:
            self.special_abilities.append("Ability Score Improvement 8th Level")
            player.increase_ability_score(2)
            self.spells_known = 9
        if level == 9:
            self.spells_known = 10
            self.spell_slot_level = 5
            self.invocations_known = 5
        if level == 10:
            self.special_abilities.append("Fiendish Resilience")
            self.cantrips_known = 4
        if level == 11:
            self.special_abilities.append("Mystic Arcanum 6th Level")
            self.spells_known = 11
            self.spell_slots = 3
        if level == 12:
            self.special_abilities.append("Ability Score Improvement 12th Level")
            player.increase_ability_score(2)
            self.invocations_known = 6
        if level == 13:
            self.special_abilities.append("Mystic Arcanum 7th Level")
            self.spells_known = 12
        if level == 14:
            self.special_abilities.append("Hurl Through Hell")
        if level == 15:
            self.special_abilities.append("Mystic Arcanum 8th Level")
            self.spells_known = 13
            self.invocations_known = 7
        if level == 16:
            self.special_abilities.append("Ability Score Improvement 16th Level")
            player.increase_ability_score(2)
        if level == 17:
            self.special_abilities.append("Mythic Arcanum 9th Level")
            self.spells_known = 14
            self.spell_slots = 4
        if level == 18:
            self.invocations_known = 8
        if level == 19:
            self.special_abilities.append("Ability Score Improvement 19th Level")
            player.increase_ability_score(2)
            self.spells_known = 15
        if level == 20:
            self.special_abilities.append("Eldritch Master")

def define_warlock():
    warlock = Warlock()
    print(f'You have chosen the warlock class.')
    print(warlock.bio)

    # Skill Proficiencies
    print("Choose 2 skills from the following list, which you will be proficient in:")
    for skill in displayed_warlock_skills:
        print(skill)
    print("Please enter your first skill choice:")
    skill_choice1 = input("> ")
    while skill_choice1.lower() not in warlock_skills:
        print("That is not a valid choice. Please choose from the list.")
        skill_choice1 = input("> ")
    print("Please enter your second skill choice:")
    skill_choice2 = input("> ")
    while skill_choice2.lower() not in warlock_skills:
        print("That is not a valid choice. Please choose from the list.")
        skill_choice2 = input("> ")
    selected_skill_proficiencies = [skill_choice1, skill_choice2]
    print(f"You have chosen {selected_skill_proficiencies[0]} and {selected_skill_proficiencies[1]} as your skill proficiencies.")
    warlock.skill_proficiencies = selected_skill_proficiencies

    # Starting Cantrips
    print("You have reached level 1 and can now choose 2 cantrips from the warlock spell list.")
    print("Please choose two cantrips from the following list:")
    for cantrip in displayed_warlock_cantrips:
        print(cantrip)
    print("Please enter your first cantrip choice:")
    cantrip_choice1 = input("> ")
    while cantrip_choice1.lower() not in warlock_cantrips:
        print("That is not a valid choice. Please choose from the list.")
        cantrip_choice1 = input("> ")
    print("Please enter your second cantrip choice:")
    cantrip_choice2 = input("> ")
    while cantrip_choice2.lower() not in warlock_cantrips:
        print("That is not a valid choice. Please choose from the list.")
        cantrip_choice2 = input("> ")
    selected_cantrips = [cantrip_choice1, cantrip_choice2]
    print(f"You have chosen {cantrip_choice1} and {cantrip_choice2} as your cantrips.")
    warlock.cantrips = selected_cantrips

    # Starting Spells
    print("You can now choose 2 spells from the warlock spell list.")
    print("Please choose two spells from the following list:")
    for spell in displayed_warlock_spells:
        print(spell)
    print("Please enter your first spell choice:")
    spell_choice1 = input("> ")
    while (spell_choice1.lower() not in warlock_spells) or (spell_choice1.lower() in warlock.spells):
        print("That is not a valid choice. Please choose from the list.")
        print("Hint: You should chose a spell that was not chosen as a cantrip.")
        print("Please enter your first spell choice:")
        spell_choice1 = input("> ")
    print("Please enter your second spell choice:")
    spell_choice2 = input("> ")
    while (spell_choice2.lower() not in warlock_spells) or (spell_choice2.lower() in warlock.spells):
        print("That is not a valid choice. Please choose from the list.")
        print("Hint: You should chose a spell that was not chosen as a cantrip.")
        print("Please enter your second spell choice:")
        spell_choice2 = input("> ")
    selected_spells = [spell_choice1, spell_choice2]
    print(f"You have chosen {selected_spells[0]} and {selected_spells[1]} as your spells.")
    warlock.spells = selected_spells

    # Starting Equipment
    equipment_choice_1 = starting_equipment.starting_equipment_choice("Light Crossbow and 20 Bolts", "Any Simple Weapon")
    if equipment_choice_1.lower() == "light crossbow and 20 bolts":
        starting_weapon = starting_equipment.starting_equipment("Light Crossbow")
        print(f"One {starting_weapon.name} has been added to your starting equipment.")
        warlock.starting_equipment.append(starting_weapon)
        # Add 20 bolts to starting equipment
    else:
        starting_weapon = starting_equipment.select_equipment_from_category("Simple Weapons")
        print(f"One {starting_weapon.name} has been added to your starting equipment.")
        warlock.starting_equipment.append(starting_weapon)
    
    equipment_choice_2 = starting_equipment.starting_equipment_choice("Component Pouch", "Arcane Focus")
    if equipment_choice_2.lower() == "component pouch":
        starting_equipment_choice = starting_equipment.starting_equipment("Component Pouch")
    else:
        starting_equipment_choice = starting_equipment.starting_equipment("Arcane Focus Crystal")
    print(f"One {starting_equipment_choice.name} has been added to your starting equipment.")
    warlock.starting_equipment.append(starting_equipment_choice)

    equipment_choice_3 = starting_equipment.starting_equipment_choice("Scholar's Pack", "Dungeoneer's Pack")
    if equipment_choice_3.lower() == "scholar's pack":
        pack_choice = starting_equipment.starting_equipment("Scholar's Pack")
    else:
        pack_choice = starting_equipment.starting_equipment("Dungeoneer's Pack")
    print(f"One {pack_choice.name} has been added to your starting equipment.")
    warlock.starting_equipment.append(pack_choice)

    equipment_choice_4 = starting_equipment.select_equipment_from_category("Simple Weapons")
    print(f"One {equipment_choice_4.name} has been added to your starting equipment.")
    warlock.starting_equipment.append(equipment_choice_4)

    leather_armor = starting_equipment.starting_equipment("Leather Light Armor")
    dagger = starting_equipment.starting_equipment("Dagger")
    print("Leather Armor and Two Daggers have been added to your starting equipment.")
    warlock.starting_equipment.append(leather_armor)
    warlock.starting_equipment.append(dagger)
    warlock.starting_equipment.append(dagger)

    return warlock
        


