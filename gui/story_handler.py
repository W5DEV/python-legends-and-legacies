import pygame
import sys
import gui.text_display as text_display  # Import the text_display module
import gui.buttons as buttons  # Import the buttons module
import gui.constants as const
import gui.surface as pygame_surface

# Initialize pygame
pygame.init()
surface = pygame_surface.surface

def handle_story(text, button):
    button_texts = button
    button_rects = buttons.create_button_rects(len(button_texts))


    animate_flag = True
    
    while True:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(button_rects):
                    if rect.collidepoint(mouse_pos):
                        return button_texts[i]
                        
        surface.fill(const.BG_COLOR)
        
        if animate_flag:
            text_display.animate_text(surface, text)
            animate_flag = False
        else:
            text_display.draw_text(surface, text)

        buttons.draw_buttons(surface, button_texts, button_rects, mouse_pos)

        pygame.display.update()