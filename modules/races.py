import pygame
import sys
import random
import gui.constants as const  # Import the constants module
import gui.text_display as text_display  # Import the text_display module
import gui.buttons as buttons  # Import the buttons module

# Initialize pygame
pygame.init()


# Setup screen
surface = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
pygame.display.set_caption('Race Selection')

class Race:
    def __init__(self, name, gender, race, subrace, size, speed, languages, ability_score_increase, traits, proficiencies):
        self.name = name
        self.gender = gender
        self.race = race
        self.subrace = subrace
        self.size = size
        self.speed = speed
        self.languages = languages
        self.constitution_increase = ability_score_increase[0]
        self.strength_increase = ability_score_increase[1]
        self.dexterity_increase = ability_score_increase[2]
        self.intelligence_increase = ability_score_increase[3]
        self.wisdom_increase = ability_score_increase[4]
        self.charisma_increase = ability_score_increase[5]
        self.traits = traits
        self.proficiencies = proficiencies

def choose_race():
    button_texts = ["Hill Dwarf", "Mountain Dwarf", "High Elf", "Wood Elf", "Lightfoot Halfling", "Stout Halfling", "Human"]
    button_rects = buttons.create_button_rects(len(button_texts))
    
    animate_flag = True  # Flag to control text animation
    
    while True:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(button_rects):
                    if rect.collidepoint(mouse_pos):
                        text_display.animate_text(surface, f'You chose {button_texts[i]}!')
                        return define_race(button_texts[i])
                    

        surface.fill(const.BG_COLOR)

        if animate_flag:
            text_display.animate_text(surface, 'Choose your character\'s race!')
            animate_flag = False
        else:
            text_display.draw_text(surface, 'Choose your character\'s race!')

        buttons.draw_buttons(surface, button_texts, button_rects, mouse_pos)

        pygame.display.update()

def define_race(race_name):
    if race_name == "Hill Dwarf":
        return define_hill_dwarf()
    if race_name == "Mountain Dwarf":
       return define_mountain_dwarf()
    if race_name == "High Elf":
        return define_high_elf()
    if race_name == "Wood Elf":
        return define_wood_elf()
    if race_name == "Lightfoot Halfling":
        return define_lightfoot_halfling()
    if race_name == "Stout Halfling":
        return define_stout_halfling()
    if race_name == "Human":
        return define_human()
    return 

def define_gender():
    button_texts = ["Male", "Female"]
    button_rects = buttons.create_button_rects(len(button_texts))
    
    animate_flag = True  # Flag to control text animation
    
    while True:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(button_rects):
                    if rect.collidepoint(mouse_pos):
                        return button_texts[i]
                    

        surface.fill(const.BG_COLOR)

        if animate_flag:
            text_display.animate_text(surface, 'Choose your character\'s gender!')
            animate_flag = False
        else:
            text_display.draw_text(surface, 'Choose your character\'s gender!')

        buttons.draw_buttons(surface, button_texts, button_rects, mouse_pos)

        pygame.display.update()

def define_hill_dwarf():
    name = ""
    gender = ""
    race = "Dwarf"
    subrace = "Hill Dwarf"
    size = "Medium"
    speed = 25
    languages = ["Common", "Dwarvish"]
    ability_score_increase = [2, 0, 0, 0, 1, 0]
    traits = ["Darkvision", "Dwarven Resilience", "Dwarven Combat Training", "Stonecunning", "Tool Proficiency", "Dwarven Toughness"]
    proficiencies = ["Battleaxe", "Handaxe", "Light Hammer", "Warhammer"]

    gender = define_gender()
    name = define_dwarf_name(gender)
    tool_proficiency = get_dwarf_tool_proficiency()

    proficiencies.append(tool_proficiency)

    hill_dwarf = Race(name, gender, race, subrace, size , speed, languages, ability_score_increase, traits, proficiencies)
    return hill_dwarf

def define_mountain_dwarf():
    name = ""
    gender = ""
    race = "Dwarf"
    subrace = "Mountain Dwarf"
    size = "Medium"
    speed = 25
    languages = ["Common", "Dwarvish"]
    ability_score_increase = [2, 2, 0, 0, 0, 0]
    traits = ["Darkvision", "Dwarven Resilience", "Dwarven Combat Training", "Stonecunning", "Tool Proficiency", "Dwarven Armor Training"]
    proficiencies = ["Battleaxe", "Handaxe", "Light Hammer", "Warhammer", "Light Armor", "Medium Armor"]

    gender = define_gender()
    name = define_dwarf_name(gender)
    tool_proficiency = get_dwarf_tool_proficiency()

    proficiencies.append(tool_proficiency)

    mountain_dwarf = Race(name, gender, race, subrace, size , speed, languages, ability_score_increase, traits, proficiencies)
    return mountain_dwarf

