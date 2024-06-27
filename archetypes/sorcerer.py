# We still need to create methods for sorcerers for the following:
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

displayed_sorcerer_skills, sorcerer_skills = skills.get_sorcerer_skills()
displayed_sorcerer_spells, sorcerer_spells = spells.get_sorcerer_spells()
displayed_sorcerer_cantrips, sorcerer_cantrips = cantrips.get_sorcerer_cantrips()
potential_starting_equipment = starting_equipment.get_starting_equipment("Sorcerer")

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

def define_sorcerer():
    sorcerer = Sorcerer()
    print(f'You have chosen the sorcerer class.')
    print(sorcerer.bio)

    # Skill Proficiencies
    print("Choose 2 skills from the following list, which you will be proficient in:")
    for skill in displayed_sorcerer_skills:
        print(skill)
    print("Please enter your first skill choice:")
    skill_choice1 = input("> ")
    while skill_choice1.lower() not in sorcerer_skills:
        print("That is not a valid choice. Please choose from the list.")
        skill_choice1 = input("> ")
    print("Please enter your second skill choice:")
    skill_choice2 = input("> ")
    while skill_choice2.lower() not in sorcerer_skills:
        print("That is not a valid choice. Please choose from the list.")
        skill_choice2 = input("> ")
    selected_skill_proficiencies = [skill_choice1, skill_choice2]
    print(f"You have chosen {selected_skill_proficiencies[0]} and {selected_skill_proficiencies[1]} as your skill proficiencies.")
    sorcerer.skill_proficiencies = selected_skill_proficiencies

    # Starting Cantrips
    print("You have reached level 1 and can now choose 4 cantrips from the sorcerer spell list.")
    print("Please choose four cantrips from the following list:")
    for cantrip in displayed_sorcerer_cantrips:
        print(cantrip)
    print("Please enter your first cantrip choice:")
    cantrip_choice1 = input("> ")
    while cantrip_choice1.lower() not in sorcerer_cantrips:
        print("That is not a valid choice. Please choose from the list.")
        cantrip_choice1 = input("> ")
    print("Please enter your second cantrip choice:")
    cantrip_choice2 = input("> ")
    while cantrip_choice2.lower() not in sorcerer_cantrips:
        print("That is not a valid choice. Please choose from the list.")
        cantrip_choice2 = input("> ")
    print("Please enter your third cantrip choice:")
    cantrip_choice3 = input("> ")
    while cantrip_choice3.lower() not in sorcerer_cantrips:
        print("That is not a valid choice. Please choose from the list.")
        cantrip_choice3 = input("> ")
    print("Please enter your fourth cantrip choice:")
    cantrip_choice4 = input("> ")
    while cantrip_choice4.lower() not in sorcerer_cantrips:
        print("That is not a valid choice. Please choose from the list.")
        cantrip_choice4 = input("> ")
    selected_cantrips = [cantrip_choice1, cantrip_choice2, cantrip_choice3, cantrip_choice4]
    print(f"You have chosen {cantrip_choice1}, {cantrip_choice2}, {cantrip_choice3}, and {cantrip_choice4} as your cantrips.")
    sorcerer.cantrips = selected_cantrips

    # Starting Spells
    print("You can now choose 2 spells from the sorcerer spell list.")
    print("Please choose two spells from the following list:")
    for spell in displayed_sorcerer_spells:
        print(spell)
    print("Please enter your first spell choice:")
    spell_choice1 = input("> ")
    while (spell_choice1.lower() not in sorcerer_spells) or (spell_choice1.lower() in sorcerer.spells):
        print("That is not a valid choice. Please choose from the list.")
        print("Hint: You should chose a spell that was not chosen as a cantrip.")
        print("Please enter your first spell choice:")
        spell_choice1 = input("> ")
    print("Please enter your second spell choice:")
    spell_choice2 = input("> ")
    while (spell_choice2.lower() not in sorcerer_spells) or (spell_choice2.lower() in sorcerer.spells):
        print("That is not a valid choice. Please choose from the list.")
        print("Hint: You should chose a spell that was not chosen as a cantrip.")
        print("Please enter your second spell choice:")
        spell_choice2 = input("> ")
    selected_spells = [spell_choice1, spell_choice2]
    print(f"You have chosen {selected_spells[0]} and {selected_spells[1]} as your spells.")
    sorcerer.spells = selected_spells

    # Starting Equipment
    equipment_choice_1 = starting_equipment.starting_equipment_choice("Light Crossbow and 20 Bolts", "Any Simple Weapon")
    if equipment_choice_1.lower() == "light crossbow and 20 bolts":
        weapon_choice = starting_equipment.starting_equipment("Light Crossbow")
        print(f"One {weapon_choice.name} has been added to your starting equipment.")
        sorcerer.starting_equipment.append(weapon_choice)
        # Add 20 bolts
    else:
        weapon_choice = starting_equipment.select_equipment_from_category("Simple Weapons")
        print(f"One {weapon_choice.name} has been added to your starting equipment.")
        sorcerer.starting_equipment.append(weapon_choice)

    equipment_choice_2 = starting_equipment.starting_equipment_choice("Component Pouch", "Arcane Focus")
    if equipment_choice_2.lower() == "component pouch":
        equipment_choice = starting_equipment.starting_equipment("Component Pouch")
    else:
        equipment_choice = starting_equipment.starting_equipment("Arcane Focus")
    print(f"One {equipment_choice.name} has been added to your starting equipment.")
    sorcerer.starting_equipment.append(equipment_choice)

    equipment_choice_3 = starting_equipment.starting_equipment_choice("Dungeoneer's Pack", "Explorer's Pack")
    if equipment_choice_3.lower() == "dungeoneer's pack":
        pack_choice = starting_equipment.starting_equipment("Dungeoneer's Pack")
    else:
        pack_choice = starting_equipment.starting_equipment("Explorer's Pack")
    print(f"One {pack_choice.name} has been added to your starting equipment.")
    sorcerer.starting_equipment.append(pack_choice)

    dagger = starting_equipment.starting_equipment("Dagger")
    print("2 Daggers have been added to your starting equipment.")
    sorcerer.starting_equipment.append(dagger)
    sorcerer.starting_equipment.append(dagger)

    return sorcerer
        


