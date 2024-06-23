import random
import math

class User:
    def __init__(self, name, race, archetype, bio, armor, weapon, abilities, xp, gp):
        self.name = name
        self.race = race
        self.archetype = archetype
        self.bio = bio
        self.armor = armor
        self.weapon = weapon
        self.abilities = abilities
        self.xp = xp
        self.gp = gp

    def add_armor(self, armor):
        self.armor = armor

    def add_weapon(self, weapon):
        self.weapon = weapon

    def greet(self):
        return f"Hello, {self.name}!"
    
    def get_info(self):
        return f"{self.name} is a {self.race} {self.archetype}"
    
    def get_bio(self):
        return f"{self.bio}"
    
    def get_armor(self):
        if self.armor == None:
            return f"{self.name} is not wearing armor."
        return f"{self.name} is wearing {self.armor}"
    
    def get_weapon(self):
        if self.weapon == None:
            return f"{self.name} is not wielding a weapon."
        return f"{self.name} is wielding {self.weapon}"
    
    def get_abilities(self):
        for ability, value in self.abilities.items():
            return f"{ability}: {value}"
    
    def get_gp(self):
        return f"{self.name} has {self.gp} gold pieces."
    
    def get_xp(self):
        level = calculate_level(self.xp)
        return f"{self.name} has {self.xp}, so they are level {level}."

    def award_xp(self, xp):
        self.xp += xp
        level = calculate_level(self.xp)
        return f"{self.name} has received {xp} XP and now has a total of {self.xp} XP, making them level {level}."
    
    def xp_needed_for_next_level(self):
        xp_needed = calculate_xp_needed(self.xp)
        return f"{self.name} needs {xp_needed} XP to reach the next level."

class Armor:
    def __init__(self, name, cost, ac, strength, stealth, weight, doff_time, don_time):
        self.name = name
        self.cost = cost
        self.ac = ac
        self.strength = strength
        self.stealth = stealth
        self.weight = weight
        self.doff_time = doff_time
        self.don_time = don_time
    
    def get_info(self):
        return f"{self.name} is {self.description}. It costs {self.cost} gold pieces, has an AC of {self.ac}, requires a strength of {self.strength}, and weighs {self.weight} pounds."
    
class Weapon:
    def __init__(self, name, cost, damage, weight, properties, proficiency):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.weight = weight
        self.properties = properties
        self.proficiency = proficiency
    
    def get_info(self):
        return f"{self.name} is {self.description}. It costs {self.cost} gold pieces, deals {self.damage} damage, and weighs {self.weight} pounds."

class Simple_Weapons:
    club_simple_weapon = Weapon("Club", 1, "1d4 bludgeoning", 2, "Light", "Simple")
    dagger_simple_weapon = Weapon("Dagger", 2, "1d4 piercing", 1, "Finesse, Light, Thrown", "Simple")
    greatclub_simple_weapon = Weapon("Greatclub", 2, "1d8 bludgeoning", 10, "Two-handed", "Simple")
    handaxe_simple_weapon = Weapon("Handaxe", 5, "1d6 slashing", 2, "Light, Thrown", "Simple")
    javelin_simple_weapon = Weapon("Javelin", 5, "1d6 piercing", 2, "Thrown", "Simple")
    light_hammer_simple_weapon = Weapon("Light Hammer", 2, "1d4 bludgeoning", 2, "Light, Thrown", "Simple")
    mace_simple_weapon = Weapon("Mace", 5, "1d6 bludgeoning", 4, "", "Simple")
    quarterstaff_simple_weapon = Weapon("Quarterstaff", 2, "1d6 bludgeoning", 4, "Versatile", "Simple")
    sickle_simple_weapon = Weapon("Sickle", 1, "1d4 slashing", 2, "Light", "Simple")
    spear_simple_weapon = Weapon("Spear", 1, "1d6 piercing", 3, "Thrown, Versatile", "Simple")

    light_crossbow_simple_weapon = Weapon("Light Crossbow", 25, "1d8 piercing", 5, "Ammunition, Loading, Two-handed", "Simple")
    dart_simple_weapon = Weapon("Dart", 5, "1d4 piercing", 0.25, "Finesse, Thrown", "Simple")
    shortbow_simple_weapon = Weapon("Shortbow", 25, "1d6 piercing", 2, "Ammunition, Two-handed", "Simple")
    sling_simple_weapon = Weapon("Sling", 1, "1d4 bludgeoning", 0, "Ammunition", "Simple")

