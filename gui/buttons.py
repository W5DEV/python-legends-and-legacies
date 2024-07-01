# buttons.py

import pygame

BUTTON_COLOR = (70, 70, 70)
BUTTON_COLOR_HOVER = (100, 100, 100)
BORDER_COLOR = (200, 200, 200)
FONT_SIZE = 36
MARGIN = 20

# Initialize the font module
pygame.font.init()
font = pygame.font.SysFont(None, FONT_SIZE)

def draw_rounded_rect(surface, rect, color, radius=10):
    pygame.draw.rect(surface, color, rect, border_radius=radius)

def draw_gradient_button(surface, rect, color, border_color, hover=False):
    gradient = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
    for y in range(rect.height):
        alpha = 255 - int(255 * (y / rect.height))
        row_color = (color[0], color[1], color[2], alpha)
        pygame.draw.line(gradient, row_color, (0, y), (rect.width, y))
    surface.blit(gradient, rect.topleft)
    
    draw_rounded_rect(surface, rect, color, radius=10)
    border_rect = rect.inflate(-4, -4)
    draw_rounded_rect(surface, border_rect, border_color, radius=10)
    if hover:
        draw_rounded_rect(surface, border_rect, BUTTON_COLOR_HOVER, radius=10)

def draw_buttons(surface, button_texts, button_rects, mouse_pos):
    for text, rect in zip(button_texts, button_rects):
        hover = rect.collidepoint(mouse_pos)
        draw_gradient_button(surface, rect, BUTTON_COLOR, BORDER_COLOR, hover=hover)
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=rect.center)
        surface.blit(text_surface, text_rect)

def create_button_rects(screen_width, screen_height, num_buttons):
    button_width = 200
    button_height = 50
    margin = 20
    cols = (screen_width - margin) // (button_width + margin)
    rows = (num_buttons + cols - 1) // cols  # Ceiling division
    button_rects = []

    for row in range(rows):
        for col in range(cols):
            if len(button_rects) >= num_buttons:
                break
            x = margin + col * (button_width + margin)
            y = screen_height - margin - (rows - row) * (button_height + margin)
            button_rects.append(pygame.Rect(x, y, button_width, button_height))
    
    return button_rects
