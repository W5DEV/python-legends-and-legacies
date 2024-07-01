import modules.equipment as equipment
import modules.skills as skills
import modules.spells as spells
import modules.cantrips as cantrips

class Bard:

    def __init__(self):
        name = "Bard"
        bio = "An inspiring magician whose power echoes the music of creation."
        hit_die = "1d8"
        primary_ability = "Charisma"
        saving_throw_proficiencies = "Dexterity, Charisma"
        armor_proficiencies = "Light Armor"
        weapon_proficiencies = "Simple Weapons, Hand Crossbows, Longswords, Rapiers, Shortswords"
        tool_proficiencies = "Three musical instruments of your choice"
        self.name = name
        self.bio = bio
        self.hit_die = hit_die
        self.base_hp = 8
        self.primary_ability = primary_ability
        self.saving_throw_proficiencies = saving_throw_proficiencies
        self.armor_proficiencies = armor_proficiencies
        self.weapon_proficiencies = weapon_proficiencies
        self.tool_proficiencies = tool_proficiencies
        self.skill_proficiencies = []
        self.instrument_proficiencies = []
        self.starting_equipment = []
        self.special_abilities = []
        self.college = ""
        self.cantrips = []
        self.spells = []
        self.expertise = []
        self.bard_spells = []
        self.cantrips_known = 2
        self.spells_known = 4
        self.spell_slots_level_1 = 2
        self.spell_slots_level_2 = 0
        self.spell_slots_level_3 = 0
        self.spell_slots_level_4 = 0
        self.spell_slots_level_5 = 0
        self.spell_slots_level_6 = 0
        self.spell_slots_level_7 = 0
        self.spell_slots_level_8 = 0
        self.spell_slots_level_9 = 0

    def sync_level(self, level, player):
        if level == 1:
            self.special_abilities.append("Spellcasting")
            self.special_abilities.append("Bardic Inspiration (d6)")
        if level == 2:
            self.special_abilities.append("Jack of All Trades")
            self.special_abilities.append("Song of Rest (d6)")
            self.spell_slots_level_1 = 3
            self.spells_known = 5
        if level == 3:
            print("You have reached level 3 and can now choose two skills to gain expertise in.")
            print("Please choose two skills from the following list:")
            for skill in self.skill_proficiencies:
                print(skill)
            print("Please enter your first skill choice:")
            expertise_choice1 = input("> ")
            self.expertise.append(expertise_choice1)
            print("Please enter your second skill choice:")
            expertise_choice2 = input("> ")
            self.expertise.append(expertise_choice2)
            print("You have reached level 3 and can now enter a Bard College.")
            self.college = "College of Lore"
            self.special_abilities.append("Cutting Words")
            self.spells_known = 6
            self.spell_slots_level_1 = 4
            self.spell_slots_level_2 = 2
        if level == 4:
            self.special_abilities.append("Ability Score Improvement 4th Level")
            player.update_ability_points(2)
            self.spells_known = 7
            self.spell_slots_level_2 = 3
        if level == 5:
            self.special_abilities.append("Bardic Inspiration (d8)")
            self.special_abilities.append("Font of Inspiration")
            self.spells_known = 8
            self.spell_slots_level_3 = 2
        if level == 6:
            self.special_abilities.append("Countercharm")
            self.special_abilities.append("Additional Magical Secrets")
            self.spells_known = 9
            self.spell_slots_level_3 = 3
        if level == 7:
            self.spells_known = 10
            self.spell_slots_level_4 = 1
        if level == 8:
            self.special_abilities.append("Ability Score Improvement 8th Level")
            player.update_ability_points(2)
            self.spells_known = 11
            self.spell_slots_level_4 = 2
        if level == 9:
            self.special_abilities.append("Song of Rest (d8)")
            self.spells_known = 12
            self.spell_slots_level_4 = 3
            self.spell_slots_level_5 = 1
        if level == 10:
            self.special_abilities.append("Bardic Inspiration (d10)")
            print("You have reached level 10 and can now choose two skills to gain expertise in.")
            print("Please choose two skills from the following list:")
            for skill in self.skill_proficiencies:
                print(skill) 
            print("Please enter your first skill choice:")
            expertise_choice1 = input("> ")
            self.expertise.append(expertise_choice1)
            print("Please enter your second skill choice:")
            expertise_choice2 = input("> ")
            self.expertise.append(expertise_choice2)
            print("You have reached level 10 and can choose two spells or cantrips to count as bard spells.")
            print("Please choose two spells from the bard table below.")
            print("Insert spell table here.")
            print("Please enter your first spell choice:")
            bard_spell_choice1 = input("> ")
            self.bard_spells.append(bard_spell_choice1)
            print("Please enter your second spell choice:")
            bard_spell_choice2 = input("> ")
            self.bard_spells.append(bard_spell_choice2)
            self.spells_known = 14
            self.spell_slots_level_5 = 2
        if level == 11:
            self.spells_known = 15
            self.spell_slots_level_6 = 1
        if level == 12:
            self.special_abilities.append("Ability Score Improvement 12th Level")
            player.update_ability_points(2)
        if level == 13:
            self.special_abilities.append("Song of Rest (d10)")
            self.spells_known = 16
            self.spell_slots_level_7 = 1
        if level == 14:
            print("You have reached level 14 and can choose two spells or cantrips to count as bard spells.")
            print("Please choose two spells from the bard table below.")
            print("Insert spell table here.")
            print("Please enter your first spell choice:")
            bard_spell_choice1 = input("> ")
            self.bard_spells.append(bard_spell_choice1)
            print("Please enter your second spell choice:")
            bard_spell_choice2 = input("> ")
            self.bard_spells.append(bard_spell_choice2)
            self.special_abilities.append("Peerless Skill")
            self.spells_known = 18
        if level == 15:
            self.special_abilities.append("Bardic Inspiration (d12)")
            self.spells_known = 19
            self.spell_slots_level_8 = 1
        if level == 16:
            self.special_abilities.append("Ability Score Improvement 16th Level")
            player.update_ability_points(2)
        if level == 17:
            self.special_abilities.append("Song of Rest (d12)")
            self.spells_known = 20
            self.spell_slots_level_9 = 1
        if level == 18:
            print("You have reached level 18 and can choose two spells or cantrips to count as bard spells.")
            print("Please choose two spells from the bard table below.")
            print("Insert spell table here.")
            print("Please enter your first spell choice:")
            bard_spell_choice1 = input("> ")
            self.bard_spells.append(bard_spell_choice1)
            print("Please enter your second spell choice:")
            bard_spell_choice2 = input("> ")
            self.bard_spells.append(bard_spell_choice2)
            self.spells_known = 22
            self.spell_slots_level_5 = 3
        if level == 19:
            self.special_abilities.append("Ability Score Improvement 19th Level")
            player.update_ability_points(2)
            self.spell_slots_level_6 = 2
        if level == 20:
            self.special_abilities.append("Superior Inspiration")
            self.spell_slots_level_7 = 2
        return self
    
