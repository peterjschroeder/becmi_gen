#!/usr/bin/python

generators = {
    ('Lupin','Heldann Shepherd') : 'heldanner',
    ('Lupin','Snoutzer') : 'heldanner',
    ('Lupin','Mastiff') : 'thyatian',
    ('Lupin','Mongrel Lupin') : 'thyatian',
    ('Lupin','Beagle') : 'thyatian',
    ('Lupin','Ochalean Houndling') : 'ochalean',
    ('Lupin','Ochalean Crested') : 'ochalean',
    ('Lupin','Shar-Pei') : 'ochalean',
    ('Lupin','Chow Chow') : 'ochalean',
    ('Lupin','Doggerman') : 'heldannic',
    ('Lupin','Das Hund') : 'heldannic',
    ('Lupin','Fennec') : 'alasiyan',
    ('Lupin','Nithian Rambler') : 'alasiyan',
    ('Lupin','Narvaezan Maremma') : 'belcadiz',
    ('Lupin','Carrasquito') : 'belcadiz',
    ('Lupin','Ispan Pistolero') : 'belcadiz',
    ('Lupin','Renardois Folk') : 'averoignese',
    ('Lupin','Bouchon') : 'averoignese',
    ('Lupin','Papillon') : 'averoignese',
    ('Lupin','Hound of Klantyre') : 'klantyrian',
    ('Lupin','Zvornikian Sentinel') : 'traladaran',
    ('Lupin','Slagovici Gonic') : 'traladaran',
    ('Human','Vatski/Vrodniki') : 'vatski',
    ('Dwarf','Alphatian') : 'dwarf',
    ('Dwarf','Montoya') : 'belcadiz',
    ('Halfling','Alphatian') : 'halfling',
    ('Rakasta','Pardasta') : 'ochalean',
    ('Rakasta','Fast Runner') : 'thothian',
    ('Human', 'Ispan'): 'belcadiz',
    ('Dwarf','Moadreg') : 'moadreg',
}

regional = {
    'Savage Coast' : {
        ('Lupin', 'Mongrel Lupin') : 'averoignese',
        ('Lupin', 'Foxfolk') : 'dunael',
    },
        'Darokin' : {
                ('Lupin', 'Mongrel Lupin') : 'daro',
                ('Lupin', 'Beagle') : 'daro',
                ('Lupin', 'Mastiff') : 'daro',
        },
}

def get_namegen(race, origin, region=None):
    if region in regional :
        for k in regional[region] :
            generators[k]=regional[region][k]
    from importlib import import_module
    if (race, origin) in generators.keys():
        return import_module('names.'+generators[race,origin]).get_name
    norm_race = race.lower()
    norm_origin = origin.lower()
    # Replace ' ' with '_'
    import re
    p=re.compile(' ')
    norm_race = p.sub('_',norm_race)
    norm_origin = p.sub('_',norm_origin)
    # Try loading from origin
    try : return  import_module('names.'+norm_origin).get_name
    except Exception : pass
    # Try loading from race
    try : return  import_module('names.'+norm_race).get_name
    except Exception : pass
    def error_gn(gender='m',cclass=None):
        print ("Name generator not available for "+origin+' '+race)
        print ("Using namemaker.")

        import namemaker
        if gender == 'm':
            first_names = namemaker.make_name_set('male first names.txt')
        else:
            first_names = namemaker.make_name_set('female first names.txt')
        
        last_names = namemaker.make_name_set('last names.txt')

        return '%s %s' % (first_names.make_name(), last_names.make_name())
    return error_gn

def get_name(race, origin, gender, cclass=None, region=None):
    if cclass : return get_namegen(race,origin,region)(gender,cclass)
    else :  return get_namegen(race,origin,region)(gender)

if __name__ == '__main__' :
    from sys import argv
    from config import races, ethnic_by_race
    from random import choice
    gender = choice(['m','f'])
    if len(argv)>1 :
        if argv[1] in ['male', 'm', '-m'] : gender='m'
        if argv[1] in ['female', 'f', '-f'] : gender='f'
    r = choice(races())
    o = choice(ethnic_by_race(r))
    res=get_name(r,o,gender)
    print (res)
