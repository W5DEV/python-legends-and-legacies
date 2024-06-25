import modules.equipment as equipment

displayed_paladin_skills = ["Athletics", "Insight", "Intimidation", "Medicine", "Persuasion", "Religion"]
paladin_skills = ["athletics", "insight", "intimidation", "medicine", "persuasion", "religion"]

displayed_paladin_spells = ["Bless", "Command", "Cure Wounds", "Detect Evil and Good", "Detect Magic", "Detect Poison and Disease", "Divine Favor", "Heroism", "Protection from Evil and Good", "Purify Food and Drink", "Searing Smite", "Shield of Faith"]
paladin_spells = ["bless", "command", "cure wounds", "detect evil and good", "detect magic", "detect poison and disease", "divine favor", "heroism", "protection from evil and good", "purify food and drink", "searing smite", "shield of faith"]

potential_starting_equipment = ["A Martial Weapon and a Shield or Two Martial Weapons", "Five Javelins or Any Simple Melee Weapon", "A Priest's Pack or an Explorer's Pack", "Chain Mail and a Holy Symbol Emblem"]
        
class Paladin:
    
    def __init__(self):
        name = "Paladin"
        bio = "A holy warrior bound to a sacred oath."
        hit_die = "10"
        primary_ability = "Strength, Charisma"
        saving_throw_proficiencies = "Wisdom, Charisma"
        armor_proficiencies = "All Armor and Shields"
        weapon_proficiencies = "Simple Weapons, Martial Weapons"
        tool_proficiencies = "None"
        self.name = name
        self.bio = bio
        self.hit_die = hit_die
        self.base_hp = 10
        self.primary_ability = primary_ability
        self.saving_throw_proficiencies = saving_throw_proficiencies
        self.armor_proficiencies = armor_proficiencies
        self.weapon_proficiencies = weapon_proficiencies
        self.tool_proficiencies = tool_proficiencies
        self.skill_proficiencies = []
        self.starting_equipment = []
        self.sacred_oath = ""
        self.channel_divinity_options = []
        self.oath_of_devotion_spells = []
        self.special_abilities = []
        self.spell_slots_level_1 = 0
        self.spell_slots_level_2 = 0
        self.spell_slots_level_3 = 0
        self.spell_slots_level_4 = 0
        self.spell_slots_level_5 = 0

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
            self.special_abilities.append("Divine Sense")
            self.special_abilities.append("Lay on Hands")
        if level >= 2:
            self.special_abilities.append("Fighting Style")
            self.special_abilities.append("Spellcasting")
            self.special_abilities.append("Divine Smite")
            self.spell_slots_level_1 = 2
        if level >= 3:
            self.sacred_oath = "Oath of Devotion"
            self.channel_divinity_options.append("Sacred Weapon")
            self.channel_divinity_options.append("Turn the Unholy")
            self.special_abilities.append("Divine Health")
            self.special_abilities.append("Sacred Oath")
            self.oath_of_devotion_spells.append("Protection from Evil and Good")
            self.oath_of_devotion_spells.append("Sanctuary")
            self.spell_slots_level_1 = 3
        if level >= 4:
            self.special_abilities.append("Ability Score Improvement 4th Level")
        if level >= 5:
            self.special_abilities.append("Extra Attack")
            self.oath_of_devotion_spells.append("Lesser Restoration")
            self.oath_of_devotion_spells.append("Zone of Truth")
            self.spell_slots_level_1 = 4
            self.spell_slots_level_2 = 2
        if level >= 6:
            self.special_abilities.append("Aura of Protection")
        if level >= 7:
            self.special_abilities.append("Aura of Devotion (10 ft)")
            self.spell_slots_level_2 = 3
        if level >= 8:
            self.special_abilities.append("Ability Score Improvement 8th Level")
        if level >= 9:
            self.oath_of_devotion_spells.append("Beacon of Hope")
            self.oath_of_devotion_spells.append("Dispel Magic")
            self.spell_slots_level_3 = 2
        if level >= 10:
            self.special_abilities.append("Aura of Courage")
        if level >= 11:
            self.special_abilities.append("Improved Divine Smite")
            self.spell_slots_level_3 = 3
        if level >= 12:
            self.special_abilities.append("Ability Score Improvement 12th Level")
        if level >= 13:
            self.oath_of_devotion_spells.append("Freedom of Movement")
            self.oath_of_devotion_spells.append("Guardian of Faith")
            self.spell_slots_level_4 = 1
        if level >= 14:
            self.special_abilities.append("Cleansing Touch")
        if level >= 15:
            self.special_abilities.append("Purity of Spirit")
            self.spell_slots_level_4 = 2
        if level >= 16:
            self.special_abilities.append("Ability Score Improvement 16th Level")
        if level >= 17:
            self.oath_of_devotion_spells.append("Commune")
            self.oath_of_devotion_spells.append("Flame Strike")
            self.spell_slots_level_4 = 3
            self.spell_slots_level_5 = 1
        if level >= 18:
            self.special_abilities.append("Aura Improvements")
            self.special_abilities.append("Aura of Devotion (30 ft)")
        if level >= 19:
            self.special_abilities.append("Ability Score Improvement 19th Level")
            self.spell_slots_level_5 = 2
        if level >= 20:
            self.special_abilities.append("Holy Nimbus")


