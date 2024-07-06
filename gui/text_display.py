import pygame
import time
import gui.constants as const

# Initialize the font module
pygame.font.init()
font = pygame.font.SysFont(None, const.FONT_SIZE)
text_position = (const.MARGIN, const.MARGIN)

def draw_text(surface, text):
    words = text.split()
    lines = []
    while words:
        line = ''
        while words and font.size(line + words[0])[0] <= const.TEXT_AREA_WIDTH and words:
            line += words.pop(0) + ' '
        lines.append(line)
    for i, line in enumerate(lines):
        surface.blit(font.render(line, True, const.TEXT_COLOR), (text_position[0], text_position[1] + i * const.FONT_SIZE))

def animate_text(surface, text):
    words = text.split()
    lines = []
    while words:
        line = ''
        while words and font.size(line + words[0])[0] <= const.TEXT_AREA_WIDTH and words:
            line += words.pop(0) + ' '
        lines.append(line)
    for i, line in enumerate(lines):
        for j in range(len(line)):
            surface.fill((0, 0, 0), (text_position[0], text_position[1] + i * const.FONT_SIZE, const.TEXT_AREA_WIDTH, const.FONT_SIZE))
            surface.blit(font.render(line[:j+1], True, const.TEXT_COLOR), (text_position[0], text_position[1] + i * const.FONT_SIZE))
            pygame.display.update()
            time.sleep(0.05)  # Typing effect speed

    