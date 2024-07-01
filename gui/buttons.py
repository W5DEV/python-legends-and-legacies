# buttons.py

import pygame

BUTTON_COLOR = (70, 70, 70)
BORDER_COLOR = (200, 200, 200)
FONT_SIZE = 36
MARGIN = 20

# Initialize the font module
pygame.font.init()
font = pygame.font.SysFont(None, FONT_SIZE)

def draw_skyrim_button(surface, rect, color, border_color):
    # Draw button background
    pygame.draw.rect(surface, color, rect)
    
    # Add an outer border with a stone-like texture
    outer_border = rect.inflate(-4, -4)
    inner_border = rect.inflate(-10, -10)
    pygame.draw.rect(surface, border_color, rect, 4)
    
    # Add engraving-like details
    pygame.draw.line(surface, border_color, outer_border.topleft, (outer_border.left + 20, outer_border.top), 2)
    pygame.draw.line(surface, border_color, outer_border.topleft, (outer_border.left, outer_border.top + 20), 2)
    pygame.draw.line(surface, border_color, outer_border.topright, (outer_border.right - 20, outer_border.top), 2)
    pygame.draw.line(surface, border_color, outer_border.topright, (outer_border.right, outer_border.top + 20), 2)
    pygame.draw.line(surface, border_color, outer_border.bottomleft, (outer_border.left + 20, outer_border.bottom), 2)
    pygame.draw.line(surface, border_color, outer_border.bottomleft, (outer_border.left, outer_border.bottom - 20), 2)
    pygame.draw.line(surface, border_color, outer_border.bottomright, (outer_border.right - 20, outer_border.bottom), 2)
    pygame.draw.line(surface, border_color, outer_border.bottomright, (outer_border.right, outer_border.bottom - 20), 2)
    
    # Add inner border
    pygame.draw.rect(surface, border_color, inner_border, 2)
    
    # Adding a faux 3D effect
    pygame.draw.line(surface, (100, 100, 100), rect.topleft, (rect.right, rect.top), 2)
    pygame.draw.line(surface, (100, 100, 100), rect.topleft, (rect.left, rect.bottom), 2)
    pygame.draw.line(surface, (200, 200, 200), rect.bottomleft, rect.bottomright, 2)
    pygame.draw.line(surface, (200, 200, 200), rect.topright, rect.bottomright, 2)

def draw_buttons(surface, button_texts, button_rects):
    for text, rect in zip(button_texts, button_rects):
        draw_skyrim_button(surface, rect, BUTTON_COLOR, BORDER_COLOR)
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=rect.center)
        surface.blit(text_surface, text_rect)

def update_button_text(button_texts, index, new_text):
    if 0 <= index < len(button_texts):
        button_texts[index] = new_text
