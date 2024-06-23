import modules.character_creation as character_creation

def main():
    player = character_creation.character_creation()

    # This is just a synopsis of the player's character sheet, which was built using the character_creation function.
    print(player.greet())
    print(player.get_info())
    print(player.get_bio())
    print(f"{player.name} has the following equipment items:")
    for item in player.get_equipment():
        print(item.name)
    print(f"{player.name} has the following abilities:")
    for ability, value in player.get_abilities().items():
        print(f"{ability}: {value}")
    print(f"{player.name} has {player.get_gp()} gold pieces.")
    print(player.get_xp())
    print(player.xp_needed_for_next_level())

main()