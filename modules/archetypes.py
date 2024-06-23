# Since the word "class" is reserved in Python, we will use the term "archetype" to refer to the D&D classes.
# This module contains a list of all the archetypes DndBeyond has for character creation.
# We will eventually expand the archetypes to be full-fledged classes, but for now, we will keep them simple.

archetypes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]

def get_archetypes():
    return archetypes

def display_archetypes():
    for archetype in archetypes:
        print(archetype)