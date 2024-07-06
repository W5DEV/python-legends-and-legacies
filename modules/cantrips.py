import pygame
import sys
import gui.text_display as text_display
import gui.buttons as buttons
import gui.constants as const

# Initialize pygame
pygame.init()

# Setup screen
surface = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
pygame.display.set_caption('Cantrip Selection')

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
                        if rect.collidepoint(mouse_pos):
                            return button_texts[i]

        surface.fill(const.BG_COLOR)

        if animate_flag:
            text_display.animate_text(surface, 'Choose a cantrip below...')
            animate_flag = False
        else:
            text_display.draw_text(surface, 'Choose a cantrip below...')

        buttons.draw_buttons(surface, button_texts, button_rects, mouse_pos)

        pygame.display.update()


bard_cantrips = ["Dancing Lights", "Light", "Mage Hand", "Mending", "Message", "Minor Illusion", "Prestidigitation", "True Strike", "Vicious Mockery"]
cleric_cantrips = ["Guidance", "Light", "Mending", "Resistance", "Sacred Flame", "Spare the Dying", "Thaumaturgy"]
druid_cantrips = ["Druidcraft", "Guidance", "Mending", "Poison Spray", "Produce Flame", "Resistance", "Shillelagh"]
sorcerer_cantrips = ["Acid Splash", "Chill Touch", "Dancing Lights", "Fire Bolt", "Light", "Mage Hand", "Mending", "Message", "Minor Illusion", "Poison Spray", "Prestidigitation", "Ray of Frost", "Shocking Grasp", "True Strike"]
warlock_cantrips = ["Chill Touch", "Eldrich Blast", "Mage Hand", "Minor Illusion", "Poison Spray", "Prestidigitation", "True Strike"]
wizard_cantrips = ["Acid Splash", "Chill Touch", "Dancing Lights", "Fire Bolt", "Light", "Mage Hand", "Mending", "Message", "Minor Illusion", "Poison Spray", "Prestidigitation", "Ray of Frost", "Shocking Grasp", "True Strike"]
