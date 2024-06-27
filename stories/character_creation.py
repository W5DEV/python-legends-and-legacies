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

    print(f"And so {player.name} finally defeated the Character Creation boss! {player.name} has emerged victorious, with a character sheet that is complete and error-free!")
    print(f"{player.name} has faired well for the Character Creation boss battle, but how will he fair against the menacing 'Biography Synposis Boogeyman'??")
    print(f"The Biography Synopsis Boogeyman is a fearsome creature that will only be defeated if {player.name} can sit through a detailed summary of his character sheet without falling asleep!")
    print(f"Only true Legends can defeat the Biography Synposis Boogeyman! Will you emerge victorious and leave your Legacy behind? Or will your character falter and end with a sad, depressing error?")
    print("The Biographical Synopsis Boogeyman laughs maniacally then proceeds to read your character sheet:")
    print(f"{player.name} is a {player.race.subrace} {player.archetype.name}.")
    print(f"{player.name}'s bio is as follows:")
    print(player.bio)
    print(f"{player.name} has the following starting equipment:")
    for item in player.equipment:
        print(item.name)
    print(f"{player.name}'s ability scores are as follows:")
    print(f"Strength: {player.strength}")
    print(f"Dexterity: {player.dexterity}")
    print(f"Constitution: {player.constitution}")
    print(f"Intelligence: {player.intelligence}")
    print(f"Wisdom: {player.wisdom}")
    print(f"Charisma: {player.charisma}")
    print(f"{player.name} has {player.max_hp} hit points.")
    print(f"{player.name} has {player.gp} gold pieces.")
    print(f"{player.name} has {player.xp} xp and is level {player.level}. This means they have a proficiency bonus of {player.proficiency_bonus}.")
    print(f"{player.name} needs {player.xp_needed_for_next_level()} xp to level up.")
    print(player.xp_needed_for_next_level())

    ac = player.calculate_armor_class()
    print(f"{player.name}'s Armor Class is {ac}.")

    print(f"{player.name} has successfully defeated the Biography Synopsis Boogeyman! {player.name} has emerged victorious, with a character sheet that is complete and error-free!")

    print(f"{player.name} has been awarded 300xp for defeating the Biography Synopsis Boogeyman!")
    player.award_xp(300)
    print(f"{player.name} is level {player.level}. They have a max of {player.max_hp} hit points. Their proficiency bonus is {player.proficiency_bonus}. They have {player.xp}xp and need an additional {player.xp_needed_for_next_level()}xp to level up.")

    print(f"{player.name} can now equip, ready and unequip items from their inventory!")
    player.equip_armor()
    player.equip_weapon()
    player.ready_weapon()
    player.equip_shield()
    player.unequip_armor()
    player.unequip_weapon()
    player.unequip_shield()

    ac = player.calculate_armor_class()
    print(f"{player.name}'s Armor Class is {ac}.")
    print(f"Expected ac: {player.dexterity_mod + 10}")

    print(f"{player.name} has successfully completed the demonstration of their equipment! They have been awarded 600xp!")
    player.award_xp(600)
    print(f"{player.name} is level {player.level}. They have a max of {player.max_hp} hit points. Their proficiency bonus is {player.proficiency_bonus}. They have {player.xp}xp and need an additional {player.xp_needed_for_next_level()}xp to level up.")

    print(f"{player.name} has emerged a Legend and has most assuredly left behind a Legacy! Congratulations on completing the Daunting Trials of Character Creation!")
    return player


def greeting():
    print("Greetings traveler! Welcome to the magical world of Legends & Legacies!")
    print("Embark on a journey with us through the magical story of 'The Daunting Trials of Character Creation'!")
    print("You are walking through the woods, when suddenly a giant figure steps out from behind a tree.")
    print("The figure is unlike any you have ever seen before. They have 4 heads and 6 arms. They look at you and say in a bellowing voice:")
    print("'I am the mighty Character Creation Boss! To defeat me, you must create your character without any errors or mistakes!'")
    player = character.Character()
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
            tool_proficiencies = ["Smith's Tools", "Brewer's Supplies", "Mason's Tools"]
            valid_tools = []
            print("Please choose a tool proficiency from the following list:")
            for tool in tool_proficiencies:
                print(tool)
                valid_tools.append(tool.lower())
            tool_proficiency = input("> ")
            while tool_proficiency.lower() not in valid_tools:
                print("Sorry, that is not a valid tool proficiency. Please try again.")
                print("Please choose a tool proficiency from the following list:")
                for tool in tool_proficiencies:
                    print(tool)
                tool_proficiency = input
            race = races.define_hill_dwarf(tool_proficiency)
        if race_choice.lower() == "mountain dwarf":
            tool_proficiencies = ["Smith's Tools", "Brewer's Supplies", "Mason's Tools"]
            valid_tools = []
            print("Please choose a tool proficiency from the following list:")
            for tool in tool_proficiencies:
                print(tool)
                valid_tools.append(tool.lower())
            tool_proficiency = input("> ")
            while tool_proficiency.lower() not in valid_tools:
                print("Sorry, that is not a valid tool proficiency. Please try again.")
                print("Please choose a tool proficiency from the following list:")
                for tool in tool_proficiencies:
                    print(tool)
                tool_proficiency = input
            race = races.define_mountain_dwarf(tool_proficiency)
        if race_choice.lower() == "high elf":
            languages = ["Arakora", "Abyssal/Infernal", "Aquan", "Auran", "Celestial", "Deep Speech", "Draconic", "Druidic", "Dwarvish", "Giant/Jotun", "Gith", "Gnoll", "Gnomish", "Goblin", "Halfling", "Orcish", "Primordial", "Sylvan", "Terran"]
            valid_languages = []
            print("Please choose a language from the following list:")
            for language in languages:
                print(language)
                valid_languages.append(language.lower())
            language = input("> ")
            while language.lower() not in valid_languages:
                print("Sorry, that is not a valid language. Please try again.")
                print("Please choose a language from the following list:")
                for language in languages:
                    print(language)
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
    player.sync_level()
    return 

def character_bio(player):
    print(f"Tell me about {player.name}'s background story.")
    player.bio = input("> ")
    return

def character_abilities(player):
    player.strength, player.dexterity, player.constitution, player.intelligence, player.wisdom, player.charisma = utils.calculate_abilities()
    if player.race.constitution_increase > 0:
        print(f"{player.name} has a racial bonus to Constitution.")
        player.constitution += player.race.constitution_increase
    if player.race.strength_increase > 0:
        print(f"{player.name} has a racial bonus to Strength.")
        player.strength += player.race.strength_increase
    if player.race.dexterity_increase > 0:
        print(f"{player.name} has a racial bonus to Dexterity.")
        player.dexterity += player.race.dexterity_increase
    if player.race.intelligence_increase > 0:
        print(f"{player.name} has a racial bonus to Intelligence.")
        player.intelligence += player.race.intelligence_increase
    if player.race.wisdom_increase > 0:
        print(f"{player.name} has a racial bonus to Wisdom.")
        player.wisdom += player.race.wisdom_increase
    if player.race.charisma_increase > 0:
        print(f"{player.name} has a racial bonus to Charisma.")
        player.charisma += player.race.charisma_increase
    return