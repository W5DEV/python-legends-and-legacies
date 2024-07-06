import pygame
import sys
import gui.text_display as text_display
import gui.buttons as buttons
import gui.constants as const
import modules.dice_rolls as dice_rolls
import modules.utils as utils

# Initialize pygame
pygame.init()

# Setup screen
surface = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
pygame.display.set_caption('Character Profile')

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

    def initialize_player(self):
        self.calculate_level()
        self.calculate_modifiers()
        self.sync_max_base_hp()
        self.calculate_max_hp()
        self.hp = self.max_hp
        self.calculate_proficiency_bonus()
        return

    def award_xp(self, xp):
        self.xp += xp
        print(f'{self.name} has been awarded {xp} experience points.')
        current_level = self.level
        print(f'{self.name} is currently level {current_level}.')
        self.calculate_level()
        print(f'{self.name} is now level {self.level}.')
        if current_level < self.level:
            self.sync_level()
            print(f'{self.name} has leveled up!')
            self.sync_max_base_hp()
            print(f'{self.name} has {self.max_base_hp} base hit points.')
            self.calculate_max_hp()
            print(f'{self.name} has {self.max_hp} hit points.')
            self.calculate_proficiency_bonus()
            print(f'{self.name} has a proficiency bonus of {self.proficiency_bonus}.')
        return
    
    def calculate_modifiers(self):
        self.strength_mod = (self.strength - 10) // 2
        self.dexterity_mod = (self.dexterity - 10) // 2
        self.constitution_mod = (self.constitution - 10) // 2
        self.intelligence_mod = (self.intelligence - 10) // 2
        self.wisdom_mod = (self.wisdom - 10) // 2
        self.charisma_mod = (self.charisma - 10) // 2
        return

    def sync_max_base_hp(self):
        if self.level == 1:
            self.max_base_hp = self.archetype.base_hp
        else:
            if self.archetype.hit_die == "1d6":
                roll = dice_rolls.roll_6_sided_dice()
                if roll < 3:
                    roll = dice_rolls.roll_6_sided_dice()
                self.max_base_hp += roll
            elif self.archetype.hit_die == "1d8":
                roll = dice_rolls.roll_8_sided_dice()
                if roll < 3:
                    roll = dice_rolls.roll_8_sided_dice()
                self.max_base_hp += roll
            elif self.archetype.hit_die == "1d10":
                roll = dice_rolls.roll_10_sided_dice()
                if roll < 3:
                    roll = dice_rolls.roll_10_sided_dice()
                self.max_base_hp += roll
            elif self.archetype.hit_die == "1d12":
                roll = dice_rolls.roll_12_sided_dice()
                if roll < 3:
                    roll = dice_rolls.roll_12_sided_dice()
                self.max_base_hp += roll
        return
    
    def calculate_max_hp(self):
        self.max_hp = self.max_base_hp + (self.constitution_mod * self.level)
        return

    def calculate_level(self):
        level = utils.calculate_level(self.xp)
        self.level = level
        return 
    
    def calculate_armor_class(self):
        base_ac = 10
        dex_mod = self.dexterity_mod
        if self.equipped_armor == None:
            armor_bonus = 0
        else:
            armor_bonus = self.equipped_armor.ac
        if self.equipped_shield == None:
            shield_bonus = 0
        else:
            shield_bonus = self.equipped_shield.ac
        armor_class = base_ac + dex_mod + armor_bonus + shield_bonus
        return armor_class

    def calculate_proficiency_bonus(self):
        self.calculate_level()
        level = self.level
        self.proficiency_bonus = (-(-level // 4)) + 1
        return

    def sync_level(self):
        self.calculate_level()
        self.archetype.sync_level(self.level, self)
        return

    def sync_equipment(self):
        self.equipment = self.archetype.starting_equipment
        return
    
    def xp_needed_for_next_level(self):
        xp_needed = utils.calculate_xp_needed(self.xp)
        return xp_needed
    
    def increase_ability_score(self):
        button_texts = [f"Strength: {self.strength}", f"Dexterity:{self.dexterity}", f"Constitution: {self.constitution}", f"Intelligence: {self.intelligence}", f"Wisdom: {self.wisdom}", f"Charisma: {self.charisma}"]
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
                            if button_texts[i] == f"Strength: {self.strength}":
                                self.strength += 1
                                self.calculate_modifiers()
                                return
                            elif button_texts[i] == f"Dexterity:{self.dexterity}":
                                self.dexterity += 1
                                self.calculate_modifiers()
                                return
                            elif button_texts[i] == f"Constitution: {self.constitution}":
                                self.constitution += 1
                                self.calculate_modifiers()
                                return
                            elif button_texts[i] == f"Intelligence: {self.intelligence}":
                                self.intelligence += 1
                                self.calculate_modifiers()
                                return
                            elif button_texts[i] == f"Wisdom: {self.wisdom}":
                                self.wisdom += 1
                                self.calculate_modifiers()
                                return
                            elif button_texts[i] == f"Charisma: {self.charisma}":
                                self.charisma += 1
                                self.calculate_modifiers()
                                return

            surface.fill(const.BG_COLOR)

            if animate_flag:
                text_display.animate_text(surface, f'Choose which ability to increase by 1...')
                animate_flag = False
            else:
                text_display.draw_text(surface, f'Choose which ability to increase by 1...')

            buttons.draw_buttons(surface, button_texts, button_rects, mouse_pos)

            pygame.display.update()

    def update_ability_points(self, number):
        for i in range(number):
            self.increase_ability_score()
        return


    def announce_character(self):
        button_texts = ["Click to Continue..."]
        button_rects = buttons.create_button_rects(len(button_texts))
        player_equipment_names = ""
        i = 0
        for equipment in self.archetype.starting_equipment:
            if i == 0:
                player_equipment_names += f'{equipment.name}'
            else:
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
                            print(f'Game over! Thanks for playing!')
                            return

            surface.fill(const.BG_COLOR)

            if animate_flag:
                text_display.animate_text(surface, f'{self.name} is a level {self.level} {self.race.subrace} {self.archetype.name} with a total of {self.xp} Experience Points. They currently have a {player_equipment_names}.')
                animate_flag = False
            else:
                text_display.draw_text(surface, f'{self.name} is a level {self.level} {self.race.subrace} {self.archetype.name} with a total of {self.xp} Experience Points. They currently have a {player_equipment_names}.')

            buttons.draw_buttons(surface, button_texts, button_rects, mouse_pos)

            pygame.display.update()