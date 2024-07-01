import pygame
import sys
import gui.text_display as text_display
import gui.buttons as buttons
import gui.constants as constants
import gui_archetypes.barbarian as barbarian
import gui_archetypes.bard as bard
import gui_archetypes.cleric as cleric
import gui_archetypes.druid as druid
import gui_archetypes.fighter as fighter
import gui_archetypes.monk as monk
import gui_archetypes.paladin as paladin
import gui_archetypes.ranger as ranger
import gui_archetypes.rogue as rogue
import gui_archetypes.sorcerer as sorcerer
import gui_archetypes.warlock as warlock
import gui_archetypes.wizard as wizard

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

archetypes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]

def select_archetype():
    button_texts = archetypes
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
                        if button_texts[i] == "Barbarian":
                            return barbarian.define_barbarian()
                        elif button_texts[i] == "Bard":
                            return bard.define_bard()
                        elif button_texts[i] == "Cleric":
                            return cleric.define_cleric()
                        elif button_texts[i] == "Druid":
                            return druid.define_druid()
                        elif button_texts[i] == "Fighter":
                            return fighter.define_fighter()
                        elif button_texts[i] == "Monk":
                            return monk.define_monk()
                        elif button_texts[i] == "Paladin":
                            return paladin.define_paladin()
                        elif button_texts[i] == "Ranger":
                            return ranger.define_ranger()
                        elif button_texts[i] == "Rogue":
                            return rogue.define_rogue()
                        elif button_texts[i] == "Sorcerer":
                            return sorcerer.define_sorcerer()
                        elif button_texts[i] == "Warlock":
                            return warlock.define_warlock()
                        elif button_texts[i] == "Wizard":
                            return wizard.define_wizard()
                    

        screen.fill(BG_COLOR)

        if animate_flag:
            text_display.animate_text(screen, 'Choose your character\'s class!', text_position, TEXT_AREA_WIDTH)
            animate_flag = False
        else:
            text_display.draw_text(screen, 'Choose your character\'s class!', text_position, TEXT_AREA_WIDTH)

        buttons.draw_buttons(screen, button_texts, button_rects, mouse_pos)

        pygame.display.update()
