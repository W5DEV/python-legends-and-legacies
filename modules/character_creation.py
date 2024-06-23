import modules.user as user
import modules.utils as utils
import modules.equipment as equipment

def character_creation():
    print("Greetings traveler! Welcome to the world of D&D!")
    name = input("What is your name? ")
    print(f"Hello, {name}!")

    races = ["Dwarf", "Elf", "Halfling", "Human", "Dragonborn", "Gnome", "Half-Elf", "Half-Orc", "Tiefling"]
    print("Please choose a race from the following list:")
    for race in races:
        print(race)
    
    race = input("Which race would you like to be? ")
    print(f"Great! You are a {race}.")

    archetypes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
    print("Please choose an class from the following list:")
    for archetype in archetypes:
        print(archetype)

    archetype = input("Which class would you like to be? ")  
    print(f"Great! You are a {archetype}.")

    xp = 0

    gp = 0

    gp = utils.calculate_starting_gp(archetype)

    print(f"You have {gp} gold pieces.")

    bio = input("Tell me a little about your character.")

    abilities = {}

    abilities["Strength"] = utils.roll_ability()
    abilities["Dexterity"] = utils.roll_ability()
    abilities["Constitution"] = utils.roll_ability()
    abilities["Intelligence"] = utils.roll_ability()
    abilities["Wisdom"] = utils.roll_ability()
    abilities["Charisma"] = utils.roll_ability()

    print("Here are your abilities: ")
    for ability, value in abilities.items():
        print(f"{ability}: {value}") 

    player_equipment = []

    print("Now it is time to choose your equipment!")
    
    has_weapon = input("Do you want to start with a weapon? (yes/no) ")
    if has_weapon.lower() == "yes":
        print("Please choose a weapon from the following list:")
        for weapon in equipment.simple_weapons:
            print(weapon.name)
        weapon_choice = input("Which weapon would you like? ")
        for weapon in equipment.simple_weapons:
            if weapon_choice.lower() == weapon.name.lower():
                gp -= weapon.cost
                player_equipment.append(weapon)
                print(f"You have chosen to start with a {weapon.name}.")
                print(f"You have {gp} gold pieces left.")
    else:
        print("You have chosen not to start with a weapon.")

    has_armor = input("Do you want to start with armor? (yes/no) ")
    if has_armor.lower() == "yes":
        print("Please choose armor from the following list:")
        for armor in equipment.light_armor:
            print(armor.name)
        armor_choice = input("Which armor would you like? ")
        for armor in equipment.light_armor:
            if armor_choice.lower() == armor.name.lower():
                gp -= armor.cost
                player_equipment.append(armor)
                print(f"You have chosen to start with {armor.name}.")
                print(f"You have {gp} gold pieces left.")
    else:
        print("You have chosen not to start with armor.")

    has_shield = input("Do you want to start with a shield? (yes/no) ")
    if has_shield.lower() == "yes":
        print("You have chosen to start with a shield.")
        gp -= 10
        player_equipment.append(equipment.shield)
        print(f"You have {gp} gold pieces left.")
    else:
        print("You have chosen not to start with a shield.")

    player = user.User(name, race, archetype, bio, player_equipment, abilities, xp, gp)

    print(player.greet())
    print(player.get_info())
    print(player.get_bio())
    print("You have the following equipment items:")
    for item in player.get_equipment():
        print(item.name)
    print("You have the following abilities:")
    for ability, value in player.get_abilities().items():
        print(f"{ability}: {value}")
    print(f"You have {player.get_gp()} gp.")
    print({player.get_xp()})
    print(player.award_xp(1))
    print(player.xp_needed_for_next_level())
    print("Expected output: 299")
    print(player.award_xp(299))
    print(player.xp_needed_for_next_level())
    print("Expected output: 600")
    print(player.award_xp(600))
    print(player.xp_needed_for_next_level())
    print("Expected output: 1800")