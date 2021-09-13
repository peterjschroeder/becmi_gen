#!/usr/bin/python

from dice import *

def __height(race, origin, strength):
    # 147 to 208  
    if race == 'Human' : 
        h = 2*strength + 136 + d20()
        if origin in [ 'Heldannic', 'Dunael', 'Heldanner' ] :
            h+= d10(2) + 4
        elif origin in [ 'Flaem', 'Alasiyan' ] : 
            h+= d10(2) + 2
        elif origin in [ 'Eusdrian', 'Thyatian', 'Alphatian', 'Klantyrian', 'Averoignese', 'Ispan' ] :
            h+= d10(2)
        elif origin in [ 'Daro', 'Hulean', 'Verdan', 'Ierendian', 'Minrothaddan' ] :
            h+= d8(2)
        elif origin in [ 'Caurenzan', 'Traladaran', 'Thothian', 'Atruaghin', 'Makai' ] :
            h+= d6(2)
        else :  h+= d12(2)
        return h
    # 109 to 136
    elif race == 'Dwarf' : return strength + d6(2) + 106  
    # 142 to 173
    elif race == 'Elf' :
        if origin=='Belcadiz' : return strength+d6(2) + 136
        else : return strength + d6(3) + 136
    #  86 to  97
    elif race == 'Halfling' : return strength/2 + d4() + 84
    elif race == 'Lupin' : 
        h = 2*strength + d6(2)
        if origin in [ 'Fennec', 'Carrasquito' ] : return h + 72
        elif origin in [ 'Ochalean Houndling' ] : return h + 92
        elif origin in [ 'Foxfolk', 'Beagle' ] : return h + 116
        elif origin in [ 'Ochalean Crested', 'Das Hund', 'Papillon',  ] : return h + 118
        elif origin in [ 'Snoutzer', 'Cimarron Hairless' ] : return h + 121
        elif origin in [ 'Chow Chow' ] : return h + 128
        elif origin in [ 'Nithian Rambler', 'Shag-Head', 'Zvornikian Sentinel' ] : return h + 136
        elif origin in [ 'Shar-Pei', 'Renardois Folk', 'Bloodhound' ] : return h + 138
        elif origin in [ 'Heldann Shepherd', 'Doggerman', 'Narvaezan Maremma', 'Glantri Mountaineer' ] : return h + 143
        elif origin in [ 'Wolvenfolk', 'Slagovici Gonic', 'Borzoi', 'Long Runner' ] : return h + 147
        elif origin in [ 'Mastiff' ] : return h + 160
        elif origin in [ 'Mongrel Lupin' ] : return h + 162
        else : return h + 162
    elif race == 'Rakasta' :
        # Mountain Rakasta 182-220
        return 2*strength + d8() + 176
    # Not recognized...
    return None

def height(race, origin, strength, gender='m'):
    h = __height(race, origin, strength)
    if gender=='f' : h = int(h*0.95)
    return h

w_div = {
    'Foxfolk' : 4.2, 
    'Fennec' : 4.2, 
    'Heldann Shepherd' : 3.8,
    'Chow Chow' : 3.8,
    'Beagle' : 4,
    'Snoutzer' : 4,
    'Ochalean Crested' : 4,
    'Ochalean Houndling' : 4,
    'Rakasta' : 4.2,
    'Human' : 4,
    'Alphatian' : 4.1,
    'Heldanner' : 3.9,
    'Dwarf' : 1.9,
    'Elf' : 4.2,
    'Halfling' : 2,
    'Lupin' : 3.3,
}


def weight(race, origin, strength, height, gender='m', deterministic=False):
    bmi = 24 if gender=='m' else 22
    w = (height/100.)**2 * bmi * 4
    # Apply racial divider 
    d = w_div[origin] if origin in w_div.keys() else w_div[race]
    w = w/d
    # Fat or Lean
    if not deterministic : w*= 1+((d10(3)-d10(3))/100.)
    if gender=='f' : w = w * 0.9
    return int(w) 


def physique(race, origin, strength, gender):
    h = height(race, origin, strength, gender)
    w = weight(race, origin, strength, h, gender)
    return h, w

def print_range(race='Human', origin='Heldanner') :
    print (race, origin)
    for s in range(3,19):
        h=height(race, origin, s)
        w=weight(race, origin, s, h, True)
        print (s, 'str', h, 'cm', w, 'kg')
    print ('')

if __name__ == '__main__' :
    print_range('Human', 'Heldanner')
    print_range('Human', 'Thyatian')
    print_range('Lupin', 'Foxfolk')
    print_range('Lupin', 'Heldann Shepherd')
    print_range('Rakasta', 'Mountain Rakasta')
    print_range('Dwarf', 'Norwold')
    print_range('Elf', 'Norwold')
    print_range('Halfling', 'Norwold')
