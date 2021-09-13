generic_nicknames_by_trait = { 
 'Cautious/Rash'        : [ [ 'the Worrier', 'the Wary', 'the Shrewd' ], [ 'the Unruly', 'the Foolhardy', 'the Audacious', 'the Reckless' ] ],
 'Modest/Proud'         : [ [ 'the Quiet', 'the Humble', 'the Meek' ], [ 'Hard-mouth', 'the Braggart', 'the Great' ] ],
 'Peaceful/Violent'     : [ [ 'the Peaceful', 'the Gentle' ], [ 'the Killer', 'the Flayer', 'the Cruel' ] ],
 'Generous/Greedy'      : [ [ 'the Fosterer', 'the Good' ], [ 'the Stone', 'the Wealthy', 'the Greedy' ] ],
 'Courageous/Fearful'   : [ [ 'the Dueler', 'Stout-Heart', 'the Bold', 'the Brave' ], [ 'the Shy', 'the Timid' ] ],
 'Reverent/Godless'     : [ [ 'the Pious', 'the Reverent' ], [ 'the Godless', 'the Heathen' ] ],
 'Forgiving/Vengeful'   : [ [ 'the Gentle', 'the Kind' ], [ 'the Bitter', 'the Avenger', 'the Implacable' ] ],
 'Energetic/Lazy'       : [ [ 'the Wild', 'the Tireless', 'the Powerful' ], [ 'the Lazy', 'the Wary', 'the Laggard' ] ],
 'Honest/Deceitful'     : [ [ 'Truth-Sayer', 'the Trustworthy', 'the Fair' ], [ 'Serpent-Tongue', 'Smooth-Tongue' ] ],
 'Trusting/Suspicious'  : [ [ 'the Fool', 'the Innocent' ], [ 'the Quiet', 'the Doubter' ] ],
 'Loyal/Unreliable'     : [ [ 'the Loyal', 'the Staunch', 'the Trustworthy' ], [ 'the Rascal', 'the Disloyal', 'the Oath-breaker', 'the Faithless', 'Two-Face' ] ],
 'Dogmatic/Open-Minded' : [ [ 'the Stone', 'the Stubborn' ], [ 'the Tolerant', 'the Free-thinker' ] ],
 }

generic_nicknames_by_ability = {
'str' : [ [ 'the Weak' ], [ 'the Strong', 'the Mighty', 'the Broad-Shouldered' ] ],
'int' : [ [ 'Halftroll' ], [ 'the Learned', 'Wry-Mouth' ] ],
'wis' : [ [ 'the Fool' ], [ 'the Deep-Minded', 'the Wise' ] ],
'dex' : [ [ 'the Awkward', 'the Clumsy' ], [ 'the Slender', 'the Lean' ] ],
'con' : [ [ 'Brittle-Bone', 'the Lean' ], [ 'the Stout', 'the Stone' ] ],
'cha' : [ [ 'Flat-Nose', 'Halftroll', 'the Shabby' ], [ 'the Handsome', 'Smooth-Tongue' ] ],
}

generators = {
    'Carrasquito' : 'belcadiz',
    'Ispan' : 'belcadiz',
    'Montoya' : 'belcadiz',
    'Narvaezan Maremma' : 'belcadiz',
        'Ispan Pistolero' : 'belcadiz',
        'Renardois Folk' : 'averoignese',
        'Papillon' : 'averoignese',
        'Bouchon' : 'averoignese',
        'Nithian Rambler' : 'alasiyan',
        'Fennec' : 'alasiyan',
}

#nicknames_by_trait = generic_nicknames_by_trait
#nicknames_by_ability = generic_nicknames_by_ability

from random import choice

def set_nicknames(origin,gender='m'):
    global nicknames_by_trait
    global nicknames_by_ability
    nicknames_by_trait = generic_nicknames_by_trait
    nicknames_by_ability = generic_nicknames_by_ability
    from importlib import import_module
    try : 
        m = import_module('nickname.'+generators[origin])
        if gender=='f' and 'nicknames_by_trait_f' in dir(m) :
            nicknames_by_trait = m.nicknames_by_trait_f
        else :
            nicknames_by_trait = m.nicknames_by_trait
        if gender=='f' and 'nicknames_by_ability_f' in dir(m) :
            nicknames_by_ability = m.nicknames_by_ability_f
        else :
            nicknames_by_ability = m.nicknames_by_ability
        return
    except Exception as e:
        print ('failed to load nicknames', e)
    norm_origin = origin.lower()
    # Replace ' ' with '_'
    import re
    p=re.compile(' ')
    norm_origin = p.sub('_',norm_origin)
    # Try loading from origin
    try : 
        m = import_module('nickname.'+norm_origin)
        if gender=='f' and 'nicknames_by_trait_f' in dir(m) :
            nicknames_by_trait = m.nicknames_by_trait_f
        else :
            nicknames_by_trait = m.nicknames_by_trait
        if gender=='f' and 'nicknames_by_ability_f' in dir(m) :
            nicknames_by_ability = m.nicknames_by_ability_f
        else :
            nicknames_by_ability = m.nicknames_by_ability
    except Exception as e: print ('failed to load nicknames', e)

def get_nickname(traits, abilities):
    min_t = min(traits, key=traits.get)
    max_t = max(traits, key=traits.get)
    min_s = min(abilities, key=abilities.get)
    max_s = max(abilities, key=abilities.get)
    selection = []
    if traits[min_t]<6 : selection.append(min_t)
    if traits[max_t]>15 : selection.append(max_t)
    if abilities[min_s]<6 : selection.append(min_s)
    if abilities[max_s]>15 : selection.append(max_s)
    if not len(selection) : 
        return ''
    c = choice(selection)
    if c == min_t : 
        return choice(nicknames_by_trait[c][1])
    elif c == max_t : 
        return choice(nicknames_by_trait[c][0])
    elif c == min_s : 
        return choice(nicknames_by_ability[c][0])
    elif c == max_s : 
        return choice(nicknames_by_ability[c][1])
    return ''
