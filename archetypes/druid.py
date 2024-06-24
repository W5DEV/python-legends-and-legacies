# We still need to create methods for druids for the following:
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

displayed_druid_skills = ["Arcana", "Animal Handling", "Insight", "Medicine", "Nature", "Perception", "Religion", "Survival"]
druid_skills = ["arcana", "animal handling", "insight", "medicine", "nature", "perception", "religion", "survival"]

displayed_druid_cantrips = ["Druidcraft", "Guidance", "Mending", "Poison Spray", "Produce Flame", "Resistance", "Shillelagh"]
displayed_druid_spells = ["Animal Friendship", "Charm Person", "Create or Destroy Water", "Cure Wounds", "Detect Magic", "Detect Poison and Disease", "Entangle", "Faerie Fire", "Fog Cloud", "Goodberry", "Healing Word", "Jump", "Longstrider", "Purify Food and Drink", "Speak with Animals", "Thunderwave"]
druid_cantrips = ["druidcraft", "guidance", "mending", "poison spray", "produce flame", "resistance", "shillelagh"]
druid_spells = ["animal friendship", "charm person", "create or destroy water", "cure wounds", "detect magic", "detect poison and disease", "entangle", "faerie fire", "fog cloud", "goodberry", "healing word", "jump", "longstrider", "purify food and drink", "speak with animals", "thunderwave"]

potential_starting_equipment = ["A Wooden Shield or any Simple Weapon", "Scimitar or any Simple Melee Weapon", "Leather Armor", "Explorer's Pack", "Druidic Focus"]

class Druid:
    def __init__(self):
        name = "Druid"
        description = "A priest of the Old Faith, wielding the powers of nature — moonlight and plant growth, fire and lightning — and adopting animal forms"
        hit_die = "1d8 for first level, then 1d8 (or 5, whichever is higher) per level after 1 + your Constitution modifier."
        primary_ability = "Wisdom"
        saving_throw_proficiencies = ["Intelligence", "Wisdom"]
        armor_proficiencies = ["Non-metal Light Armor", "Non-metal Medium Armor", "Non-metal Shields"]
        weapon_proficiencies = ["Clubs", "Daggers", "Darts", "Javelins", "Maces", "Quarterstaffs", "Scimitars", "Sickles", "Slings", "Spears"]
        tool_proficiencies = ["Herbalism Kit"]
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
        self.circle = ""
        self.cantrips = []
        self.spells = []
        self.cantrips_known = 2
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
            self.special_abilities.append("Druidic")
            self.special_abilities.append("Spellcasting")
        if level >= 2:
            self.circle = "Circle of the Land"
            self.special_abilities.append("Wild Shape - No flying or swimming speed (1/4 CR)")
            self.special_abilities.append("Bonus Cantrip")
            self.special_abilities.append("Natural Recovery")
        if level >= 3:
            self.special_abilities.append("3rd Level Circle Spells")
        if level >= 4:
            self.special_abilities.append("Wild Shape Improvement 4th Level - No flying speed (1/2 CR)")
            self.special_abilities.append("Ability Score Improvement 4th Level")
        if level >= 5:
            self.special_abilities.append("5th Level Circle Spells")
        if level >= 6:
            self.special_abilities.append("Land's Stride")
        if level >= 7:
            self.special_abilities.append("7th Level Circle Spells")
        if level >= 8:
            self.special_abilities.append("Wild Shape Improvement 8th Level (1 CR)")
            self.special_abilities.append("Ability Score Improvement 8th Level")
        if level >= 9:
            self.special_abilities.append("9th Level Circle Spells")
        if level >= 10:
            self.special_abilities.append("Nature's Ward")
        if level >= 12:
            self.special_abilities.append("Ability Score Improvement 12th Level")
        if level >= 14:
            self.special_abilities.append("Nature's Sanctuary")
        if level >= 16:
            self.special_abilities.append("Ability Score Improvement 16th Level")
        if level >= 18:
            self.special_abilities.append("Timeless Body")
            self.special_abilities.append("Beast Spells")
        if level >= 19:
            self.special_abilities.append("Ability Score Improvement 19th Level")
        if level >= 20:
            self.special_abilities.append("Archdruid")
        return self
    
