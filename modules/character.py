import pygame
import sys
import gui.text_display as text_display
import gui.buttons as buttons
import gui.constants as constants
import modules.dice_rolls as dice_rolls
import modules.utils as utils
import modules.equipment as equipment

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
        current_level = self.level
        self.calculate_level()
        if current_level < self.level:
            self.sync_level()
            self.sync_max_base_hp()
            self.calculate_max_hp()
            self.calculate_proficiency_bonus()
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
    
    def equip_armor(self):
        selected_item = ""
        valid_choices = []
        if self.equipped_armor == None:
            print("You do not have any armor to equip.")
            return
        print("Please choose an armor type from the following list:")
        for item in self.equipment:
            if item in equipment.armor:
                print(item.name)
                valid_choices.append(item.name.lower())
        selected_item = input("> ")
        while selected_item.lower() not in valid_choices:
            print("Sorry, that is not a valid choice. Please try again.")
            print("Please choose an armor type from the following list:")
            for item in self.equipment:
                if item in equipment.armor:
                    print(item.name)
            selected_item = input("> ")
        for item in self.equipment:
            if item.name.lower() == selected_item.lower():
                self.equipped_armor = item
                print(f"You have equipped {self.equipped_armor.name}.")
                return
        print("You do not have any armor equipped.")
        return
    
    def unequip_armor(self):
        if self.equipped_armor == None:
            print("You do not have any armor equipped.")
            return
        self.equipped_armor = None
        print("You have unequipped your armor.")
        return
    
    def equip_weapon(self):
        selected_item = ""
        valid_choices = []
        if self.equipped_weapon == None:
            print("You do not have any weapons to equip.")
            return
        print("Please choose a weapon from the following list:")
        for item in self.equipment:
            if item in equipment.weapons:
                print(item.name)
                valid_choices.append(item.name.lower())
        selected_item = input("> ")
        while selected_item.lower() not in valid_choices:
            print("Sorry, that is not a valid choice. Please try again.")
            print("Please choose a weapon from the following list:")
            for item in self.equipment:
                if item in equipment.weapons:
                    print(item.name)
            selected_item = input("> ")
        for item in self.equipment:
            if item.name.lower() == selected_item.lower():
                self.equipped_weapon.append(item)
                print(f"You have equipped {item.name}.")
                print("You have the following weapons equipped:")
                for weapon in self.equipped_weapon:
                    print(weapon.name)
                return
        print("You have not equipped any weapons.")
        return
    
    def unequip_weapon(self):
        if self.equipped_weapon == []:
            print("You do not have any weapons equipped.")
            return
        print("Please choose a weapon to unequip from the following list:")
        valid_choices = []
        for weapon in self.equipped_weapon:
            print(weapon.name)
            valid_choices.append(weapon.name.lower())
        selected_item = input("> ")
        while selected_item.lower() not in valid_choices:
            print("Sorry, that is not a valid choice. Please try again.")
            print("Please choose a weapon to unequip from the following list:")
            for weapon in self.equipped_weapon:
                print(weapon.name)
            selected_item = input("> ")
        for weapon in self.equipped_weapon:
            if weapon.name.lower() == selected_item.lower():
                self.equipped_weapon.remove(weapon)
                print(f"You have unequipped {weapon.name}.")
                return
        print("You have not uneqiupped any weapons.")
        return
    
    def equip_shield(self):
        equipped_items = []
        for item in self.equipment:
            equipped_items.append(item.name)
        if "Shield" not in equipped_items:
            print("You do not have a shield to equip.")
            return
        self.equipped_shield = True
        print("You have equipped a shield.")
        return
    
    def unequip_shield(self):
        if self.equipped_shield == None:
            print("You do not have a shield equipped.")
            return
        self.equipped_shield = None
        print("You have unequipped your shield.")
        return
    
    def ready_weapon(self):
        if self.equipped_weapon == []:
            print("You do not have any weapons equipped. Please equip a weapon before readying it.")
            return
        print("Please choose a weapon to ready from the following list:")
        valid_choices = []
        for weapon in self.equipped_weapon:
            print(weapon.name)
            valid_choices.append(weapon.name.lower())
        selected_item = input("> ")
        while selected_item.lower() not in valid_choices:
            print("Sorry, that is not a valid choice. Please try again.")
            print("Please choose a weapon to ready from the following list:")
            for weapon in self.equipped_weapon:
                print(weapon.name)
            selected_item = input("> ")
        for weapon in self.equipped_weapon:
            if weapon.name.lower() == selected_item.lower():
                self.readied_weapon = weapon
                print(f"You have readied {weapon.name}.")
                return
        print("You have not readied any weapons.")    
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
    
    def increase_ability_score(self, number):
        ability_points = number
        while ability_points > 0:
            print("Please choose an ability score to increase:")
            for ability in ("Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"):
                print(ability)
            ability_choice = input("> ")
            while ability_choice.lower() not in ("strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"):
                print("That is not a valid choice. Please choose from the list.")
                ability_choice = input("> ")
            if ability_choice.lower() == "strength":
                self.strength += 1
            elif ability_choice.lower() == "dexterity":
                self.dexterity += 1
            elif ability_choice.lower() == "constitution":
                self.constitution += 1
            elif ability_choice.lower() == "intelligence":
                self.intelligence += 1
            elif ability_choice.lower() == "wisdom":
                self.wisdom += 1
            elif ability_choice.lower() == "charisma":
                self.charisma += 1
            ability_points -= 1
        self.calculate_modifiers()
        return


    def announce_character(self):
        button_texts = ["Click to Continue..."]
        button_rects = buttons.create_button_rects(SCREEN_WIDTH, SCREEN_HEIGHT, len(button_texts))
        text_position = (MARGIN, MARGIN)
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
                            return

            screen.fill(BG_COLOR)

            if animate_flag:
                text_display.animate_text(screen, f'{self.name} is a {self.race.subrace} {self.archetype.name}. They currently have a {player_equipment_names}.', text_position, TEXT_AREA_WIDTH)
                animate_flag = False
            else:
                text_display.draw_text(screen, f'{self.name} is a {self.race.subrace} {self.archetype.name}. They currently have a {player_equipment_names}.', text_position, TEXT_AREA_WIDTH)

            buttons.draw_buttons(screen, button_texts, button_rects, mouse_pos)

            pygame.display.update()