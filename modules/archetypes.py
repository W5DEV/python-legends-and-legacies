# This module contains a list of all the classes DndBeyond has for character creation.
# Since the word "class" is reserved in Python, we will use the term "archetype" to refer to the D&D classes.

import archetypes.barbarian as Barbarian
import archetypes.bard as Bard
import archetypes.cleric as Cleric
import archetypes.druid as Druid
import archetypes.fighter as Fighter
import archetypes.monk as Monk
import archetypes.paladin as Paladin

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
    else: 
        return archetype_name
   
