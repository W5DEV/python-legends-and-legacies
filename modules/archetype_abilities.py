barbarian_abilities = {
    "rage": {
        "description": "In battle, you fight with primal ferocity. On your turn, you can enter a rage as a bonus action. While raging, you gain the following benefits if you aren't wearing heavy armor:",
        "benefits": [
            "You have advantage on Strength checks and Strength saving throws.",
            "When you make a melee weapon attack using Strength, you gain a bonus to the damage roll that increases as you gain levels as a barbarian, as shown in the Rage Damage column of the Barbarian table.",
            "You have resistance to bludgeoning, piercing, and slashing damage."
        ],
        "level_requirement": 1,
        "number_of_uses": {
            "1": 2,
            "2": 2,
            "3": 3,
            "4": 3,
            "5": 3,
            "6": 4,
            "7": 4,
            "8": 4,
            "9": 4,
            "10": 4,
            "11": 4,
            "12": 5,
            "13": 5,
            "14": 5,
            "15": 5,
            "16": 5,
            "17": 5,
            "18": 6,
            "19": 6,
            "20": 6
        }

    },
    "unarmored_defense": {
        "description": "While you are not wearing any armor, your Armor Class equals 10 + your Dexterity modifier + your Constitution modifier. You can use a shield and still gain this benefit.",
        "level_requirement": 1
    },
    "reckless_attack": {
        "description": "Starting at 2nd level, you can throw aside all concern for defense to attack with fierce desperation. When you make your first attack on your turn, you can decide to attack recklessly. Doing so gives you advantage on all melee weapon attack rolls using Strength during that turn, but attack rolls against you have advantage until your next turn.",
        "level_requirement": 2
    },
    "danger_sense": {
        "description": "At 2nd level, you gain an uncanny sense of when things nearby aren't as they should be, giving you an edge when you dodge away from danger. You have advantage on Dexterity saving throws against effects that you can see, such as traps and spells. To gain this benefit, you can't be blinded, deafened, or incapacitated.",
        "level_requirement": 2
    },
    "primal_path": {
        "description": "At 3rd level, you choose a path that shapes the nature of your rage. Choose the Path of the Berserker or the Path of the Totem Warrior, both detailed at the end of the class description. Your choice grants you features at 3rd level and again at 6th, 10th, and 14th levels.",
        "level_requirement": 3,
        "path": {
            "path_of_the_berserker": {
                "description": "For some barbarians, rage is a means to an end—that end being violence. The Path of the Berserker is a path of untrammeled fury, slick with blood. As you enter the berserker's rage, you thrill in the chaos of battle, heedless of your own health or well-being.",
                "level_requirement": 3,
                "primal_abilities": {
                    "frenzy": {
                        "description": "Starting when you choose this path at 3rd level, you can go into a frenzy when you rage. If you do so, for the duration of your rage you can make a single melee weapon attack as a bonus action on each of your turns after this one. When your rage ends, you suffer one level of exhaustion.",
                        "level_requirement": 3
                    },
                    "mindless_rage": {
                        "description": "Beginning at 6th level, you can't be charmed or frightened while raging. If you are charmed or frightened when you enter your rage, the effect is suspended for the duration of the rage.",
                        "level_requirement": 6
                    },
                    "intimidating_presence": {
                        "description": "Beginning at 10th level, you can use your action to frighten someone with your menacing presence. When you do so, choose one creature that you can see within 30 feet of you. If the creature can see or hear you, it must succeed on a Wisdom saving throw (DC equal to 8 + your proficiency bonus + your Charisma modifier) or be frightened of you until the end of your next turn. On subsequent turns, you can use your action to extend the duration of this effect on the frightened creature until the end of your next turn. This effect ends if the creature ends its turn out of line of sight or more than 60 feet away from you.",
                        "level_requirement": 10
                    },
                    "retaliation": {
                        "description": "Starting at 14th level, when you take damage from a creature that is within 5 feet of you, you can use your reaction to make a melee weapon attack against that creature.",
                        "level_requirement": 14
                    }
                }
            },
            "path_of_the_totem_warrior": {
                "description": "The Path of the Totem Warrior is a spiritual journey, as the barbarian accepts a spirit animal as guide, protector, and inspiration. In battle, your totem spirit fills you with supernatural might, adding magical fuel to your barbarian rage. Most barbarian tribes consider a totem animal to be kin to a particular clan. In such cases, it is unusual for an individual to have more than one totem animal spirit, though exceptions exist.",
                "level_requirement": 3,
                "primal_abilities": {
                    "spirit_seekers": {
                        "description": "At 3rd level, when you adopt this path, you gain the ability to cast the beast sense and speak with animals spells, but only as rituals.",
                        "level_requirement": 3
                    },
                    "totem_spirit": {
                        "description": "At 3rd level, when you adopt this path, you choose a totem spirit and gain its feature. You must make or acquire a physical totem object—an amulet or similar adornment—that incorporates fur or feathers, claws, teeth, or bones of the totem animal. At your option, you also gain minor physical attributes that are reminiscent of your totem spirit. For example, if you have a bear totem spirit, you might be unusually hairy and thick-skinned, or if your totem is the eagle, your eyes turn bright yellow.",
                        "level_requirement": 3
                    },
                    "aspect_of_the_beast": {
                        "description": "At 6th level, you gain a magical benefit based on the totem animal of your choice. You can choose the same animal you selected at 3rd level or a different one.",
                        "level_requirement": 6
                    },
                    "spirit_walker": {
                        "description": "At 10th level, you can cast the commune with nature spell, but only as a ritual. When you do so, a spiritual version of one of the animals you chose for Totem Spirit or Aspect of the Beast appears to you to convey the information you seek.",
                        "level_requirement": 10
                    },
                    "totemic_attunement": {
                        "description": "At 14th level, you gain a magical benefit based on a totem animal of your choice. You can choose the same animal you selected previously or a different one.",
                        "level_requirement": 14
                    }
                }
            }
        }
    },
    "ability_score_improvement_level_4": {
        "description": "When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.",
        "level_requirement": 4
    },
    "ability_score_improvement_level_8": {
        "description": "When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.",
        "level_requirement": 8
    },
    "ability_score_improvement_level_12": {
        "description": "When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.",
        "level_requirement": 12
    },
    "ability_score_improvement_level_16": {
        "description": "When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.",
        "level_requirement": 16
    },
    "ability_score_improvement_level_19": {
        "description": "When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.",
        "level_requirement": 19
    },
    "extra_attack": {
        "description": "Beginning at 5th level, you can attack twice, instead of once, whenever you take the Attack action on your turn.",
        "level_requirement": 5
    },
    "fast_movement": {
        "description": "Starting at 5th level, your speed increases by 10 feet while you aren't wearing heavy armor.",
        "level_requirement": 5
    },
    "feral_instinct": {
        "description": "By 7th level, your instincts are so honed that you have advantage on initiative rolls.",
        "level_requirement": 7
    },
    "brutal_critical": {
        "description": "Beginning at 9th level, you can roll one additional weapon damage die when determining the extra damage for a critical hit with a melee attack.",
        "level_requirement": 9
    },
    "relentless_rage": {
        "description": "Starting at 11th level, your rage can keep you fighting despite grievous wounds. If you drop to 0 hit points while you're raging and don't die outright, you can make a DC 10 Constitution saving throw. If you succeed, you drop to 1 hit point instead.",
        "level_requirement": 11
    },
    "indomitable_might": {
        "description": "Beginning at 18th level, if your total for a Strength check is less than your Strength score, you can use that score in place of the total.",
        "level_requirement": 18
    },
    "primal_champion": {
        "description": "At 20th level, you embody the power of the wilds. Your Strength and Constitution scores increase by 4. Your maximum for those scores is now 24.",
        "level_requirement": 20
    },
}