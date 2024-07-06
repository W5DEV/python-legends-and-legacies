import pygame
import sys
import gui.text_display as text_display
import gui.buttons as buttons
import gui.constants as const
import archetypes.barbarian as barbarian
import archetypes.bard as bard
import archetypes.cleric as cleric
import archetypes.druid as druid
import archetypes.fighter as fighter
import archetypes.monk as monk
import archetypes.paladin as paladin
import archetypes.ranger as ranger
import archetypes.rogue as rogue
import archetypes.sorcerer as sorcerer
import archetypes.warlock as warlock
import archetypes.wizard as wizard

# Initialize pygame
pygame.init()

# Setup screen
surface = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
pygame.display.set_caption('Class Selection')

archetypes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]

def select_archetype():
    button_texts = archetypes
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
                    

        surface.fill(const.BG_COLOR)

        if animate_flag:
            text_display.animate_text(surface, 'Choose your character\'s class!')
            animate_flag = False
        else:
            text_display.draw_text(surface, 'Choose your character\'s class!')

        buttons.draw_buttons(surface, button_texts, button_rects, mouse_pos)

        pygame.display.update()
