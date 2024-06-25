import modules.equipment as equipment

def equipment_shop(player):
    print(f"Hello, {player.name}!")
    print("Welcome to the equipment shop!")
    print(f"You have {player.gp} gp.")
    shopping = True
    receipt = []
    print("Would you like to buy equipment? (yes or no)")
    buy_equipment = input()
    while buy_equipment.lower() not in ['yes', 'no']:
        print("Invalid input. Please enter 'yes' or 'no'.")
        buy_equipment = input()
    if buy_equipment.lower() == 'no':
        shopping = False
    elif buy_equipment.lower() == 'yes':
        shopping = True
    while shopping:
        print("Please choose a category from the below list:")
        valid_categories = []
        for category in equipment.equipment_types:
            valid_categories.append(category.lower())
            print(category)
        print("Please enter a category or type 'exit' to leave the shop:")
        category_selection = input()
        if category_selection.lower() == 'exit':
            shopping = False
            break
        while category_selection.lower() not in valid_categories:
            print("Invalid category. Please enter a valid category or type 'exit' to leave the shop:")
            category_selection = input()
            if category_selection.lower() == 'exit':
                shopping = False
                break
        if category_selection == 'simple melee weapons':
            print("Simple Melee Weapons:")
            valid_simple_melee_weapons = []
            for weapon in equipment.simple_melee_weapons:
                valid_simple_melee_weapons.append(weapon.name.lower())
                print(f"Weapon Name: {weapon.name}. Cost: {weapon.cost}.")
            print("Would you like to buy any of these weapons? (yes or no)")
            buy_weapon_confirm = input()
            while buy_weapon_confirm.lower() not in ['yes', 'no']:
                print("Invalid input. Please enter 'yes' or 'no'.")
                buy_weapon_confirm = input()
            if buy_weapon_confirm.lower() == 'yes':
                print("Please enter the name of the weapon you would like to buy:")
                weapon_to_buy = input()
                while weapon_to_buy not in valid_simple_melee_weapons:
                    print("Invalid weapon name. Please enter a valid weapon name:")
                    weapon_to_buy = input()
                for weapon in equipment.simple_melee_weapons:
                    if weapon.name.lower() == weapon_to_buy.lower():
                        if player.gp >= weapon.cost:
                            player.gp -= weapon.cost
                            player.equipment.append(weapon)
                            print(f"{weapon.name} has been added to your inventory.")
                            print(f"You have {player.gp} gp remaining.")
                            receipt.append(weapon.name)
                        else:
                            print(f"You have {player.gp} gp, but the {item.name} costs {item.cost} gp.")
                            print("You do not have enough gp to purchase this item.")
                            break

        elif category_selection == 'simple ranged weapons':
            print("Simple Ranged Weapons:")
            valid_simple_ranged_weapons = []
            for weapon in equipment.simple_ranged_weapons:
                valid_simple_ranged_weapons.append(weapon.name.lower())
                print(f"Weapon Name: {weapon.name}. Cost: {weapon.cost}.")
            print("Would you like to buy any of these weapons? (yes or no)")
            buy_weapon_confirm = input()
            while buy_weapon_confirm.lower() not in ['yes', 'no']:
                print("Invalid input. Please enter 'yes' or 'no'.")
                buy_weapon_confirm = input()
            if buy_weapon_confirm.lower() == 'yes':
                print("Please enter the name of the weapon you would like to buy:")
                weapon_to_buy = input()
                while weapon_to_buy not in valid_simple_ranged_weapons:
                    print("Invalid weapon name. Please enter a valid weapon name:")
                    weapon_to_buy = input()
                for weapon in equipment.simple_ranged_weapons:
                    if weapon.name.lower() == weapon_to_buy.lower():
                        if player.gp >= weapon.cost:
                            player.gp -= weapon.cost
                            player.equipment.append(weapon)
                            print(f"{weapon.name} has been added to your inventory.")
                            print(f"You have {player.gp} gp remaining.")
                            receipt.append(weapon.name)
                        else:
                            print(f"You have {player.gp} gp, but the {item.name} costs {item.cost} gp.")
                            print("You do not have enough gp to purchase this item.")
                            break
        
        elif category_selection == 'martial melee weapons':
            print("Martial Melee Weapons:")
            valid_martial_melee_weapons = []
            for weapon in equipment.martial_melee_weapons:
                valid_martial_melee_weapons.append(weapon.name.lower())
                print(f"Weapon Name: {weapon.name}. Cost: {weapon.cost}.")
            print("Would you like to buy any of these weapons? (yes or no)")
            buy_weapon_confirm = input()
            while buy_weapon_confirm.lower() not in ['yes', 'no']:
                print("Invalid input. Please enter 'yes' or 'no'.")
                buy_weapon_confirm = input()
            if buy_weapon_confirm.lower() == 'yes':
                print("Please enter the name of the weapon you would like to buy:")
                weapon_to_buy = input()
                while weapon_to_buy not in valid_martial_melee_weapons:
                    print("Invalid weapon name. Please enter a valid weapon name:")
                    weapon_to_buy = input()
                for weapon in equipment.martial_melee_weapons:
                    if weapon.name.lower() == weapon_to_buy.lower():
                        if player.gp >= weapon.cost:
                            player.gp -= weapon.cost
                            player.equipment.append(weapon)
                            print(f"{weapon.name} has been added to your inventory.")
                            print(f"You have {player.gp} gp remaining.")
                            receipt.append(weapon.name)
                        else:
                            print(f"You have {player.gp} gp, but the {item.name} costs {item.cost} gp.")
                            print("You do not have enough gp to purchase this item.")
                            break

        elif category_selection == 'martial ranged weapons':
            print("Martial Ranged Weapons:")
            valid_martial_ranged_weapons = []
            for weapon in equipment.martial_ranged_weapons:
                valid_martial_ranged_weapons.append(weapon.name.lower())
                print(f"Weapon Name: {weapon.name}. Cost: {weapon.cost}.")
            print("Would you like to buy any of these weapons? (yes or no)")
            buy_weapon_confirm = input()
            while buy_weapon_confirm.lower() not in ['yes', 'no']:
                print("Invalid input. Please enter 'yes' or 'no'.")
                buy_weapon_confirm = input()
            if buy_weapon_confirm.lower() == 'yes':
                print("Please enter the name of the weapon you would like to buy:")
                weapon_to_buy = input()
                while weapon_to_buy not in valid_martial_ranged_weapons:
                    print("Invalid weapon name. Please enter a valid weapon name:")
                    weapon_to_buy = input()
                for weapon in equipment.martial_ranged_weapons:
                    if weapon.name.lower() == weapon_to_buy.lower():
                        if player.gp >= weapon.cost:
                            player.gp -= weapon.cost
                            player.equipment.append(weapon)
                            print(f"{weapon.name} has been added to your inventory.")
                            print(f"You have {player.gp} gp remaining.")
                            receipt.append(weapon.name)
                        else:
                            print(f"You have {player.gp} gp, but the {item.name} costs {item.cost} gp.")
                            print("You do not have enough gp to purchase this item.")
                            break
        
        elif category_selection == 'light armor':
            print("Light Armor:")
            valid_light_armor = []
            for armor in equipment.light_armor:
                valid_light_armor.append(armor.name.lower())
                print(f"Armor Name: {armor.name}. Cost: {armor.cost}.")
            print("Would you like to buy any of these armors? (yes or no)")
            buy_armor_confirm = input()
            while buy_armor_confirm.lower() not in ['yes', 'no']:
                print("Invalid input. Please enter 'yes' or 'no'.")
                buy_armor_confirm = input()
            if buy_armor_confirm.lower() == 'yes':
                print("Please enter the name of the armor you would like to buy:")
                armor_to_buy = input()
                while armor_to_buy not in valid_light_armor:
                    print("Invalid armor name. Please enter a valid armor name:")
                    armor_to_buy = input()
                for armor in equipment.light_armor:
                    if armor.name.lower() == armor_to_buy.lower():
                        if player.gp >= armor.cost:
                            player.gp -= armor.cost
                            player.equipment.append(armor)
                            print(f"{armor.name} has been added to your inventory.")
                            print(f"You have {player.gp} gp remaining.")
                            receipt.append(armor.name)
                        else:
                            print(f"You have {player.gp} gp, but the {item.name} costs {item.cost} gp.")
                            print("You do not have enough gp to purchase this item.")
                            break

        elif category_selection == 'medium armor':
            print("Medium Armor:")
            valid_medium_armor = []
            for armor in equipment.medium_armor:
                valid_medium_armor.append(armor.name.lower())
                print(f"Armor Name: {armor.name}. Cost: {armor.cost}.")
            print("Would you like to buy any of these armors? (yes or no)")
            buy_armor_confirm = input()
            while buy_armor_confirm.lower() not in ['yes', 'no']:
                print("Invalid input. Please enter 'yes' or 'no'.")
                buy_armor_confirm = input()
            if buy_armor_confirm.lower() == 'yes':
                print("Please enter the name of the armor you would like to buy:")
                armor_to_buy = input()
                while armor_to_buy not in valid_medium_armor:
                    print("Invalid armor name. Please enter a valid armor name:")
                    armor_to_buy = input()
                for armor in equipment.medium_armor:
                    if armor.name.lower() == armor_to_buy.lower():
                        if player.gp >= armor.cost:
                            player.gp -= armor.cost
                            player.equipment.append(armor)
                            print(f"{armor.name} has been added to your inventory.")
                            print(f"You have {player.gp} gp remaining.")
                            receipt.append(armor.name)
                        else:
                            print(f"You have {player.gp} gp, but the {item.name} costs {item.cost} gp.")
                            print("You do not have enough gp to purchase this item.")
                            break
        
        elif category_selection == 'heavy armor':
            print("Heavy Armor:")
            valid_heavy_armor = []
            for armor in equipment.heavy_armor:
                valid_heavy_armor.append(armor.name.lower())
                print(f"Armor Name: {armor.name}. Cost: {armor.cost}.")
            print("Would you like to buy any of these armors? (yes or no)")
            buy_armor_confirm = input()
            while buy_armor_confirm.lower() not in ['yes', 'no']:
                print("Invalid input. Please enter 'yes' or 'no'.")
                buy_armor_confirm = input()
            if buy_armor_confirm.lower() == 'yes':
                print("Please enter the name of the armor you would like to buy:")
                armor_to_buy = input()
                while armor_to_buy not in valid_heavy_armor:
                    print("Invalid armor name. Please enter a valid armor name:")
                    armor_to_buy = input()
                for armor in equipment.heavy_armor:
                    if armor.name.lower() == armor_to_buy.lower():
                        if player.gp >= armor.cost:
                            player.gp -= armor.cost
                            player.equipment.append(armor)
                            print(f"{armor.name} has been added to your inventory.")
                            print(f"You have {player.gp} gp remaining.")
                            receipt.append(armor.name)
                        else:
                            print(f"You have {player.gp} gp, but the {item.name} costs {item.cost} gp.")
                            print("You do not have enough gp to purchase this item.")
                            break
        
        elif category_selection == 'shields':
            print("Shields:")
            valid_shields = []
            for shield in equipment.shields:
                valid_shields.append(shield.name.lower())
                print(f"Shield Name: {shield.name}. Cost: {shield.cost}.")
            print("Would you like to buy any of these shields? (yes or no)")
            buy_shield_confirm = input()
            while buy_shield_confirm.lower() not in ['yes', 'no']:
                print("Invalid input. Please enter 'yes' or 'no'.")
                buy_shield_confirm = input()
            if buy_shield_confirm.lower() == 'yes':
                print("Please enter the name of the shield you would like to buy:")
                shield_to_buy = input()
                while shield_to_buy not in valid_shields:
                    print("Invalid shield name. Please enter a valid shield name:")
                    shield_to_buy = input()
                for shield in equipment.shields:
                    if shield.name.lower() == shield_to_buy.lower():
                        if player.gp >= shield.cost:
                            player.gp -= shield.cost
                            player.equipment.append(shield)
                            print(f"{shield.name} has been added to your inventory.")
                            print(f"You have {player.gp} gp remaining.")
                            receipt.append(shield.name)
                        else:
                            print(f"You have {player.gp} gp, but the {item.name} costs {item.cost} gp.")
                            print("You do not have enough gp to purchase this item.")
                            break
        
        elif category_selection == 'packs':
            print("Packs:")
            valid_packs = []
            for pack in equipment.packs:
                valid_packs.append(pack.name.lower())
                print(f"Pack Name: {pack.name}. Cost: {pack.cost}.")
            print("Would you like to buy any of these packs? (yes or no)")
            buy_pack_confirm = input()
            while buy_pack_confirm.lower() not in ['yes', 'no']:
                print("Invalid input. Please enter 'yes' or 'no'.")
                buy_pack_confirm = input()
            if buy_pack_confirm.lower() == 'yes':
                print("Please enter the name of the pack you would like to buy:")
                pack_to_buy = input()
                while pack_to_buy not in valid_packs:
                    print("Invalid pack name. Please enter a valid pack name:")
                    pack_to_buy = input()
                for pack in equipment.packs:
                    if pack.name.lower() == pack_to_buy.lower():
                        if player.gp >= pack.cost:
                            player.gp -= pack.cost
                            player.equipment.append(pack)
                            print(f"{pack.name} has been added to your inventory.")
                            print(f"You have {player.gp} gp remaining.")
                            receipt.append(pack.name)
                        else:
                            print(f"You have {player.gp} gp, but the {item.name} costs {item.cost} gp.")
                            print("You do not have enough gp to purchase this item.")
                            break

        elif category_selection == 'instruments':
            print("Instruments:")
            valid_instruments = []
            for instrument in equipment.instruments:
                valid_instruments.append(instrument.name.lower())
                print(f"Instrument Name: {instrument.name}. Cost: {instrument.cost}.")
            print("Would you like to buy any of these instruments? (yes or no)")
            buy_instrument_confirm = input()
            while buy_instrument_confirm.lower() not in ['yes', 'no']:
                print("Invalid input. Please enter 'yes' or 'no'.")
                buy_instrument_confirm = input()
            if buy_instrument_confirm.lower() == 'yes':
                print("Please enter the name of the instrument you would like to buy:")
                instrument_to_buy = input()
                while instrument_to_buy not in valid_instruments:
                    print("Invalid instrument name. Please enter a valid instrument name:")
                    instrument_to_buy = input()
                for instrument in equipment.instruments:
                    if instrument.name.lower() == instrument_to_buy.lower():
                        if player.gp >= instrument.cost:
                            player.gp -= instrument.cost
                            player.equipment.append(instrument)
                            print(f"{instrument.name} has been added to your inventory.")
                            print(f"You have {player.gp} gp remaining.")
                            receipt.append(instrument.name)
                        else:
                            print(f"You have {player.gp} gp, but the {item.name} costs {item.cost} gp.")
                            print("You do not have enough gp to purchase this item.")
                            break

        elif category_selection == 'holy symbols':
            print("Holy Symbols:")
            valid_holy_symbols = []
            for symbol in equipment.holy_symbols:
                valid_holy_symbols.append(symbol.name.lower())
                print(f"Symbol Name: {symbol.name}. Cost: {symbol.cost}.")
            print("Would you like to buy any of these symbols? (yes or no)")
            buy_symbol_confirm = input()
            while buy_symbol_confirm.lower() not in ['yes', 'no']:
                print("Invalid input. Please enter 'yes' or 'no'.")
                buy_symbol_confirm = input()
            if buy_symbol_confirm.lower() == 'yes':
                print("Please enter the name of the symbol you would like to buy:")
                symbol_to_buy = input()
                while symbol_to_buy not in valid_holy_symbols:
                    print("Invalid symbol name. Please enter a valid symbol name:")
                    symbol_to_buy = input()
                for symbol in equipment.holy_symbols:
                    if symbol.name.lower() == symbol_to_buy.lower():
                        if player.gp >= symbol.cost:
                            player.gp -= symbol.cost
                            player.equipment.append(symbol)
                            print(f"{symbol.name} has been added to your inventory.")
                            print(f"You have {player.gp} gp remaining.")
                            receipt.append(symbol.name)
                        else:
                            print(f"You have {player.gp} gp, but the {item.name} costs {item.cost} gp.")
                            print("You do not have enough gp to purchase this item.")
                            break
        
        elif category_selection == "artisan's tools":
            print("Artisan's Tools:")
            valid_artisans_tools = []
            for tool in equipment.artisans_tools:
                valid_artisans_tools.append(tool.name.lower())
                print(f"Tool Name: {tool.name}. Cost: {tool.cost}.")
            print("Would you like to buy any of these tools? (yes or no)")
            buy_tool_confirm = input()
            while buy_tool_confirm.lower() not in ['yes', 'no']:
                print("Invalid input. Please enter 'yes' or 'no'.")
                buy_tool_confirm = input()
            if buy_tool_confirm.lower() == 'yes':
                print("Please enter the name of the tool you would like to buy:")
                tool_to_buy = input()
                while tool_to_buy not in valid_artisans_tools:
                    print("Invalid tool name. Please enter a valid tool name:")
                    tool_to_buy = input()
                for tool in equipment.artisans_tools:
                    if tool.name.lower() == tool_to_buy.lower():
                        if player.gp >= tool.cost:
                            player.gp -= tool.cost
                            player.equipment.append(tool)
                            print(f"{tool.name} has been added to your inventory.")
                            print(f"You have {player.gp} gp remaining.")
                            receipt.append(tool.name)
                        else:
                            print(f"You have {player.gp} gp, but the {item.name} costs {item.cost} gp.")
                            print("You do not have enough gp to purchase this item.")
                            break

        elif category_selection == 'other tools':
            print("Other Tools:")
            valid_other_tools = []
            for tool in equipment.other_tools:
                valid_other_tools.append(tool.name.lower())
                print(f"Tool Name: {tool.name}. Cost: {tool.cost}.")
            print("Would you like to buy any of these tools? (yes or no)")
            buy_tool_confirm = input()
            while buy_tool_confirm.lower() not in ['yes', 'no']:
                print("Invalid input. Please enter 'yes' or 'no'.")
                buy_tool_confirm = input()
            if buy_tool_confirm.lower() == 'yes':
                print("Please enter the name of the tool you would like to buy:")
                tool_to_buy = input()
                while tool_to_buy not in valid_other_tools:
                    print("Invalid tool name. Please enter a valid tool name:")
                    tool_to_buy = input()
                for tool in equipment.other_tools:
                    if tool.name.lower() == tool_to_buy.lower():
                        if player.gp >= tool.cost:
                            player.gp -= tool.cost
                            player.equipment.append(tool)
                            print(f"{tool.name} has been added to your inventory.")
                            print(f"You have {player.gp} gp remaining.")
                            receipt.append(tool.name)
                        else:
                            print(f"You have {player.gp} gp, but the {item.name} costs {item.cost} gp.")
                            print("You do not have enough gp to purchase this item.")
                            break

        elif category_selection == 'class equipment':
            print("Class Equipment:")
            valid_class_equipment = []
            for item in equipment.class_equipment:
                valid_class_equipment.append(item.name.lower())
                print(f"Item Name: {item.name}. Cost: {item.cost}.")
            print("Would you like to buy any of these items? (yes or no)")
            buy_item_confirm = input()
            while buy_item_confirm.lower() not in ['yes', 'no']:
                print("Invalid input. Please enter 'yes' or 'no'.")
                buy_item_confirm = input()
            if buy_item_confirm.lower() == 'yes':
                print("Please enter the name of the item you would like to buy:")
                item_to_buy = input()
                while item_to_buy not in valid_class_equipment:
                    print("Invalid item name. Please enter a valid item name:")
                    item_to_buy = input()
                for item in equipment.class_equipment:
                    if item.name.lower() == item_to_buy.lower():
                        if player.gp >= item.cost:
                            player.gp -= item.cost
                            player.equipment.append(item)
                            print(f"{item.name} has been added to your inventory.")
                            print(f"You have {player.gp} gp remaining.")
                            receipt.append(item.name)
                        else:
                            print(f"You have {player.gp} gp, but the {item.name} costs {item.cost} gp.")
                            print("You do not have enough gp to purchase this item.")
                            break
    print("Thank you for visiting the equipment shop!")
    print(f"You have {player.gp} gp remaining.")
    print("You have purchased the following items:")
    for item in receipt:
        print(item)
    print("You currently have the following items in your inventory:")
    for item in player.equipment:
        print(item.name)
    print("Good luck on your adventures! Goodbye!")
    