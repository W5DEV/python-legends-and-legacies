displayed_barbarian_skills = ["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"]
barbarian_skills = ["animal handling", "athletics", "intimidation", "nature", "perception", "survival"]

def get_barbarian_skills(type):
    if type == "displayed":
        return displayed_barbarian_skills
    elif type == "logical":
        return barbarian_skills
    
displayed_bard_skills = ["Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History", "Insight", "Intimidation", "Investigation", "Medicine", "Nature", "Perception", "Performance", "Persuasion", "Religion", "Sleight of Hand", "Stealth", "Survival"]
bard_skills = ["acrobatics", "animal handling", "arcana", "athletics", "deception", "history", "insight", "intimidation", "investigation", "medicine", "nature", "perception", "performance", "persuasion", "religion", "sleight of hand", "stealth", "survival"]

def get_bard_skills(type):
    if type == "displayed":
        return displayed_bard_skills
    elif type == "logical":
        return bard_skills
