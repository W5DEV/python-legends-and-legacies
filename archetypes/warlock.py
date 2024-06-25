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

import modules.equipment as equipment
import modules.instruments as instruments

displayed_warlock_spells = ["Charm Person", "Comprehend Languages", "Expeditious Retreat", "Hellish Rebuke", "Illusory Script", "Protection from Evil and Good", "Unseen Servant"]
warlock_spells = ["charm person", "comprehend languages", "expeditious retreat", "hellish rebuke", "illusory script", "protection from evil and good", "unseen servant"]
displayed_warlock_cantrips = ["Chill Touch", "Eldrich Blast", "Mage Hand", "Minor Illusion", "Poison Spray", "Prestidigitation", "True Strike"]
warlock_cantrips = ["chill touch", "eldrich blast", "mage hand", "minor illusion", "poison spray", "prestidigitation", "true strike"]

potential_starting_equipment = ["A Light Crossbow and 20 Bolts or Any Simple Weapon", "A Component Pouch or an Arcane Focus", "A Dungeoneer's Pack or a Scholar's Pack", "Leather Armor, Any Simple Weapon, and Two Daggers"]

displayed_warlock_skills = ["Arcana", "Deception", "History", "Intimidation", "Investigation", "Nature", "Religion"]
warlock_skills = ["arcana", "deception", "history", "intimidation", "investigation", "nature", "religion"]

def display_warlock_spells():
    for spell in displayed_warlock_spells:
        print(spell)

