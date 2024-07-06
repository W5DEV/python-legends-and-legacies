import pygame
import sys
import gui.text_display as text_display
import gui.buttons as buttons
import gui.constants as const

# Initialize pygame
pygame.init()

# Setup screen
surface = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
pygame.display.set_caption('Equipment Selection')

def weapon_choices(choices):
    button_texts = choices
    button_rects = buttons.create_button_rects(len(button_texts))
    
    animate_flag = True  # Flag to control text animation

    while True:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(button_rects):
                    if rect.collidepoint(mouse_pos):
                        if rect.collidepoint(mouse_pos):
                            return choices[i]

        surface.fill(const.BG_COLOR)

        if animate_flag:
            text_display.animate_text(surface, 'Choose from the starting equipment items below...')
            animate_flag = False
        else:
            text_display.draw_text(surface, 'Choose from the starting equipment items below...')

        buttons.draw_buttons(surface, button_texts, button_rects, mouse_pos)

        pygame.display.update()

def get_weapons_from_category(category):
    if category == "Simple Melee Weapons":
        return select_weapon_from_category(simple_melee_weapons)
    if category == "Simple Ranged Weapons":
        return select_weapon_from_category(simple_ranged_weapons)
    if category == "Simple Weapons":
        return select_weapon_from_category(simple_weapons)
    if category == "Martial Melee Weapons":
        return select_weapon_from_category(martial_melee_weapons)
    if category == "Martial Ranged Weapons":
        return select_weapon_from_category(martial_ranged_weapons)
    if category == "Martial Weapons":
        return select_weapon_from_category(martial_weapons)
    if category == "Light Armor":
        return select_weapon_from_category(light_armor)
    if category == "Medium Armor":
        return select_weapon_from_category(medium_armor)
    if category == "Heavy Armor":
        return select_weapon_from_category(heavy_armor)
    if category == "Shields":
        return select_weapon_from_category(shields)
    if category == "Instruments":
        return select_weapon_from_category(instruments)
    if category == "Holy Symbols":
        return select_weapon_from_category(holy_symbols)
    if category == "Packs":
        return select_weapon_from_category(packs)
    if category == "Artisan's Tools":
        return select_weapon_from_category(artisans_tools)
    if category == "Other Tools":
        return select_weapon_from_category(other_tools)
    if category == "Class Equipment":
        return select_weapon_from_category(class_equipment)

def select_weapon_from_category(weapons):
    weapon_names = []
    for weapon in weapons:
        weapon_names.append(weapon.name)
    
    button_texts = weapon_names
    button_rects = buttons.create_button_rects(len(button_texts))

    animate_flag = True  # Flag to control text animation

    while True:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(button_rects):
                    if rect.collidepoint(mouse_pos):
                        return weapons[i]
                        
        surface.fill(const.BG_COLOR)

        if animate_flag:
            text_display.animate_text(surface, 'Choose an item from the equipment category below...')
            animate_flag = False
        else:
            text_display.draw_text(surface, 'Choose an item from the equipment category below...')

        buttons.draw_buttons(surface, button_texts, button_rects, mouse_pos)

        pygame.display.update()


class Weapon:
    def __init__(self, name, cost, damage, weight, properties, proficiency, is_ranged, is_melee, is_versatile = False, versatile_damage = None):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.weight = weight
        self.properties = properties
        self.proficiency = proficiency
        self.is_ranged = is_ranged
        self.is_melee = is_melee
        self.is_versatile = is_versatile
        self.versatile_damage = versatile_damage
    
    def get_info(self):
        print(f"{self.name} is a {self.proficiency} weapon. It costs {self.cost} gold pieces, does {self.damage} damage, weighs {self.weight} pounds, and has the following properties: {self.properties}.")
        return

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
        print(f"{self.name} costs {self.cost} gold pieces, has an AC of {self.ac}, requires a strength of {self.strength}, and weighs {self.weight} pounds.")
        return

def get_info(equipment):
    return equipment.get_info()

class Equipment:
    def __init__(self, name, cost, weight, properties):
        self.name = name
        self.cost = cost
        self.weight = weight
        self.properties = properties
    
    def get_info(self):
        print(f"{self.name} costs {self.cost} gold pieces, weighs {self.weight} pounds, and has the following properties: {self.properties}.")
        return