class Martial_Weapons:
    battleaxe_martial_weapon = Weapon("Battleaxe", 10, "1d8 slashing", 4, "Versatile", "Martial")
    flail_martial_weapon = Weapon("Flail", 10, "1d8 bludgeoning", 2, "", "Martial")
    glaive_martial_weapon = Weapon("Glaive", 20, "1d10 slashing", 6, "Heavy, Reach, Two-handed", "Martial")
    greataxe_martial_weapon = Weapon("Greataxe", 30, "1d12 slashing", 7, "Heavy, Two-handed", "Martial")
    greatsword_martial_weapon = Weapon("Greatsword", 50, "2d6 slashing", 6, "Heavy, Two-handed", "Martial")
    halberd_martial_weapon = Weapon("Halberd", 20, "1d10 slashing", 6, "Heavy, Reach, Two-handed", "Martial")
    lance_martial_weapon = Weapon("Lance", 10, "1d12 piercing", 6, "Reach, Special", "Martial")
    longsword_martial_weapon = Weapon("Longsword", 15, "1d8 slashing", 3, "Versatile", "Martial")
    maul_martial_weapon = Weapon("Maul", 10, "2d6 bludgeoning", 10, "Heavy, Two-handed", "Martial")
    morningstar_martial_weapon = Weapon("Morningstar", 15, "1d8 piercing", 4, "", "Martial")
    pike_martial_weapon = Weapon("Pike", 5, "1d10 piercing", 18, "Heavy, Reach, Two-handed", "Martial")
    rapier_martial_weapon = Weapon("Rapier", 25, "1d8 piercing", 2, "Finesse", "Martial")
    scimitar_martial_weapon = Weapon("Scimitar", 25, "1d6 slashing", 3, "Finesse, Light", "Martial")
    shortsword_martial_weapon = Weapon("Shortsword", 10, "1d6 piercing", 2, "Finesse, Light", "Martial")
    trident_martial_weapon = Weapon("Trident", 5, "1d6 piercing", 4, "Thrown, Versatile", "Martial")
    war_pick_martial_weapon = Weapon("War Pick", 5, "1d8 piercing", 2, "", "Martial")
    warhammer_martial_weapon = Weapon("Warhammer", 15, "1d8 bludgeoning", 2, "Versatile", "Martial")
    whip_martial_weapon = Weapon("Whip", 2, "1d4 slashing", 3, "Finesse, Reach", "Martial")

    blowgun_martial_weapon = Weapon("Blowgun", 10, "1 piercing", 1, "Ammunition, Loading", "Martial")
    hand_crossbow_martial_weapon = Weapon("Hand Crossbow", 75, "1d6 piercing", 3, "Ammunition, Light, Loading", "Martial")
    heavy_crossbow_martial_weapon = Weapon("Heavy Crossbow", 50, "1d10 piercing", 18, "Ammunition, Heavy, Loading, Two-handed", "Martial")
    longbow_martial_weapon = Weapon("Longbow", 50, "1d8 piercing", 2, "Ammunition, Heavy, Two-handed", "Martial")
    net_martial_weapon = Weapon("Net", 1, "", 3, "Special, Thrown", "Martial")

class Light_Armor:
    padded_light_armor = Armor("Padded Light Armor", 5, 11, 0, -1, 8, 1, 1)
    leather_light_armor = Armor("Leather Light Armor", 10, 11, 0, 0, 10, 1, 1)
    studded_light_armor = Armor("Studded Light Armor", 45, 12, 0, 0, 13, 1, 1)