def define_dwarf_name(gender):
    button_texts = ["Click to Continue"]
    button_rects = buttons.create_button_rects(len(button_texts))
    
    dwarf_male_names = ["Adrik", "Alberich", "Baern", "Barendd", "Brottor", "Bruenor", "Dain", "Darrak", "Delg", "Eberk", "Einkil", "Fargrim", "Flint", "Gardain", "Harbek", "Kildrak", "Morgran", "Orsik", "Oskar", "Rangrim", "Rurik", "Taklinn", "Thoradin", "Thorin", "Tordek", "Traubon", "Travok", "Ulfgar", "Veit", "Vondal"]
    dwarf_female_names = ["Amber", "Artin", "Audhild", "Bardryn", "Dagnal", "Diesa", "Eldeth", "Falkrunn", "Finellen", "Gunnloda", "Gurdis", "Helja", "Hlin", "Kathra", "Kristryd", "Ilde", "Liftrasa", "Mardred", "Riswynn", "Sannl", "Torbera", "Torgga", "Vistra"]
    dwarf_clan_names = ["Balderk", "Battlehammer", "Brawnanvil", "Dankil", "Fireforge", "Frostbeard", "Gorunn", "Holderhek", "Ironfist", "Loderr", "Lutgehr", "Rumnaheim", "Strakeln", "Torunn", "Ungart"]

    first_names = []
    if gender == "Male":
        first_names = dwarf_male_names
    if gender == "Female":
        first_names = dwarf_female_names

    clan_names = dwarf_clan_names

    first_name = random.choice(first_names) 
    clan_name = random.choice(clan_names)

    name = first_name + " " + clan_name

    
    animate_flag = True  # Flag to control text animation
    
    while True:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(button_rects):
                    if rect.collidepoint(mouse_pos):
                        return name
                    
        surface.fill(const.BG_COLOR)

        if animate_flag:
            text_display.animate_text(surface, f'Dwarves have a first name and a clan name. A dwarf\'s name is granted by a clan elder in accordance with tradition! Your name is {first_name} of clan {clan_name}')
            animate_flag = False
        else:
            text_display.draw_text(surface, f'Dwarves have a first name and a clan name. A dwarf\'s name is granted by a clan elder in accordance with tradition! Your name is {first_name} of clan {clan_name}')

        buttons.draw_buttons(surface, button_texts, button_rects, mouse_pos)

        pygame.display.update()

def get_dwarf_tool_proficiency():
    tool_proficiency_options = ["Smith's Tools", "Brewer's Supplies", "Mason's Tools"]
    button_texts = tool_proficiency_options
    button_rects = buttons.create_button_rects(len(button_texts))

    animate_flag = True

    while True:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(button_rects):
                    if rect.collidepoint(mouse_pos):
                        return button_texts[i]

        surface.fill(const.BG_COLOR)

        if animate_flag:
            text_display.animate_text(surface, 'Choose a tool proficiency!')
            animate_flag = False
        else:
            text_display.draw_text(surface, 'Choose a tool proficiency!')

        buttons.draw_buttons(surface, button_texts, button_rects, mouse_pos)

        pygame.display.update()

def define_high_elf():
    name = ""
    gender = ""
    race = "Elf"
    subrace = "High Elf"
    size = "Medium"
    speed = 30
    languages = ["Common", "Elvish"]
    ability_score_increase = [0, 0, 2, 1, 0, 0]
    traits = ["Darkvision", "Keen Senses", "Fey Ancestry", "Trance", "Elf Weapon Training", "Cantrip", "Extra Language"]
    proficiencies = ["Longsword", "Shortsword", "Longbow", "Shortbow"]

    gender = define_gender()
    name = define_elf_name(gender)
    language = choose_languages()
    languages.append(language)

    high_elf = Race(name, gender, race, subrace, size , speed, languages, ability_score_increase, traits, proficiencies)
    return high_elf

def define_wood_elf():
    name = ""
    gender = ""
    race = "Elf"
    subrace = "Wood Elf"
    size = "Medium"
    speed = 35
    languages = ["Common", "Elvish"]
    ability_score_increase = [0, 0, 2, 0, 1, 0]
    traits = ["Darkvision", "Keen Senses", "Fey Ancestry", "Trance", "Elf Weapon Training", "Fleet of Foot", "Mast of the Wild"]
    proficiencies = ["Longsword", "Shortsword", "Longbow", "Shortbow"]

    gender = define_gender()
    name = define_elf_name(gender)

    wood_elf = Race(name, gender, race, subrace, size , speed, languages, ability_score_increase, traits, proficiencies)
    return wood_elf

