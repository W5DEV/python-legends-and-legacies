# text_logic.py

def get_updated_text(action, state):
    # Define the storyline and consequences
    story = {
        'start': {
            'text': 'You are standing at the entrance of a dark cave. What do you do?',
            'choices': ['Enter the cave', 'Walk away']
        },
        'enter_cave': {
            'text': 'You enter the cave and find a treasure chest. What do you do?',
            'choices': ['Open the chest', 'Leave the chest']
        },
        'walk_away': {
            'text': 'You walk away from the cave and find a village. What do you do?',
            'choices': ['Enter the village', 'Keep walking']
        },
        'open_chest': {
            'text': 'You open the chest and find gold! You win!',
            'choices': ['Restart', 'Quit']
        },
        'leave_chest': {
            'text': 'You leave the chest and exit the cave. You are safe but poorer.',
            'choices': ['Restart', 'Quit']
        },
        'enter_village': {
            'text': 'You enter the village and find friendly villagers. You win!',
            'choices': ['Restart', 'Quit']
        },
        'keep_walking': {
            'text': 'You keep walking and get lost. Game over.',
            'choices': ['Restart', 'Quit']
        }
    }

    # Determine the next state based on the action and current state
    next_state = {
        ('start', 'Enter the cave'): 'enter_cave',
        ('start', 'Walk away'): 'walk_away',
        ('enter_cave', 'Open the chest'): 'open_chest',
        ('enter_cave', 'Leave the chest'): 'leave_chest',
        ('walk_away', 'Enter the village'): 'enter_village',
        ('walk_away', 'Keep walking'): 'keep_walking',
        ('open_chest', 'Restart'): 'start',
        ('open_chest', 'Quit'): 'quit',
        ('leave_chest', 'Restart'): 'start',
        ('leave_chest', 'Quit'): 'quit',
        ('enter_village', 'Restart'): 'start',
        ('enter_village', 'Quit'): 'quit',
        ('keep_walking', 'Restart'): 'start',
        ('keep_walking', 'Quit'): 'quit'
    }.get((state, action), 'start')

    # Return the updated text and choices
    return story[next_state]['text'], story[next_state]['choices'], next_state