class Warlock:
    def __init__(self):
        name = "Warlock"
        bio = "A wielder of magic that is derived from a bargain with an extraplanar entity"
        hit_die = "8 for first level, then 1d8 (or 5, whichever is higher) per level after 1 + your Constitution modifier"
        primary_ability = "Charisma"
        saving_throw_proficiencies = "Wisdom, Charisma"
        armor_proficiencies = "Light Armor"
        weapon_proficiencies = "Simple Weapons"
        tool_proficiencies = "None"
        self.name = name
        self.bio = bio
        self.hit_die = hit_die
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
        print(f"Skill Proficiencies: {self.skill_proficiencies}")
        print(f"Starting Equipment: {self.starting_equipment}")
        print(f"Special Abilities: {self.special_abilities}")
        return self
    
    def sync_level(self, level):
        if level >= 1:
            self.otherworldly_patrons = "The Fiend"
            self.special_abilities.append("Fiend Expanded Spells Level 1")
            self.special_abilities.append("Pact Magic")
            self.special_abilities.append("Dark One's Blessing")
        if level >= 2:
            self.special_abilities.append("Eldritch Invocations")
            self.special_abilities.append("Fiend Expanded Spells Level 2")
        if level >= 3:
            self.special_abilities.append("Pact Boom")
            self.special_abilities.append("Fiend Expanded Spells Level 3")
        if level >= 4:
            self.special_abilities.append("Ability Score Improvement 4th Level")
            self.special_abilities.append("Fiend Expanded Spells Level 4")
        if level >= 5:
            self.special_abilities.append("Fiend Expanded Spells Level 5")
        if level >= 6:
            self.special_abilities.append("Dark One's Own Luck")
        if level >= 7:
            pass
        if level >= 8:
            self.special_abilities.append("Ability Score Improvement 8th Level")
        if level >= 9:
            pass
        if level >= 10:
            self.special_abilities.append("Fiendish Resilience")
        if level >= 11:
            self.special_abilities.append("Mystic Arcanum 6th Level")
        if level >= 12:
            self.special_abilities.append("Ability Score Improvement 12th Level")
        if level >= 13:
            self.special_abilities.append("Mystic Arcanum 7th Level")
        if level >= 14:
            self.special_abilities.append("Hurl Through Hell")
        if level >= 15:
            self.special_abilities.append("Mystic Arcanum 8th Level")
        if level >= 16:
            self.special_abilities.append("Ability Score Improvement 16th Level")
        if level >= 17:
            self.special_abilities.append("Mythic Arcanum 9th Level")
        if level >= 18:
            pass
        if level >= 19:
            self.special_abilities.append("Ability Score Improvement 19th Level")
        if level >= 20:
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
    equipment_choice1 = ""
    equipment_choice2 = ""
    equipment_choice3 = ""
    print("Choose your starting equipment:")
    for item in potential_starting_equipment:
        print(item)

    print("Please enter your choice of a 'Light Crossbow and 20 Bolts' or 'any Simple Weapon':")
    equipment_choice1 = input("> ")
    while equipment_choice1.lower() not in ["light crossbow and 20 bolts", "any simple weapon"]:
        print("That is not a valid choice. Please choose from the list.")
        equipment_choice1 = input("> ")
    if equipment_choice1.lower() == "light crossbow and 20 bolts":
        print("You have chosen a Light Crossbow and 20 Bolts.")
        print("A Light Crossbow and 20 Bolts has been added to your starting equipment.")
        warlock.starting_equipment.append(equipment.light_crossbow)
    else:
        for weapon in equipment.simple_weapons:
            print(weapon.name)
        print("Please enter your choice of simple weapon:")
        weapon_choice = input("> ")
        while weapon_choice.lower() not in [weapon.name.lower() for weapon in equipment.simple_weapons]:
            print("That is not a valid choice. Please choose from the list.")
            weapon_choice = input("> ")
        for weapon in equipment.simple_weapons:
            if weapon_choice.lower() == weapon.name.lower():
                print(f"You have chosen {weapon.name}.")
                print(f"{weapon.name} has been added to your starting equipment.")
                warlock.starting_equipment.append(weapon)
                break

    print("Please enter your choice of a 'Component Pouch' or an 'Arcane Focus':")
    equipment_choice2 = input("> ")
    while equipment_choice2.lower() not in ["component pouch", "arcane focus"]:
        print("That is not a valid choice. Please choose from the list.")
        equipment_choice2 = input("> ")
    if equipment_choice2.lower() == "component pouch":
        print("You have chosen a Component Pouch.")
        print("A Component Pouch has been added to your starting equipment.")
        warlock.starting_equipment.append(equipment.component_pouch)
    elif equipment_choice2.lower() == "arcane focus":
        print("You have chosen an Arcane Focus.")
        print("An Arcane Focus has been added to your starting equipment.")
        warlock.starting_equipment.append(equipment.arcane_focus_crystal)

    print("Please enter your choice of a 'Dungeoneer's Pack' or an 'Scholar's Pack':")
    equipment_choice3 = input("> ")
    while equipment_choice3.lower() not in ["dungeoneer's pack", "scholar's pack"]:
        print("That is not a valid choice. Please choose from the list.")
        equipment_choice3 = input("> ")
    if equipment_choice3.lower() == "dungeoneer's pack":
        print("You have chosen a Dungeoneer's Pack.")
        print("A Dungeoneer's Pack has been added to your starting equipment.")
        warlock.starting_equipment.append(equipment.dungeoneers_pack)
    elif equipment_choice3.lower() == "scholar's pack":
        print("You have chosen an Scholar's Pack.")
        print("An Scholar's Pack has been added to your starting equipment.")
        warlock.starting_equipment.append(equipment.scholars_pack)

    print("You may also choose any Simple Weapon as part of your starting equipment.")
    print("Please enter your choice of simple weapon from the list below:")
    valid_weapon_choices = []
    for weapon in equipment.simple_weapons:
        valid_weapon_choices.append(weapon.name.lower())
        print(weapon.name)
    weapon_choice = input("> ")
    while weapon_choice.lower() not in valid_weapon_choices:
        print("That is not a valid choice. Please choose from the list.")
        weapon_choice = input("> ")
    for weapon in equipment.simple_weapons:
        if weapon_choice.lower() == weapon.name.lower():
            print(f"You have chosen {weapon.name}.")
            print(f"{weapon.name} has been added to your starting equipment.")
            warlock.starting_equipment.append(weapon)
            break

    print("You also start with Leather Armor and Two Daggers.")
    print("Leather Armor has been added to your starting equipment.")
    warlock.starting_equipment.append(equipment.leather_light_armor)
    print("Two Daggers have been added to your starting equipment.")
    warlock.starting_equipment.append(equipment.dagger)
    warlock.starting_equipment.append(equipment.dagger)
    
    print(f"You have chosen the following starting equipment:")
    for item in warlock.starting_equipment:
        print(item.name)

    return warlock
        


