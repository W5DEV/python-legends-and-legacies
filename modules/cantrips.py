import pygame
import sys
import gui.text_display as text_display
import gui.buttons as buttons
import gui.constants as constants

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

def cantrip_choices(archetype):
    if archetype == "Bard":
        return bard_cantrips
    if archetype == "Cleric":
        return cleric_cantrips
    if archetype == "Druid":
        return druid_cantrips
    if archetype == "Sorcerer":
        return sorcerer_cantrips
    if archetype == "Warlock":
        return warlock_cantrips
    if archetype == "Wizard":
        return wizard_cantrips

def select_cantrips(archetype):
    button_texts = cantrip_choices(archetype)
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
                            return button_texts[i]

        screen.fill(BG_COLOR)

        if animate_flag:
            text_display.animate_text(screen, 'Choose a cantrip below...', text_position, TEXT_AREA_WIDTH)
            animate_flag = False
        else:
            text_display.draw_text(screen, 'Choose a cantrip below...', text_position, TEXT_AREA_WIDTH)

        buttons.draw_buttons(screen, button_texts, button_rects, mouse_pos)

        pygame.display.update()


bard_cantrips = ["Dancing Lights", "Light", "Mage Hand", "Mending", "Message", "Minor Illusion", "Prestidigitation", "True Strike", "Vicious Mockery"]
cleric_cantrips = ["Guidance", "Light", "Mending", "Resistance", "Sacred Flame", "Spare the Dying", "Thaumaturgy"]
druid_cantrips = ["Druidcraft", "Guidance", "Mending", "Poison Spray", "Produce Flame", "Resistance", "Shillelagh"]
sorcerer_cantrips = ["Acid Splash", "Chill Touch", "Dancing Lights", "Fire Bolt", "Light", "Mage Hand", "Mending", "Message", "Minor Illusion", "Poison Spray", "Prestidigitation", "Ray of Frost", "Shocking Grasp", "True Strike"]
warlock_cantrips = ["Chill Touch", "Eldrich Blast", "Mage Hand", "Minor Illusion", "Poison Spray", "Prestidigitation", "True Strike"]
wizard_cantrips = ["Acid Splash", "Chill Touch", "Dancing Lights", "Fire Bolt", "Light", "Mage Hand", "Mending", "Message", "Minor Illusion", "Poison Spray", "Prestidigitation", "Ray of Frost", "Shocking Grasp", "True Strike"]
