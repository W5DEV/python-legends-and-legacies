import modules.character_creation as character_creation

def main():
    player = character_creation.character_creation()

    # This is just a synopsis of the player's character sheet, which was built using the character_creation function.
    
    print(f"{player.name} is a {player.race.subrace} {player.archetype.name}.")
    print(f"{player.name}'s bio is as follows:")
    print(player.bio)
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
    print(f"{player.name} needs {player.xp_needed_for_next_level()} xp to level up.")
    print(player.xp_needed_for_next_level())
    print("Simulating a level up...")
    player.award_xp(300)
    print(f"{player.name} is level {player.level}. They have a max of {player.max_hp} hit points. Their proficiency bonus is {player.proficiency_bonus}. They need {player.xp_needed_for_next_level()} to level up.")

    player.equip_armor()
    player.equip_weapon()
    player.ready_weapon()
    player.equip_shield()
    player.unequip_armor()
    player.unequip_weapon()
    player.unequip_shield()

    ac = player.calculate_armor_class()
    print(f"{player.name}'s Armor Class is {ac}.")

    return
main()