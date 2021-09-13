#!/usr/bin/python
from config import freq
from dice import *
from random import choice

knights_by_origin = {
    'default'   : { 'Sir' : 'common' },
    'Ierendian' : { "Ki'ai" : 'common' },
    'Heldannic' : { 'Grand Knight' : 'common' },
    'Alphatian' : { '' : 'common' },
    'Alasiyan'  : { 'Sidi' : 'common', 'Faris' : 'common', 'Sayf al-Dawla' : 'rare' },
    'Halfling'  : { 'Krondar' : 'common' },
    'Vatski/Vrodniki' : { 'Bogatyr' : 'common' },
    'Averoignese' : { 'Sieur' : 'common' },
    'Belcadiz' : { 'Don' : 'common' },
    'Ethengar' : { 'Keshak' : 'common' },
    'Caurenzan' : { 'Messer' : 'common', 'Monsignor' : 'common' },
    'Daro' : { 'Sir' : 'common', },
    'Hulean' : { 'Effendi' : 'prevalent', 'Agha' : 'common', 'Bey' : 'uncommon', 'Pasha' : 'rare' },
    'Ierendi' : { "Kia'i" : 'common', },
    'Atruaghin' : { 'War Chief' : 'common' },
}

clerics_by_origin = {
    'default'  : { 'Patriarch' : 'prevalent' },
    'Thyatian' : { 'Pontifex' : 'prevalent', 'Flamen' : 'uncommon' },
    'Traladaran' : { 'Patriach' : 'prevalent' },
    'Alasiyan' : { 'Imam' : 'prevalent', 'Sayf al-Din' : 'uncommon' },
    'Heldannic': { 'Abbot': 'prevalent' },
    'Daro' : { 'Archbishop' : 'common', 'Bishop' : 'prevalent', 'Patriarch' : 'uncommon', 'Head Patriarch' : 'rare' },
    'Hulean' : { 'Rahib' : 'prevalent', 'Resul' : 'common', 'Keshish' : 'uncommon', 'Falci' : 'rare', 'Aziz' : 'very rare' },
    'Dwarf' : { 'High Cleric' : 'prevalent', 'Forge Keeper' : 'very rare' },
    'Ierendi' : { 'Patriarch' : 'uncommon', 'High Priest' : 'prevalent' },
    'Atruaghin': { 'Faith Keeper' : 'common', 'Medicine Man' : 'common' },
}

landed_titles = {
    'default' : { 'Lord' : 'common' },
    'Atruaghin' : { 'Chief' : 'common',  'Great Chief' : 'rare' },
    'Heldannic' : { 'Hauskomtur' : 'prevalent', 'Landkomtur': 'common', 'Landmeister' : 'very rare' },
    'Thyatian' : { 'Lord' : 'prevalent', 'Baron' : 'common', 'Count' : 'uncommon', 'Duke' : 'very rare' },
    'Karameikos' : { 'Lord' : 'prevalent', 'Baron' : 'rare' },
    'Glantri' : { 'Baron' : 'prevalent', 'Viscount' : 'common', 'Count': 'uncommon', 'Marquis': 'rare', 'Duke' : 'very rare' },
    'Alphatian' :  { 'Lord' : 'prevalent' },
    'Alasiyan' : { 'Sayyid' : 'prevalent', 'Qadi' : 'prevalent', 'Sheik' : 'prevalent', 'Bey' : 'common', 
    'Malik' : 'very rare', 'Vizier' : 'rare' },
    'Heldanner' : { 'Jarl' : 'common' },
    'Vatski/Vrodniki' : { 'Boyar' : 'common' },
    'Dunael' : { 'Ri' : 'common', 'Ruiri' : 'rare' },
    'Halfling' : { 'Sheriff' : 'common' },
    'Dwarf' : { 'Clanholder' : 'common' },
    'Elf' : { 'Clanholder' : 'common', 'Treekeeper' : 'very rare' },
    'Norwold' : { 'Lord' : 'prevalent', 'Baron' : 'common', 'Count' : 'uncommon', 'Duke' : 'very rare' },
    'Ispan' : { 'Baronet' : 'uncommon', 'Baron' : 'rare' },
    'Verdan' : { 'Baronet' : 'uncommon', 'Baron' : 'rare' },
    'Ethengar' : { 'Arkhan' : 'prevalent', 'Dakhan' : 'common', 'Orkhan': 'rare', 'Khan' : 'very rare' },
    'Daro' : { 'Master' : 'prevalent', 'Guildmaster' : 'common', 'Councillor': 'uncommon', 'Magistrate': 'common' },
    'Hulean' : { 'Pasha' : 'rare', 'Beg' : 'prevalent', 'Vali' : 'uncommon'  },
    'Ierendi' : { 'The Honorable' : 'prevalent', 'Lord' : 'common', 'Baron' : 'rare', 'Tribune' : 'very rare' },
}


female_titles = {
    'Chief' : 'Clan Mother',
    'Great Chief' : 'Clan Mother',
    'Bey' : 'Hatun',
    'Beg' : 'Begum',
    'Messer' : 'Madama',
    'Monsignor': 'Madama',
    'Don' : 'Do\~na',
    'Patriarch' : 'Matriarch',
    'Prior' : 'Prioress',
    'Abbot' : 'Abbess',
    'Landmeister' : 'Landmeisterin',
    'Lord' : 'Lady',
    'Sir' : 'Dame',
    'Sire' : 'Dame',
    'Sieur' : 'Dame',
    'Sheik' : 'Sheika',
    'Malik' : 'Malika',
    'Baron' : 'Baroness',
    'Count' : 'Countess',
    'Duke'  : 'Duchess',
    'Marquis' : 'Marchioness',
    'Viscount' : 'Viscountess',
    'Baronet' : 'Baronetess',
}

