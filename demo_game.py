import pygame
import gui.constants as constants  # Import the constants module
import gui.text_display as text_display  # Import the text_display module
import gui.buttons as buttons  # Import the buttons module
import gui_modules.character as character
import gui_modules.races as races

def main():
    player = character.Character()
    player_race = races.choose_race()
    player.race = player_race
    player.name = player.race.name
    print(f"{player.name} the {player.race.subrace} has been created!")
    

if __name__ == '__main__':
    main()
