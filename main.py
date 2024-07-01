import modules.character as character
import modules.races as races
import modules.archetypes as archetypes
import modules.abilities as abilities

def main():
    player = character.Character()
    player_race = races.choose_race()
    player.race = player_race
    player.name = player.race.name
    player.archetype = archetypes.select_archetype()
    abilities.calculate_abilities(player)
    player.announce_character()
    

if __name__ == '__main__':
    main()
