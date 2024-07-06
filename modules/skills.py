import pygame
import sys
import gui.text_display as text_display
import gui.buttons as buttons
import gui.constants as const

# Initialize pygame
pygame.init()

# Setup screen
surface = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
pygame.display.set_caption('Skill Selection')

def skill_choices(archetype):
    if archetype == "Barbarian":
        return barbarian_skills
    if archetype == "Bard":
        return bard_skills
    if archetype == "Cleric":
        return cleric_skills
    if archetype == "Druid":
        return druid_skills
    if archetype == "Fighter":
        return fighter_skills
    if archetype == "Monk":
        return monk_skills
    if archetype == "Paladin":
        return paladin_skills
    if archetype == "Ranger":
        return ranger_skills
    if archetype == "Rogue":
        return rogue_skills
    if archetype == "Sorcerer":
        return sorcerer_skills
    if archetype == "Warlock":
        return warlock_skills
    if archetype == "Wizard":
        return wizard_skills

def select_skill_proficiencies(archetype):
    button_texts = skill_choices(archetype)
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
                            return button_texts[i]

        surface.fill(const.BG_COLOR)

        if animate_flag:
            text_display.animate_text(surface, 'Choose a skill proficiency below...')
            animate_flag = False
        else:
            text_display.draw_text(surface, 'Choose a skill proficiency below...')

        buttons.draw_buttons(surface, button_texts, button_rects, mouse_pos)

        pygame.display.update()


barbarian_skills = ["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"]
bard_skills = ["Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History", "Insight", "Intimidation", "Investigation", "Medicine", "Nature", "Perception", "Performance", "Persuasion", "Religion", "Sleight of Hand", "Stealth", "Survival"]
cleric_skills = ["History", "Insight", "Medicine", "Persuasion", "Religion"]
druid_skills = ["Arcana", "Animal Handling", "Insight", "Medicine", "Nature", "Perception", "Religion", "Survival"]
fighter_skills = ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"]
monk_skills = ["Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"]
paladin_skills = ["Athletics", "Insight", "Intimidation", "Medicine", "Persuasion", "Religion"]
ranger_skills = ["Animal Handling", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth", "Survival"]
rogue_skills = ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight of Hand", "Stealth"]
sorcerer_skills = ["Arcana", "Deception", "Insight", "Intimidation", "Persuasion", "Religion"]
warlock_skills = ["Arcana", "Deception", "History", "Intimidation", "Investigation", "Nature", "Religion"]
wizard_skills = ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"]
