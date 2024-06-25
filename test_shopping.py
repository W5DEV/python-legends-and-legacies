import modules.character as character
import modules.equipment_shop as equipment_shop

player = character.Character("PLAYER NAME", "", "", "", [], [], 0, 1500)

equipment_shop.equipment_shop(player)

player_equipment = player.get_equipment()

print(f"TEST: {player.name} has the following equipment items:")
for item in player_equipment:
    print(item.name)
print(f"TEST: {player.name} has {player.get_gp()} gold pieces.")

print("Test Completed!")