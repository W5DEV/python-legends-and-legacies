import random

def get_human_name():
    confirm = "no"
    while confirm.lower() != "yes":
        print("Humans don't have specific names. They are named like any other human.")
        print("What is your character's name?")
        name =  input("> ")
        print("What is your character's house name?")
        house_name = input("> ")
        print(f"Your human's name is {name} of house {house_name}.")
        print("Is this correct? (yes/no)")
        confirm = input("> ")
        while confirm.lower() not in ['yes', 'no']:
            print("Please enter 'yes' or 'no'.")
            confirm = input("> ")
    return name + " " + house_name
        

def get_dwarf_name(gender):
    name = ""
    clan_name = ""
    dwarf_male_names = ["Adrik", "Alberich", "Baern", "Barendd", "Brottor", "Bruenor", "Dain", "Darrak", "Delg", "Eberk", "Einkil", "Fargrim", "Flint", "Gardain", "Harbek", "Kildrak", "Morgran", "Orsik", "Oskar", "Rangrim", "Rurik", "Taklinn", "Thoradin", "Thorin", "Tordek", "Traubon", "Travok", "Ulfgar", "Veit", "Vondal"]
    dwarf_female_names = ["Amber", "Artin", "Audhild", "Bardryn", "Dagnal", "Diesa", "Eldeth", "Falkrunn", "Finellen", "Gunnloda", "Gurdis", "Helja", "Hlin", "Kathra", "Kristryd", "Ilde", "Liftrasa", "Mardred", "Riswynn", "Sannl", "Torbera", "Torgga", "Vistra"]
    dwarf_clan_names = ["Balderk", "Battlehammer", "Brawnanvil", "Dankil", "Fireforge", "Frostbeard", "Gorunn", "Holderhek", "Ironfist", "Loderr", "Lutgehr", "Rumnaheim", "Strakeln", "Torunn", "Ungart"]
    print("Dwarves have a first name and a clan name.")
    print("A dwarf's name is granted by a clan elder, in accordance with tradition.")
    if gender.lower() == 'male':
        name = random.choice(dwarf_male_names)
    elif gender.lower() == 'female':
        name = random.choice(dwarf_female_names)

    clan_name = random.choice(dwarf_clan_names)

    print(f"Your dwarf's name is {name} of clan {clan_name}.")
    return name + " " + clan_name

def get_elf_name(gender):
    name = ""
    family_name = ""
    elf_child_names = ["Ara", "Bryn", "Del", "Eryn", "Faen", "Innil", "Lael", "Mella", "Naill", "Naeris", "Phann", "Rael", "Rinn", "Sai", "Syllin", "Thia", "Vall"]
    elf_male_names = ["Adran", "Aelar", "Aramil", "Arannis", "Aust", "Beiro", "Berrian", "Carric", "Enialis", "Erdan", "Erevan", "Galinndan", "Hadarai", "Heian", "Himo", "Immeral", "Ivellios", "Laucian", "Mindartis", "Paelias", "Peren", "Quarion", "Riardon", "Rolen", "Soveliss", "Thamior", "Tharivol", "Theren", "Varis"]
    elf_female_names = ["Adrie", "Althaea", "Anastrianna", "Andraste", "Antinua", "Bethrynna", "Birel", "Caelynn", "Drusilia", "Enna", "Felosial", "Ielenia", "Jelenneth", "Keyleth", "Leshanna", "Lia", "Meriele", "Mialee", "Naivara", "Quelenna", "Quillathe", "Sariel", "Shanairra", "Shava", "Silaqui", "Theirastra", "Thia", "Vadania", "Valanthe", "Xanaphia"]
    elf_family_names = ["Amakiir", "Amastacia", "Galanodel", "Holimion", "Ilphelkiir", "Liadon", "Meliamne", "Nai'lo", "Siannodel", "Xiloscient"]
    print("Elves have a first name and a family name.")
    print("Is your elf a child?")
    is_child = input("> ")
    while is_child.lower() not in ['yes', 'no']:
        print("Please enter 'yes' or 'no'.")
        is_child = input("> ")
    if is_child == 'yes':
        name = random.choice(elf_child_names)
        family_name = random.choice(elf_family_names)
    else:
        print("Adult Elves have the ability to choose their own name.")
        print("Please choose a name from the following list:")
        if gender.lower() == "male":
            for name in elf_male_names:
                print(name)
            name = input("> ")
            while name not in elf_male_names:
                print("That name is not compatible with male elves.")
                print("Please choose a name from the list.")
                name = input("> ")
        elif gender.lower() == "female":
            for name in elf_female_names:
                print(name)
            name = input("> ")
            while name not in elf_female_names:
                print("That name is not compatible with female elves.")
                print("Please choose a name from the list.")
                name = input("> ")

        family_name = random.choice(elf_family_names)
    print(f"Your elf's name is {name} of the family {family_name}.")
    return name + " " + family_name
            
def get_halfling_name(gender):
    name = ""
    family_name = ""
    nickname = ""
    random_chance = random.randint(0, 1)
    halfling_male_names = ["Alton", "Ander", "Cade", "Corrin", "Eldon", "Errich", "Finnan", "Garret", "Lindal", "Lyle", "Merric", "Milo", "Osborn", "Perrin", "Reed", "Roscoe", "Wellby"]
    halfling_female_names = ["Andry", "Bree", "Callie", "Cora", "Euphemia", "Jillian", "Kithri", "Lavinia", "Lidda", "Merla", "Nedda", "Paela", "Portia", "Seraphina", "Shaena", "Trym", "Vani", "Verna"]
    halfling_family_names = ["Brushgather", "Goodbarrel", "Greenbottle", "High-hill", "Hilltopple", "Leagallow", "Tealeaf", "Thorngage", "Tosscobble", "Underbough"]
    print("Halflings have a first name and a family name.")
    print("A halfling's name is a gift from their family.")
    if random_chance == 1:
        print("Your halfling has a nickname given by friends or family to suit their personality.")
        print("Pick a memorable nickname which your halfling will be known by: ")
        nickname = input("> ")
        print(f"Your halfling's nickname is {nickname}.")
        print("Please confirm you are happy with this nickname. (yes/no)")
        nickname_confirm = input("> ")
        while nickname_confirm.lower() not in ['yes', 'no']:
            print("Invalid answer. Please enter 'yes' or 'no'.")
            print(f"Your halfling's nickname is {nickname}.")
            print("Please confirm you are happy with this nickname. (yes/no)")
            nickname_confirm = input("> ")
        while nickname_confirm.lower() == 'no':
            print("Pick a memorable nickname which your halfling will be known by: ")
            nickname = input("> ")
            print(f"Your halfling's nickname is {nickname}.")
            print("Please confirm you are happy with this nickname. (yes/no)")
            nickname_confirm = input("> ")
    if gender.lower() == 'male':
        name = random.choice(halfling_male_names)
    elif gender.lower() == 'female':
        name = random.choice(halfling_female_names)
    family_name = random.choice(halfling_family_names)
    if random_chance == 1:
        print(f"Your halfling's name is {name} of family {family_name}, but people call them {nickname}.")
        return name + " '" + nickname + "' " + family_name
    else:
        print(f"Your halfling's name is {name} of family {family_name}.")
        return name + " " + family_name




