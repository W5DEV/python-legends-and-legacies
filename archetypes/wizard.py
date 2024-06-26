# We still need to create methods for wizards for the following:
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

displayed_wizard_skills, wizard_skills = skills.get_wizard_skills()
displayed_wizard_spells, wizard_spells = spells.get_wizard_spells()
displayed_wizard_cantrips, wizard_cantrips = cantrips.get_wizard_cantrips()
potential_starting_equipment = starting_equipment.get_starting_equipment("Wizard")

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
        if level >= 1:
            self.special_abilities.append("Spellcasting")
            self.special_abilities.append("Arcane Recovery")
        if level >= 2:
            self.arcane_tradition = "School of Evocation"
            self.special_abilities.append("Evocation Savant")
            self.special_abilities.append("Sculpt Spells")
            self.spell_slots_level_1 = 3
        if level >= 3:
            self.spell_slots_level_1 = 4
            self.spell_slots_level_2 = 2
        if level >= 4:
            self.special_abilities.append("Ability Score Improvement 4th Level")
            self.cantrips_known = 4
            self.spell_slots_level_2 = 3
        if level >= 5:
            self.spell_slots_level_3 = 2
        if level >= 6:
            self.special_abilities.append("Potent Cantrip")
            self.spell_slots_level_3 = 3
        if level >= 7:
            self.spell_slots_level_4 = 1
        if level >= 8:
            self.special_abilities.append("Ability Score Improvement 8th Level")
            self.spell_slots_level_4 = 2
        if level >= 9:
            self.spell_slots_level_4 = 3
            self.spell_slots_level_5 = 1
        if level >= 10:
            self.special_abilities.append("Empowered Evocation")
            self.cantrips_known = 5
            self.spell_slots_level_5 = 2
        if level >= 11:
            self.spell_slots_level_6 = 1
        if level >= 12:
            self.special_abilities.append("Ability Score Improvement 12th Level")
        if level >= 13:
            self.spell_slots_level_7 = 1
        if level >= 14:
            self.special_abilities.append("Overchannel")
        if level >= 15:
            self.spell_slots_level_8 = 1
        if level >= 16:
            self.special_abilities.append("Ability Score Improvement 16th Level")
        if level >= 17:
            self.spell_slots_level_9 = 1
        if level >= 18:
            self.special_abilities.append("Spell Mastery")
            self.spell_slots_level_5 = 3
        if level >= 19:
            self.special_abilities.append("Ability Score Improvement 19th Level")
            self.spell_slots_level_6 = 2
        if level >= 20:
            self.special_abilities.append("Signature Spells")
            self.spell_slots_level_7 = 2

def define_wizard():
    wizard = Wizard()
    print(f'You have chosen the wizard class.')
    print(wizard.bio)

    # Skill Proficiencies
    print("Choose 2 skills from the following list, which you will be proficient in:")
    for skill in displayed_wizard_skills:
        print(skill)
    print("Please enter your first skill choice:")
    skill_choice1 = input("> ")
    while skill_choice1.lower() not in wizard_skills:
        print("That is not a valid choice. Please choose from the list.")
        skill_choice1 = input("> ")
    print("Please enter your second skill choice:")
    skill_choice2 = input("> ")
    while skill_choice2.lower() not in wizard_skills:
        print("That is not a valid choice. Please choose from the list.")
        skill_choice2 = input("> ")
    selected_skill_proficiencies = [skill_choice1, skill_choice2]
    print(f"You have chosen {selected_skill_proficiencies[0]} and {selected_skill_proficiencies[1]} as your skill proficiencies.")
    wizard.skill_proficiencies = selected_skill_proficiencies

    # Starting Cantrips
    print("You have reached level 1 and can now choose 3 cantrips from the wizard spell list.")
    print("Please choose three cantrips from the following list:")
    for cantrip in displayed_wizard_cantrips:
        print(cantrip)
    print("Please enter your first cantrip choice:")
    cantrip_choice1 = input("> ")
    while cantrip_choice1.lower() not in wizard_cantrips:
        print("That is not a valid choice. Please choose from the list.")
        cantrip_choice1 = input("> ")
    print("Please enter your second cantrip choice:")
    cantrip_choice2 = input("> ")
    while cantrip_choice2.lower() not in wizard_cantrips:
        print("That is not a valid choice. Please choose from the list.")
        cantrip_choice2 = input("> ")
    print("Please enter your third cantrip choice:")
    cantrip_choice3 = input("> ")
    while cantrip_choice3.lower() not in wizard_cantrips:
        print("That is not a valid choice. Please choose from the list.")
        cantrip_choice3 = input("> ")
    selected_cantrips = [cantrip_choice1, cantrip_choice2, cantrip_choice3]
    print(f"You have chosen {cantrip_choice1}, {cantrip_choice2} and {cantrip_choice3} as your cantrips.")
    wizard.cantrips = selected_cantrips

    # Starting Spells
    print("You can now choose 2 spells from the wizard spell list.")
    print("Please choose two spells from the following list:")
    for spell in displayed_wizard_spells:
        print(spell)
    print("Please enter your first spell choice:")
    spell_choice1 = input("> ")
    while (spell_choice1.lower() not in wizard_spells) or (spell_choice1.lower() in wizard.spells):
        print("That is not a valid choice. Please choose from the list.")
        print("Hint: You should chose a spell that was not chosen as a cantrip.")
        print("Please enter your first spell choice:")
        spell_choice1 = input("> ")
    print("Please enter your second spell choice:")
    spell_choice2 = input("> ")
    while (spell_choice2.lower() not in wizard_spells) or (spell_choice2.lower() in wizard.spells):
        print("That is not a valid choice. Please choose from the list.")
        print("Hint: You should chose a spell that was not chosen as a cantrip.")
        print("Please enter your second spell choice:")
        spell_choice2 = input("> ")
    selected_spells = [spell_choice1, spell_choice2]
    print(f"You have chosen {selected_spells[0]} and {selected_spells[1]} as your spells.")
    wizard.spells = selected_spells

    # Starting Equipment
    equipment_choice_1 = starting_equipment.starting_equipment_choice("Quarterstaff", "Dagger")
    if equipment_choice_1.lower() == "quarterstaff":
        weapon_choice = starting_equipment.starting_equipment("Quarterstaff")
    else:
        weapon_choice = starting_equipment.starting_equipment("Dagger")
    print(f"One {weapon_choice.name} has been added to your starting equipment.")
    wizard.starting_equipment.append(weapon_choice)

    equipment_choice_2 = starting_equipment.starting_equipment_choice("Component Pouch", "Arcane Focus")
    if equipment_choice_2.lower() == "component pouch":
        focus_choice = starting_equipment.starting_equipment("Component Pouch")
    else:
        focus_choice = starting_equipment.starting_equipment("Arcane Focus")
    print(f"One {focus_choice.name} has been added to your starting equipment.")
    wizard.starting_equipment.append(focus_choice)

    equipment_choice_3 = starting_equipment.starting_equipment_choice("Scholar's Pack", "Explorer's Pack")
    if equipment_choice_3.lower() == "scholar's pack":
        pack_choice = starting_equipment.starting_equipment("Scholar's Pack")
    else:
        pack_choice = starting_equipment.starting_equipment("Explorer's Pack")
    print(f"One {pack_choice.name} has been added to your starting equipment.")
    wizard.starting_equipment.append(pack_choice)

    spellbook = starting_equipment.starting_equipment("Spellbook")
    print("A Spellbook has been added to your starting equipment.")
    wizard.starting_equipment.append(spellbook)
    
    return wizard
        


