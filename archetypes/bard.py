# We still need to create methods for Bards for the following:
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
import modules.instruments as instruments

displayed_bard_skills, bard_skills = skills.get_bard_skills()
displayed_bard_spells, bard_spells = spells.get_bard_spells()
displayed_bard_cantrips, bard_cantrips = cantrips.get_bard_cantrips()
potential_starting_equipment = starting_equipment.get_starting_equipment("Bard")

class Bard:
    def __init__(self):
        name = "Bard"
        bio = "An inspiring magician whose power echoes the music of creation."
        hit_die = "1d8"
        primary_ability = "Charisma"
        saving_throw_proficiencies = "Dexterity, Charisma"
        armor_proficiencies = "Light Armor"
        weapon_proficiencies = "Simple Weapons, Hand Crossbows, Longswords, Rapiers, Shortswords"
        tool_proficiencies = "Three musical instruments of your choice"
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
        self.instrument_proficiencies = []
        self.starting_equipment = []
        self.special_abilities = []
        self.college = ""
        self.cantrips = []
        self.spells = []
        self.expertise = []
        self.bard_spells = []
        self.cantrips_known = 2
        self.spells_known = 4
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
            self.special_abilities.append("Bardic Inspiration (d6)")
        if level == 2:
            self.special_abilities.append("Jack of All Trades")
            self.special_abilities.append("Song of Rest (d6)")
            self.spell_slots_level_1 = 3
            self.spells_known = 5
        if level == 3:
            print("You have reached level 3 and can now choose two skills to gain expertise in.")
            print("Please choose two skills from the following list:")
            for skill in self.skill_proficiencies:
                print(skill)
            print("Please enter your first skill choice:")
            expertise_choice1 = input("> ")
            self.expertise.append(expertise_choice1)
            print("Please enter your second skill choice:")
            expertise_choice2 = input("> ")
            self.expertise.append(expertise_choice2)
            print("You have reached level 3 and can now enter a Bard College.")
            self.college = "College of Lore"
            self.special_abilities.append("Cutting Words")
            self.spells_known = 6
            self.spell_slots_level_1 = 4
            self.spell_slots_level_2 = 2
        if level == 4:
            self.special_abilities.append("Ability Score Improvement 4th Level")
            player.increase_ability_score(2)
            self.spells_known = 7
            self.spell_slots_level_2 = 3
        if level == 5:
            self.special_abilities.append("Bardic Inspiration (d8)")
            self.special_abilities.append("Font of Inspiration")
            self.spells_known = 8
            self.spell_slots_level_3 = 2
        if level == 6:
            self.special_abilities.append("Countercharm")
            self.special_abilities.append("Additional Magical Secrets")
            self.spells_known = 9
            self.spell_slots_level_3 = 3
        if level == 7:
            self.spells_known = 10
            self.spell_slots_level_4 = 1
        if level == 8:
            self.special_abilities.append("Ability Score Improvement 8th Level")
            player.increase_ability_score(2)
            self.spells_known = 11
            self.spell_slots_level_4 = 2
        if level == 9:
            self.special_abilities.append("Song of Rest (d8)")
            self.spells_known = 12
            self.spell_slots_level_4 = 3
            self.spell_slots_level_5 = 1
        if level == 10:
            self.special_abilities.append("Bardic Inspiration (d10)")
            print("You have reached level 10 and can now choose two skills to gain expertise in.")
            print("Please choose two skills from the following list:")
            for skill in self.skill_proficiencies:
                print(skill) 
            print("Please enter your first skill choice:")
            expertise_choice1 = input("> ")
            self.expertise.append(expertise_choice1)
            print("Please enter your second skill choice:")
            expertise_choice2 = input("> ")
            self.expertise.append(expertise_choice2)
            print("You have reached level 10 and can choose two spells or cantrips to count as bard spells.")
            print("Please choose two spells from the bard table below.")
            print("Insert spell table here.")
            print("Please enter your first spell choice:")
            bard_spell_choice1 = input("> ")
            self.bard_spells.append(bard_spell_choice1)
            print("Please enter your second spell choice:")
            bard_spell_choice2 = input("> ")
            self.bard_spells.append(bard_spell_choice2)
            self.spells_known = 14
            self.spell_slots_level_5 = 2
        if level == 11:
            self.spells_known = 15
            self.spell_slots_level_6 = 1
        if level == 12:
            self.special_abilities.append("Ability Score Improvement 12th Level")
            player.increase_ability_score(2)
        if level == 13:
            self.special_abilities.append("Song of Rest (d10)")
            self.spells_known = 16
            self.spell_slots_level_7 = 1
        if level == 14:
            print("You have reached level 14 and can choose two spells or cantrips to count as bard spells.")
            print("Please choose two spells from the bard table below.")
            print("Insert spell table here.")
            print("Please enter your first spell choice:")
            bard_spell_choice1 = input("> ")
            self.bard_spells.append(bard_spell_choice1)
            print("Please enter your second spell choice:")
            bard_spell_choice2 = input("> ")
            self.bard_spells.append(bard_spell_choice2)
            self.special_abilities.append("Peerless Skill")
            self.spells_known = 18
        if level == 15:
            self.special_abilities.append("Bardic Inspiration (d12)")
            self.spells_known = 19
            self.spell_slots_level_8 = 1
        if level == 16:
            self.special_abilities.append("Ability Score Improvement 16th Level")
            player.increase_ability_score(2)
        if level == 17:
            self.special_abilities.append("Song of Rest (d12)")
            self.spells_known = 20
            self.spell_slots_level_9 = 1
        if level == 18:
            print("You have reached level 18 and can choose two spells or cantrips to count as bard spells.")
            print("Please choose two spells from the bard table below.")
            print("Insert spell table here.")
            print("Please enter your first spell choice:")
            bard_spell_choice1 = input("> ")
            self.bard_spells.append(bard_spell_choice1)
            print("Please enter your second spell choice:")
            bard_spell_choice2 = input("> ")
            self.bard_spells.append(bard_spell_choice2)
            self.spells_known = 22
            self.spell_slots_level_5 = 3
        if level == 19:
            self.special_abilities.append("Ability Score Improvement 19th Level")
            player.increase_ability_score(2)
            self.spell_slots_level_6 = 2
        if level == 20:
            self.special_abilities.append("Superior Inspiration")
            self.spell_slots_level_7 = 2
        print(f"Special Abilities for level {level}:")
        i = 1
        for ability in self.special_abilities:
            print(f"{i}: {ability}")
            i += 1
        return self

