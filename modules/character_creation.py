import modules.character as character
import modules.utils as utils
import modules.equipment_shop as equipment_shop
import modules.races as races
import modules.archetypes as archetypes


def character_creation():
    # We are calling the functions defined for each section of Character Creation (defined below)
    player = greeting()

    character_race(player)

    # This is the D&D Class... I'm calling it archetype to avoid confusion with Python classes
    character_archetype(player)
    player.sync_equipment()
    print(f"Your character is called {player.name}, a {player.race.subrace} {player.archetype.name}.")

    character_bio(player)

    character_abilities(player)
    player.initialize_player()

    player.gp = utils.calculate_starting_gp(player.archetype.name)
    if player.gp > 0:
        print(f"You have {player.gp} gold pieces to spend on additional equipment.")
        equipment_shop.equipment_shop(player)

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
        
    
    archetype = archetypes.create_archetype(archetype.lower())
    player.archetype = archetype
    player.sync_level(1)
    return 

def character_bio(player):
    print(f"Tell me about {player.name}'s background story.")
    player.bio = input("> ")
    return

def character_abilities(player):
    player.strength = utils.roll_ability()
    player.dexterity = utils.roll_ability()
    player.constitution = utils.roll_ability()
    player.intelligence = utils.roll_ability()
    player.wisdom = utils.roll_ability()
    player.charisma = utils.roll_ability()

    print(f"{player.name}'s ability scores are as follows:")
    print(f"Strength: {player.strength}")
    print(f"Dexterity: {player.dexterity}")
    print(f"Constitution: {player.constitution}")
    print(f"Intelligence: {player.intelligence}")
    print(f"Wisdom: {player.wisdom}")
    print(f"Charisma: {player.charisma}")

    return