def define_druid():
    druid = Druid()
    print("You have chosen the Druid class.")
    print(druid.description)

    # Skill Proficiencies
    print("Choose two skills from the following:")
    for skill in displayed_druid_skills:
        print(skill)
    print("Please enter your first skill choice:")
    skill_choice_1 = input("> ")
    while skill_choice_1.lower() not in druid_skills:
        print("Please enter a valid skill choice:")
        skill_choice_1 = input("> ")

    print("Please enter your second skill choice:")
    skill_choice_2 = input("> ")
    while skill_choice_2.lower() not in druid_skills:
        print("Please enter a valid skill choice:")
        skill_choice_2 = input("> ")
    
    selected_skills = [skill_choice_1, skill_choice_2]
    print(f"You have chosen proficiency in {selected_skills[0]} and {selected_skills[1]}.")
    druid.skill_proficiencies = selected_skills

     # Starting Cantrips
    print("Druids start with 2 Cantrips. Choose 2 Cantrips from the following list:")
    for cantrip in displayed_druid_cantrips:
        print(cantrip)
    print("Please choose your first Cantrip:")
    cantrip_choice1 = input("> ")
    while (cantrip_choice1.lower() not in druid_cantrips):
        print("Please enter a valid Cantrip choice:")
        cantrip_choice1 = input("> ")
    for cantrip in displayed_druid_cantrips:
        if cantrip.lower() == cantrip_choice1.lower():
            druid.cantrips.append(cantrip)
            break
    print("Please choose your second Cantrip:")
    cantrip_choice2 = input("> ")
    while (cantrip_choice2.lower() not in druid_cantrips) or (cantrip_choice2.lower() in [cantrip_choice1.lower()]):
        print("You should not choose the same Cantrip twice.")
        print("Please enter a valid Cantrip choice:")
        cantrip_choice2 = input("> ")
    for cantrip in displayed_druid_cantrips:
        if cantrip.lower() == cantrip_choice2.lower():
            druid.cantrips.append(cantrip)
            break
    print(f"You have chosen the following Cantrips:")
    for cantrip in druid.cantrips:
        print(cantrip)

    # Starting Spells
    print("Druids can prepare 1 spell. Choose 1 spell from the following list:")
    for spell in displayed_druid_spells:
        print(spell)
    print("Please choose your spell:")
    spell_choice = input("> ")
    while spell_choice.lower() not in druid_spells:
        print("Please enter a valid spell choice:")
        spell_choice = input("> ")
    for spell in displayed_druid_spells:
        if spell.lower() == spell_choice.lower():
            druid.spells.append(spell)
            break
    print(f"You have chosen the following Spell:")
    for spell in druid.spells:
        print(spell)

    # Starting Equipment
    weapon_choice1 = ""
    weapon_choice2 = ""
    armor_choice = ""
    print("Druids are able to choose from the following starting equipment:")
    for item in potential_starting_equipment:
        print(item)
    
    print("Please choose between a Shield or any Simple Weapon:")
    weapon_choice1 = input("> ")
    while weapon_choice1.lower() not in ["shield", "other simple weapon"]:
        print("Please enter either 'shield' or 'other weapon choice':")
        weapon_choice1 = input("> ")
    if weapon_choice1.lower() == "shield":
        print("You have chosen a Shield.")
        print("A Shield has been added to your starting equipment.")
        druid.starting_equipment.append(equipment.shield)
    else:
        print("Please choose a simple weapon from the list below:")
        for weapon in equipment.simple_weapons:
            print(weapon.name)
        other_weapon1 = input("> ")
        while other_weapon1.lower() not in [weapon.name.lower() for weapon in equipment.simple_weapons]:
            print("Please enter a valid weapon choice:")
            other_weapon1 = input("> ")
        for weapon in equipment.simple_weapons:
            if other_weapon1.lower() == weapon.name.lower():
                print(f"You have chosen {weapon.name}.")
                print(f"One {weapon.name} has been added to your starting equipment.")
                druid.starting_equipment.append(weapon)
                break

    print("Please choose between Scimitar or any Simple Melee Weapon:")
    weapon_choice2 = input("> ")
    while weapon_choice2.lower() not in ["scimitar", "other simple melee weapon"]:
        print("Please enter a valid armor choice:")
        weapon_choice2 = input("> ")
    if weapon_choice2.lower() == "scimitar":
        print("You have chosen a Scimitar.")
        print("A Scimitar has been added to your starting equipment.")
        druid.starting_equipment.append(equipment.scimitar)
    else:
        print("Please choose a simple weapon from the list below:")
        for weapon in equipment.simple_melee_weapons:
            print(weapon.name)
        other_weapon2 = input("> ")
        while other_weapon2.lower() not in [weapon.name.lower() for weapon in equipment.simple_weapons]:
            print("Please enter a valid weapon choice:")
            other_weapon2 = input("> ")
        for weapon in equipment.simple_melee_weapons:
            if other_weapon2.lower() == weapon.name.lower():
                print(f"You have chosen {weapon.name}.")
                print(f"One {weapon.name} has been added to your starting equipment.")
                druid.starting_equipment.append(weapon)
                break

    print("You will also receive Leather Armor, an Explorer's Pack, and a Druidic Focus.")
    print("Leather Armor, an Explorer's Pack, and a Druidic Focus have been added to your starting equipment.")
    druid.starting_equipment.append(equipment.leather_light_armor)
    druid.starting_equipment.append(equipment.explorers_pack)
    druid.starting_equipment.append(equipment.druidic_focus)

    print("You will start with the following equipment:")
    for item in druid.starting_equipment:
        print(item.name)

    return druid