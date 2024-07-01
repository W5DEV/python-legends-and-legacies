import gui.constants as constants  # Import the constants module
import gui.text_display as text_display  # Import the text_display module
import gui.buttons as buttons  # Import the buttons module
import modules.character as character
import modules.races as races
import modules.archetypes as archetypes

def main():
    player = character.Character()
    player_race = races.choose_race()
    player.race = player_race
    player.name = player.race.name
    player.archetype = archetypes.select_archetype()
    player.announce_character()
    

if __name__ == '__main__':
    main()
