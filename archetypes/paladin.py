import modules.equipment as equipment
import modules.skills as skills
import modules.spells as spells

class Paladin:
    
    def __init__(self):
        name = "Paladin"
        bio = "A holy warrior bound to a sacred oath."
        hit_die = "10"
        primary_ability = "Strength, Charisma"
        saving_throw_proficiencies = "Wisdom, Charisma"
        armor_proficiencies = "All Armor and Shields"
        weapon_proficiencies = "Simple Weapons, Martial Weapons"
        tool_proficiencies = "None"
        self.name = name
        self.bio = bio
        self.hit_die = hit_die
        self.base_hp = 10
        self.primary_ability = primary_ability
        self.saving_throw_proficiencies = saving_throw_proficiencies
        self.armor_proficiencies = armor_proficiencies
        self.weapon_proficiencies = weapon_proficiencies
        self.tool_proficiencies = tool_proficiencies
        self.skill_proficiencies = []
        self.starting_equipment = []
        self.spells = []
        self.sacred_oath = ""
        self.channel_divinity_options = []
        self.oath_of_devotion_spells = []
        self.special_abilities = []
        self.spell_slots_level_1 = 0
        self.spell_slots_level_2 = 0
        self.spell_slots_level_3 = 0
        self.spell_slots_level_4 = 0
        self.spell_slots_level_5 = 0

    def sync_level(self, level, player):
        if level == 1:
            self.special_abilities.append("Divine Sense")
            self.special_abilities.append("Lay on Hands")
        if level == 2:
            self.special_abilities.append("Fighting Style")
            self.special_abilities.append("Spellcasting")
            self.special_abilities.append("Divine Smite")
            self.spell_slots_level_1 = 2
        if level == 3:
            self.sacred_oath = "Oath of Devotion"
            self.channel_divinity_options.append("Sacred Weapon")
            self.channel_divinity_options.append("Turn the Unholy")
            self.special_abilities.append("Divine Health")
            self.special_abilities.append("Sacred Oath")
            self.oath_of_devotion_spells.append("Protection from Evil and Good")
            self.oath_of_devotion_spells.append("Sanctuary")
            self.spell_slots_level_1 = 3
        if level == 4:
            self.special_abilities.append("Ability Score Improvement 4th Level")
            player.update_ability_points(2)
        if level == 5:
            self.special_abilities.append("Extra Attack")
            self.oath_of_devotion_spells.append("Lesser Restoration")
            self.oath_of_devotion_spells.append("Zone of Truth")
            self.spell_slots_level_1 = 4
            self.spell_slots_level_2 = 2
        if level == 6:
            self.special_abilities.append("Aura of Protection")
        if level == 7:
            self.special_abilities.append("Aura of Devotion (10 ft)")
            self.spell_slots_level_2 = 3
        if level == 8:
            self.special_abilities.append("Ability Score Improvement 8th Level")
            player.update_ability_points(2)
        if level == 9:
            self.oath_of_devotion_spells.append("Beacon of Hope")
            self.oath_of_devotion_spells.append("Dispel Magic")
            self.spell_slots_level_3 = 2
        if level == 10:
            self.special_abilities.append("Aura of Courage")
        if level == 11:
            self.special_abilities.append("Improved Divine Smite")
            self.spell_slots_level_3 = 3
        if level == 12:
            self.special_abilities.append("Ability Score Improvement 12th Level")
            player.update_ability_points(2)
        if level == 13:
            self.oath_of_devotion_spells.append("Freedom of Movement")
            self.oath_of_devotion_spells.append("Guardian of Faith")
            self.spell_slots_level_4 = 1
        if level == 14:
            self.special_abilities.append("Cleansing Touch")
        if level == 15:
            self.special_abilities.append("Purity of Spirit")
            self.spell_slots_level_4 = 2
        if level == 16:
            self.special_abilities.append("Ability Score Improvement 16th Level")
            player.update_ability_points(2)
        if level == 17:
            self.oath_of_devotion_spells.append("Commune")
            self.oath_of_devotion_spells.append("Flame Strike")
            self.spell_slots_level_4 = 3
            self.spell_slots_level_5 = 1
        if level == 18:
            self.special_abilities.append("Aura Improvements")
            self.special_abilities.append("Aura of Devotion (30 ft)")
        if level == 19:
            self.special_abilities.append("Ability Score Improvement 19th Level")
            player.update_ability_points(2)
            self.spell_slots_level_5 = 2
        if level == 20:
            self.special_abilities.append("Holy Nimbus")
        return self
    
def define_paladin():
    paladin = Paladin()

    ### Equipment Choices ###
    first_equipment_choice = equipment.weapon_choices(["Short Sword", "Simple Weapon"])
    if first_equipment_choice == "Short Sword":
        paladin.starting_equipment.append(equipment.short_sword)
    elif first_equipment_choice == "Simple Weapon":
        paladin.starting_equipment.append(equipment.get_weapons_from_category("Simple Weapons"))

    second_equipment_choice = equipment.weapon_choices(["Priest's Pack", "Explorer's Pack"])
    if second_equipment_choice == "Priest's Pack":
        paladin.starting_equipment.append(equipment.priests_pack)
    elif second_equipment_choice == "Explorer's Pack":
        paladin.starting_equipment.append(equipment.explorers_pack)

    # Add 10 Darts

    paladin.starting_equipment.append(equipment.chain_mail_heavy_armor)
    paladin.starting_equipment.append(equipment.holy_symbol_emblem)

    ### Skill Choices ###
    for i in range(2):
        skill = skills.select_skill_proficiencies("Paladin")
        paladin.skill_proficiencies.append(skill)

    ### Spell Choices ###
    for i in range(1):
        spell = spells.select_spells("Paladin")
        paladin.spells.append(spell)

    return paladin
 