postfix = [ 'Bogatyr', 'Arkhan', 'Dakhan', 'Orkhan', 'Khan', 'Bey', 'Keshak', 'Pasha', 'Agha', 'Effendi', 'Beg', 'Vali', 'Rahib', 'Keshish', 'Aziz', 'Resul', 'Falci', 'Begum', 'Hatun' ]

def fix_gender(title, gender):
    c = title
    if gender=='f' :
        if c in female_titles :
            c=female_titles[c]
    return c

def title_selector(region, race, origin, cclass) :
    # Setup selection of titles
    selection = []
    if region == 'Ylaruam' :
        if race in [ 'Human', 'Lupin' ] :
            selection.append('Alasiyan')
    if region == 'Thyatis' :
        selection.append('Thyatian')
        selection.append('default')
    if region == 'Alphatia' :
        selection.append('Alphatian')
    if region == 'Isle of Dawn' :
        selection.append('Alphatian')
        selection.append('Thyatian')
        if origin in [ 'Heldanner', 'Heldannic', 'Dunael' ] :
            selection.append(origin)
        selection.append('default')
    if region == 'Norwold' :
        selection.append('Norwold')
        if origin in [ 'Heldanner', 'Heldannic', 'Dunael', 'Vatski/Vrodniki' ] :
            selection.append(origin)
        selection.append('default')
    if region == 'Karameikos' :
        selection.append('Karameikos')
        selection.append('default')
    if region == 'Glantri' :
        selection.append('Glantri')
        selection.append('default')
    if region == 'Savage Coast' :
        selection.append('default')
        if origin in [ 'Traladaran', 'Ispan', 'Verdan' ] :
            selection.append(origin)
        else : selection.append('Glantri')
    if region == 'Ethengar Khanate' :
        selection.append('Ethengar')
        if region == 'Darokin' :
                selection.append('Daro')
        if region == 'Hule'  :
                selection.append('Hulean')
        if region == 'Alfheim' :
                if race=='Elf' : 
                        selection.append('Elf')
                else : selection.append('default')
        if region == 'Ierendi' : 
                selection.append('Ierendi')
        if region == 'Atruaghin Clans' :
                selection.append('Atruaghin')
        # Force non-landed title for wandering fighter subclasses
    if cclass in [ 'Knight', 'Paladin', 'Avenger', 'Druidic Knight' ] :
        t = []
        for o in selection :
            try : t+=sum([ [ c ] * freq[knights_by_origin[o][c]] for c in knights_by_origin[o] ],[])
            except KeyError : pass
        return t
    # Select landed title
    if d6() < 3 or cclass=='Fighter' : 
        if region == 'Glantri' and cclass not in [ 'Magic User', 'Elf', 'Elf Lord', 'Elf Wizard' ] : return 'Sire'
        if region == 'Alphatia' and cclass not in [ 'Dervish', 'Magic User', 'Elf', 'Cleric', 'Druid', 'Shaman', 'Dwarf Cleric', 'Hin Master', 'Elf Treekeeper', 'Elf Lord', 'Elf Wizard' ] : return 'Sir'
        t = []
        for o in selection :
            try : t+=sum([ [ c ] * freq[landed_titles[o][c]] for c in landed_titles[o] ],[])
            except KeyError : pass
        return t
    # Select non-landed title
    if cclass in [ 'Cleric', 'Dwarf Cleric', 'Dervish' ] :
        t = []
        for o in selection :
            try : t+=sum([ [ c ] * freq[clerics_by_origin[o][c]] for c in clerics_by_origin[o] ],[])
            except KeyError : pass
        return t
    if cclass == 'Druid' :
        return 'Archdruid'
    t = []
    for o in selection :
        try : t+=sum([ [ c ] * freq[knights_by_origin[o][c]] for c in knights_by_origin[o] ],[])
        except KeyError : pass
    return t


def high_level_class(cclass,align):
    if cclass=='Fighter' :
        d = d6() 
        if d <=2 : return None
        if d <=4 : return 'Knight'
        if align == 'Lawful' : return 'Paladin'
        if align == 'Chaotic' : return 'Avenger'
        if align == 'Neutral' : return 'Druidic Knight'
    if cclass == 'Elf' :
        d = d6() 
        if d <2 : return 'Elf Treekeeper'
        if d <3 : return 'Elf Wizard'
        else : return 'Elf Lord'
    if cclass == 'Halfling' and d12()==1 : return 'Hin Master'
    return None

def get_title(region, race, origin, cclass, gender):
    t=title_selector(region, race, origin, cclass)
    if not len(t) : return ''
    return fix_gender(choice(t), gender)

def set_title(name, title):
    if not title : return name
    if title in postfix :
        return name+' '+title
    else :
        return title+' '+name

if __name__ == '__main__' :
    t=title_selector('Norwold', 'Human', 'Heldanner', 'Cleric')
    print (fix_gender(choice(t), 'f'))
