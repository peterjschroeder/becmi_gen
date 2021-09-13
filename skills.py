#!/usr/bin/python

from random import choice
from dice import *

s_fighter = [ 'Intimidate', 'Muscle', 'Endurance', 'Pilot (Boat)', 'Pilot (Galley)', 'Pilot (Sailing Ship)', 'Riding', 'Navigation', 'Nature Lore', 'Survival (Forest)', 'Survival (Mountains)', 'Survival (Ocean)', 'Survival (Arctic)', 'Survival (Plains)',  'Hunting', 'Snares', 'Wrestling', 'Military Tactics', 'Labor', 'Leadership', 'Craft (Ship Building)', 'Stealth', 'Quick Draw' ]
s_thief = [ 'Intimidate', 'Pilot (Boat)', 'Riding', 'Navigation', 'Nature Lore', 'Survival (Forest)', 'Survival (Ocean)', 'Persuasion', 'Deceive', 'Hunting', 'Appraise', 'Snares', 'Danger Sense' ]
s_dwarf = [ 'Craft (Miner)', 'Intimidate', 'Craft (Stonemason)', 'Craft (Metalsmith)', 'Craft (Tinker)', 'Muscle', 'Endurance', 'Appraise', 'Craft (Jeweler)', 'Survival (Mountains)', 'Profession (Engineer)', 'Military Tactics', 'Knowledge (Geology)', 'Knowledge (History)', 'Caving', 'Law and Justice', 'Mountaineering', 'Bargaining', 'Persuasion', 'Singing', 'Storytelling', 'Gambling', 'Stealth' ]
s_elf = [ 'Tracking', 'Treewalking', 'Stealth', 'Singing', 'Hunting', 'Nature Lore', 'Endurance', 'Survival (Forest)', 'Craft (Bowmaker)', 'Pilot (Boat)', 'Persuasion', 'Animal Training', 'Riding', 'Knowledge (History)', 'Law and Justice', 'Alternate Magics', 'Craft (Leatherworker)', 'Bargaining', 'Storytelling', 'Magic Lore' ]
s_cleric = [ 'Detect Deception', 'Persuasion', 'Skald', 'Gain Trust', 'Read Runes', 'Ceremony', 'Knowledge (Religion)', 'Knowledge (History)', 'Law and Justice' ]
s_druid =  [ 'Detect Deception', 'Nature Lore', 'Skald', 'Gain Trust', 'Read Runes', 'Ceremony', 'Knowledge (Religion)', 'Survival (Forest)', 'Survival (Mountains)', 'Survival (Plains)', 'Stealth', 'Veterinary Healing' ]
s_muser = [ 'Knowledge (History)', 'Read Runes', 'Skald', 'Planar Geography', 'Magical Engineering', 'Alchemy', 'Alternate Magics', 'Clerical Magics', 'Mapping', 'Art' ]
s_horsew = [ 'Intimidate', 'Riding', 'Acrobatics', 'Artillery', 'Craft (Bowmaker)', 'Quick Draw', 'Leadership', 'Stealth', 'Military Tactics', 'Tracking' ]
s_bratak = [ 'Disguise', 'Riding', 'Acrobatics', 'Mountaineering', 'Craft (Bowmaker)', 'Quick Draw', 'Persuasion', 'Appraise', 'Gain Trust', 'Tracking' ]
s_hakomon = [ 'Sigil Lore', 'Planar Geography', 'Magical Engineering', 'Alchemy', 'Alternate Magics', ]
s_dervish = [ 'Nature Lore', 'Detect Deception', 'Survival (Desert)', 'Singing', 'Knowledge (Religion)', 'Ceremony', 'Stealth', 'Endurance', 'Acrobatics', 'Danger Sense' ]
s_shamani = [ 'Knowledge (History)', 'Nature Lore', 'Ceremony', 'Animal Empathy', 'Storytelling', 'Animal Training', 'Healing', 'Leadership', 'Fire-building' ]