club = Weapon("Club", 1, "1d4 bludgeoning", 2, "Light", "Simple", False, True)
dagger = Weapon("Dagger", 2, "1d4 piercing", 1, "Finesse, Light, Thrown", "Simple", True, True)
great_club = Weapon("Great Club", 2, "1d8 bludgeoning", 10, "Two-handed", "Simple", False, True)
hand_axe = Weapon("Hand Axe", 5, "1d6 slashing", 2, "Light, Thrown", "Simple", True, True)
javelin = Weapon("Javelin", 5, "1d6 piercing", 2, "Thrown", "Simple", True, True)
light_hammer = Weapon("Light Hammer", 2, "1d4 bludgeoning", 2, "Light, Thrown", "Simple", True, True)
mace = Weapon("Mace", 5, "1d6 bludgeoning", 4, "", "Simple", False, True)
quarter_staff = Weapon("Quarterstaff", 2, "1d6 bludgeoning", 4, "Versatile", "Simple", False, True, True, "1d8")
sickle = Weapon("Sickle", 1, "1d4 slashing", 2, "Light", "Simple", True, False)
spear = Weapon("Spear", 1, "1d6 piercing", 3, "Thrown, Versatile", "Simple",  True, True, True, "1d8")
light_crossbow = Weapon("Light Crossbow", 25, "1d8 piercing", 5, "Ammunition, Loading, Two-handed", "Simple", True, False)
dart = Weapon("Dart", 5, "1d4 piercing", 0.25, "Finesse, Thrown", "Simple", True, False)
short_bow = Weapon("Short Bow", 25, "1d6 piercing", 2, "Ammunition, Two-handed", "Simple", True, False)
sling = Weapon("Sling", 1, "1d4 bludgeoning", 0, "Ammunition", "Simple", True, False)

battleaxe = Weapon("Battleaxe", 10, "1d8 slashing", 4, "Versatile", "Martial", False, True, True, "1d10")
flail = Weapon("Flail", 10, "1d8 bludgeoning", 2, "", "Martial", False, True)
glaive = Weapon("Glaive", 20, "1d10 slashing", 6, "Heavy, Reach, Two-handed", "Martial", False, True)
great_axe = Weapon("Great Axe", 30, "1d12 slashing", 7, "Heavy, Two-handed", "Martial", False, True)
great_sword = Weapon("Great Sword", 50, "2d6 slashing", 6, "Heavy, Two-handed", "Martial", False, True)
halberd = Weapon("Halberd", 20, "1d10 slashing", 6, "Heavy, Reach, Two-handed", "Martial", False, True)
lance = Weapon("Lance", 10, "1d12 piercing", 6, "Reach, Special", "Martial", False, True)
long_sword = Weapon("Long Sword", 15, "1d8 slashing", 3, "Versatile", "Martial", False, True, True, "1d10")
maul = Weapon("Maul", 10, "2d6 bludgeoning", 10, "Heavy, Two-handed", "Martial", False, True)
morningstar = Weapon("Morningstar", 15, "1d8 piercing", 4, "", "Martial", False, True)
pike = Weapon("Pike", 5, "1d10 piercing", 18, "Heavy, Reach, Two-handed", "Martial", False, True)
rapier = Weapon("Rapier", 25, "1d8 piercing", 2, "Finesse", "Martial", False, True)
scimitar = Weapon("Scimitar", 25, "1d6 slashing", 3, "Finesse, Light", "Martial", False, True)
short_sword = Weapon("Short Sword", 10, "1d6 piercing", 2, "Finesse, Light", "Martial", False, True)
trident = Weapon("Trident", 5, "1d6 piercing", 4, "Thrown, Versatile", "Martial", True, True, True, "1d8")
war_pick = Weapon("War Pick", 5, "1d8 piercing", 2, "", "Martial", False, True)
war_hammer = Weapon("War Hammer", 15, "1d8 bludgeoning", 2, "Versatile", "Martial", False, True, True, "1d10")
whip = Weapon("Whip", 2, "1d4 slashing", 3, "Finesse, Reach", "Martial", False, True)
blowgun = Weapon("Blowgun", 10, "1 piercing", 1, "Ammunition, Loading", "Martial", True, False)
hand_crossbow = Weapon("Hand Crossbow", 75, "1d6 piercing", 3, "Ammunition, Light, Loading", "Martial",  True, False)
heavy_crossbow = Weapon("Heavy Crossbow", 50, "1d10 piercing", 18, "Ammunition, Heavy, Loading, Two-handed", "Martial",  True, False)
longbow = Weapon("Longbow", 50, "1d8 piercing", 2, "Ammunition, Heavy, Two-handed", "Martial",  True, False)
net = Weapon("Net", 1, "", 3, "Special, Thrown", "Martial",  True, False)

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

light_armor = [padded_light_armor, leather_light_armor, studded_light_armor]
medium_armor = [hide_medium_armor, chain_shirt_medium_armor, scale_mail_medium_armor, breastplate_medium_armor, half_plate_medium_armor]
heavy_armor = [ring_mail_heavy_armor, chain_mail_heavy_armor, splint_heavy_armor, plate_heavy_armor]


