import modules.character as character
import modules.utils as utils
import modules.equipment as equipment
import modules.races as races
import modules.archetypes as archetypes

completed_archetypes = ["barbarian", "bard", "cleric", "druid", "fighter", "monk", "paladin"]


def character_creation():
    # We are calling the functions defined for each section of Character Creation (defined below)
    player = greeting()
    character_race(player)
    # This is the D&D Class... I'm calling it archetype to avoid confusion with Python classes
    character_archetype(player)
    
    print(f"Your character is called {player.name}, a {player.race.subrace} {player.archetype.name}.")

    player.xp = 0

    if player.archetype.name.lower() in completed_archetypes:
        player.gp = utils.calculate_starting_gp(player.archetype.name)
    else:
        player.gp = utils.calculate_starting_gp(player.archetype)

    print(f"{player.name} has {player.gp} gold pieces.")

    character_bio(player)
    character_abilities(player)
    character_equipment(player)

    return player


def greeting():
    print("Greetings traveler! Welcome to the magical world of Legends & Legacies!")
    player = character.Character("", "", "", "", [], [], 0, 0)
    return player

def character_race(player):
    race = None
    print(f"Please choose {player.name}'s race from the following list:")
    races.display_races()

    # This loop will continue until the user selects a valid race
    while race == None:
        print("Which race is your character?")
        race_choice = input("> ")
        while race_choice.lower() not in races.races:
            print("Sorry, that is not a valid race. Please try again.")
            print("Which race is your character?")
            race_choice = input("> ")
        if race_choice.lower() == "hill dwarf":
            print("Please choose a tool proficiency from the following list:")
            tool_proficiency = input("> ")
            race = races.define_hill_dwarf(tool_proficiency)
        if race_choice.lower() == "mountain dwarf":
            print("Please choose a tool proficiency from the following list:")
            tool_proficiency = input
            race = races.define_mountain_dwarf(tool_proficiency)
        if race_choice.lower() == "high elf":
            print("Please choose a language from the following list:")
            language = input("> ")
            race = races.define_high_elf(language)
        if race_choice.lower() == "wood elf":
            race = races.define_wood_elf()
        if race_choice.lower() == "lightfoot halfling":
            race = races.define_lightfoot_halfling()
        if race_choice.lower() == "stout halfling":
            race = races.define_stout_halfling()
        if race_choice.lower() == "human":
            race = races.define_human()
    
    player.race = race
    player.name = race.name

    return

def character_archetype(player):
    archetype = None
    print("Great! Now please choose an class from the following list:")
    archetypes.display_archetypes()

    # This loop will continue until the user selects a valid class
    while archetype == None:
        print("Which class is your character?")
        archetype_choice = input("> ")
        while archetype_choice.lower() not in archetypes.archetypes:
            print("Sorry, that is not a valid class. Please try again.")
            print("Which class is your character?")
            archetype_choice = input("> ")
        archetype = archetype_choice
        
    if archetype.lower() in completed_archetypes:
        archetype = archetypes.create_archetype(archetype.lower())
    player.archetype = archetype
    player.sync_level(1)
    return 

def character_bio(player):
    print(f"Tell me about {player.name}'s background story.")
    player.bio = input("> ")
    return

def character_abilities(player):
    abilities = {}

    abilities["Strength"] = utils.roll_ability()
    abilities["Dexterity"] = utils.roll_ability()
    abilities["Constitution"] = utils.roll_ability()
    abilities["Intelligence"] = utils.roll_ability()
    abilities["Wisdom"] = utils.roll_ability()
    abilities["Charisma"] = utils.roll_ability()

    print(f"Here are {player.name}'s abilities: ")
    for ability, value in abilities.items():
        print(f"{ability}: {value}") 

    player.abilities = abilities
    return

