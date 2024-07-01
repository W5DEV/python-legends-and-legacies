import pygame
import sys
import gui.constants as constants  # Import the constants module
import gui.text_display as text_display  # Import the text_display module
import gui.buttons as buttons  # Import the buttons module
import modules.dice_rolls as dice_rolls

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

# This function will roll 4 six-sided dice, drop the lowest value, and return the sum of the remaining 3 dice
def roll_ability():
    initial_roll = [dice_rolls.roll_6_sided_dice(), dice_rolls.roll_6_sided_dice(), dice_rolls.roll_6_sided_dice(), dice_rolls.roll_6_sided_dice()]
    initial_roll.remove(min(initial_roll))
    return initial_roll[0] + initial_roll[1] + initial_roll[2]

def calculate_abilities(player):
    roll_1 = roll_ability()
    roll_2 = roll_ability()
    roll_3 = roll_ability()
    roll_4 = roll_ability()
    roll_5 = roll_ability()
    roll_6 = roll_ability()
    rolls = [roll_1, roll_2, roll_3, roll_4, roll_5, roll_6]
    rolls.sort(reverse=True)
    available_abilities = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]

    button_texts = available_abilities
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
                        if button_texts[i] == "Strength":
                            player.strength = rolls.pop(0)
                            button_texts.remove("Strength")
                        elif button_texts[i] == "Dexterity":
                            player.dexterity = rolls.pop(0)
                            button_texts.remove("Dexterity")
                        elif button_texts[i] == "Constitution":
                            player.constitution = rolls.pop(0)
                            button_texts.remove("Constitution")
                        elif button_texts[i] == "Intelligence":
                            player.intelligence = rolls.pop(0)
                            button_texts.remove("Intelligence")
                        elif button_texts[i] == "Wisdom":
                            player.wisdom = rolls.pop(0)
                            button_texts.remove("Wisdom")
                        elif button_texts[i] == "Charisma":
                            player.charisma = rolls.pop(0)
                            button_texts.remove("Charisma")
                        
                        pygame.display.update()
                        if len(rolls) == 0:
                            return
                    

        screen.fill(BG_COLOR)

        if animate_flag:
            text_display.animate_text(screen, f'Your available rolls are: {rolls}. Choose which ability to assign the highest roll...', text_position, TEXT_AREA_WIDTH)
            animate_flag = False
        else:
            text_display.draw_text(screen, f'Your available rolls are: {rolls}. Choose which ability to assign the highest roll...', text_position, TEXT_AREA_WIDTH)

        buttons.draw_buttons(screen, button_texts, button_rects, mouse_pos)

        pygame.display.update()