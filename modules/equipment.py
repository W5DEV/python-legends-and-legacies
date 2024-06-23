class Weapon:
    def __init__(self, name, cost, damage, weight, properties, proficiency):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.weight = weight
        self.properties = properties
        self.proficiency = proficiency
    
    def get_info(self, lookup_name):
        return f"{self.name} is a {self.proficiency} weapon. It costs {self.cost} gold pieces, does {self.damage} damage, weighs {self.weight} pounds, and has the following properties: {self.properties}."

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

equipment_types = ["Simple Weapons", "Martial Weapons", "Light Armor", "Medium Armor", "Heavy Armor", "Shield"]

club = Weapon("Club", 1, "1d4 bludgeoning", 2, "Light", "Simple")
dagger = Weapon("Dagger", 2, "1d4 piercing", 1, "Finesse, Light, Thrown", "Simple")
great_club = Weapon("Great Club", 2, "1d8 bludgeoning", 10, "Two-handed", "Simple")
hand_axe = Weapon("Hand Axe", 5, "1d6 slashing", 2, "Light, Thrown", "Simple")
javelin = Weapon("Javelin", 5, "1d6 piercing", 2, "Thrown", "Simple")
light_hammer = Weapon("Light Hammer", 2, "1d4 bludgeoning", 2, "Light, Thrown", "Simple")
mace = Weapon("Mace", 5, "1d6 bludgeoning", 4, "", "Simple")
quarter_staff = Weapon("Quarterstaff", 2, "1d6 bludgeoning", 4, "Versatile", "Simple")
sickle = Weapon("Sickle", 1, "1d4 slashing", 2, "Light", "Simple")
spear = Weapon("Spear", 1, "1d6 piercing", 3, "Thrown, Versatile", "Simple")
light_crossbow = Weapon("Light Crossbow", 25, "1d8 piercing", 5, "Ammunition, Loading, Two-handed", "Simple")
dart = Weapon("Dart", 5, "1d4 piercing", 0.25, "Finesse, Thrown", "Simple")
short_bow = Weapon("Short Bow", 25, "1d6 piercing", 2, "Ammunition, Two-handed", "Simple")
sling = Weapon("Sling", 1, "1d4 bludgeoning", 0, "Ammunition", "Simple")

battleaxe = Weapon("Battleaxe", 10, "1d8 slashing", 4, "Versatile", "Martial")
flail = Weapon("Flail", 10, "1d8 bludgeoning", 2, "", "Martial")
glaive = Weapon("Glaive", 20, "1d10 slashing", 6, "Heavy, Reach, Two-handed", "Martial")
great_axe = Weapon("Great Axe", 30, "1d12 slashing", 7, "Heavy, Two-handed", "Martial")
great_sword = Weapon("Great Sword", 50, "2d6 slashing", 6, "Heavy, Two-handed", "Martial")
halberd = Weapon("Halberd", 20, "1d10 slashing", 6, "Heavy, Reach, Two-handed", "Martial")
lance = Weapon("Lance", 10, "1d12 piercing", 6, "Reach, Special", "Martial")
long_sword = Weapon("Long Sword", 15, "1d8 slashing", 3, "Versatile", "Martial")
maul = Weapon("Maul", 10, "2d6 bludgeoning", 10, "Heavy, Two-handed", "Martial")
morningstar = Weapon("Morningstar", 15, "1d8 piercing", 4, "", "Martial")
pike = Weapon("Pike", 5, "1d10 piercing", 18, "Heavy, Reach, Two-handed", "Martial")
rapier = Weapon("Rapier", 25, "1d8 piercing", 2, "Finesse", "Martial")
scimitar = Weapon("Scimitar", 25, "1d6 slashing", 3, "Finesse, Light", "Martial")
short_sword = Weapon("Short Sword", 10, "1d6 piercing", 2, "Finesse, Light", "Martial")
trident = Weapon("Trident", 5, "1d6 piercing", 4, "Thrown, Versatile", "Martial")
war_pick = Weapon("War Pick", 5, "1d8 piercing", 2, "", "Martial")
war_hammer = Weapon("War Hammer", 15, "1d8 bludgeoning", 2, "Versatile", "Martial")
whip = Weapon("Whip", 2, "1d4 slashing", 3, "Finesse, Reach", "Martial")
blowgun = Weapon("Blowgun", 10, "1 piercing", 1, "Ammunition, Loading", "Martial")
hand_crossbow = Weapon("Hand Crossbow", 75, "1d6 piercing", 3, "Ammunition, Light, Loading", "Martial")
heavy_crossbow = Weapon("Heavy Crossbow", 50, "1d10 piercing", 18, "Ammunition, Heavy, Loading, Two-handed", "Martial")
longbow = Weapon("Longbow", 50, "1d8 piercing", 2, "Ammunition, Heavy, Two-handed", "Martial")
net = Weapon("Net", 1, "", 3, "Special, Thrown", "Martial")

padded_light_armor = Armor("Padded Light Armor", 5, 11, 0, -1, 8, 1, 1)
leather_light_armor = Armor("Leather Light Armor", 10, 11, 0, 0, 10, 1, 1)
studded_light_armor = Armor("Studded Light Armor", 45, 12, 0, 0, 13, 1, 1)

hide_medium_armor = Armor("Hide Medium Armor", 10, 12, 0, 0, 12, 5, 1)
chain_shirt_medium_armor = Armor("Chain Shirt Medium Armor", 50, 13, 0, 0, 20, 1, 5)
scale_mail_medium_armor = Armor("Scale Mail Medium Armor", 50, 14, 0, -1, 45, 1, 5)
breastplate_medium_armor = Armor("Breastplate Medium Armor", 400, 14, 0, 0, 20, 1, 5)
half_plate_medium_armor = Armor("Half Plate Medium Armor", 750, 15, 0, -1, 40, 1, 5)

ring_mail_heavy_armor = Armor("Ring Mail Heavy Armor", 30, 14, 0, -1, 40, 5, 10)
chain_mail_heavy_armor = Armor("Chain Mail Heavy Armor", 75, 16, 13, -1, 55, 5, 10)
splint_heavy_armor = Armor("Splint Heavy Armor", 200, 17, 15, -1, 60, 5, 10)
plate_heavy_armor = Armor("Plate Heavy Armor", 1500, 18, 15, -1, 65, 5, 10)

shield = Armor("Shield", 10, 2, 0, 0, 6, 1, 1)

simple_weapons = [club, dagger, great_club, hand_axe, javelin, light_hammer, mace, quarter_staff, sickle, spear, light_crossbow, dart, short_bow, sling]
martial_weapons = [battleaxe, flail, glaive, great_axe, great_sword, halberd, lance, long_sword, maul, morningstar, pike, rapier, scimitar, short_sword, trident, war_pick, war_hammer, whip, blowgun, hand_crossbow, heavy_crossbow, longbow, net]
light_armor = [padded_light_armor, leather_light_armor, studded_light_armor]
medium_armor = [hide_medium_armor, chain_shirt_medium_armor, scale_mail_medium_armor, breastplate_medium_armor, half_plate_medium_armor]
heavy_armor = [ring_mail_heavy_armor, chain_mail_heavy_armor, splint_heavy_armor, plate_heavy_armor]

def get_info(equipment):
    return equipment.get_info()