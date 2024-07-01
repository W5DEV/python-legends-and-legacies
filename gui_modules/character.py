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

class Character:
    def __init__(self):
        self.name = ""
        self.race = None
        self.archetype = None
        self.bio = None
        self.equipment = None
        self.level = 0
        self.equipped_armor = None
        self.equippped_weapon = None
        self.readied_weapon = None
        self.proficincy_bonus = 0
        self.strength = 0
        self.strength_mod = 0
        self.dexterity = 0
        self.dexterity_mod = 0
        self.constitution = 0
        self.constitution_mod = 0
        self.intelligence = 0
        self.intelligence_mod = 0
        self.wisdom = 0
        self.wisdom_mod = 0
        self.charisma = 0
        self.charisma_mod = 0
        self.equipped_armor = None
        self.equipped_weapon = []
        self.readied_weapon = None
        self.equipped_shield = None
        self.xp = 0
        self.gp = 0
        self.hp = 0
        self.max_base_hp = 0
        self.max_hp = 0

    def announce_character(self):
        button_texts = ["Click to Continue..."]
        button_rects = buttons.create_button_rects(SCREEN_WIDTH, SCREEN_HEIGHT, len(button_texts))
        text_position = (MARGIN, MARGIN)
        player_equipment_names = ""
        i = 0
        for equipment in self.archetype.starting_equipment:
            if i == 0:
                player_equipment_names += f'{equipment.name}'
            player_equipment_names += f', {equipment.name}'
            i += 1

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
                            return

            screen.fill(BG_COLOR)

            if animate_flag:
                text_display.animate_text(screen, f'{self.name} is a {self.race.subrace} {self.archetype.name}. They currently have {player_equipment_names}.', text_position, TEXT_AREA_WIDTH)
                animate_flag = False
            else:
                text_display.draw_text(screen, f'{self.name} is a {self.race.subrace} {self.archetype.name}. They currently have {player_equipment_names}.', text_position, TEXT_AREA_WIDTH)

            buttons.draw_buttons(screen, button_texts, button_rects, mouse_pos)

            pygame.display.update()