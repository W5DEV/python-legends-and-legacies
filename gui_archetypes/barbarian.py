import pygame
import sys
import gui.text_display as text_display
import gui.buttons as buttons
import gui.constants as constants
import gui_utils.select_starting_equipment as select_starting_equipment

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

class Barbarian:
    
    def __init__(self):
        name = "Barbarian"
        bio = "A fierce warrior of primitive background who can enter a battle rage."
        hit_die = "1d12"
        primary_ability = "Strength"
        saving_throw_proficiencies = "Strength, Constitution"
        armor_proficiencies = "Light Armor, Medium Armor, Shields"
        weapon_proficiencies = "Simple Weapons, Martial Weapons"
        tool_proficiencies = "None"
        self.name = name
        self.bio = bio
        self.hit_die = hit_die
        self.base_hp = 12
        self.primary_ability = primary_ability
        self.saving_throw_proficiencies = saving_throw_proficiencies
        self.armor_proficiencies = armor_proficiencies
        self.weapon_proficiencies = weapon_proficiencies
        self.tool_proficiencies = tool_proficiencies
        self.skill_proficiencies = []
        self.starting_equipment = []
        self.special_abilities = []
        self.primal_path = ""
        self.rages = 0
        self.rage_damage_bonus = 0

    def sync_level(self, level, player):
        if level == 1:
            self.special_abilities.append("Rage")
            self.special_abilities.append("Unarmored Defense")
            self.rages = 1
            self.rage_damage_bonus = 2
        if level == 2:
            self.special_abilities.append("Reckless Attack")
            self.special_abilities.append("Danger Sense")
        if level == 3:
            self.primal_path = "Path of the Berserker"
            self.special_abilities.append("Frenzy")
            self.rages = 3
        if level == 4:
            self.special_abilities.append("Ability Score Improvement 4th Level")
            player.increase_ability_score(2)
        if level == 5:
            self.special_abilities.append("Extra Attack")
            self.special_abilities.append("Fast Movement")
        if level == 6:
            self.special_abilities.append("Mindless Rage")
            self.rages = 4
        if level == 7:
            self.special_abilities.append("Feral Instinct")
        if level == 8:
            self.special_abilities.append("Ability Score Improvement 8th Level")
            player.increase_ability_score(2)
        if level == 9:
            self.special_abilities.append("Brutal Critical")
            self.rage_damage_bonus = 3
        if level == 10:
            self.special_abilities.append("Intimidating Presence")
        if level == 11:
            self.special_abilities.append("Reliable Talent")
            self.special_abilities.append("Relentless Rage")
        if level == 12:
            self.special_abilities.append("Ability Score Improvement 12th Level")
            player.increase_ability_score(2)
            self.rages = 5
        if level == 13:
            self.special_abilities.append("Bear Totem")
        if level == 14:
            self.special_abilities.append("Retaliation")
        if level == 15:
            self.special_abilities.append("Persistent Rage")
        if level == 16:
            self.special_abilities.append("Ability Score Improvement 16th Level")
            player.increase_ability_score(2)
            self.rage_damage_bonus = 4
        if level == 17:
            self.rages = 6
        if level == 18:
            self.special_abilities.append("Indomitable Might")
        if level == 19:
            self.special_abilities.append("Ability Score Improvement 19th Level")
            player.increase_ability_score(2)
        if level == 20:
            self.special_abilities.append("Primal Champion")
            self.rages = 9999
        return
    
def define_barbarian():
    barbarian = Barbarian()

    ### Equipment Choices ###

    first_equipment_choice = select_starting_equipment.weapon_choices(["Great Axe", "Martial Melee Weapons"])
    second_equipment_choice = select_starting_equipment.weapon_choices(["Hand Axe", "Simple Weapons"])
    third_equipment_choice = select_starting_equipment.weapon_choices(["Explorer's Pack"])
    fourth_equipment_choice = select_starting_equipment.weapon_choices(["Javelin"])

    barbarian.starting_equipment.append(first_equipment_choice)
    if second_equipment_choice == "Hand Axe":
        barbarian.starting_equipment.append(second_equipment_choice)
        barbarian.starting_equipment.append(second_equipment_choice)
    else:
        barbarian.starting_equipment.append(second_equipment_choice)
    
    barbarian.starting_equipment.append(third_equipment_choice)

    barbarian.starting_equipment.append(fourth_equipment_choice)
    barbarian.starting_equipment.append(fourth_equipment_choice)
    barbarian.starting_equipment.append(fourth_equipment_choice)
    barbarian.starting_equipment.append(fourth_equipment_choice)


    ### Skill Choices ###

    return barbarian
