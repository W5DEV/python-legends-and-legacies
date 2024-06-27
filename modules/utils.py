import modules.dice_rolls as dice_rolls

# This list contains the XP thresholds for each level. It is set from DnDBeyond's XP thresholds for a standard campaign.
xp_thresholds = [
        0,      # Level 1
        300,    # Level 2
        900,    # Level 3
        2700,   # Level 4
        6500,   # Level 5
        14000,  # Level 6
        23000,  # Level 7
        34000,  # Level 8
        48000,  # Level 9
        64000,  # Level 10
        85000,  # Level 11
        100000, # Level 12
        120000, # Level 13
        140000, # Level 14
        165000, # Level 15
        195000, # Level 16
        225000, # Level 17
        265000, # Level 18
        305000, # Level 19
        355000  # Level 20
    ]

# This function will calculate the starting gp based on the archetype
def calculate_starting_gp(archetype):
    gp = 0
    if archetype.lower() == "cleric":
        dice_roll = dice_rolls.roll_4_sided_dice() + dice_rolls.roll_4_sided_dice() + dice_rolls.roll_4_sided_dice() + dice_rolls.roll_4_sided_dice() + dice_rolls.roll_4_sided_dice()
        gp = dice_roll * 10 
    elif archetype.lower() == "fighter":
        dice_roll = dice_rolls.roll_4_sided_dice() + dice_rolls.roll_4_sided_dice() + dice_rolls.roll_4_sided_dice() + dice_rolls.roll_4_sided_dice() + dice_rolls.roll_4_sided_dice()
        gp = dice_roll * 10
    elif archetype.lower() == "rogue":
        dice_roll = dice_rolls.roll_4_sided_dice() + dice_rolls.roll_4_sided_dice() + dice_rolls.roll_4_sided_dice() + dice_rolls.roll_4_sided_dice()
        gp = dice_roll * 10
    elif archetype.lower() == "wizard":
        dice_roll = dice_rolls.roll_4_sided_dice() + dice_rolls.roll_4_sided_dice() + dice_rolls.roll_4_sided_dice() + dice_rolls.roll_4_sided_dice()
        gp = dice_roll * 10
    else:
        gp = 0

    return gp

# This function will calculate the level based on the XP thresholds
def calculate_level(xp):
    # Determine the level based on the XP thresholds
    level = 1
    for i in range(len(xp_thresholds)):
        if xp >= xp_thresholds[i]:
            level = i + 1
        else:
            break
    
    return level

# This function will calculate the XP needed to reach the next level. It is based on the above thresholds.
def calculate_xp_needed(xp):
    # Determine the XP needed for the next level based on the XP thresholds
    next_level_xp = xp_thresholds[1]  # Default to level 2 threshold

    for i in range(len(xp_thresholds)):
        if xp >= xp_thresholds[i]:
            if i + 1 < len(xp_thresholds):
                next_level_xp = xp_thresholds[i + 1]
            else:
                next_level_xp = None  # No next level, max level reached
        else:
            break
    
    if next_level_xp is None:
        return "Max level reached"
    else:
        xp_needed = next_level_xp - xp

        return xp_needed

# This function will roll 4 six-sided dice, drop the lowest value, and return the sum of the remaining 3 dice
def roll_ability():
    initial_roll = [dice_rolls.roll_6_sided_dice(), dice_rolls.roll_6_sided_dice(), dice_rolls.roll_6_sided_dice(), dice_rolls.roll_6_sided_dice()]
    initial_roll.remove(min(initial_roll))
    return initial_roll[0] + initial_roll[1] + initial_roll[2]

def calculate_abilities():
    roll_1 = roll_ability()
    roll_2 = roll_ability()
    roll_3 = roll_ability()
    roll_4 = roll_ability()
    roll_5 = roll_ability()
    roll_6 = roll_ability()
    rolls = [roll_1, roll_2, roll_3, roll_4, roll_5, roll_6]
    rolls.sort(reverse=True)
    displayed_available_abilities = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
    available_abilities = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
    print(f"Your available ability scores are {rolls}")
    for i in range(6):
        print(f"Please assign an ability to the score of {rolls[i]}:")
        print(displayed_available_abilities)
        ability = input(f"Enter the ability you would like to assign {rolls[i]}: ")
        while ability.lower() not in available_abilities:
            print("Invalid ability. Please choose from the following:")
            print(available_abilities)
            ability = input("Enter the ability you would like to assign: ")
        if ability.lower() == "strength":
            str = rolls[i]
            displayed_available_abilities.remove("Strength")
            available_abilities.remove("strength")
        elif ability.lower() == "dexterity":
            dex = rolls[i]
            displayed_available_abilities.remove("Dexterity")
            available_abilities.remove("dexterity")
        elif ability.lower() == "constitution":
            con = rolls[i]
            displayed_available_abilities.remove("Constitution")
            available_abilities.remove("constitution")
        elif ability.lower() == "intelligence":
            int = rolls[i]
            displayed_available_abilities.remove("Intelligence")
            available_abilities.remove("intelligence")
        elif ability.lower() == "wisdom":
            wis = rolls[i]
            displayed_available_abilities.remove("Wisdom")
            available_abilities.remove("wisdom")
        elif ability.lower() == "charisma":
            cha = rolls[i]
            displayed_available_abilities.remove("Charisma")
            available_abilities.remove("charisma")
    
    return str, dex, con, int, wis, cha

