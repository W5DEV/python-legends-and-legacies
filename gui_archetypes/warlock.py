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

class Warlock:

    def __init__(self):
        name = "Warlock"
        bio = "A wielder of magic that is derived from a bargain with an extraplanar entity."
        hit_die = "1d8"
        primary_ability = "Charisma"
        saving_throw_proficiencies = "Wisdom, Charisma"
        armor_proficiencies = "Light Armor"
        weapon_proficiencies = "Simple Weapons"
        tool_proficiencies = "None"
        self.name = name
        self.bio = bio
        self.hit_die = hit_die
        self.base_hp = 8
        self.primary_ability = primary_ability
        self.saving_throw_proficiencies = saving_throw_proficiencies
        self.armor_proficiencies = armor_proficiencies
        self.weapon_proficiencies = weapon_proficiencies
        self.tool_proficiencies = tool_proficiencies
        self.skill_proficiencies = []
        self.starting_equipment = []
        self.special_abilities = []
        self.otherworldly_patrons = ""
        self.cantrips = []
        self.spells = []
        self.cantrips_known = 2
        self.spells_known = 2
        self.spell_slots = 1
        self.spell_slot_level = 1
        self.invocations_known = 0

    def sync_level(self, level, player):
        if level == 1:
            self.otherworldly_patrons = "The Fiend"
            self.special_abilities.append("Fiend Expanded Spells Level 1")
            self.special_abilities.append("Pact Magic")
            self.special_abilities.append("Dark One's Blessing")
        if level == 2:
            self.special_abilities.append("Eldritch Invocations")
            self.special_abilities.append("Fiend Expanded Spells Level 2")
            self.spells_known = 3
            self.spell_slots = 2
            self.invocations_known = 2
        if level == 3:
            self.special_abilities.append("Pact Boom")
            self.special_abilities.append("Fiend Expanded Spells Level 3")
            self.spells_known = 4
            self.spell_slot_level = 2
        if level == 4:
            self.special_abilities.append("Ability Score Improvement 4th Level")
            player.increase_ability_score(2)
            self.special_abilities.append("Fiend Expanded Spells Level 4")
            self.cantrips_known = 3
            self.spells_known = 5
        if level == 5:
            self.special_abilities.append("Fiend Expanded Spells Level 5")
            self.spells_known = 6
            self.spell_slot_level = 3
            self.invocations_known = 3
        if level == 6:
            self.special_abilities.append("Dark One's Own Luck")
            self.spells_known = 7
        if level == 7:
            self.spells_known = 8
            self.spell_slot_level = 4
            self.invocations_known = 4
        if level == 8:
            self.special_abilities.append("Ability Score Improvement 8th Level")
            player.increase_ability_score(2)
            self.spells_known = 9
        if level == 9:
            self.spells_known = 10
            self.spell_slot_level = 5
            self.invocations_known = 5
        if level == 10:
            self.special_abilities.append("Fiendish Resilience")
            self.cantrips_known = 4
        if level == 11:
            self.special_abilities.append("Mystic Arcanum 6th Level")
            self.spells_known = 11
            self.spell_slots = 3
        if level == 12:
            self.special_abilities.append("Ability Score Improvement 12th Level")
            player.increase_ability_score(2)
            self.invocations_known = 6
        if level == 13:
            self.special_abilities.append("Mystic Arcanum 7th Level")
            self.spells_known = 12
        if level == 14:
            self.special_abilities.append("Hurl Through Hell")
        if level == 15:
            self.special_abilities.append("Mystic Arcanum 8th Level")
            self.spells_known = 13
            self.invocations_known = 7
        if level == 16:
            self.special_abilities.append("Ability Score Improvement 16th Level")
            player.increase_ability_score(2)
        if level == 17:
            self.special_abilities.append("Mythic Arcanum 9th Level")
            self.spells_known = 14
            self.spell_slots = 4
        if level == 18:
            self.invocations_known = 8
        if level == 19:
            self.special_abilities.append("Ability Score Improvement 19th Level")
            player.increase_ability_score(2)
            self.spells_known = 15
        if level == 20:
            self.special_abilities.append("Eldritch Master")
        return self
    
def define_warlock():
    warlock = Warlock()
    return warlock
 