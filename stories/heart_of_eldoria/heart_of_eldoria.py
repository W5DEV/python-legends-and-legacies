import pygame
import pygame_gui

# Initialize Pygame and Pygame GUI
pygame.init()
pygame.display.set_caption('The Heart of Eldoria - Legends & Legacies')
window_surface = pygame.display.set_mode((800, 600))
background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((800, 600))

# Function to display text
def animate_text(text, manager, window_surface):
    # Assuming text_display.animate_text() is a custom function
    # Here we simulate it with pygame_gui elements
    text_box = pygame_gui.elements.UITextBox(
        html_text=text,
        relative_rect=pygame.Rect((50, 50), (700, 500)),
        manager=manager
    )
    return text_box

# Function to handle button clicks
def handle_button_click(event, button_texts):
    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
        if event.ui_element.text == button_texts[0]:
            venture_into_forest()
        elif event.ui_element.text == button_texts[1]:
            ask_about_curse()
        elif event.ui_element.text == button_texts[2]:
            decline_quest()
        elif event.ui_element.text == "Yes":
            introduction()
        elif event.ui_element.text == "No":
            pygame.quit()

# Introduction to the game
def introduction():
    text = ("Welcome to 'The Heart of Eldoria'!\n"
            "You are about to embark on a perilous journey into the Cursed Forest of Eldoria.\n"
            "The town of Greenhaven has tasked you with retrieving the legendary Heart of Eldoria to lift the curse.\n"
            "Prepare yourself, brave adventurer, for the journey ahead will test your courage, wit, and skill.\n")
    animate_text(text, manager, window_surface)
    global button_texts
    button_texts = ["Accept the quest", "Ask about the curse", "Decline the quest"]
    create_buttons(button_texts)

# Function to create buttons
def create_buttons(button_texts):
    for i, text in enumerate(button_texts):
        pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((50, 450 + i * 50), (200, 50)),
            text=text,
            manager=manager
        )

# Function to venture into the forest
def venture_into_forest():
    text = ("You accept the quest and step out of the meeting hall, ready to venture into the Cursed Forest.\n"
            "As you approach the edge of the forest, you feel an eerie chill in the air.\n"
            "The trees are twisted and gnarled, and a thick fog blankets the ground.\n")
    animate_text(text, manager, window_surface)
    # Proceed to the next part of the story
    # forest_adventure()

# Function to ask more about the curse and the Heart of Eldoria
def ask_about_curse():
    text = ("Elder: 'The curse was cast by the dark sorcerer Malakar a century ago. It turned the forest into a place of darkness and danger.'\n"
            "Elder: 'The Heart of Eldoria is a mystical gem that holds the power to lift the curse. It is hidden deep within the forest, protected by powerful magic.'\n"
            "Elder: 'We believe you have the strength and courage to retrieve it and save our land.'\n")
    animate_text(text, manager, window_surface)
    global button_texts
    button_texts = ["Accept the quest", "Decline the quest"]
    create_buttons(button_texts)

# Function to decline the quest
def decline_quest():
    text = ("You decline the quest and leave the meeting hall.\n"
            "As you walk away, you can't help but feel a sense of guilt and unease.\n"
            "The fate of Eldoria rests in someone else's hands now...\n")
    animate_text(text, manager, window_surface)
    # End the game or provide an option to restart
    end_game()

# Function to handle the end of the game
def end_game():
    text = ("Thank you for playing 'The Heart of Eldoria - Legends & Legacies'!\n"
            "Would you like to play again? (yes/no)\n")
    animate_text(text, manager, window_surface)
    global button_texts
    button_texts = ["Yes", "No"]
    create_buttons(button_texts)

# Main game loop
clock = pygame.time.Clock()
is_running = True

introduction()

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.USEREVENT:
            handle_button_click(event, button_texts)

        manager.process_events(event)

    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()

pygame.quit()