def define_elf_name(gender):
    button_texts = ["Click to Continue..."]
    button_rects = buttons.create_button_rects(len(button_texts))
    
    elf_child_names = ["Ara", "Bryn", "Del", "Eryn", "Faen", "Innil", "Lael", "Mella", "Naill", "Naeris", "Phann", "Rael", "Rinn", "Sai", "Syllin", "Thia", "Vall"]
    elf_male_names = ["Adran", "Aelar", "Aramil", "Arannis", "Aust", "Beiro", "Berrian", "Carric", "Enialis", "Erdan", "Erevan", "Galinndan", "Hadarai", "Heian", "Himo", "Immeral", "Ivellios", "Laucian", "Mindartis", "Paelias", "Peren", "Quarion", "Riardon", "Rolen", "Soveliss", "Thamior", "Tharivol", "Theren", "Varis"]
    elf_female_names = ["Adrie", "Althaea", "Anastrianna", "Andraste", "Antinua", "Bethrynna", "Birel", "Caelynn", "Drusilia", "Enna", "Felosial", "Ielenia", "Jelenneth", "Keyleth", "Leshanna", "Lia", "Meriele", "Mialee", "Naivara", "Quelenna", "Quillathe", "Sariel", "Shanairra", "Shava", "Silaqui", "Theirastra", "Thia", "Vadania", "Valanthe", "Xanaphia"]
    elf_family_names = ["Amakiir", "Amastacia", "Galanodel", "Holimion", "Ilphelkiir", "Liadon", "Meliamne", "Nai'lo", "Siannodel", "Xiloscient"]
    
    first_names = []
    if gender == "Male":
        first_names = elf_male_names
    if gender == "Female":
        first_names = elf_female_names

    family_names = elf_family_names

    family_name = random.choice(family_names)

    
    animate_flag = True  # Flag to control text animation

    if is_elf_child():
        first_name = random.choice(elf_child_names)
    else:
        first_name = choose_elf_first_name(first_names)

    name = first_name + " " + family_name
    
    while True:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(button_rects):
                    if rect.collidepoint(mouse_pos):
                        return name
                    
        surface.fill(const.BG_COLOR)

        if animate_flag:
            text_display.animate_text(surface, f'Your name is {first_name} of clan {family_name}')
            animate_flag = False
        else:
            text_display.draw_text(surface, f'Your name is {first_name} of clan {family_name}')

        buttons.draw_buttons(surface, button_texts, button_rects, mouse_pos)

        pygame.display.update()

def choose_elf_first_name(first_names):
    button_texts = first_names
    button_rects = buttons.create_button_rects(len(button_texts))
    
    animate_flag = True  # Flag to control text animation

    first_name = None

    while True:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(button_rects):
                    if rect.collidepoint(mouse_pos):
                        first_name = button_texts[i]
                        return first_name
                    
        surface.fill(const.BG_COLOR)

        if animate_flag:
            text_display.animate_text(surface, 'Choose your elf\'s first name!')
            animate_flag = False
        else:
            text_display.draw_text(surface, 'Choose your elf\'s first name!')

        buttons.draw_buttons(surface, button_texts, button_rects, mouse_pos)

        pygame.display.update()

def is_elf_child():
    button_texts = ["Yes", "No"]
    button_rects = buttons.create_button_rects(len(button_texts))
    
    animate_flag = True  # Flag to control text animation

    is_child = None

    while True:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(button_rects):
                    if rect.collidepoint(mouse_pos):
                        if button_texts[i] == "Yes":
                            is_child = True
                        else:
                            is_child = False
                        return is_child
                    
        surface.fill(const.BG_COLOR)

        if animate_flag:
            text_display.animate_text(surface, 'Is your elf a child?')
            animate_flag = False
        else:
            text_display.draw_text(surface, 'Is your elf a child?')

        buttons.draw_buttons(surface, button_texts, button_rects, mouse_pos)

        pygame.display.update()

def choose_languages():
    languages = ["Arakora", "Abyssal/Infernal", "Aquan", "Auran", "Celestial", "Deep Speech", "Draconic", "Druidic", "Dwarvish", "Giant/Jotun", "Gith", "Gnoll", "Gnomish", "Goblin", "Halfling", "Orcish", "Primordial", "Sylvan", "Terran", "Undercommon"]
    button_texts = languages
    button_rects = buttons.create_button_rects(len(button_texts))

    animate_flag = True

    while True:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(button_rects):
                    if rect.collidepoint(mouse_pos):
                        return button_texts[i]

        surface.fill(const.BG_COLOR)

        if animate_flag:
            text_display.animate_text(surface, 'Choose an additional language to be proficient in...')
            animate_flag = False
        else:
            text_display.draw_text(surface, 'Choose an additional language to be proficient in...')

        buttons.draw_buttons(surface, button_texts, button_rects, mouse_pos)

        pygame.display.update()