shield = Armor("Shield", 10, 2, 0, 0, 6, 1, 1)

simple_melee_weapons = [club, dagger, great_club, hand_axe, javelin, light_hammer, mace, quarter_staff, sickle, spear]
simple_ranged_weapons = [light_crossbow, dart, short_bow, sling]
simple_weapons = simple_melee_weapons + simple_ranged_weapons
martial_melee_weapons = [battleaxe, flail, glaive, great_axe, great_sword, halberd, lance, long_sword, maul, morningstar, pike, rapier, scimitar, short_sword, trident, war_pick, war_hammer, whip]
martial_ranged_weapons = [blowgun, hand_crossbow, heavy_crossbow, longbow, net]
martial_weapons = martial_melee_weapons + martial_ranged_weapons
weapons = simple_weapons + martial_weapons

light_armor = [padded_light_armor, leather_light_armor, studded_light_armor]
medium_armor = [hide_medium_armor, chain_shirt_medium_armor, scale_mail_medium_armor, breastplate_medium_armor, half_plate_medium_armor]
heavy_armor = [ring_mail_heavy_armor, chain_mail_heavy_armor, splint_heavy_armor, plate_heavy_armor]
armor = light_armor + medium_armor + heavy_armor

shields = [shield]

explorers_pack = Equipment("Explorer's Pack", 10, 59, "Includes a backpack, a bedroll, a mess kit, a tinderbox, 10 torches, 10 days of rations, and a waterskin")
diplomats_pack = Equipment("Diplomat's Pack", 39, 46, "Includes a chest, 2 cases for maps and scrolls, a set of fine clothes, a bottle of ink, an ink pen, a lamp, 2 flasks of oil, 5 sheets of paper, a vial of perfume, sealing wax, and soap")
entertainers_pack = Equipment("Entertainer's Pack", 40, 38, "Includes a backpack, a bedroll, 2 costumes, 5 candles, 5 days of rations, a waterskin, and a disguise kit")
priests_pack = Equipment("Priest's Pack", 19, 25, "Includes a backpack, a blanket, 10 candles, a tinderbox, an alms box, 2 blocks of incense, a censer, vestments, 2 days of rations, and a waterskin")
scholars_pack = Equipment("Scholar's Pack", 40, 11, "Includes a backpack, a book of lore, a bottle of ink, an ink pen, 10 sheets of parchment, a little bag of sand, and a small knife")
burglars_pack = Equipment("Burglar's Pack", 16, 46.5, "Includes a backpack, a bag of 1000 ball bearings, 10 feet of string, a bell, 5 candles, a crowbar, a hammer, 10 pitons, a hooded lantern, 2 flasks of oil, 5 days of rations, a tinderbox, and a waterskin")
dungeoneers_pack = Equipment("Dungeoneer's Pack", 12, 61.5, "Includes a backpack, a crowbar, a hammer, 10 pitons, 10 torches, a tinderbox, 10 days of rations, and a waterskin")

packs = [explorers_pack, diplomats_pack, entertainers_pack, priests_pack, scholars_pack, burglars_pack, dungeoneers_pack]

bagpipes = Equipment("Bagpipes", 30, 6, "Musical Instrument")
drum = Equipment("Drum", 6, 3, "Musical Instrument")
dulcimer = Equipment("Dulcimer", 25, 10, "Musical Instrument")
flute = Equipment("Flute", 2, 1, "Musical Instrument")
lute = Equipment("Lute", 35, 2, "Musical Instrument")
lyre = Equipment("Lyre", 30, 2, "Musical Instrument")
horn = Equipment("Horn", 3, 2, "Musical Instrument")
pan_flute = Equipment("Pan Flute", 12, 2, "Musical Instrument")
shawm = Equipment("Shawm", 2, 1, "Musical Instrument")
viol = Equipment("Viol", 30, 1, "Musical Instrument")

instruments = [bagpipes, drum, dulcimer, flute, lute, lyre, horn, pan_flute, shawm, viol]

holy_symbol_amulet = Equipment("Holy Symbol Amulet", 5, 1, "Holy Symbol")
holy_symbol_emblem = Equipment("Holy Symbol Emblem", 5, 0, "Holy Symbol")
holy_symbol_reliquary = Equipment("Holy Symbol Reliquary", 5, 2, "Holy Symbol")

holy_symbols = [holy_symbol_amulet, holy_symbol_emblem, holy_symbol_reliquary]

druidic_focus = Equipment("Druidic Focus", 0, 0, "Sprig of Mistletoe")

