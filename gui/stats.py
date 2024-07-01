# stats.py

import pygame

STATS_FONT_SIZE = 24
STATS_MARGIN = 20
STATS_TEXT_COLOR = (255, 255, 255)

# Initialize the font module
pygame.font.init()
stats_font = pygame.font.SysFont(None, STATS_FONT_SIZE)

def draw_stats(surface, stats, position):
    y_offset = 0
    for key, value in stats.items():
        stat_text = f"{key}: {value}"
        text_surface = stats_font.render(stat_text, True, STATS_TEXT_COLOR)
        surface.blit(text_surface, (position[0], position[1] + y_offset))
        y_offset += STATS_FONT_SIZE + STATS_MARGIN

# Example stats dictionary
player_stats = {
    "Level": 5,
    "XP": 2500,
    "HP": "75/100",
    "AC": 15,
    "Dex": 12,
    "Str": 14,
    "Con": 13,
    "Int": 10,
    "Wis": 8,
    "Cha": 11
}
