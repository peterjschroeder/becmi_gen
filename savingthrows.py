#!/usr/bin/python

ST_tables_l_1_3 = {
    'Cleric' :      [ 11, 12, 14, 16, 15 ],
    'Fighter':      [ 12, 13, 14, 15, 16 ],
    'Magic User' :  [ 13, 14, 13, 16, 15 ],
    'Thief'  :      [ 13, 14, 13, 16, 15 ],
    'Dwarf'  :      [  8,  9, 10, 13, 12 ],
    'Elf'    :      [ 12, 13, 13, 15, 15 ],
    'Halfling' :    [  8,  9, 10, 13, 12 ],
    'Mystic' :      [ 12, 13, 14, 15, 16 ]
}

ST_tables_l_4_6 = {
    'Cleric' :      [  9, 10, 12, 14, 13 ],
    'Fighter':      [ 10, 11, 12, 13, 14 ],
    'Magic User' :  [ 11, 12, 11, 14, 12 ],
    'Thief'  :      [ 11, 12, 11, 14, 13 ],
    'Dwarf'  :      [  6,  7,  8, 10,  9 ],
    'Elf'    :      [  8, 10, 10, 11, 11 ],
    'Halfling' :    [  6,  7,  8, 10,  9 ],
    'Mystic' :      [ 10, 11, 12, 13, 14 ]
}

ST_tables_l_7_9 = {
    'Cleric' :      [  7,  8, 10, 12, 11 ],
    'Fighter':      [  8,  9, 10, 11, 12 ],
    'Magic User' :  [  9, 10,  9, 12,  9 ],
    'Thief'  :      [  9, 10,  9, 12, 11 ],
    'Dwarf'  :      [  4,  5,  6,  7,  6 ],
    'Elf'    :      [  4,  7,  7,  7,  7 ],
    'Halfling' :    [  2,  3,  4,  5,  4 ],
    'Mystic' :      [  8,  9, 10, 11, 12 ]
}

ST_tables_l_10_12 = {
    'Cleric' :      [  6,  7,  8, 10,  9 ],
    'Fighter':      [  6,  7,  8,  9, 10 ],
    'Magic User' :  [  7,  8,  7, 10,  6 ],
    'Thief'  :      [  7,  8,  7, 10,  9 ],
    'Dwarf'  :      [  2,  3,  4,  4,  3 ],
    'Elf'    :      [  2,  4,  4,  3,  3 ],
    'Mystic' :      [  6,  7,  8,  9, 10 ]
}

ST_tables_l_13_15 = {
    'Cleric' :      [  5,  6,  6,  8,  7 ],
    'Fighter':      [  6,  6,  7,  8,  9 ],
    'Thief'  :      [  5,  6,  5,  8,  7 ],
    'Magic User' :  [  5,  6,  5,  8,  4 ],
    'Mystic' :      [  6,  6,  7,  8,  9 ],
}

ST_tables_l_16_18 = {
    'Cleric' :          [  4,  5,  5,  6,  5 ],
    'Fighter':          [  5,  6,  6,  7,  8 ],
    'Thief'  :      [  4,  5,  4,  6,  5 ],
    'Magic User' :  [  4,  4,  4,  6,  3 ],
    'Mystic' :          [  5,  6,  6,  7,  8 ],
}

ST_tables_l_19_21 = {
    'Cleric' :          [  3,  4,  4,  4,  4 ],
    'Fighter':          [  5,  5,  6,  6,  7 ],
    'Thief'  :      [  3,  4,  3,  4,  4 ],
    'Magic User' :  [  3,  3,  3,  4,  2 ],
}

ST_tables_l_22_24 = {
    'Cleric' :          [  2,  3,  3,  3,  3 ],
    'Fighter':          [  4,  5,  5,  5,  6 ],
    'Thief'  :      [  2,  3,  2,  3,  3 ],
    'Magic User' :  [  2,  2,  2,  2,  2 ],
}

ST_tables_l_25_27 = {
    'Cleric' :          [  2,  2,  2,  2,  2 ],
    'Fighter':          [  4,  4,  5,  4,  5 ],
    'Thief'  :      [  2,  2,  2,  2,  2 ],
}

ST_tables_l_28_30 = {
    'Fighter':          [  3,  4,  4,  3,  4 ],
}