def define_bard():
    bard = Bard()

    ### Equipment Choices ###
    first_equipment_choice = equipment.weapon_choices(["Rapier", "Longsword", "Any Simple Weapon"])
    if first_equipment_choice == "Rapier":
        bard.starting_equipment.append(equipment.rapier)
    elif first_equipment_choice == "Longsword":
        bard.starting_equipment.append(equipment.long_sword)
    else:
        bard.starting_equipment.append(equipment.get_weapons_from_category("Simple Weapons"))

    second_equipment_choice = equipment.weapon_choices(["Diplomat's Pack", "Entertainer's Pack"])
    if second_equipment_choice == "Diplomat's Pack":
        bard.starting_equipment.append(equipment.diplomats_pack)
    else:
        bard.starting_equipment.append(equipment.entertainers_pack)

    third_equipment_choice = equipment.weapon_choices(["Lute", "Any Musical Instrument"])
    if third_equipment_choice == "Lute":
        bard.starting_equipment.append(equipment.lute)
    else:
        bard.starting_equipment.append(equipment.get_weapons_from_category("Instruments"))

    bard.starting_equipment.append(equipment.leather_light_armor)
    bard.starting_equipment.append(equipment.dagger)

    ### Skill Choices ###
    for i in range(3):
        skill = skills.select_skill_proficiencies("Bard")
        bard.skill_proficiencies.append(skill)

    ### Spell Choices ###
    for i in range(4):
        spell = spells.select_spells("Bard")
        bard.spells.append(spell)

    ### Cantrip Choices ###
    for i in range(2):
        cantrip = cantrips.select_cantrips("Bard")
        bard.cantrips.append(cantrip)

    return bard
