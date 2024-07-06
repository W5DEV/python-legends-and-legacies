import pygame
import sys
import gui.surface as pygame_surface
import gui.story_handler as story

# Initialize pygame
pygame.init()
surface = pygame_surface.surface
pygame.display.set_caption('The Heart of Eldoria')

# Introduction to the game
def introduction():
    text = ("Welcome to 'The Heart of Eldoria'! You are about to embark on a perilous journey into the Cursed Forest of Eldoria. The town of Greenhaven has tasked you with retrieving the legendary Heart of Eldoria to lift the curse. Prepare yourself, brave adventurer, for the journey ahead will test your courage, wit, and skill.")
    button_texts = ["Accept the quest", "Ask about the curse", "Decline the quest"]
    
    response = story.handle_story(text, button_texts)

    if response == "Accept the quest":
        venture_into_forest()
    elif response == "Ask about the curse":
        ask_about_curse()
    elif response == "Decline the quest":
        decline_quest()

# Function to venture into the forest
def venture_into_forest():
    text = ("You accept the quest and step out of the meeting hall, ready to venture into the Cursed Forest. As you approach the edge of the forest, you feel an eerie chill in the air. The trees are twisted and gnarled, and a thick fog blankets the ground.")
    button_texts = ["Continue into the forest", "Turn back"]

    response = story.handle_story(text, button_texts)
    
    if response == "Continue into the forest":
        end_game()
    elif response == "Turn back":
        decline_quest()

# Function to ask more about the curse and the Heart of Eldoria
def ask_about_curse():
    text = ("The Elder looks at you with deep eyes and explains, 'The curse was cast by the dark sorcerer Malakar a century ago. It turned the forest into a place of darkness and danger. The Heart of Eldoria is a mystical gem that holds the power to lift the curse. It is hidden deep within the forest, protected by powerful magic. We believe you have the strength and courage to retrieve it and save our land.'")
    button_texts = ["Accept the quest", "Decline the quest"]

    response = story.handle_story(text, button_texts)

    if response == "Accept the quest":
        venture_into_forest()
    elif response == "Decline the quest":
        decline_quest()

# Function to decline the quest
def decline_quest():
    text = ("You decline the quest and leave the meeting hall. As you walk away, you can't help but feel a sense of guilt and unease. The fate of Eldoria rests in someone else's hands now...")
    button_texts = ["Play Again", "Exit"]
    
    response = story.handle_story(text, button_texts)

    if response == "Play Again":
        introduction()
    elif response == "Exit":
        pygame.quit()
        sys.exit()

# Function to handle the end of the game
def end_game():
    text = ("Thank you for playing 'Legends & Legacies: The Heart of Eldoria'! Would you like to play again?")
    button_texts = ["Yes", "No"]
    
    response = story.handle_story(text, button_texts)

    if response == "Yes":
        introduction()
    elif response == "No":
        pygame.quit()
        sys.exit()

# Main game loop
clock = pygame.time.Clock()
is_running = True

introduction()

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    pygame.display.update()

pygame.quit()