ST_tables_l_31_33 = {
    'Fighter':          [  3,  3,  3,  2,  3 ],
}

ST_tables_l_34_36 = {
    'Fighter':          [  2,  2,  2,  2,  2 ],
}

def __get_ST_table(cclass,lvl):
    cls = ST_tables_map[cclass]
    if cclass == 'Dervish' and lvl > 12 : lvl=12
    table = ST_tables_l_1_3 
    if cls in [ 'Thief', 'Cleric' ] :
        if lvl >= 33 : table = ST_tables_l_25_27
        elif lvl >= 29 : table = ST_tables_l_22_24
        elif lvl >= 25 : table = ST_tables_l_19_21
        elif lvl >= 21 : table = ST_tables_l_16_18 
        elif lvl >= 17 : table = ST_tables_l_13_15 
        elif lvl >= 13 : table = ST_tables_l_10_12 
        elif lvl >=  9 : table = ST_tables_l_7_9 
        elif lvl >=  5 : table = ST_tables_l_4_6
    elif cls in [ 'Magic User' ] :
        if lvl >= 33 : table = ST_tables_l_22_24
        elif lvl >= 29 : table = ST_tables_l_19_21
        elif lvl >= 25 : table = ST_tables_l_16_18
        elif lvl >= 21 : table = ST_tables_l_13_15
        elif lvl >= 16 : table = ST_tables_l_10_12 
        elif lvl >= 11 : table = ST_tables_l_7_9 
        elif lvl >=  6 : table = ST_tables_l_4_6
    elif lvl >= 34 : table = ST_tables_l_34_36
    elif lvl >= 31 : table = ST_tables_l_31_33
    elif lvl >= 28 : table = ST_tables_l_28_30
    elif lvl >= 25 : table = ST_tables_l_25_27
    elif lvl >= 22 : table = ST_tables_l_22_24
    elif lvl >= 19 : table = ST_tables_l_19_21
    elif lvl >= 16 : table = ST_tables_l_16_18
    elif lvl >= 13 : table = ST_tables_l_13_15
    elif lvl >= 10 : table = ST_tables_l_10_12
    elif lvl >=  7 : table = ST_tables_l_7_9
    elif lvl >=  4 : table = ST_tables_l_4_6
    try : return table[cls]
    except KeyError :
        print (cclass, lvl)
        return None 

ST_tables_map = {
    'Fighter' : 'Fighter',
    'Thief' : 'Thief',
    'Bard' : 'Thief',
    'Rake' : 'Thief',
    'Magic User' : 'Magic User',
    'Cleric' : 'Cleric',
    'Druid' : 'Cleric',
    'Shaman' : 'Cleric',
    'Dwarf' : 'Dwarf',
    'Dwarf Cleric' : 'Dwarf',
    'Elf' : 'Elf',
    'Halfling' : 'Halfling',
    'Mystic' : 'Mystic',
    'Forester' : 'Elf',
    'Hakomon' : 'Magic User',
    'Bratak' : 'Thief',
    'Horse Warrior' : 'Fighter',
        'Dervish' : 'Dwarf',
        'Shamani' : 'Cleric',
}   

def get_best_of(cclass1, lvl1, cclass2, lvl2):
    t1=__get_ST_table(cclass1,lvl1)
    t2=__get_ST_table(cclass2,lvl2)
    return [ min(x,y) for x, y in zip(t1,t2) ]

def get_ST_table(race,cclass,lvl):
    if cclass in ['Rakasta','Lupin'] :
        return get_best_of(cclass,lvl,'Fighter',2)
    else :
        return __get_ST_table(cclass,lvl)

if __name__ == '__main__' :
    def print_table():
        ST = [ 'Poison', 'Wands', 'Paralysis', 'Breath Atks', 'Spells' ]
        cls = [ 'Fighter', 'Cleric', 'Thief', 'Magic User' ]
        print ('Lv  {:12} {:12} {:12} {:12} {:12}'.format(*ST))
        print ('  '),
        for n in range(len(ST)):
            print (' F  C  T  MU'),
        print ('')
        for i in range(1,37):
            print ('{:2} '.format(i)),
            for n in range(len(ST)):
                st = tuple([ __get_ST_table(c,i)[n] for c in cls ])
                print ('{:2} {:2} {:2} {:2} '.format(*st)),
            print ('')
    print_table()

