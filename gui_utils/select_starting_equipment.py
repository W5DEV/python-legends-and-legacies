import pygame
import sys
import gui.text_display as text_display
import gui.buttons as buttons
import gui.constants as constants
import gui_utils.equipment as equipment

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

def weapon_choices(choices):
    button_texts = choices
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
                        if rect.collidepoint(mouse_pos):
                            return choices[i]

        screen.fill(BG_COLOR)

        if animate_flag:
            text_display.animate_text(screen, 'Choose from the starting equipment items below...', text_position, TEXT_AREA_WIDTH)
            animate_flag = False
        else:
            text_display.draw_text(screen, 'Choose from the starting equipment items below...', text_position, TEXT_AREA_WIDTH)

        buttons.draw_buttons(screen, button_texts, button_rects, mouse_pos)

        pygame.display.update()

def get_weapons_from_category(category):
    if category == "Simple Melee Weapons":
        return select_weapon_from_category(equipment.simple_melee_weapons)
    if category == "Simple Ranged Weapons":
        return select_weapon_from_category(equipment.simple_ranged_weapons)
    if category == "Simple Weapons":
        return select_weapon_from_category(equipment.simple_weapons)
    if category == "Martial Melee Weapons":
        return select_weapon_from_category(equipment.martial_melee_weapons)
    if category == "Martial Ranged Weapons":
        return select_weapon_from_category(equipment.martial_ranged_weapons)
    if category == "Martial Weapons":
        return select_weapon_from_category(equipment.martial_weapons)
    if category == "Light Armor":
        return select_weapon_from_category(equipment.light_armor)
    if category == "Medium Armor":
        return select_weapon_from_category(equipment.medium_armor)
    if category == "Heavy Armor":
        return select_weapon_from_category(equipment.heavy_armor)
    if category == "Shields":
        return select_weapon_from_category(equipment.shields)
    if category == "Instruments":
        return select_weapon_from_category(equipment.instruments)
    if category == "Holy Symbols":
        return select_weapon_from_category(equipment.holy_symbols)
    if category == "Packs":
        return select_weapon_from_category(equipment.packs)
    if category == "Artisan's Tools":
        return select_weapon_from_category(equipment.artisans_tools)
    if category == "Other Tools":
        return select_weapon_from_category(equipment.other_tools)
    if category == "Class Equipment":
        return select_weapon_from_category(equipment.class_equipment)

def select_weapon_from_category(weapons):
    weapon_names = []
    for weapon in weapons:
        weapon_names.append(weapon.name)
    
    button_texts = weapon_names
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
                        return weapons[i]
                        
        screen.fill(BG_COLOR)

        if animate_flag:
            text_display.animate_text(screen, 'Choose an item from the equipment category below...', text_position, TEXT_AREA_WIDTH)
            animate_flag = False
        else:
            text_display.draw_text(screen, 'Choose an item from the equipment category below...', text_position, TEXT_AREA_WIDTH)

        buttons.draw_buttons(screen, button_texts, button_rects, mouse_pos)

        pygame.display.update()