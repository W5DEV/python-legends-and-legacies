import pygame
import gui.constants as const


# Initialize the font module
pygame.font.init()
font = pygame.font.SysFont(None, const.FONT_SIZE)

def draw_fantasy_button(surface, rect, color, border_color, hover=False):
    # Draw button background
    pygame.draw.rect(surface, color, rect, border_radius=10)
    
    # Add an outer border with a fantasy-like texture
    outer_border = rect.inflate(-4, -4)
    inner_border = rect.inflate(-10, -10)
    pygame.draw.rect(surface, color, rect, 4, border_radius=10)
    
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
    pygame.draw.rect(surface, border_color, inner_border, 2, border_radius=10)
    
    if hover:
        pygame.draw.rect(surface, color, inner_border, 2, border_radius=10)

def draw_buttons(surface, button_texts, button_rects, mouse_pos):
    for text, rect in zip(button_texts, button_rects):
        hover = rect.collidepoint(mouse_pos)
        draw_fantasy_button(surface, rect, const.BUTTON_COLOR, const.BORDER_COLOR, hover=hover)
        text_surface = font.render(text, True, const.TEXT_COLOR)
        text_rect = text_surface.get_rect(center=rect.center)
        surface.blit(text_surface, text_rect)

def create_button_rects(num_buttons):
    button_width = 350
    button_height = 50
    margin = 20
    cols = (const.SCREEN_WIDTH - margin) // (button_width + margin)
    rows = (num_buttons + cols - 1) // cols  # Ceiling division
    button_rects = []

    for row in range(rows):
        for col in range(cols):
            if len(button_rects) >= num_buttons:
                break
            x = margin + col * (button_width + margin)
            y = const.SCREEN_HEIGHT - margin - (rows - row) * (button_height + margin)
            button_rects.append(pygame.Rect(x, y, button_width, button_height))
    
    return button_rects