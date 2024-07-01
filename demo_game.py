import pygame
import sys
import gui.buttons as buttons  # Import the buttons module
import gui.text_logic as text_logic  # Import the text_logic module
import gui.stats as stats  # Import the stats module

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 800
BG_COLOR = (0, 0, 0)
TEXT_COLOR = (255, 255, 255)
BORDER_COLOR = (150, 150, 150)
BUTTON_COLOR = (50, 50, 50)
BUTTON_COLOR_HOVER = (100, 100, 100)
FONT_SIZE = 36
MARGIN = 20
BUTTON_HEIGHT = SCREEN_HEIGHT // 5
TEXT_AREA_WIDTH = 800
TEXT_AREA_HEIGHT = 200
BUTTON_WIDTH = 300
BUTTON_HEIGHT = 50

# Setup screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Fantasy Story Game')
font = pygame.font.SysFont(None, FONT_SIZE)

def draw_text(surface, text, position, wrap_width):
    words = text.split()
    lines = []
    while words:
        line = ''
        while words and font.size(line + words[0])[0] <= wrap_width:
            line += words.pop(0) + ' '
        lines.append(line)
    for i, line in enumerate(lines):
        surface.blit(font.render(line, True, TEXT_COLOR), (position[0], position[1] + i * FONT_SIZE))

def animate_text(surface, text, position, wrap_width):
    words = text.split()
    lines = []
    while words:
        line = ''
        while words and font.size(line + words[0])[0] <= wrap_width:
            line += words.pop(0) + ' '
        lines.append(line)
    for i, line in enumerate(lines):
        for j in range(len(line)):
            surface.fill(BG_COLOR, (position[0], position[1] + i * FONT_SIZE, wrap_width, FONT_SIZE))
            surface.blit(font.render(line[:j+1], True, TEXT_COLOR), (position[0], position[1] + i * FONT_SIZE))
            pygame.display.update()
            pygame.time.delay(50)  # Typing effect speed

def main():
    def reset_game():
        nonlocal current_text, choices, state, button_rects, text_updated
        current_text, choices, state = text_logic.get_updated_text('', 'start')
        button_rects = [pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 2, SCREEN_HEIGHT - (i+1) * (BUTTON_HEIGHT + MARGIN), BUTTON_WIDTH, BUTTON_HEIGHT) for i in range(len(choices))]
        text_updated = True

    reset_game()

    # Example stats
    player_stats = {
        "Level": 5,
        "XP": 2500,
        "HP/Max HP": "75/100",
        "AC": 15,
        "Dex": 12,
        "Str": 14,
        "Con": 13,
        "Int": 10,
        "Wis": 8,
        "Cha": 11
    }

    while True:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(button_rects):
                    if rect.collidepoint(event.pos):
                        if choices[i] == "Restart":
                            reset_game()
                        elif choices[i] == "Quit":
                            pygame.quit()
                            sys.exit()
                        else:
                            current_text, choices, state = text_logic.get_updated_text(choices[i], state)
                            button_rects = [pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 2, SCREEN_HEIGHT - (j+1) * (BUTTON_HEIGHT + MARGIN), BUTTON_WIDTH, BUTTON_HEIGHT) for j in range(len(choices))]
                            text_updated = True
                        break

        screen.fill(BG_COLOR)
        
		# Draw stats on the left side of the screen
        stats.draw_stats(screen, player_stats, (MARGIN, MARGIN))
        
        if text_updated:
            animate_text(screen, current_text, ((SCREEN_WIDTH - TEXT_AREA_WIDTH) // 2, MARGIN), TEXT_AREA_WIDTH)
            text_updated = False
        else:
            draw_text(screen, current_text, ((SCREEN_WIDTH - TEXT_AREA_WIDTH) // 2, MARGIN), TEXT_AREA_WIDTH)
        
        for i, rect in enumerate(button_rects):
            if rect.collidepoint(mouse_pos):
                buttons.draw_skyrim_button(screen, rect, BUTTON_COLOR_HOVER, BORDER_COLOR)
            else:
                buttons.draw_skyrim_button(screen, rect, BUTTON_COLOR, BORDER_COLOR)
            text_surface = font.render(choices[i], True, TEXT_COLOR)
            text_rect = text_surface.get_rect(center=rect.center)
            screen.blit(text_surface, text_rect)

        pygame.display.update()

if __name__ == '__main__':
    main()
