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

import modules.equipment as equipment
import modules.skills as skills
import modules.instruments as instruments

displayed_bard_spells = ["Animal Friendship", "Bane", "Charm Person", "Comprehend Languages", "Cure Wounds", "Detect Magic", "Disguise Self", "Faerie Fire", "Feather Fall", "Healing Word", "Heroism", "Hideous Laughter", "Identify", "Illusory Script", "Longstrider", "Silent Image", "Sleep", "Speak with Animals", "Thunderwave", "Unseen Servant"]
bard_spells = ["animal friendship", "bane", "charm person", "comprehend languages", "cure wounds", "detect magic", "disguise self", "faerie fire", "feather fall", "healing word", "heroism", "hideous laughter", "identify", "illusory script", "longstrider", "silent image", "sleep", "speak with animals", "thunderwave", "unseen servant"]

def display_bard_spells():
    for spell in displayed_bard_spells:
        print(spell)

class Bard:
    def __init__(self):
        name = "Bard"
        description = "An inspiring magician whose power echoes the music of creation."
        hit_die = "1d8 for first level, then 1d8 (or 5, whichever is higher) per level after 1 + your Constitution modifier"
        primary_ability = "Charisma"
        saving_throw_proficiencies = ["Dexterity", "Charisma"]
        armor_proficiencies = ["Light Armor"]
        weapon_proficiencies = "Simple Weapons, Hand Crossbows, Longswords, Rapiers, Shortswords"
        tool_proficiencies = "Three musical instruments of your choice"
        skill_proficiencies = []
        potential_starting_equipment = ["a rapier, a longsword, or any simple weapon", "a diplomat's pack or an entertainer's pack", "a lute or any other musical instrument", "Lether Armor", "Dagger"]
        special_abilities = []
        self.name = name
        self.description = description
        self.hit_die = hit_die
        self.primary_ability = primary_ability
        self.saving_throw_proficiencies = saving_throw_proficiencies
        self.armor_proficiencies = armor_proficiencies
        self.weapon_proficiencies = weapon_proficiencies
        self.tool_proficiencies = tool_proficiencies
        self.skill_proficiencies = skill_proficiencies
        self.instrument_proficiencies = []
        self.potential_starting_equipment = potential_starting_equipment
        self.starting_equipment = []
        self.special_abilities = special_abilities
        self.college = ""
        self.cantrips = []
        self.spells = []
        self.expertise = []
        self.bard_spells = []
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
        print(f"The {self.name}: {self.description}")
        print(f"Hit Die: {self.hit_die}")
        print(f"Primary Ability: {self.primary_ability}")
        print(f"Saving Throw Proficiencies: {self.saving_throw_proficiencies}")
        print(f"Armor Proficiencies: {self.armor_proficiencies}")
        print(f"Weapon Proficiencies: {self.weapon_proficiencies}")
        print(f"Tool Proficiencies: {self.tool_proficiencies}")
        print(f"Skill Proficiencies: {self.displayed_skill_proficiencies}")
        print(f"Starting Equipment: {self.potential_starting_equipment}")
        print(f"Special Abilities: {self.special_abilities}")
        return self
    
    def update_special_abilities(self, level):
        if level >= 1:
            self.special_abilities.append("Spellcasting")
            self.special_abilities.append("Bardic Inspiration (d6)")
        if level >= 2:
            self.special_abilities.append("Jack of All Trades")
            self.special_abilities.append("Song of Rest (d6)")
        if level >= 3:
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
        if level >= 4:
            self.special_abilities.append("Ability Score Improvement 4th Level")
        if level >= 5:
            self.special_abilities.append("Bardic Inspiration (d8)")
            self.special_abilities.append("Font of Inspiration")
        if level >= 6:
            self.special_abilities.append("Countercharm")
            self.special_abilities.append("Additional Magical Secrets")
        if level >= 8:
            self.special_abilities.append("Ability Score Improvement 8th Level")
        if level >= 9:
            self.special_abilities.append("Song of Rest (d8)")
        if level >= 10:
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
        if level >= 12:
            self.special_abilities.append("Ability Score Improvement 12th Level")
        if level >= 13:
            self.special_abilities.append("Song of Rest (d10)")
        if level >= 14:
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
        if level >= 15:
            self.special_abilities.append("Bardic Inspiration (d12)")
        if level >= 16:
            self.special_abilities.append("Ability Score Improvement 16th Level")
        if level >= 17:
            self.special_abilities.append("Song of Rest (d12)")
        if level >= 18:
            print("You have reached level 18 and can choose two spells or cantrips to count as bard spells.")
            print("Please choose two spells from the bard table below.")
            print("Insert spell table here.")
            print("Please enter your first spell choice:")
            bard_spell_choice1 = input("> ")
            self.bard_spells.append(bard_spell_choice1)
            print("Please enter your second spell choice:")
            bard_spell_choice2 = input("> ")
            self.bard_spells.append(bard_spell_choice2)
        if level >= 19:
            self.special_abilities.append("Ability Score Improvement 19th Level")
        if level >= 20:
            self.special_abilities.append("Superior Inspiration")
        print(f"Special Abilities for level {level}:")
        i = 1
        for ability in self.special_abilities:
            print(f"{i}: {ability}")
            i += 1
        return self

