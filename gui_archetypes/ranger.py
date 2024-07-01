import gui_modules.equipment as equipment
import gui_modules.skills as skills
import gui_modules.spells as spells
import gui_modules.cantrips as cantrips

class Ranger:
    
    def __init__(self):
        name = "Ranger"
        bio = "A warrior who uses martial prowess and nature magic to combat threats on the edges of civilization"
        hit_die = "1d10"
        primary_ability = "Dexterity, Wisdom"
        saving_throw_proficiencies = "Strength, Dexterity"
        armor_proficiencies = "Light Armor, Medium Armor, Shields"
        weapon_proficiencies = "Simple Weapons, Martial Weapons"
        self.name = name
        self.bio = bio
        self.hit_die = hit_die
        self.base_hp = 10
        self.primary_ability = primary_ability
        self.saving_throw_proficiencies = saving_throw_proficiencies
        self.armor_proficiencies = armor_proficiencies
        self.weapon_proficiencies = weapon_proficiencies
        self.tool_proficiencies = []
        self.skill_proficiencies = []
        self.starting_equipment = []
        self.fighting_style = []
        self.ranger_archetype = ""
        self.special_abilities = []
        self.spells_known = 0
        self.spell_slots_level_1 = 0
        self.spell_slots_level_2 = 0
        self.spell_slots_level_3 = 0
        self.spell_slots_level_4 = 0
        self.spell_slots_level_5 = 0
    
    def sync_level(self, level, player):
        if level == 1:
            self.special_abilities.append("Favored Enemy")
            self.special_abilities.append("Natural Explorer")
        if level == 2:
            print("You have reached level 1 and now have the following fighting styles:")
            for style in ["Archery", "Defense", "Dueling", "Two-Weapon Fighting"]:
                print(style)
            print("Please enter your choice of fighting style:")
            fighting_style_choice = input("> ")
            while fighting_style_choice.lower() not in ["archery", "defense", "dueling", "two-weapon fighting"]:
                print("That is not a valid choice. Please choose from the list.")
                fighting_style_choice = input("> ")
            self.fighting_style.append(fighting_style_choice)
            print(f"You have chosen the {fighting_style_choice} fighting style.")
            print("You cannot specialize in this fighting style in the future.")
            print("You have also gained the following special abilities:")
            self.special_abilities.append("Spellcasting")
            self.spells_known = 2
            self.spell_slots_level_1 = 2
        if level == 3:
            self.ranger_archetype = "Hunter"
            self.special_abilities.append("Hunter's Prey")
            self.special_abilities.append("Primeval Awareness")
            self.spells_known = 3
            self.spell_slots_level_1 = 3
        if level == 4:
            self.special_abilities.append("Ability Score Improvement 4th Level")
            player.increase_ability_score(2)
        if level == 5:
            self.special_abilities.append("Extra Attack")
            self.spells_known = 4
            self.spell_slots_level_1 = 4
            self.spell_slots_level_2 = 2
        if level == 6:
            self.special_abilities.append("Favorite Enemy Improvement")
            self.special_abilities.append("Natural Explorer Improvement")
        if level == 7:
            self.special_abilities.append("Defensive Tactics")
            self.spells_known = 5
            self.spell_slots_level_3 = 3
        if level == 8:
            self.special_abilities.append("Ability Score Improvement 8th Level")
            player.increase_ability_score(2)
            self.special_abilities.append("Land's Stride")
        if level == 9:
            self.spells_known = 6
            self.spell_slots_level_3 = 2
        if level == 10:
            self.special_abilities.append("Natural Explorer Improvement")
            self.special_abilities.append("Hide in Plain Sight")
        if level == 11:
            self.special_abilities.append("Multiattack")
            self.spells_known = 7
            self.spell_slots_level_3 = 3
        if level == 12:
            self.special_abilities.append("Ability Score Improvement 12th Level")
            player.increase_ability_score(2)
        if level == 13:
            self.spells_known = 8
            self.spell_slots_level_4 = 1
        if level == 14:
            self.special_abilities.append("Favored Enemy Improvement")
            self.special_abilities.append("Vanish")
        if level == 15:
            self.special_abilities.append("Superior Hunter's Defense")
            self.spells_known = 9
            self.spell_slots_level_4 = 2
        if level == 16:
            self.special_abilities.append("Ability Score Improvement 16th Level")
            player.increase_ability_score(2)
        if level == 17:
            self.spells_known = 10
            self.spell_slots_level_4 = 3
            self.spell_slots_level_5 = 1
        if level == 18:
            self.special_abilities.append("Fereal Senses")
        if level == 19:
            self.special_abilities.append("Ability Score Improvement 19th Level")
            player.increase_ability_score(2)
            self.spells_known = 11
            self.spell_slots_level_5 = 2
        if level == 20:
            self.special_abilities.append("Foe Slayer")
        return self
    
def define_ranger():
    ranger = Ranger()

    ### Equipment Choices ###
    first_equipment_choice = equipment.weapon_choices(["Mace", "Warhammer"])
    if first_equipment_choice == "Mace":
        ranger.starting_equipment.append(equipment.mace)
    elif first_equipment_choice == "Warhammer":
        ranger.starting_equipment.append(equipment.war_hammer)

    second_equipment_choice = equipment.weapon_choices(["Scale Mail", "Leather Armor", "Chain Mail"])
    if second_equipment_choice == "Scale Mail":
        ranger.starting_equipment.append(equipment.scale_mail_medium_armor)
    elif second_equipment_choice == "Leather Armor":
        ranger.starting_equipment.append(equipment.leather_light_armor)
    elif second_equipment_choice == "Chain Mail":
        ranger.starting_equipment.append(equipment.chain_mail_heavy_armor)

    third_equipment_choice = equipment.weapon_choices(["Light Crossbow", "Any Simple Weapon"])
    if third_equipment_choice == "Light Crossbow":
        ranger.starting_equipment.append(equipment.light_crossbow)
    else:
        ranger.starting_equipment.append(equipment.get_weapons_from_category("Simple Weapons"))

        third_equipment_choice = equipment.weapon_choices(["Priest's Pack", "Explorer's Pack"])
    if third_equipment_choice == "Priest's Pack":
        ranger.starting_equipment.append(equipment.priests_pack)
    else:
        ranger.starting_equipment.append(equipment.explorers_pack)

    ranger.starting_equipment.append(equipment.shield)
    ranger.starting_equipment.append(equipment.holy_symbol_emblem)

    ### Skill Choices ###
    for i in range(2):
        skill = skills.select_skill_proficiencies("ranger")
        ranger.skill_proficiencies.append(skill)

    ### Spell Choices ###
    for i in range(1):
        spell = spells.select_spells("ranger")
        ranger.spells.append(spell)

    ### Cantrip Choices ###
    for i in range(3):
        cantrip = cantrips.select_cantrips("ranger")
        ranger.cantrips.append(cantrip)

    return ranger
