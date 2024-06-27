import modules.character as character
import modules.equipment_shop as equipment_shop

player = character.Character()

player.name = "PLAYER NAME"

player.equipment = []

player.gp = 1500

equipment_shop.equipment_shop(player)
if player.equipment == [] or player.equipment == None:
    print(f"TEST: {player.name} has no equipment items.")
else:
    print(f"TEST: {player.name} has the following equipment items:")
    for item in player.equipment:
        print(item.name)
print(f"TEST: {player.name} has {player.gp} gold pieces.")

print("Test Completed!")