skill_lists = {
    'Fighter' : s_fighter,
    'Thief' : s_thief,
    'Bard' : s_thief + s_cleric + [ 'Music', 'Singing', 'Art' ],
    'Rake' : s_thief,
    'Magic User' : s_muser,
    'Cleric' : s_cleric,
    'Druid' : s_druid,
    'Shaman' : s_druid + ['Spirit Lore'],
    'Dwarf' : s_dwarf,
    'Dwarf Cleric' : s_dwarf + s_cleric,
    'Elf' : s_elf,
    'Halfling' : s_fighter + s_thief,
    'Mystic' : s_cleric,
    'Forester' : s_fighter + s_muser,
    'Horse Warrior' : s_horsew,
    'Bratak': s_bratak,
    'Hakomon' : s_hakomon,
    'Dervish' : s_dervish,
    'Shamani' : s_shamani,
}

skill_scores = {
    'Alchemy' : 'int',
    'Acrobatics' : 'dex',
    'Acting' : 'cha',
    'Alertness' : 'dex',
    'Alternate Magics' : 'int',
    'Animal Empathy' : 'wis',
    'Animal Training' : 'wis',
    'Appraise' : 'int',
    'Art' : 'wis',
    'Artillery' : 'int',
    'Bargaining' : 'cha',
    'Bravery' : 'wis',
    'Caving' : 'wis',
    'Ceremony' : 'wis',
    'Cheating' : 'dex',
    'Clerical Magics'  : 'int',
    'Craft (Bowmaker)' : 'int',
    'Craft (Jeweler)' : 'int',
    'Craft (Leatherworker)' : 'int',
    'Craft (Metalsmith)' : 'int',
    'Craft (Miner)' : 'int',
    'Craft (Ship Building)' : 'int',
    'Craft (Stonemason)' : 'int',
    'Craft (Tinker)' : 'int',
    'Danger Sense' : 'wis',
    'Deceive' : 'cha',
    'Disguise' : 'int',
    'Detect Deception' : 'wis',
    'Endurance' : 'con',
    'Escape' : 'dex',
    'Gain Trust' : 'cha',
    'Gambling'  : 'wis',
    'Fire-building' : 'int',
    'Food Tasting' : 'con',
    'Healing' : 'int',
    'Hunting' : 'dex',
    'Intimidate' : 'str',
    'Knowledge (Geology)' : 'int',
    'Knowledge (History)' : 'int',
    'Knowledge (Religion)' : 'int',
    'Labor' : 'int',
    'Law and Justice' : 'wis',
    'Leadership' : 'cha',
    'Lip Reading' : 'int',
    'Magical Engineering' : 'int',
    'Magic Lore'  : 'int',
    'Mapping'  : 'int',
    'Military Tactics' : 'int',
    'Mimicry' : 'int',
    'Mountaineering' : 'dex',
    'Muscle' : 'str',
    'Music' : 'cha',    
    'Nature Lore' : 'int',
    'Navigation' : 'int',
    'Persuasion' : 'cha',
    'Pilot (Boat)' : 'int',
    'Pilot (Galley)' : 'int',
    'Pilot (Sailing Ship)' : 'int',
    'Pilot (Airship)' : 'int',
    'Planar Geography' : 'int',
    'Profession (Engineer)' : 'int',
    'Quick Draw' : 'dex',
    'Read Runes' : 'int',
    'Riding' : 'dex',
    'Sigil Lore': 'int',
    'Signaling' : 'int',
    'Singing' : 'cha',
    'Skald' : 'int',
    'Snares' : 'int',
    'Spirit Lore' : 'int',
    'Stealth' : 'dex',
    'Storytelling' : 'cha',
    'Survival (Arctic)' : 'int',
    'Survival (Desert)' : 'int',
    'Survival (Forest)' : 'int',
    'Survival (Mountains)' : 'int',
    'Survival (Ocean)' : 'int',
    'Survival (Plains)' : 'int',
    'Tracking' : 'int',
    'Treewalking' : 'dex',
    'Veterinary Healing' : 'int',
    'Wrestling' : 'str',
}