def define_lightfoot_halfling():
    name = ""
    gender = ""
    race = "Halfling"
    subrace = "Lightfoot Halfling"
    size = "Small"
    speed = 25
    languages = ["Common", "Halfling"]
    ability_score_increase = [0, 0, 2, 0, 0, 1]
    traits = ["Lucky", "Brave", "Halfling Nimbleness", "Naturally Stealthy"]
    proficiencies = ["None"]

    gender = define_gender()
    name = define_halfling_name(gender)

    lightfoot_halfling = Race(name, gender, race, subrace, size , speed, languages, ability_score_increase, traits, proficiencies)
    return lightfoot_halfling

def define_stout_halfling():
    name = ""
    gender = ""
    race = "Halfling"
    subrace = "Stout Halfling"
    size = "Small"
    speed = 25
    languages = ["Common", "Halfling"]
    ability_score_increase = [1, 0, 2, 0, 0, 0]
    traits = ["Lucky", "Brave", "Halfling Nimbleness", "Stout Resilience"]
    proficiencies = ["None"]

    gender = define_gender()
    name = define_halfling_name(gender)

    stout_halfling = Race(name, gender, race, subrace, size , speed, languages, ability_score_increase, traits, proficiencies)
    return stout_halfling

def define_halfling_name(gender):
    name = ""
    first_name = ""
    family_name = ""
    nickname = ""
    random_chance = random.randint(0, 1)
    halfling_male_names = ["Alton", "Ander", "Cade", "Corrin", "Eldon", "Errich", "Finnan", "Garret", "Lindal", "Lyle", "Merric", "Milo", "Osborn", "Perrin", "Reed", "Roscoe", "Wellby"]
    halfling_female_names = ["Andry", "Bree", "Callie", "Cora", "Euphemia", "Jillian", "Kithri", "Lavinia", "Lidda", "Merla", "Nedda", "Paela", "Portia", "Seraphina", "Shaena", "Trym", "Vani", "Verna"]
    halfling_family_names = ["Brushgather", "Goodbarrel", "Greenbottle", "High-hill", "Hilltopple", "Leagallow", "Tealeaf", "Thorngage", "Tosscobble", "Underbough"]

    if gender == "Male":
        first_name = random.choice(halfling_male_names)
    else:
        first_name = random.choice(halfling_female_names)

    family_name = random.choice(halfling_family_names)

    if random_chance == 1:
        nickname = get_halfling_nickname()
        name = first_name + " '" + nickname + "' " + family_name
    else :
        nickname = "None"
        name = first_name + " " + family_name

    button_texts = ["Click to Continue..."]
    button_rects = buttons.create_button_rects(len(button_texts))

    animate_flag = True

    while True:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(button_rects):
                    if rect.collidepoint(mouse_pos):
                        return name
                    
        surface.fill(const.BG_COLOR)

        if nickname == "None":
            if animate_flag:
                text_display.animate_text(surface, f'Your halfling\'s name is {first_name} of the family {family_name}.')
                animate_flag = False
            else:
                text_display.draw_text(surface, f'Your halfling\'s name is {first_name} of the family {family_name}.')
        else:
            if animate_flag:
                text_display.animate_text(surface, f'Your halfling\'s name is {first_name} of the family {family_name}, but you prefer to go by {nickname}')
                animate_flag = False
            else:
                text_display.draw_text(surface, f'Your halfling\'s name is {first_name} of the family {family_name}, but you prefer to go by {nickname}')
        buttons.draw_buttons(surface, button_texts, button_rects, mouse_pos)

        pygame.display.update()

def get_halfling_nickname():
    return "JimBob"
    
def define_human():
    name = ""
    gender = ""
    race = "Human"
    subrace = "Human"
    size = "Medium"
    speed = 30
    languages = ["Common"]
    ability_score_increase = [1, 1, 1, 1, 1, 1]
    traits = ["None"]
    proficiencies = ["None"]

    gender = define_gender()
    name = define_human_name(gender)

    human = Race(name, gender, race, subrace, size , speed, languages, ability_score_increase, traits, proficiencies)
    return human

def define_human_name(gender):
    if gender == "Male":
        return "Jon Snow"
    else:
        return "Daenerys Targaryen"