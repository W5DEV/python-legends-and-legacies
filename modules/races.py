# This module contains a list of all the races DndBeyond has for character creation.
# We will eventually expand the races to be full-fledged classes, but for now, we will keep them simple.

races = ["Dwarf", "Elf", "Halfling", "Human", "Dragonborn", "Gnome", "Half-Elf", "Half-Orc", "Tiefling"]

def get_races():
    return races

def display_races():
    for race in races:
        print(race)