import random

# This module contains functions that simulate rolling dice of various sizes.

def roll_2_sided_dice():
    return random.randint(1, 2)

def roll_4_sided_dice():
    return random.randint(1, 4)

def roll_6_sided_dice():
    return random.randint(1, 6)

def roll_8_sided_dice():
    return random.randint(1, 8)

def roll_10_sided_dice():
    return random.randint(1, 10)

def roll_12_sided_dice():
    return random.randint(1, 12)

def roll_20_sided_dice():
    return random.randint(1, 20)

def roll_percentage_dice():
    return roll_10_sided_dice() * 10 + roll_10_sided_dice()