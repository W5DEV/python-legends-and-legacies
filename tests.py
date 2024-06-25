import modules.races as races
import modules.archetypes as archetypes
import modules.coins as coins
import modules.dice_rolls as dice_rolls
import modules.equipment as equipment

def tests():
    print("Starting tests...")

    print("Testing Races...")
    races.test_races()
    print("Race Tests completed...")

    print("Testing Classes...")
    archetypes.test_archetypes()
    print("Class Tests completed...")
   
    print("Testing Dice Rolls...")
    print(f"Rolling 2-sided dice: {dice_rolls.roll_2_sided_dice()}")
    print(f"Rolling 4-sided dice: {dice_rolls.roll_4_sided_dice()}")
    print(f"Rolling 6-sided dice: {dice_rolls.roll_6_sided_dice()}")
    print(f"Rolling 8-sided dice: {dice_rolls.roll_8_sided_dice()}")
    print(f"Rolling 10-sided dice: {dice_rolls.roll_10_sided_dice()}")
    print(f"Rolling 12-sided dice: {dice_rolls.roll_12_sided_dice()}")
    print(f"Rolling 20-sided dice: {dice_rolls.roll_20_sided_dice()}")
    print(f"Rolling percentage dice: {dice_rolls.roll_percentage_dice()}")
    print("Dice Rolls Tests completed...")

    print("Testing Equipment...")
    equipment.club.get_info()
    equipment.dagger.get_info()
    equipment.great_club.get_info()
    equipment.hand_axe.get_info()
    equipment.javelin.get_info()
    equipment.light_hammer.get_info()
    equipment.mace.get_info()
    equipment.quarter_staff.get_info()
    equipment.sickle.get_info()
    equipment.spear.get_info()
    equipment.light_crossbow.get_info()
    equipment.dart.get_info()
    equipment.short_bow.get_info()
    equipment.sling.get_info()

    equipment.battleaxe.get_info()
    equipment.flail.get_info()
    equipment.glaive.get_info()
    equipment.great_axe.get_info()
    equipment.great_sword.get_info()
    equipment.halberd.get_info()
    equipment.lance.get_info()
    equipment.long_sword.get_info()
    equipment.maul.get_info()
    equipment.morningstar.get_info()
    equipment.pike.get_info()
    equipment.rapier.get_info()
    equipment.scimitar.get_info()
    equipment.short_sword.get_info()
    equipment.trident.get_info()
    equipment.war_pick.get_info()
    equipment.war_hammer.get_info()
    equipment.whip.get_info()
    equipment.blowgun.get_info()
    equipment.hand_crossbow.get_info()
    equipment.heavy_crossbow.get_info()
    equipment.longbow.get_info()
    equipment.net.get_info()

    equipment.padded_light_armor.get_info()
    equipment.leather_light_armor.get_info()
    equipment.studded_light_armor.get_info()

    equipment.hide_medium_armor.get_info()
    equipment.chain_shirt_medium_armor.get_info()
    equipment.scale_mail_medium_armor.get_info()
    equipment.breastplate_medium_armor.get_info()
    equipment.half_plate_medium_armor.get_info()

    equipment.ring_mail_heavy_armor.get_info()
    equipment.chain_mail_heavy_armor.get_info()
    equipment.splint_heavy_armor.get_info()
    equipment.plate_heavy_armor.get_info()

    equipment.shield.get_info()

    equipment.explorers_pack.get_info()
    equipment.dungeoneers_pack.get_info()
    equipment.burglars_pack.get_info()
    equipment.entertainers_pack.get_info()
    equipment.priests_pack.get_info()
    equipment.scholars_pack.get_info()
    equipment.diplomats_pack.get_info()

    equipment.bagpipes.get_info()
    equipment.drum.get_info()
    equipment.dulcimer.get_info()
    equipment.flute.get_info()
    equipment.lute.get_info()
    equipment.lyre.get_info()
    equipment.horn.get_info()
    equipment.pan_flute.get_info()
    equipment.shawm.get_info()

    equipment.holy_symbol_amulet.get_info()
    equipment.holy_symbol_emblem.get_info()
    equipment.holy_symbol_reliquary.get_info()

    equipment.druidic_focus.get_info()

    equipment.alchemists_supplies.get_info()
    equipment.brewers_supplies.get_info()
    equipment.calligraphers_supplies.get_info()
    equipment.carpenters_tools.get_info()
    equipment.cartographers_tools.get_info()
    equipment.cobblers_tools.get_info()
    equipment.cooks_utensils.get_info()
    equipment.glassblowers_tools.get_info()
    equipment.jewelers_tools.get_info()
    equipment.leatherworkers_tools.get_info()
    equipment.masons_tools.get_info()
    equipment.painters_supplies.get_info()
    equipment.potters_tools.get_info()
    equipment.smiths_tools.get_info()
    equipment.tinkers_tools.get_info()
    equipment.weavers_tools.get_info()
    equipment.woodcarvers_tools.get_info()

    equipment.disguise_kit.get_info()
    equipment.forgery_kit.get_info()
    equipment.herbalism_kit.get_info()
    equipment.navigator_tools.get_info()
    equipment.poisoners_kit.get_info()
    equipment.thieves_tools.get_info()

    equipment.component_pouch.get_info()

    equipment.arcane_focus_crystal.get_info()
    equipment.arcane_focus_orb.get_info()
    equipment.arcane_focus_rod.get_info()
    equipment.arcane_focus_staff.get_info()
    equipment.arcane_focus_wand.get_info()

    equipment.spellbook.get_info()
    print("Equipment Tests completed...")

    print("All tests completed...")
    print("Please report any bugs or errors.")

    return


tests()