alchemists_supplies = Equipment("Alchemist's Supplies", 50, 8, "Artisan Tools")
brewers_supplies = Equipment("Brewer's Supplies", 20, 9, "Artisan Tools")
calligraphers_supplies = Equipment("Calligrapher's Supplies", 10, 5, "Artisan Tools")
carpenters_tools = Equipment("Carpenter's Tools", 8, 6, "Artisan Tools")
cartographers_tools = Equipment("Cartographer's Tools", 15, 6, "Artisan Tools")
cobblers_tools = Equipment("Cobbler's Tools", 5, 5, "Artisan Tools")
cooks_utensils = Equipment("Cook's Utensils", 1, 8, "Artisan Tools")
glassblowers_tools = Equipment("Glassblower's Tools", 30, 5, "Artisan Tools")
jewelers_tools = Equipment("Jeweler's Tools", 25, 2, "Artisan Tools")
leatherworkers_tools = Equipment("Leatherworker's Tools", 5, 5, "Artisan Tools")
masons_tools = Equipment("Mason's Tools", 10, 8, "Artisan Tools")
painters_supplies = Equipment("Painter's Supplies", 10, 5, "Artisan Tools")
potters_tools = Equipment("Potter's Tools", 10, 3, "Artisan Tools")
smiths_tools = Equipment("Smith's Tools", 20, 8, "Artisan Tools")
tinkers_tools = Equipment("Tinker's Tools", 50, 10, "Artisan Tools")
weavers_tools = Equipment("Weaver's Tools", 1, 5, "Artisan Tools")
woodcarvers_tools = Equipment("Woodcarver's Tools", 1, 5, "Artisan Tools")

artisans_tools = [alchemists_supplies, brewers_supplies, calligraphers_supplies, carpenters_tools, cartographers_tools, cobblers_tools, cooks_utensils, glassblowers_tools, jewelers_tools, leatherworkers_tools, masons_tools, painters_supplies, potters_tools, smiths_tools, tinkers_tools, weavers_tools, woodcarvers_tools]

disguise_kit = Equipment("Disguise Kit", 25, 3, "Other Tools")
forgery_kit = Equipment("Forgery Kit", 15, 5, "Other Tools")
herbalism_kit = Equipment("Herbalism Kit", 5, 3, "Other Tools")
navigator_tools = Equipment("Navigator's Tools", 25, 2, "Other Tools")
poisoners_kit = Equipment("Poisoner's Kit", 50, 2, "Other Tools")
thieves_tools = Equipment("Thieves' Tools", 25, 1, "Other Tools")

other_tools = [disguise_kit, forgery_kit, herbalism_kit, navigator_tools, poisoners_kit, thieves_tools]

component_pouch = Equipment("Component Pouch", 25, 2, "Contains a variety of components needed for spellcasting")

arcane_focus_crystal = Equipment("Arcane Focus Crystal", 10, 1, "Arcane Focus")
arcane_focus_orb = Equipment("Arcane Focus Orb", 20, 3, "Arcane Focus")
arcane_focus_rod = Equipment("Arcane Focus Rod", 10, 2, "Arcane Focus")
arcane_focus_staff = Equipment("Arcane Focus Staff", 5, 4, "Arcane Focus")
arcane_focus_wand = Equipment("Arcane Focus Wand", 10, 1, "Arcane Focus")

spellbook = Equipment("Spellbook", 50, 3, "Contains a variety of spells")

class_equipment = [component_pouch, arcane_focus_crystal, arcane_focus_orb, arcane_focus_rod, arcane_focus_staff, arcane_focus_wand, druidic_focus, spellbook]

equipment_types = ["Simple Weapons","Simple Melee Weapons", "Simple Ranged Weapons", "Martial Weapons", "Martial Melee Weapons", "Martial Ranged Weapons", "Light Armor", "Medium Armor", "Heavy Armor", "Shields", "Packs", "Instruments", "Holy Symbols", "Artisan's Tools", "Other Tools", "Class Equipment"]

def starting_equipment(item):
    for equip_item in simple_weapons:
        if item == equip_item.name:
            return equip_item
    for equip_item in martial_weapons:
        if item == equip_item.name:
            return equip_item
    for equip_item in light_armor:
        if item == equip_item.name:
            return equip_item
    for equip_item in medium_armor:
        if item == equip_item.name:
            return equip_item
    for equip_item in heavy_armor:
        if item == equip_item.name:
            return equip_item
    for equip_item in shields:
        if item == equip_item.name:
            return equip_item
    for equip_item in packs:
        if item == equip_item.name:
            return equip_item
    for equip_item in instruments:
        if item == equip_item.name:
            return equip_item
    for equip_item in holy_symbols:
        if item == equip_item.name:
            return equip_item
    for equip_item in artisans_tools:
        if item == equip_item.name:
            return equip_item
    for equip_item in other_tools:
        if item == equip_item.name:
            return equip_item
    for equip_item in class_equipment:
        if item == equip_item.name:
            return equip_item
    return None