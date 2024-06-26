from archetypes.barbarian import define_barbarian
from archetypes.bard import define_bard
from archetypes.cleric import define_cleric
from archetypes.druid import define_druid
from archetypes.fighter import define_fighter
from archetypes.monk import define_monk
from archetypes.paladin import define_paladin
from archetypes.ranger import define_ranger
from archetypes.rogue import define_rogue
from archetypes.sorcerer import define_sorcerer
from archetypes.warlock import define_warlock
from archetypes.wizard import define_wizard


def test_archetypes():
    print("Choose a number to test:")
    print("1. Barbarian")
    print("2. Bard")
    print("3. Cleric")
    print("4. Druid")
    print("5. Fighter")
    print("6. Monk")
    print("7. Paladin")
    print("8. Ranger")
    print("9. Rogue")
    print("10. Sorcerer")
    print("11. Warlock")
    print("12. Wizard")
    print("> ", end="")
    choice = input()
    if choice == "1":
        define_barbarian()
    elif choice == "2":
        define_bard()
    elif choice == "3":
        define_cleric()
    elif choice == "4":
        define_druid()
    elif choice == "5":
        define_fighter()
    elif choice == "6":
        define_monk()
    elif choice == "7":
        define_paladin()
    elif choice == "8":
        define_ranger()
    elif choice == "9":
        define_rogue()
    elif choice == "10":
        define_sorcerer()
    elif choice == "11":
        define_warlock()
    elif choice == "12":
        define_wizard()
    else:
        print("Invalid choice.")
        test_archetypes()
    return

test_archetypes()
    