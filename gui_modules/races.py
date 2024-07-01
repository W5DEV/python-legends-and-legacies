import pygame
import sys
import random
import gui.constants as constants  # Import the constants module
import gui.text_display as text_display  # Import the text_display module
import gui.buttons as buttons  # Import the buttons module

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT
BG_COLOR = constants.BG_COLOR
TEXT_COLOR = constants.TEXT_COLOR
FONT_SIZE = constants.FONT_SIZE
MARGIN = constants.MARGIN
TEXT_AREA_WIDTH = constants.TEXT_AREA_WIDTH
TEXT_AREA_HEIGHT = constants.TEXT_AREA_HEIGHT

# Setup screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('UI Example')
font = pygame.font.SysFont(None, FONT_SIZE)

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
    button_rects = buttons.create_button_rects(SCREEN_WIDTH, SCREEN_HEIGHT, len(button_texts))
    text_position = (MARGIN, MARGIN)
    
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
                        text_display.animate_text(screen, f'You chose {button_texts[i]}!', text_position, TEXT_AREA_WIDTH)
                        return define_race(button_texts[i])
                    

        screen.fill(BG_COLOR)

        if animate_flag:
            text_display.animate_text(screen, 'Choose your character\'s race!', text_position, TEXT_AREA_WIDTH)
            animate_flag = False
        else:
            text_display.draw_text(screen, 'Choose your character\'s race!', text_position, TEXT_AREA_WIDTH)

        buttons.draw_buttons(screen, button_texts, button_rects, mouse_pos)

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
    button_rects = buttons.create_button_rects(SCREEN_WIDTH, SCREEN_HEIGHT, len(button_texts))
    text_position = (MARGIN, MARGIN)
    
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
                    

        screen.fill(BG_COLOR)

        if animate_flag:
            text_display.animate_text(screen, 'Choose your character\'s gender!', text_position, TEXT_AREA_WIDTH)
            animate_flag = False
        else:
            text_display.draw_text(screen, 'Choose your character\'s gender!', text_position, TEXT_AREA_WIDTH)

        buttons.draw_buttons(screen, button_texts, button_rects, mouse_pos)

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
    button_rects = buttons.create_button_rects(SCREEN_WIDTH, SCREEN_HEIGHT, len(button_texts))
    
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

    text_position = (MARGIN, MARGIN)
    
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
                    
        screen.fill(BG_COLOR)

        if animate_flag:
            text_display.animate_text(screen, f'Dwarves have a first name and a clan name. A dwarf\'s name is granted by a clan elder in accordance with tradition! Your name is {first_name} of clan {clan_name}', text_position, TEXT_AREA_WIDTH)
            animate_flag = False
        else:
            text_display.draw_text(screen, f'Dwarves have a first name and a clan name. A dwarf\'s name is granted by a clan elder in accordance with tradition! Your name is {first_name} of clan {clan_name}', text_position, TEXT_AREA_WIDTH)

        buttons.draw_buttons(screen, button_texts, button_rects, mouse_pos)

        pygame.display.update()

def get_dwarf_tool_proficiency():
    tool_proficiency_options = ["Smith's Tools", "Brewer's Supplies", "Mason's Tools"]
    button_texts = tool_proficiency_options
    button_rects = buttons.create_button_rects(SCREEN_WIDTH, SCREEN_HEIGHT, len(button_texts))
    text_position = (MARGIN, MARGIN)

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

        screen.fill(BG_COLOR)

        if animate_flag:
            text_display.animate_text(screen, 'Choose a tool proficiency!', text_position, TEXT_AREA_WIDTH)
            animate_flag = False
        else:
            text_display.draw_text(screen, 'Choose a tool proficiency!', text_position, TEXT_AREA_WIDTH)

        buttons.draw_buttons(screen, button_texts, button_rects, mouse_pos)

        pygame.display.update()

    





