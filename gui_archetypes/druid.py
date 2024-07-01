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

class Druid:

    def __init__(self):
        name = "Druid"
        bio = "A priest of the Old Faith, wielding the powers of nature — moonlight and plant growth, fire and lightning — and adopting animal forms."
        hit_die = "1d8"
        primary_ability = "Wisdom"
        saving_throw_proficiencies = "Intelligence, Wisdom"
        armor_proficiencies = "Non-metal Light Armor, Non-metal Medium Armor, Non-metal Shields"
        weapon_proficiencies = "Clubs, Daggers, Darts, Javelins, Maces, Quarterstaffs, Scimitars, Sickles, Slings, Spears"
        tool_proficiencies = "Herbalism Kit"
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
        self.circle = ""
        self.cantrips = []
        self.spells = []
        self.cantrips_known = 2
        self.spell_slots_level_1 = 2
        self.spell_slots_level_2 = 0
        self.spell_slots_level_3 = 0
        self.spell_slots_level_4 = 0
        self.spell_slots_level_5 = 0
        self.spell_slots_level_6 = 0
        self.spell_slots_level_7 = 0
        self.spell_slots_level_8 = 0
        self.spell_slots_level_9 = 0
    
    def sync_level(self, level, player):
        if level == 1:
            self.special_abilities.append("Druidic")
            self.special_abilities.append("Spellcasting")
        if level == 2:
            self.circle = "Circle of the Land"
            self.special_abilities.append("Wild Shape - No flying or swimming speed (1/4 CR)")
            self.special_abilities.append("Bonus Cantrip")
            self.special_abilities.append("Natural Recovery")
            self.spell_slots_level_1 = 3
        if level == 3:
            self.special_abilities.append("3rd Level Circle Spells")
            self.spell_slots_level_1 = 4
            self.spell_slots_level_2 = 2
        if level == 4:
            self.special_abilities.append("Wild Shape Improvement 4th Level - No flying speed (1/2 CR)")
            self.special_abilities.append("Ability Score Improvement 4th Level")
            player.increase_ability_score(2)
            self.spell_slots_level_2 = 3
        if level == 5:
            self.special_abilities.append("5th Level Circle Spells")
            self.spell_slots_level_3 = 2
        if level == 6:
            self.special_abilities.append("Land's Stride")
            self.spell_slots_level_3 = 3
        if level == 7:
            self.special_abilities.append("7th Level Circle Spells")
            self.spell_slots_level_4 = 1
        if level == 8:
            self.special_abilities.append("Wild Shape Improvement 8th Level (1 CR)")
            self.special_abilities.append("Ability Score Improvement 8th Level")
            player.increase_ability_score(2)
            self.spell_slots_level_4 = 2
        if level == 9:
            self.special_abilities.append("9th Level Circle Spells")
            self.spell_slots_level_4 = 3
            self.spell_slots_level_5 = 1
        if level == 10:
            self.special_abilities.append("Nature's Ward")
            self.spell_slots_level_5 = 2
        if level == 11:
            self.spell_slots_level_6 = 1
        if level == 12:
            self.special_abilities.append("Ability Score Improvement 12th Level")
            player.increase_ability_score(2)
        if level == 13:
            self.spell_slots_level_7 = 1
        if level == 14:
            self.special_abilities.append("Nature's Sanctuary")
        if level == 15:
            self.spell_slots_level_8 = 1
        if level == 16:
            self.special_abilities.append("Ability Score Improvement 16th Level")
            player.increase_ability_score(2)
        if level == 17:
            self.spell_slots_level_9 = 1
        if level == 18:
            self.special_abilities.append("Timeless Body")
            self.special_abilities.append("Beast Spells")
            self.spell_slots_level_5 = 3
        if level == 19:
            self.special_abilities.append("Ability Score Improvement 19th Level")
            player.increase_ability_score(2)
            self.spell_slots_level_6 = 2
        if level == 20:
            self.special_abilities.append("Archdruid")
            self.spell_slots_level_7 = 2
        return self
    
def define_druid():
    druid = Druid()
    return druid