class Medium_Armor:
    hide_medium_armor = Armor("Hide Medium Armor", 10, 12, 0, 0, 12, 5, 1)
    chain_shirt_medium_armor = Armor("Chain Shirt Medium Armor", 50, 13, 0, 0, 20, 1, 5)
    scale_mail_medium_armor = Armor("Scale Mail Medium Armor", 50, 14, 0, -1, 45, 1, 5)
    breastplate_medium_armor = Armor("Breastplate Medium Armor", 400, 14, 0, 0, 20, 1, 5)
    half_plate_medium_armor = Armor("Half Plate Medium Armor", 750, 15, 0, -1, 40, 1, 5)

class Heavy_Armor:
    ring_mail_heavy_armor = Armor("Ring Mail Heavy Armor", 30, 14, 0, -1, 40, 5, 10)
    chain_mail_heavy_armor = Armor("Chain Mail Heavy Armor", 75, 16, 13, -1, 55, 5, 10)
    splint_heavy_armor = Armor("Splint Heavy Armor", 200, 17, 15, -1, 60, 5, 10)
    plate_heavy_armor = Armor("Plate Heavy Armor", 1500, 18, 15, -1, 65, 5, 10)

class Shields:
    shield = Armor("Shield", 10, 2, 0, 0, 6, 1, 1)

class Coin_Types:
    copper = 1
    silver = 10
    electrum = 50
    gold = 100
    platinum = 1000

def main():
    print("Greetings traveller! Welcome to the world of D&D!")
    name = input("What is your name? ")
    print(f"Hello, {name}!")

    races = ["Dwarf", "Elf", "Halfling", "Human", "Dragonborn", "Gnome", "Half-Elf", "Half-Orc", "Tiefling"]
    print("Please choose a race from the following list:")
    for race in races:
        print(race)
    
    race = input("Which race would you like to be? ")
    print(f"Great! You are a {race}.")

    archetypes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
    print("Please choose an class from the following list:")
    for archetype in archetypes:
        print(archetype)

    archetype = input("Which class would you like to be? ")  
    print(f"Great! You are a {archetype}.")

    xp = 0

    gp = 0

    gp = calculate_starting_gp(archetype)

    print(f"You have {gp} gold pieces.")

    bio = input("Tell me a little about your character.")

    abilities = {}

    abilities["Strength"] = roll_ability()
    abilities["Dexterity"] = roll_ability()
    abilities["Constitution"] = roll_ability()
    abilities["Intelligence"] = roll_ability()
    abilities["Wisdom"] = roll_ability()
    abilities["Charisma"] = roll_ability()

    print("Here are your abilities: ")
    for ability, value in abilities.items():
        print(f"{ability}: {value}") 

    armor = None

    has_armor = input("Would you like to wear armor? (yes/no) ")
    if has_armor.lower() == "yes":
        print("Please choose a type of armor from the following list: ")
        armor_types = []
        for armor in Light_Armor.__dict__.values():
            if isinstance(armor, Armor):
                armor_types.append(armor)
        for armor in Medium_Armor.__dict__.values():
            if isinstance(armor, Armor):
                armor_types.append(armor)
        for armor in Heavy_Armor.__dict__.values():
            if isinstance(armor, Armor):
                armor_types.append(armor)
        for armor in Shields.__dict__.values():
            if isinstance(armor, Armor):
                armor_types.append(armor)
        for armor in armor_types:
            print(armor.name, armor.cost, armor.ac, armor.strength, armor.stealth, armor.weight, armor.doff_time, armor.don_time)
        armor_answer = input("Which armor would you like to wear? ")
        armor_choice = None
        for armor in armor_types:
            if armor_answer.lower() == armor.name.lower():
                armor_choice = armor
        if armor_choice == None:
            print("That is not a valid armor.")
        if gp >= armor_choice.cost:
            gp -= armor_choice.cost
            print(f"You have chosen {armor_choice.name}. You have {gp} gold pieces remaining.")
            armor = armor_choice.name
        else:
            print("You cannot afford that armor.")
    else:
        print("You are not wearing armor.")

    weapon = None

    has_weapon = input("Would you like to wield a weapon? (yes/no) ")
    if has_weapon.lower() == "yes":
        print("Please choose a type of weapon from the following list: ")
        weapon_types = []
        for weapon in Simple_Weapons.__dict__.values():
            if isinstance(weapon, Weapon):
                weapon_types.append(weapon)
        for weapon in Martial_Weapons.__dict__.values():
            if isinstance(weapon, Weapon):
                weapon_types.append(weapon)
        for weapon in weapon_types:
            print(weapon.name, weapon.cost, weapon.damage, weapon.weight, weapon.properties, weapon.proficiency)    
        weapon_answer = input("Which weapon would you like to wield? ")
        weapon_choice = None
        for weapon in weapon_types:
            if weapon_answer.lower() == weapon.name.lower():
                weapon_choice = weapon
        if weapon_choice == None:
            print("That is not a valid weapon.")
        if gp >= weapon_choice.cost:
            gp -= weapon_choice.cost
            print(f"You have chosen {weapon_choice.name}. You have {gp} gold pieces remaining.")
            weapon = weapon_choice.name
        else: 
            print("You cannot afford that weapon.")
    else:
        print("You are not wielding a weapon.")

    user = User(name, race, archetype, bio, armor, weapon, abilities, xp, gp)

    print(user.greet())
    print(user.get_info())
    print(user.get_bio())
    print(user.get_armor())
    print(user.get_weapon())
    print(user.get_abilities())
    print(user.get_gp())
    print(user.get_xp())
    print(user.award_xp(49))
    print(user.award_xp(1))
    print(user.xp_needed_for_next_level())
    print(user.award_xp(24))
    print(user.xp_needed_for_next_level())
    print(user.award_xp(1))
    print(user.xp_needed_for_next_level())

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

