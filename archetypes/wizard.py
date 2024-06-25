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

import modules.equipment as equipment

displayed_wizard_spells = ["Alarm", "Burning Hands", "Charm Person", "Color Spray", "Comprehend Languages", "Detect Magic", "Disguise Self", "Expeditious Retreat", "False Life", "Feather Fall", "Find Familiar", "Fog Cloud", "Grease", "Hideous Laughter", "Identify", "Illusory Script", "Jump", "Longstrider", "Mage Armor", "Magic Missile", "Protection from Evil and Good", "Shield", "Silent Image", "Sleep", "Thunderwave", "Unseen Servant"]
wizard_spells = ["alarm", "burning hands", "charm person", "color spray", "comprehend languages", "detect magic", "disguise self", "expeditious retreat", "false life", "feather fall", "find familiar", "fog cloud", "grease", "hideous laughter", "identify", "illusory script", "jump", "longstrider", "mage armor", "magic missile", "protection from evil and good", "shield", "silent image", "sleep", "thunderwave", "unseen servant"]
displayed_wizard_cantrips = ["Acid Splash", "Chill Touch", "Dancing Lights", "Fire Bolt", "Light", "Mage Hand", "Mending", "Message", "Minor Illusion", "Poison Spray", "Prestidigitation", "Ray of Frost", "Shocking Grasp", "True Strike"]
wizard_cantrips = ["acid splash", "chill touch", "dancing lights", "fire bolt", "light", "mage hand", "mending", "message", "minor illusion", "poison spray", "prestidigitation", "ray of frost", "shocking grasp", "true strike"]

potential_starting_equipment = ["A Quarterstaff or a Dagger", "A Component Pouch or an Arcane Focus", "A Scholar's Pack or and Explorer's Pack", "A Spellbook"]

displayed_wizard_skills = ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"]
wizard_skills = ["arcana", "history", "insight", "investigation", "medicine", "religion"]

def display_wizard_spells():
    for spell in displayed_wizard_spells:
        print(spell)

class Wizard:
    def __init__(self):
        name = "Wizard"
        bio = "A scholarly magic-user capable of manipulating the structures of reality"
        hit_die = "6 for first level, then 1d6 (or 4, whichever is higher) per level after 1 + your Constitution modifier"
        primary_ability = "Intelligence"
        saving_throw_proficiencies = "Intelligence, Wisdom"
        armor_proficiencies = "None"
        weapon_proficiencies = "Daggers, Darts, Slings, Quarterstaffs, Light Crossbows"
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
        print(f"Skill Proficiencies: {self.skill_proficiencies}")
        print(f"Starting Equipment: {self.starting_equipment}")
        print(f"Special Abilities: {self.special_abilities}")
        return self
    
    def sync_level(self, level):
        if level >= 1:
            self.special_abilities.append("Spellcasting")
            self.special_abilities.append("Arcane Recovery")
        if level >= 2:
            self.arcane_tradition = "School of Evocation"
            self.special_abilities.append("Evocation Savant")
            self.special_abilities.append("Sculpt Spells")
        if level >= 3:
            pass
        if level >= 4:
            self.special_abilities.append("Ability Score Improvement 4th Level")
        if level >= 5:
            pass
        if level >= 6:
            self.special_abilities.append("Potent Cantrip")
        if level >= 7:
            pass
        if level >= 8:
            self.special_abilities.append("Ability Score Improvement 8th Level")
        if level >= 9:
            pass
        if level >= 10:
            self.special_abilities.append("Empowered Evocation")
        if level >= 11:
            pass
        if level >= 12:
            self.special_abilities.append("Ability Score Improvement 12th Level")
        if level >= 13:
            pass
        if level >= 14:
            self.special_abilities.append("Overchannel")
        if level >= 15:
            pass
        if level >= 16:
            self.special_abilities.append("Ability Score Improvement 16th Level")
        if level >= 17:
            pass
        if level >= 18:
            self.special_abilities.append("Spell Mastery")
        if level >= 19:
            self.special_abilities.append("Ability Score Improvement 19th Level")
        if level >= 20:
            self.special_abilities.append("Signature Spells")

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
    equipment_choice1 = ""
    equipment_choice2 = ""
    equipment_choice3 = ""
    print("Choose your starting equipment:")
    for item in potential_starting_equipment:
        print(item)

    print("Please enter your choice of a 'Quarterstaff' or 'Dagger':")
    equipment_choice1 = input("> ")
    while equipment_choice1.lower() not in ["quarterstaff", "dagger"]:
        print("That is not a valid choice. Please choose from the list.")
        equipment_choice1 = input("> ")
    if equipment_choice1.lower() == "quarterstaff":
        print("You have chosen a Quarterstaff.")
        print("A Quarterstaff has been added to your starting equipment.")
        wizard.starting_equipment.append(equipment.quarter_staff)
    elif equipment_choice1.lower() == "dagger":
        print("You have chosen a Dagger.")
        print("A Dagger has been added to your starting equipment.")
        wizard.starting_equipment.append(equipment.dagger)

    print("Please enter your choice of a 'Component Pouch' or an 'Arcane Focus':")
    equipment_choice2 = input("> ")
    while equipment_choice2.lower() not in ["component pouch", "arcane focus"]:
        print("That is not a valid choice. Please choose from the list.")
        equipment_choice2 = input("> ")
    if equipment_choice2.lower() == "component pouch":
        print("You have chosen a Component Pouch.")
        print("A Component Pouch has been added to your starting equipment.")
        wizard.starting_equipment.append(equipment.component_pouch)
    elif equipment_choice2.lower() == "arcane focus":
        print("You have chosen an Arcane Focus.")
        print("An Arcane Focus has been added to your starting equipment.")
        wizard.starting_equipment.append(equipment.arcane_focus_crystal)

    print("Please enter your choice of a 'Scholar's Pack' or an 'Explorer's Pack':")
    equipment_choice3 = input("> ")
    while equipment_choice3.lower() not in ["scholar's pack", "explorer's pack"]:
        print("That is not a valid choice. Please choose from the list.")
        equipment_choice3 = input("> ")
    if equipment_choice3.lower() == "scholar's pack":
        print("You have chosen a Scholar's Pack.")
        print("A Scholar's Pack has been added to your starting equipment.")
        wizard.starting_equipment.append(equipment.scholars_pack)
    elif equipment_choice3.lower() == "explorer's pack":
        print("You have chosen an Explorer's Pack.")
        print("An Explorer's Pack has been added to your starting equipment.")
        wizard.starting_equipment.append(equipment.explorers_pack)

    print("You also start with a Spellbook.")
    print("A Spellbook has been added to your starting equipment.")
    wizard.starting_equipment.append(equipment.spellbook)
    
    print(f"You have chosen the following starting equipment:")
    for item in wizard.starting_equipment:
        print(item.name)

    return wizard
        