def define_paladin():
    paladin = Paladin()
    print("You have chosen the paladin class.")
    print(paladin.bio)

    # Skill Proficiencies
    print("Choose two skills from the following list:")
    for skill in displayed_paladin_skills:
        print(skill)
    print("Please enter your first skill choice:")
    skill_choice1 = input("> ")
    while skill_choice1.lower() not in paladin_skills:
        print("That is not a valid choice. Please choose from the list.")
        skill_choice1 = input("> ")
    paladin.skill_proficiencies.append(skill_choice1)

    print("Please enter your second skill choice:")
    skill_choice2 = input("> ")
    while skill_choice2.lower() not in paladin_skills:
        print("That is not a valid choice. Please choose from the list.")
        skill_choice2 = input("> ")
    paladin.skill_proficiencies.append(skill_choice2)

    print("You have chosen the following skills:")
    for skill in paladin.skill_proficiencies:
        print(skill)

    # Starting Spells
    spell_choice = ""
    print("Choose your starting spell:")
    for spell in displayed_paladin_spells:
        print(spell)
    print("Please enter your choice:")
    spell_choice = input("> ")
    while spell_choice.lower() not in paladin_spells:
        print("That is not a valid choice. Please choose from the list.")
        spell_choice = input("> ")
    for spell in displayed_paladin_spells:
        if spell_choice.lower() == spell.lower():
            print(f"You have chosen {spell}.")
            print(f"{spell} has been added to your starting spells.")
            paladin.oath_of_devotion_spells.append(spell)
            break

    # Starting Equipment
    equipment_choice1 = ""
    equipment_choice2 = ""
    print("Choose your starting equipment:")
    for item in potential_starting_equipment:
        print(item)

    print("Please enter your choice of a 'Shortsword' or 'any Simple Weapon':")
    equipment_choice1 = input("> ")
    while equipment_choice1.lower() not in ["shortsword", "any simple weapon"]:
        print("That is not a valid choice. Please choose from the list.")
        equipment_choice1 = input("> ")
    if equipment_choice1.lower() == "shortsword":
        print("You have chosen Shortsword.")
        print("One Shortsword has been added to your starting equipment.")
        paladin.starting_equipment.append(equipment.short_sword)
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
                paladin.starting_equipment.append(weapon)
                break

    print("Please enter your choice of a 'Priest's Pack' or an 'Explorer's Pack':")
    equipment_choice2 = input("> ")
    while equipment_choice2.lower() not in ["priest's pack", "explorer's pack"]:
        print("That is not a valid choice. Please choose from the list.")
        equipment_choice2 = input("> ")
    if equipment_choice2.lower() == "priest's pack":
        print("You have chosen a Priest's Pack.")
        print("A priest's Pack has been added to your starting equipment.")
        paladin.starting_equipment.append(equipment.priests_pack)
    elif equipment_choice2.lower() == "explorer's pack":
        print("You have chosen an Explorer's Pack.")
        print("An Explorer's Pack has been added to your starting equipment.")
        paladin.starting_equipment.append(equipment.explorers_pack)

    print("You also start with 10 Darts.")
    print("10 Darts have been added to your starting equipment.")
    # Add darts to starting equipment

    print("You also start with Chain Mail and a Holy Symbol Emblem.")
    print("Chain Mail and a Holy Symbol Emblem have been added to your starting equipment.")
    paladin.starting_equipment.append(equipment.chain_mail_heavy_armor)
    paladin.starting_equipment.append(equipment.holy_symbol_emblem)
    
    print(f"You have chosen the following starting equipment:")
    for item in paladin.starting_equipment:
        print(item.name)

    return paladin