import pygame
import sys
import gui.text_display as text_display
import gui.buttons as buttons
import gui.constants as const

# Initialize pygame
pygame.init()

# Setup screen
surface = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
pygame.display.set_caption('Spell Selection')

def spell_choices(archetype):
    if archetype == "Bard":
        return bard_spells
    if archetype == "Cleric":
        return cleric_spells
    if archetype == "Druid":
        return druid_spells
    if archetype == "Paladin":
        return paladin_spells
    if archetype == "Sorcerer":
        return sorcerer_spells
    if archetype == "Warlock":
        return warlock_spells
    if archetype == "Wizard":
        return wizard_spells

def select_spells(archetype):
    button_texts = spell_choices(archetype)
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
            text_display.animate_text(surface, 'Choose a spell below...')
            animate_flag = False
        else:
            text_display.draw_text(surface, 'Choose a spell below...')

        buttons.draw_buttons(surface, button_texts, button_rects, mouse_pos)

        pygame.display.update()

bard_spells = ["Animal Friendship", "Bane", "Charm Person", "Comprehend Languages", "Cure Wounds", "Detect Magic", "Disguise Self", "Faerie Fire", "Feather Fall", "Healing Word", "Heroism", "Hideous Laughter", "Identify", "Illusory Script", "Longstrider", "Silent Image", "Sleep", "Speak with Animals", "Thunderwave", "Unseen Servant"]
cleric_spells = ["Bane", "Bless", "Command", "Create or Destroy Water", "Cure Wounds", "Detect Evil and Good", "Detect Magic", "Detect Poison and Disease", "Guiding Bolt", "Healing Word", "Inflict Wounds", "Protection from Evil and Good", "Purify Food and Drink", "Sanctuary", "Shield of Faith"]
druid_spells = ["Animal Friendship", "Charm Person", "Create or Destroy Water", "Cure Wounds", "Detect Magic", "Detect Poison and Disease", "Entangle", "Faerie Fire", "Fog Cloud", "Goodberry", "Healing Word", "Jump", "Longstrider", "Purify Food and Drink", "Speak with Animals", "Thunderwave"]
paladin_spells = ["Bless", "Command", "Cure Wounds", "Detect Evil and Good", "Detect Magic", "Detect Poison and Disease", "Divine Favor", "Heroism", "Protection from Evil and Good", "Purify Food and Drink", "Searing Smite", "Shield of Faith"]
sorcerer_spells = ["Burning Hands", "Charm Person", "Color Spray", "Comprehend Languages", "Detect Magic", "Disguise Self", "Expeditious Retreat", "False Life", "Feather Fall", "Fog Cloud", "Jump", "Mage Armor", "Magic Missile", "Shield", "Silent Image", "Sleep", "Thunderwave"]
warlock_spells = ["Charm Person", "Comprehend Languages", "Expeditious Retreat", "Hellish Rebuke", "Illusory Script", "Protection from Evil and Good", "Unseen Servant"]
wizard_spells = ["Alarm", "Burning Hands", "Charm Person", "Color Spray", "Comprehend Languages", "Detect Magic", "Disguise Self", "Expeditious Retreat", "False Life", "Feather Fall", "Find Familiar", "Fog Cloud", "Grease", "Hideous Laughter", "Identify", "Illusory Script", "Jump", "Longstrider", "Mage Armor", "Magic Missile", "Protection from Evil and Good", "Shield", "Silent Image", "Sleep", "Thunderwave", "Unseen Servant"]