def define_bard():
    bard = Bard()
    print(f'You have chosen the Bard class.')
    print(bard.description)

    # Skill Proficiencies
    print("Choose 3 skills from the following list, which you will be proficient in:")
    for skill in skills.displayed_skills:
        print(skill)
    print("Please enter your first skill choice:")
    skill_choice1 = input("> ")
    while skill_choice1.lower() not in skills.skills:
        print("That is not a valid choice. Please choose from the list.")
        skill_choice1 = input("> ")
    print("Please enter your second skill choice:")
    skill_choice2 = input("> ")
    while skill_choice2.lower() not in skills.skills:
        print("That is not a valid choice. Please choose from the list.")
        skill_choice2 = input("> ")
    print("Please enter your third skill choice:")
    skill_choice3 = input("> ")
    while skill_choice3.lower() not in skills.skills:
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
    first_weapon = ""
    second_weapon = ""
    print(f"Bard's are able to choose between a few different starting equipment options.")
    print(f'You will start with the following equipment: {bard.starting_equipment}')
    print("Would you like to start with a Rapier, Longsword, or any other simple weapon?")
    print("Please enter your either 'Rapier' or 'Longsword', 'Other Simple Weapon':")
    first_weapon_preference = input("> ")
    while first_weapon_preference.lower() not in ["rapier", "longsword", "other simple weapon"]:
        print("That is not a valid choice. Please choose from the list.")
        first_weapon_preference = input("> ")
    if first_weapon_preference.lower() == "rapier":
        first_weapon = equipment.rapier
    elif first_weapon_preference.lower() == "longsword":
        first_weapon = equipment.long_sword
    else:
        print("Please choose a simple weapon from the following list:")
        valid_weapons = []
        for weapon in equipment.simple_weapons:
            valid_weapons.append(weapon.name.lower())
            print(weapon.name)
        first_weapon_choice = input("> ")
        while first_weapon_choice.lower() not in valid_weapons:
            print("That is not a valid choice. Please choose from the list.")
            first_weapon_choice = input("> ")
        for weapon in equipment.simple_weapons:
            if first_weapon_choice.lower() == weapon.name.lower():
                first_weapon = weapon
                break
    print(f"You have chosen {first_weapon.name} as your first weapon.")
    print(f"One {first_weapon.name} has been added to your starting equipment.")
    bard.starting_equipment.append(first_weapon)

    print("Would you like to start with a Diplomat's Pack or an Entertainer's Pack?")
    print("Please enter your either 'Diplomat's Pack' or 'Entertainer's Pack':")
    pack_choice = input("> ")
    while pack_choice.lower() not in ["diplomat's pack", "entertainer's pack"]:
        print("That is not a valid choice. Please choose from the list.")
        pack_choice = input("> ")
    if pack_choice.lower() == "diplomat's pack":
        print("You have chosen the Diplomat's Pack.")
        bard.starting_equipment.append(equipment.diplomats_pack)
    else:
        print("You have chosen the Entertainer's Pack.")
        bard.starting_equipment.append(equipment.entertainers_pack)
    
    print("Would you like to start with a Lute or another musical instrument?")
    print("Please enter your either 'Lute' or 'Other Musical Instrument':")
    instrument_choice = input("> ")
    while instrument_choice.lower() not in ["lute", "other musical instrument"]:
        print("That is not a valid choice. Please choose from the list.")
        instrument_choice = input("> ")
    if instrument_choice.lower() == "lute":
        print("You have chosen the Lute.")
        bard.starting_equipment.append(equipment.lute)
    else:
        print("Please choose a musical instrument from the following list:")
        valid_instruments = []
        for instrument in instruments.instruments:
            valid_instruments.append(instrument.name.lower())
            print(instrument.name)
        instrument_choice = input("> ")
        while instrument_choice.lower() not in valid_instruments:
            print("That is not a valid choice. Please choose from the list.")
            instrument_choice = input("> ")
        for instrument in equipment.instruments:
            if instrument_choice.lower() == instrument.name.lower():
                print(f"You have chosen the {instrument.name}.")
                bard.starting_equipment.append(instrument)
                break
    
    print("You will also start with Leather Armor and a Dagger.")
    bard.starting_equipment.append(equipment.leather_light_armor)
    bard.starting_equipment.append(equipment.dagger)

    print(f'You will start with the following equipment:')
    for item in bard.starting_equipment:
        print(item.name)

    # Starting Cantrips
    print("You have reached level 1 and can now choose 2 cantrips from the bard spell list.")
    print("Please choose two cantrips from the following list:")
    display_bard_spells()
    print("Please enter your first cantrip choice:")
    cantrip_choice1 = input("> ")
    while cantrip_choice1.lower() not in bard_spells:
        print("That is not a valid choice. Please choose from the list.")
        cantrip_choice1 = input("> ")
    print("Please enter your second cantrip choice:")
    cantrip_choice2 = input("> ")
    while cantrip_choice2.lower() not in bard_spells:
        print("That is not a valid choice. Please choose from the list.")
        cantrip_choice2 = input("> ")
    selected_cantrips = [cantrip_choice1, cantrip_choice2]
    print(f"You have chosen {selected_cantrips[0]} and {selected_cantrips[1]} as your cantrips.")
    bard.cantrips = selected_cantrips

    # Starting Spells
    print("You have reached level 1 and can now choose 4 spells from the bard spell list.")
    print("Please choose four spells from the following list:")
    display_bard_spells()
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
        


