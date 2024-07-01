import pygame
import time

TEXT_COLOR = (255, 255, 255)
FONT_SIZE = 36

# Initialize the font module
pygame.font.init()
font = pygame.font.SysFont(None, FONT_SIZE)

def draw_text(surface, text, position, wrap_width):
    words = text.split()
    lines = []
    while words:
        line = ''
        while words and font.size(line + words[0])[0] <= wrap_width and words:
            line += words.pop(0) + ' '
        lines.append(line)
    for i, line in enumerate(lines):
        surface.blit(font.render(line, True, TEXT_COLOR), (position[0], position[1] + i * FONT_SIZE))

def animate_text(surface, text, position, wrap_width):
    words = text.split()
    lines = []
    while words:
        line = ''
        while words and font.size(line + words[0])[0] <= wrap_width and words:
            line += words.pop(0) + ' '
        lines.append(line)
    for i, line in enumerate(lines):
        for j in range(len(line)):
            surface.fill((0, 0, 0), (position[0], position[1] + i * FONT_SIZE, wrap_width, FONT_SIZE))
            surface.blit(font.render(line[:j+1], True, TEXT_COLOR), (position[0], position[1] + i * FONT_SIZE))
            pygame.display.update()
            time.sleep(0.05)  # Typing effect speed
