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

