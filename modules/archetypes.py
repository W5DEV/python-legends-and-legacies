# This module contains a list of all the classes DndBeyond has for character creation.
# Since the word "class" is reserved in Python, we will use the term "archetype" to refer to the D&D classes.

import archetypes.barbarian as Barbarian
import archetypes.bard as Bard
import archetypes.cleric as Cleric
import archetypes.druid as Druid
import archetypes.fighter as Fighter
import archetypes.monk as Monk
import archetypes.paladin as Paladin
import archetypes.ranger as Ranger
import archetypes.rogue as Rogue
import archetypes.sorcerer as Sorcerer
import archetypes.warlock as Warlock
import archetypes.wizard as Wizard

displayed_archetypes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]

archetypes = ["barbarian", "bard", "cleric", "druid", "fighter", "monk", "paladin", "ranger", "rogue", "sorcerer", "warlock", "wizard"]

def display_archetypes():
    for archetype in displayed_archetypes:
        print(archetype)

def create_archetype(archetype_name):
    if archetype_name == "barbarian":
        barbarian = Barbarian.define_barbarian()
        return barbarian
    elif archetype_name == "bard":
        bard = Bard.define_bard()
        return bard
    elif archetype_name == "cleric":
        cleric = Cleric.define_cleric()
        return cleric
    elif archetype_name == "druid":
        druid = Druid.define_druid()
        return druid
    elif archetype_name == "fighter":
        fighter = Fighter.define_fighter()
        return fighter
    elif archetype_name == "monk":
        monk = Monk.define_monk()
        return monk
    elif archetype_name == "paladin":
        paladin = Paladin.define_paladin()
        return paladin
    elif archetype_name == "ranger":
        ranger = Ranger.define_ranger()
        return ranger
    elif archetype_name == "rogue":
        rogue = Rogue.define_rogue()
        return rogue
    elif archetype_name == "sorcerer":
        sorcerer = Sorcerer.define_sorcerer()
        return sorcerer
    elif archetype_name == "warlock":
        warlock = Warlock.define_warlock()
        return warlock
    elif archetype_name == "wizard":
        wizard = Wizard.define_wizard()
        return wizard
    else: 
        return "archetype_name not found"
    
def test_archetypes():
    print("Testing Classes...")
    display_archetypes()
    print("Testing Barbarian... ")
    barbarian_test = create_archetype("barbarian")
    barbarian_test.get_info()
    print("Testing Bard... ")
    bard_test = create_archetype("bard")
    bard_test.get_info()
    print("Testing Cleric... ")
    cleric_test = create_archetype("cleric")
    cleric_test.get_info()
    print("Testing Druid... ")
    druid_test = create_archetype("druid")
    druid_test.get_info()
    print("Testing Fighter... ")
    fighter_test = create_archetype("fighter")
    fighter_test.get_info()
    print("Testing Monk... ")
    monk_test = create_archetype("monk")
    monk_test.get_info()
    print("Testing Paladin... ")
    paladin_test = create_archetype("paladin")
    paladin_test.get_info()
    print("Testing Ranger... ")
    ranger_test = create_archetype("ranger")
    ranger_test.get_info()
    print("Testing Rogue... ")
    rogue_test = create_archetype("rogue")
    rogue_test.get_info()
    print("Testing Sorcerer... ")
    sorcerer_test = create_archetype("sorcerer")
    sorcerer_test.get_info()
    print("Testing Warlock... ")
    warlock_test = create_archetype("warlock")
    warlock_test.get_info()
    print("Testing Wizard... ")
    wizard_test = create_archetype("wizard")
    wizard_test.get_info()
    print("Class Tests Completed...")
    print("Please Report Any Bugs or Errors.")
    return
   
