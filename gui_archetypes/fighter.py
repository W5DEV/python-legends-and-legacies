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

class Fighter:
    
    def __init__(self):
        name = "Fighter"
        bio = "A master of martial combat, skilled with a variety of weapons and armor."
        hit_die = "1d10"
        primary_ability = "Strength or Dexterity"
        saving_throw_proficiencies = "Strength, Constitution"
        armor_proficiencies = "All Armor, Shields"
        weapon_proficiencies = "All Simple Weapons and Martial Weapons"
        tool_proficiencies = "None"
        self.name = name
        self.bio = bio
        self.hit_die = hit_die
        self.base_hp = 10
        self.primary_ability = primary_ability
        self.saving_throw_proficiencies = saving_throw_proficiencies
        self.armor_proficiencies = armor_proficiencies
        self.weapon_proficiencies = weapon_proficiencies
        self.tool_proficiencies = tool_proficiencies
        self.skill_proficiencies = []
        self.starting_equipment = []
        self.fighting_style = []
        self.marital_archetype = ""
        self.special_abilities = []
    
    def sync_level(self, level, player):
        if level == 1:
            print("You have reached level 1 and now have the following fighting styles:")
            for style in ["Archery", "Defense", "Dueling", "Great Weapon Fighting", "Protection", "Two-Weapon Fighting"]:
                print(style)
            print("Please enter your choice of fighting style:")
            fighting_style_choice = input("> ")
            while fighting_style_choice.lower() not in ["archery", "defense", "dueling", "great weapon fighting", "protection", "two-weapon fighting"]:
                print("That is not a valid choice. Please choose from the list.")
                fighting_style_choice = input("> ")
            self.fighting_style.append(fighting_style_choice)
            print(f"You have chosen the {fighting_style_choice} fighting style.")
            print("You cannot specialize in this fighting style in the future.")
            print("You have also gained the following special abilities:")
            self.special_abilities.append("Second Wind")
        if level == 2:
            self.special_abilities.append("Action Surge (1/rest)")
        if level == 3:
            self.marital_archetype = "Champion"
            self.special_abilities.append("Improved Critical (crit range 19-20)")
        if level == 4:
            self.special_abilities.append("Ability Score Improvement 4th Level")
            player.increase_ability_score(2)
        if level == 5:
            self.special_abilities.append("Extra Attack (1 extra attack)")
        if level == 6:
            self.special_abilities.append("Ability Score Improvement 6th Level")
            player.increase_ability_score(2)
        if level == 7:
            self.special_abilities.append("Remarkable Athlete")
        if level == 8:
            self.special_abilities.append("Ability Score Improvement 8th Level")
            player.increase_ability_score(2)
        if level == 9:
            self.special_abilities.append("Indomitable (1/rest)")
        if level == 10:
            self.special_abilities.append("Additional Fighting Style")
            print("You have reached level 10 and now have the following fighting styles:")
            for style in ["Archery", "Defense", "Dueling", "Great Weapon Fighting", "Protection", "Two-Weapon Fighting"]:
                print(style)
            print("Please enter your choice of fighting style:")
            fighting_style_choice = input("> ")
            while (fighting_style_choice.lower() not in ["archery", "defense", "dueling", "great weapon fighting", "protection", "two-weapon fighting"]) and (fighting_style_choice not in self.fighting_style):
                print("That is not a valid choice. Please choose an unused style from the list.")
                print("Your current fighting styles are:")
                for style in self.fighting_style:
                    print(style)
                fighting_style_choice = input("> ")
            self.fighting_style.append(fighting_style_choice)
            print(f"You have chosen the {fighting_style_choice} fighting style.")
        if level == 11:
            self.special_abilities.append("Extra Attack (2 extra attacks)")
        if level == 12:
            self.special_abilities.append("Ability Score Improvement 12th Level")
            player.increase_ability_score(2)
        if level == 13:
            self.special_abilities.append("Indomitable (2/rest)")
        if level == 14:
            self.special_abilities.append("Ability Score Improvement 14th Level")
            player.increase_ability_score(2)
        if level == 15:
            self.special_abilities.append("Superior Critical (crit range 18-20)")
        if level == 16:
            self.special_abilities.append("Ability Score Improvement 16th Level")
            player.increase_ability_score(2)
        if level == 17:
            self.special_abilities.append("Action Surge (2/rest)")
            self.special_abilities.append("Indomitable (3/rest)")
        if level == 18:
            self.special_abilities.append("Survivor")
        if level == 19:
            self.special_abilities.append("Ability Score Improvement 19th Level")
            player.increase_ability_score(2)
        if level == 20:
            self.special_abilities.append("Extra Attack (3 extra attacks)")
        return self
    
def define_fighter():
    fighter = Fighter()
    return fighter