spirit_guide = { 
 'Ceremony': 'Snake',
 'Law and Justice': 'Owl',
 'Survival (Mountains)': 'Cat',
 'Alertness': 'Eagle',
 'Muscle': 'Ox',
 'Tracking': 'Wolf',
 'Danger Sense': 'Tiger',
 'Animal Training': 'Falcon',
 'Deceive': 'Goat',
 'Nature Lore': 'Sheep',
 'Detect Deception': 'Swan',
 'Disguise': 'Chameleon',
 'Escape': 'Monkey',
 'Wrestling': 'Bear',
 'Gain Trust' : 'Dog',
 'Navigation' : 'Hawk',
}

shaman_bonus_skills = list(spirit_guide.keys())


def get_common(region, origin=None):
    if region == 'Norwold' : 
        if origin=='Mountain Rakasta' :
            return 'Chogh Dene'
        elif origin=='Vatski/Vrodniki' : return 'Vanatic'
        elif origin=='Alphatian' : return 'Alphatian'
        elif origin=='Thyatian' : return 'Thyatian'
        else  : return 'Heldanner'
    elif region in [ 'Thyatis', 'Karameikos', 'Glantri' ] : return 'Thyatian'
    elif region == 'Alphatia' : return 'Alphatian'
    elif region == 'Ylaruam' : return 'Alasiyan'
    elif region == 'Alfheim' : return 'Elven'
    elif region == 'Darokin' : return 'Daro'
    elif region == 'Rockhome' : return 'Denwarf'
    elif region == 'Atruaghin' : return 'Atruaghin'
    elif region == 'Isle of Dawn' : 
        if origin in [ 'Alphatian', 'Thothian'] : return 'Alphatian'
        elif origin == 'Thyatian' : return 'Thyatian'
        else : return choice(['Alphatian','Thyatian']) 
    elif region == 'Savage Coast' :
        if origin in [ 'Renardois Folk', 'Bouchon', 'Mongrel Lupin', 'Papillon' ] : return 'Renardois'
        elif origin in [ 'Ispan', 'Ispan Pistolero', 'Montoya', 'Carrasquito', 'Narvaezan Maremma' ] : return 'Espa'
        elif origin == 'Verdan' : return 'Verdan'
        elif origin in [ 'Traladaran', 'Zvornikian Sentinel', 'Slagovici Gonic' ] : return 'Traladaran'
        elif origin == 'Bellaynish' : return 'Bellaynish'
        else : return 'Thyatian'
    return origin

def get_skills(intel, cclass, race, origin, level, languages, region):
        skills = []
        cspirit_guide = None
        nskills = 5 + (level-1)/4
        if intel > 12 : nskills +=1
        if intel > 15 : nskills +=1
        if intel > 17 : nskills +=1
        if cclass == 'Shaman' : 
            bs=choice(shaman_bonus_skills)
            skills.append(bs)
            cspirit_guide = spirit_guide[bs]
            nskills+=1
        skills.append('Language ({})'.format(get_common(region, origin)))
        if race == 'Elf' and region != 'Savage Coast' :
            skills.append('Language ('+origin+')')
            nskills+=1
        elif race == 'Dwarf' :
            skills.append('Language (Denwarf)')
            nskills+=1
        elif race == 'Halfling' and region == 'Norwold' :
            skills.append('Language (Nytt-Or)')
            nskills+=1
        elif race == 'Lupin' :
            skills.append('Tracking')
            nskills +=1
        elif cclass == 'Bard' :
            skills.append(choice([ 'Skald', 'Singing', 'Music', 'Storytelling' ]))
        while len(skills)<nskills:
            if d6()<2 : skills.append('Language ({})'.format(choice([ get_common(region) ,choice(languages)])))
            elif d8()<2 : skills.append(choice(list(skill_scores.keys())))
            else : skills.append(choice(skill_lists[cclass]))
            skills=list(set(skills))
        skills.sort()
        return skills, cspirit_guide
