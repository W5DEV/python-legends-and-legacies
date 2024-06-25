import modules.character_creation as character_creation

def main():
    player = character_creation.character_creation()

    # This is just a synopsis of the player's character sheet, which was built using the character_creation function.
    
    print(f"{player.name} is a {player.race.subrace} {player.archetype.name}.")
    print(f"{player.name} has the following starting equipment:")
    for item in player.equipment:
        print(item.name)
    print(f"{player.name}'s ability scores are as follows:")
    print(f"Strength: {player.strength}")
    print(f"Dexterity: {player.dexterity}")
    print(f"Constitution: {player.constitution}")
    print(f"Intelligence: {player.intelligence}")
    print(f"Wisdom: {player.wisdom}")
    print(f"Charisma: {player.charisma}")
    print(f"{player.name} has {player.max_hp} hit points.")
    print(f"{player.name} has {player.gp} gold pieces.")
    print(f"{player.name} has {player.xp} xp and is level {player.level}. This means they have a proficiency bonus of {player.proficiency_bonus}.")
    print(player.xp_needed_for_next_level())

main()