def define_bard():
    bard = Bard()
    print(f'You have chosen the Bard class.')
    print(bard.bio)

    # Skill Proficiencies
    print("Choose 3 skills from the following list, which you will be proficient in:")
    for skill in displayed_bard_skills:
        print(skill)
    print("Please enter your first skill choice:")
    skill_choice1 = input("> ")
    while skill_choice1.lower() not in bard_skills:
        print("That is not a valid choice. Please choose from the list.")
        skill_choice1 = input("> ")
    print("Please enter your second skill choice:")
    skill_choice2 = input("> ")
    while skill_choice2.lower() not in bard_skills:
        print("That is not a valid choice. Please choose from the list.")
        skill_choice2 = input("> ")
    print("Please enter your third skill choice:")
    skill_choice3 = input("> ")
    while skill_choice3.lower() not in bard_skills:
        print("That is not a valid choice. Please choose from the list.")
        skill_choice3 = input("> ")
    selected_skill_proficiencies = [skill_choice1, skill_choice2, skill_choice3]
    print(f"You have chosen {selected_skill_proficiencies[0]}, {selected_skill_proficiencies[1]}, and {selected_skill_proficiencies[2]} as your skill proficiencies.")
    bard.skill_proficiencies = selected_skill_proficiencies

    # Instrument Proficiencies
    print("Choose 3 musical instruments from the following list, which you will be proficient in:")
    instruments.display_instruments()
    print("Please enter your first instrument choice:")
    instrument_choice1 = input("> ")
    while instrument_choice1.lower() not in instruments.instruments:
        print("That is not a valid choice. Please choose from the list.")
        instrument_choice1 = input("> ")
    print("Please enter your second instrument choice:")
    instrument_choice2 = input("> ")
    while instrument_choice2.lower() not in instruments.instruments:
        print("That is not a valid choice. Please choose from the list.")
        instrument_choice2 = input("> ")
    print("Please enter your third instrument choice:")
    instrument_choice3 = input("> ")
    while instrument_choice3.lower() not in instruments.instruments:
        print("That is not a valid choice. Please choose from the list.")
        instrument_choice3 = input("> ")
    selected_instrument_proficiencies = [instrument_choice1, instrument_choice2, instrument_choice3]    
    print(f"You have chosen {selected_instrument_proficiencies[0]}, {selected_instrument_proficiencies[1]}, and {selected_instrument_proficiencies[2]} as your instrument proficiencies.")
    bard.instrument_proficiencies = selected_instrument_proficiencies
    
    # Starting Equipment
    equipment_choice_1 = starting_equipment.starting_equipment_choice_three("Rapier", "Longsword", "Any Other Simple Weapon")
    if equipment_choice_1.lower() == "rapier":
        starting_weapon = starting_equipment.starting_equipment("Rapier")
    elif equipment_choice_1.lower() == "longsword":
        starting_weapon = starting_equipment.starting_equipment("Longsword")
    else:
        starting_weapon = starting_equipment.select_equipment_from_category("Simple Weapons")
    print(f"One {starting_weapon.name} has been added to your starting equipment.")
    bard.starting_equipment.append(starting_weapon)

    equipment_choice_2 = starting_equipment.starting_equipment_choice("Diplomat's Pack", "Entertainer's Pack")
    if equipment_choice_2.lower() == "diplomat's pack":
        starting_pack = starting_equipment.starting_equipment("Diplomat's Pack")
    else:
        starting_pack = starting_equipment.starting_equipment("Entertainer's Pack")
    print(f"One {starting_pack.name} has been added to your starting equipment.")
    bard.starting_equipment.append(starting_pack)

    equipment_choice_3 = starting_equipment.starting_equipment_choice("Lute", "Any Other Musical Instrument")
    if equipment_choice_3.lower() == "lute":
        starting_instrument = starting_equipment.starting_equipment("Lute")
    else:
        starting_instrument = starting_equipment.select_equipment_from_category("Musical Instruments")
    print(f"One {starting_instrument.name} has been added to your starting equipment.")
    bard.starting_equipment.append(starting_instrument)

    leather_armor = starting_equipment.starting_equipment("Leather Light Armor")
    dagger = starting_equipment.starting_equipment("Dagger")
    print(f"Leather Armor and One Dagger has been added to your starting equipment.")
    bard.starting_equipment.append(leather_armor)
    bard.starting_equipment.append(dagger)

    # Starting Cantrips
    print("You have reached level 1 and can now choose 2 cantrips from the bard spell list.")
    print("Please choose two cantrips from the following list:")
    for cantrip in displayed_bard_cantrips:
        print(cantrip)
    print("Please enter your first cantrip choice:")
    cantrip_choice1 = input("> ")
    while cantrip_choice1.lower() not in bard_cantrips:
        print("That is not a valid choice. Please choose from the list.")
        cantrip_choice1 = input("> ")
    print("Please enter your second cantrip choice:")
    cantrip_choice2 = input("> ")
    while cantrip_choice2.lower() not in bard_cantrips:
        print("That is not a valid choice. Please choose from the list.")
        cantrip_choice2 = input("> ")
    selected_cantrips = [cantrip_choice1, cantrip_choice2]
    print(f"You have chosen {selected_cantrips[0]} and {selected_cantrips[1]} as your cantrips.")
    bard.cantrips = selected_cantrips

    # Starting Spells
    print("You have reached level 1 and can now choose 4 spells from the bard spell list.")
    print("Please choose four spells from the following list:")
    for spell in displayed_bard_spells:
        print(spell)
    print("Please enter your first spell choice:")
    spell_choice1 = input("> ")
    while (spell_choice1.lower() not in bard_spells) or (spell_choice1.lower() in bard.cantrips):
        print("That is not a valid choice. Please choose from the list.")
        print("Hint: You should chose a spell that was not chosen as a cantrip.")
        print("Please enter your first spell choice:")
        spell_choice1 = input("> ")
    print("Please enter your second spell choice:")
    spell_choice2 = input("> ")
    while (spell_choice2.lower() not in bard_spells) or (spell_choice2.lower() in bard.cantrips):
        print("That is not a valid choice. Please choose from the list.")
        print("Hint: You should chose a spell that was not chosen as a cantrip.")
        print("Please enter your second spell choice:")
        spell_choice2 = input("> ")
    print("Please enter your third spell choice:")
    spell_choice3 = input("> ")
    while (spell_choice3.lower() not in bard_spells) or (spell_choice3.lower() in bard.cantrips):
        print("That is not a valid choice. Please choose from the list.")
        print("Hint: You should chose a spell that was not chosen as a cantrip.")
        print("Please enter your third spell choice:")
        spell_choice3 = input("> ")
    print("Please enter your fourth spell choice:")
    spell_choice4 = input("> ")
    while (spell_choice4.lower() not in bard_spells) or (spell_choice4.lower() in bard.cantrips):
        print("That is not a valid choice. Please choose from the list.")
        print("Hint: You should chose a spell that was not chosen as a cantrip.")
        print("Please enter your fourth spell choice:")
        spell_choice4 = input("> ")
    selected_spells = [spell_choice1, spell_choice2, spell_choice3, spell_choice4]
    print(f"You have chosen {selected_spells[0]}, {selected_spells[1]}, {selected_spells[2]}, and {selected_spells[3]} as your spells.")
    bard.spells = selected_spells

    return bard
        


