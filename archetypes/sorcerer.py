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

import modules.equipment as equipment
import modules.instruments as instruments

displayed_sorcerer_spells = ["Burning Hands", "Charm Person", "Color Spray", "Comprehend Languages", "Detect Magic", "Disguise Self", "Expeditious Retreat", "False Life", "Feather Fall", "Fog Cloud", "Jump", "Mage Armor", "Magic Missile", "Shield", "Silent Image", "Sleep", "Thunderwave"]
sorcerer_spells = ["burning hands", "charm person", "color spray", "comprehend languages", "detect magic", "disguise self", "expeditious retreat", "false life", "feather fall", "fog cloud", "jump", "mage armor", "magic missile", "shield", "silent image", "sleep", "thunderwave"]
displayed_sorcerer_cantrips = ["Acid Splash", "Chill Touch", "Dancing Lights", "Fire Bolt", "Light", "Mage Hand", "Mending", "Message", "Minor Illusion", "Poison Spray", "Prestidigitation", "Ray of Frost", "Shocking Grasp", "True Strike"]
sorcerer_cantrips = ["acid splash", "chill touch", "dancing lights", "fire bolt", "light", "mage hand", "mending", "message", "minor illusion", "poison spray", "prestidigitation", "ray of frost", "shocking grasp", "true strike"]

potential_starting_equipment = ["A Light Crossbow and 20 Bolts or Any Simple Weapon", "A Component Pouch or an Arcane Focus", "A Dungeoneer's Pack or and Explorer's Pack", "Two Daggers"]

displayed_sorcerer_skills = ["Arcana", "Deception", "Insight", "Intimidation", "Persuasion", "Religion"]
sorcerer_skills = ["arcana", "deception", "insight", "intimidation", "persuasion", "religion"]

def display_sorcerer_spells():
    for spell in displayed_sorcerer_spells:
        print(spell)

class Sorcerer:
    def __init__(self):
        name = "Sorcerer"
        description = "A spellcaster who draws on inherent magic from a gift or bloodline"
        hit_die = "1d6 for first level, then 1d6 (or 4, whichever is higher) per level after 1 + your Constitution modifier"
        primary_ability = "Charisma"
        saving_throw_proficiencies = "Constitution, Charisma"
        armor_proficiencies = "None"
        weapon_proficiencies = "Daggers, Darts, Slings, Quarterstaffs, Light Crossbows"
        tool_proficiencies = "None"
        self.name = name
        self.description = description
        self.hit_die = hit_die
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
        print(f"The {self.name}: {self.description}")
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
            self.special_abilities.append("Spellcasting")
            self.sorcerous_origin = "Dragon Bloodline"
            self.special_abilities.append("Dragon Ancestor")
            self.special_abilities.append("Dracoic Resilience")
        if level >= 2:
            self.special_abilities.append("Font of Magic")
        if level >= 3:
            self.special_abilities.append("Metamagic")
        if level >= 4:
            self.special_abilities.append("Ability Score Improvement 4th Level")
        if level >= 5:
            pass
        if level >= 6:
            self.special_abilities.append("Elemental Affinity")
        if level >= 7:
            pass
        if level >= 8:
            self.special_abilities.append("Ability Score Improvement 8th Level")
        if level >= 9:
            pass
        if level >= 10:
            self.special_abilities.append("Metamagic")
        if level >= 11:
            pass
        if level >= 12:
            self.special_abilities.append("Ability Score Improvement 12th Level")
        if level >= 13:
            pass
        if level >= 14:
            self.special_abilities.append("Dragon Wings")
        if level >= 15:
            pass
        if level >= 16:
            self.special_abilities.append("Ability Score Improvement 16th Level")
        if level >= 17:
            self.special_abilities.append("Metamagic")
        if level >= 18:
            self.special_abilities.append("Draconic Presence")
        if level >= 19:
            self.special_abilities.append("Ability Score Improvement 19th Level")
        if level >= 20:
            self.special_abilities.append("Sorcerous Restoration")

def define_sorcerer():
    sorcerer = Sorcerer()
    print(f'You have chosen the sorcerer class.')
    print(sorcerer.description)

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
    print("Please choose two cantrips from the following list:")
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
        sorcerer.starting_equipment.append(equipment.light_crossbow)
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
                sorcerer.starting_equipment.append(weapon)
                break

    print("Please enter your choice of a 'Component Pouch' or an 'Arcane Focus':")
    equipment_choice2 = input("> ")
    while equipment_choice2.lower() not in ["component pouch", "arcane focus"]:
        print("That is not a valid choice. Please choose from the list.")
        equipment_choice2 = input("> ")
    if equipment_choice2.lower() == "component pouch":
        print("You have chosen a Component Pouch.")
        print("A Component Pouch has been added to your starting equipment.")
        sorcerer.starting_equipment.append(equipment.component_pouch)
    elif equipment_choice2.lower() == "arcane focus":
        print("You have chosen an Arcane Focus.")
        print("An Arcane Focus has been added to your starting equipment.")
        sorcerer.starting_equipment.append(equipment.arcane_focus_crystal)

    print("Please enter your choice of a 'Dungeoneer's Pack' or an 'Explorer's Pack':")
    equipment_choice3 = input("> ")
    while equipment_choice3.lower() not in ["dungeoneer's pack", "explorer's pack"]:
        print("That is not a valid choice. Please choose from the list.")
        equipment_choice3 = input("> ")
    if equipment_choice3.lower() == "dungeoneer's pack":
        print("You have chosen a Dungeoneer's Pack.")
        print("A Dungeoneer's Pack has been added to your starting equipment.")
        sorcerer.starting_equipment.append(equipment.dungeoneers_pack)
    elif equipment_choice3.lower() == "explorer's pack":
        print("You have chosen an Explorer's Pack.")
        print("An Explorer's Pack has been added to your starting equipment.")
        sorcerer.starting_equipment.append(equipment.explorers_pack)

    print("You also start with 2 Daggerss.")
    print("2 Daggers have been added to your starting equipment.")
    sorcerer.starting_equipment.append(equipment.dagger)
    sorcerer.starting_equipment.append(equipment.dagger)
    
    print(f"You have chosen the following starting equipment:")
    for item in sorcerer.starting_equipment:
        print(item.name)

    return sorcerer
        


