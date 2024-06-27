import modules.utils as utils
import modules.dice_rolls as dice_rolls
import modules.equipment as equipment
class Character:
    def __init__(self, name, race, archetype, bio, equipment, abilities, xp, gp, hp=0, max_hp=0, equipped_armor=None, equipped_weapon=None, readied_weapon=None):
        self.name = name
        self.race = race
        self.archetype = archetype
        self.bio = bio
        self.equipment = equipment
        self.xp = xp
        self.gp = gp
        self.hp = hp
        self.max_hp = max_hp
        self.level = 0
        self.equipped_armor = equipped_armor
        self.equippped_weapon = equipped_weapon
        self.readied_weapon = readied_weapon
        self.proficincy_bonus = 0
        self.strength = 0
        self.strength_mod = 0
        self.dexterity = 0
        self.dexterity_mod = 0
        self.constitution = 0
        self.constitution_mod = 0
        self.intelligence = 0
        self.intelligence_mod = 0
        self.wisdom = 0
        self.wisdom_mod = 0
        self.charisma = 0
        self.charisma_mod = 0
        self.equipped_armor = None
        self.equipped_weapon = []
        self.readied_weapon = None
        self.equipped_shield = None

    def initialize_player(self):
        self.calculate_level()
        self.calculate_modifiers()
        self.sync_max_hp()
        self.calculate_proficiency_bonus()
        return

    def award_xp(self, xp):
        self.xp += xp
        current_level = self.level
        self.calculate_level()
        if current_level < self.level:
            self.sync_level()
            self.sync_max_hp()
            self.hp = self.max_hp
            self.calculate_proficiency_bonus()
        return
    
    def calculate_modifiers(self):
        self.strength_mod = (self.strength - 10) // 2
        self.dexterity_mod = (self.dexterity - 10) // 2
        self.constitution_mod = (self.constitution - 10) // 2
        self.intelligence_mod = (self.intelligence - 10) // 2
        self.wisdom_mod = (self.wisdom - 10) // 2
        self.charisma_mod = (self.charisma - 10) // 2
        return

    def sync_max_hp(self):
        if self.level == 1:
            self.max_hp = self.archetype.base_hp + self.constitution_mod
        else:
            if self.archetype.hit_die == "1d6":
                self.max_hp += dice_rolls.roll_6_sided_dice() + self.constitution_mod
            elif self.archetype.hit_die == "1d8":
                self.max_hp += dice_rolls.roll_8_sided_dice() + self.constitution_mod
            elif self.archetype.hit_die == "1d10":
                self.max_hp += dice_rolls.roll_10_sided_dice() + self.constitution_mod
            elif self.archetype.hit_die == "1d12":
                self.max_hp += dice_rolls.roll_12_sided_dice() + self.constitution_mod
        return

    def calculate_level(self):
        level = utils.calculate_level(self.xp)
        self.level = level
        return 
    
    def equip_armor(self):
        selected_item = ""
        valid_choices = []
        if self.equipped_armor == None:
            print("You do not have any armor to equip.")
            return
        print("Please choose an armor type from the following list:")
        for item in self.equipment:
            if item in equipment.armor:
                print(item.name)
                valid_choices.append(item.name.lower())
        selected_item = input("> ")
        while selected_item.lower() not in valid_choices:
            print("Sorry, that is not a valid choice. Please try again.")
            print("Please choose an armor type from the following list:")
            for item in self.equipment:
                if item in equipment.armor:
                    print(item.name)
            selected_item = input("> ")
        for item in self.equipment:
            if item.name.lower() == selected_item.lower():
                self.equipped_armor = item
                print(f"You have equipped {self.equipped_armor.name}.")
                return
        print("You do not have any armor equipped.")
        return
    
    def unequip_armor(self):
        if self.equipped_armor == None:
            print("You do not have any armor equipped.")
            return
        self.equipped_armor = None
        print("You have unequipped your armor.")
        return
    
    def equip_weapon(self):
        selected_item = ""
        valid_choices = []
        if self.equipped_weapon == None:
            print("You do not have any weapons to equip.")
            return
        print("Please choose a weapon from the following list:")
        for item in self.equipment:
            if item in equipment.weapons:
                print(item.name)
                valid_choices.append(item.name.lower())
        selected_item = input("> ")
        while selected_item.lower() not in valid_choices:
            print("Sorry, that is not a valid choice. Please try again.")
            print("Please choose a weapon from the following list:")
            for item in self.equipment:
                if item in equipment.weapons:
                    print(item.name)
            selected_item = input("> ")
        for item in self.equipment:
            if item.name.lower() == selected_item.lower():
                self.equipped_weapon.append(item)
                print(f"You have equipped {item.name}.")
                print("You have the following weapons equipped:")
                for weapon in self.equipped_weapon:
                    print(weapon.name)
                return
        print("You have not equipped any weapons.")
        return
    
    def unequip_weapon(self):
        if self.equipped_weapon == []:
            print("You do not have any weapons equipped.")
            return
        print("Please choose a weapon to unequip from the following list:")
        valid_choices = []
        for weapon in self.equipped_weapon:
            print(weapon.name)
            valid_choices.append(weapon.name.lower())
        selected_item = input("> ")
        while selected_item.lower() not in valid_choices:
            print("Sorry, that is not a valid choice. Please try again.")
            print("Please choose a weapon to unequip from the following list:")
            for weapon in self.equipped_weapon:
                print(weapon.name)
            selected_item = input("> ")
        for weapon in self.equipped_weapon:
            if weapon.name.lower() == selected_item.lower():
                self.equipped_weapon.remove(weapon)
                print(f"You have unequipped {weapon.name}.")
                return
        print("You have not uneqiupped any weapons.")
        return
    
    def equip_shield(self):
        equipped_items = []
        for item in self.equipment:
            equipped_items.append(item.name)
        if "Shield" not in equipped_items:
            print("You do not have a shield to equip.")
            return
        self.equipped_shield = True
        print("You have equipped a shield.")
        return
    
    def unequip_shield(self):
        if self.equipped_shield == None:
            print("You do not have a shield equipped.")
            return
        self.equipped_shield = None
        print("You have unequipped your shield.")
        return
    
    def ready_weapon(self):
        if self.equipped_weapon == []:
            print("You do not have any weapons equipped. Please equip a weapon before readying it.")
            return
        print("Please choose a weapon to ready from the following list:")
        valid_choices = []
        for weapon in self.equipped_weapon:
            print(weapon.name)
            valid_choices.append(weapon.name.lower())
        selected_item = input("> ")
        while selected_item.lower() not in valid_choices:
            print("Sorry, that is not a valid choice. Please try again.")
            print("Please choose a weapon to ready from the following list:")
            for weapon in self.equipped_weapon:
                print(weapon.name)
            selected_item = input("> ")
        for weapon in self.equipped_weapon:
            if weapon.name.lower() == selected_item.lower():
                self.readied_weapon = weapon
                print(f"You have readied {weapon.name}.")
                return
        print("You have not readied any weapons.")    
        return

    def calculate_proficiency_bonus(self):
        self.calculate_level()
        level = self.level
        self.proficiency_bonus = (-(-level // 4)) + 1
        return

    def sync_level(self):
        self.calculate_level()
        self.archetype.sync_level(self.level)
        return

    def sync_equipment(self):
        self.equipment = self.archetype.starting_equipment
        return
    
    def xp_needed_for_next_level(self):
        xp_needed = utils.calculate_xp_needed(self.xp)
        return xp_needed

