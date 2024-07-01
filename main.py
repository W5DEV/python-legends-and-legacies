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
    player.initialize_player()
    player.award_xp(300)
    player.award_xp(600)
    player.award_xp(1800)
    player.award_xp(3800)
    player.award_xp(7500)
    player.award_xp(9000)
    player.award_xp(11000)
    player.announce_character()
    

if __name__ == '__main__':
    main()