def roll_100_sided_dice():
    return random.randint(1, 100)

def calculate_starting_gp(archetype):
    gp = 0
    if archetype.lower() == "cleric":
        dice_roll = roll_4_sided_dice() + roll_4_sided_dice() + roll_4_sided_dice() + roll_4_sided_dice() + roll_4_sided_dice()
        gp = dice_roll * 10 
    elif archetype.lower() == "fighter":
        dice_roll = roll_4_sided_dice() + roll_4_sided_dice() + roll_4_sided_dice() + roll_4_sided_dice() + roll_4_sided_dice()
        gp = dice_roll * 10
    elif archetype.lower() == "rogue":
        dice_roll = roll_4_sided_dice() + roll_4_sided_dice() + roll_4_sided_dice() + roll_4_sided_dice()
        gp = dice_roll * 10
    elif archetype.lower() == "wizard":
        dice_roll = roll_4_sided_dice() + roll_4_sided_dice() + roll_4_sided_dice() + roll_4_sided_dice()
        gp = dice_roll * 10
    else:
        gp = 0

    return gp

def calculate_level(xp):
    # Using the quadratic formula to solve for n in the equation: xp = 5 * n * (n - 1) / 2
    # This simplifies to: n^2 - n - (2 * xp / 5) = 0
    a = 1
    b = -1
    c = -2 * xp / 5
    
    # Calculate the discriminant
    discriminant = b**2 - 4 * a * c
    
    if discriminant < 0:
        return 0  # No real solution, should not happen with valid XP
    
    # Calculate the positive root of the quadratic equation
    level = (-b + math.sqrt(discriminant)) / (2 * a)

    return math.floor(level)

def calculate_xp_needed(current_xp):
    level = calculate_level(current_xp)
    xp_for_level = 0
    for i in range(0, level + 1):
        xp_for_level += i * 5
    needed_xp = xp_for_level - current_xp
    return needed_xp

def roll_ability():
    initial_roll = [roll_6_sided_dice(), roll_6_sided_dice(), roll_6_sided_dice(), roll_6_sided_dice()]
    initial_roll.remove(min(initial_roll))
    return initial_roll[0] + initial_roll[1] + initial_roll[2]


main()