def character_equipment(player):
    name = player.name
    gp = player.gp
    player_equipment = player.archetype.starting_equipment
    print(f"Now it is time to choose {name}'s equipment!")
    equipment_loop = True

    # This loop will continue until the user decides to stop buying equipment
    while equipment_loop:
        print(f"{player.name} currently has the following equipment:")
        for item in player_equipment:
            print(item.name)
        print(f"{name} has {gp} gold pieces.")

        # This is our first "out" from the loop. If the player doesn't have enough gold pieces, they can't buy more equipment
        if gp < 1:
            print(f"{name} does not have enough gold pieces to buy more equipment.")
            equipment_loop = False
            break
        
        # This is our second "out" from the loop. If the player doesn't want to buy more equipment, they can exit the loop
        print("Would you like to buy additional equipment? (yes/no)")
        buy_equipment = input("> ")
        while buy_equipment.lower() not in ["yes", "no"]:
            print("Sorry, that is not a valid choice. Please try again.")
            print("Would you like to buy additional equipment? (yes/no)")
            buy_equipment = input("> ")
        if buy_equipment.lower() == "no":
            equipment_loop = False
            break

        print("Please choose equipment from the following list:")
        for equipment_type in equipment.equipment_types:
            print(equipment_type)
        equipment_choice = input("> ")
        if equipment_choice == "cancel":
            break

        # This is the main equipment selection loop. It will continue until the player selects a valid equipment type
        equipment_types_lower = [equipment.lower() for equipment in equipment.equipment_types]
        while equipment_choice.lower() not in equipment_types_lower:
            print("Sorry, that is not a valid equipment type. Please try again.")
            equipment_choice = input("> ")

        # This is the Simple Weapons selection loop. It will trigger if the player selects "Simple Weapons"
        if equipment_choice.lower() == "simple weapons":
            print("Please choose a weapon from the following list:")
            for weapon in equipment.simple_weapons:
                print(weapon.name)
            weapon_choice = input("> ")
            if weapon_choice == "cancel":
                    break
            simple_weapons_lower = [weapon.name.lower() for weapon in equipment.simple_weapons]
            while weapon_choice not in simple_weapons_lower:
                print("Sorry, that is not a valid weapon. Please try again.")
                weapon_choice = input("> ")
                if weapon_choice == "cancel":
                    break
            for weapon in equipment.simple_weapons:
                if weapon_choice.lower() == weapon.name.lower():
                    print(f"{name} has {gp} gold pieces.")
                    print(f"The {weapon.name} costs {weapon.cost} gold pieces.")
                    if gp < weapon.cost:
                        print(f"{name} does not have enough gold pieces to buy the {weapon.name}.")
                        break
                    else:
                        player_equipment.append(weapon)
                        gp -= weapon.cost
                        print(f"{name} now has {gp} gold pieces and a new {weapon.name}.")

        # This is the Martial Weapons selection loop. It will trigger if the player selects "Martial Weapons"
        elif equipment_choice.lower() == "martial weapons":
            print("Please choose a weapon from the following list:")
            for weapon in equipment.martial_weapons:
                print(weapon.name)
            weapon_choice = input("> ")
            if weapon_choice == "cancel":
                    break
            martial_weapons_lower = [weapon.name.lower() for weapon in equipment.martial_weapons]
            while weapon_choice not in martial_weapons_lower:
                print("Sorry, that is not a valid weapon. Please try again.")
                weapon_choice = input("> ")
                if weapon_choice == "cancel":
                    break
            for weapon in equipment.martial_weapons:
                if weapon_choice.lower() == weapon.name.lower():
                    print(f"{name} has {gp} gold pieces.")
                    print(f"The {weapon.name} costs {weapon.cost} gold pieces.")
                    if gp < weapon.cost:
                        print(f"{name} does not have enough gold pieces to buy the {weapon.name}.")
                        break
                    else:
                        player_equipment.append(weapon)
                        gp -= weapon.cost
                        print(f"{name} now has {gp} gold pieces and a new {weapon.name}.")

        # This is the Light Armor selection loop. It will trigger if the player selects "Light Armor"
        elif equipment_choice.lower() == "light armor":
            print("Please choose armor from the following list:")
            for armor in equipment.light_armor:
                print(armor.name)
            armor_choice = input("> ")
            if armor_choice == "cancel":
                    break
            light_armor_lower = [armor.name.lower() for armor in equipment.light_armor]
            while armor_choice not in light_armor_lower:
                print("Sorry, that is not valid armor. Please try again.")
                armor_choice = input("> ")
                if armor_choice == "cancel":
                        break
            for armor in equipment.light_armor:
                if armor_choice.lower() == armor.name.lower():
                    print(f"{name} has {gp} gold pieces.")
                    print(f"The {armor.name} costs {armor.cost} gold pieces.")
                    if gp < armor.cost:
                        print(f"{name} does not have enough gold pieces to buy the {armor.name}.")
                        break
                    else:
                        player_equipment.append(armor)
                        gp -= armor.cost
                        print(f"{name} now has {gp} gold pieces and new {armor.name}.")

        # This is the Medium Armor selection loop. It will trigger if the player selects "Medium Armor"
        elif equipment_choice.lower() == "medium armor":
            print("Please choose armor from the following list:")
            for armor in equipment.medium_armor:
                print(armor.name)
            armor_choice = input("> ")
            if armor_choice == "cancel":
                    break
            medium_armor_lower = [armor.name.lower() for armor in equipment.medium_armor]
            while armor_choice not in medium_armor_lower:
                print("Sorry, that is not valid armor. Please try again.")
                armor_choice = input("> ")
                if armor_choice == "cancel":
                        break
            for armor in equipment.medium_armor:
                if armor_choice.lower() == armor.name.lower():
                    print(f"{name} has {gp} gold pieces.")
                    print(f"The {armor.name} costs {armor.cost} gold pieces.")
                    if gp < armor.cost:
                        print(f"{name} does not have enough gold pieces to buy the {armor.name}.")
                        break
                    else:
                        player_equipment.append(armor)
                        gp -= armor.cost
                        print(f"{name} now has {gp} gold pieces and new {armor.name}.")

        # This is the Heavy Armor selection loop. It will trigger if the player selects "Heavy Armor"
        elif equipment_choice.lower() == "heavy armor":
            print(f"Please choose armor from the following list:")
            for armor in equipment.heavy_armor:
                print(armor.name)
            armor_choice = input("> ")
            if armor_choice == "cancel":
                    break
            heavy_armor_lower = [armor.name.lower() for armor in equipment.heavy_armor]
            while armor_choice not in heavy_armor_lower:
                print("Sorry, that is not valid armor. Please try again.")
                armor_choice = input("> ")
                if armor_choice == "cancel":
                        break
            for armor in equipment.heavy_armor:
                if armor_choice.lower() == armor.name.lower():
                    print(f"{name} has {gp} gold pieces.")
                    print(f"The {armor.name} costs {armor.cost} gold pieces.")
                    if gp < armor.cost:
                        print(f"{name} does not have enough gold pieces to buy the {armor.name}.")
                        break
                    else:
                        player_equipment.append(armor)
                        gp -= armor.cost
                        print(f"{name} now has {gp} gold pieces and new {armor.name}.")

        # This is the Shield selection loop. It will trigger if the player selects "Shield"
        elif equipment_choice.lower() == "shield":
            print(f"{name} has {gp} gold pieces.")
            print(f"The {equipment.shield.name} costs {equipment.shield.cost} gold pieces.")
            print(f"Please confirm {name} would like a shield: (yes/no)")
            shield_choice = input("> ")
            while shield_choice.lower() not in ["yes", "no"]:
                print("Sorry, that is not a valid choice. Please try again.")
                print(f"{name} has {gp} gold pieces.")
                print(f"The {equipment.shield.name} costs {equipment.shield.cost} gold pieces.")
                print(f"Please confirm {name} would like a shield: (yes/no)")
                shield_choice = input("> ")
            if shield_choice == "no":
                break
            elif shield_choice == "yes":
                print(f"{name} has {gp} gold pieces.")
                print(f"The {equipment.shield.name} costs {equipment.shield.cost} gold pieces.")
                if gp < equipment.shield.cost:
                    print(f"{name} does not have enough gold pieces to buy the {equipment.shield.name}.")
                    break
                else:
                    player_equipment.append(equipment.shield)
                    gp -= equipment.shield.cost
                    print(f"{name} now has {gp} gold pieces and a new {equipment.shield.name}.")

    player.gp = gp
    player.equipment = player_equipment
    return