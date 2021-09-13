#!/usr/bin/python
from random import choice, randint

if __name__=='__main__' :
	import sys
	sys.path.append("..")
from dice import d6

male_names = [ 'Gan', 'Jek', 'Dak', 'Reno', 'Fero', 'Den', 'Han', 'Pol', 'Jin', 'Keril', 'Garot', 'Ru', 'Vimo', 'Wert', 'Marny', 'Avral', 'Ganti', 'Ruly', 'Nero', 'Bat', 'Kelam', 'Hari', 'Toc', 'Gelek', 'Beneeck', 'Noril', 'Aster', 'Farrem', 'Dak', 'Pariman', 'Erias', 'Kiko', 'Jarren', 'Ruce', 'Nizo', 'Mannie', ]
female_names = [ 'Tia', 'Rena', 'Kani', 'Kira', 'Jin', 'Keril', 'Vima', 'Hanni', 'Mina', 'Leethra', 'Mora', 'Gen', 'Hatara', 'Verta', 'Moana', 'Hetta', ]

start = [ 'Ti', 'Ga', 'Je', 'Fe', 'Da', 'De', 'Re', 'Ha', 'Po', 'Jo', 'Ke', 'Ru', 'Vi', 'We', 'Ve', 'Mar', 'Av', 'Gan', 'Ki', 'Jar', 'Ka', 'He', 'Moa' ]
male_ends = [ 'n', 'k', 'no', 'ro', 'l', 'rot', 'rt', 'ny', 'ral', 'ti', 'ce', 'nnie' ]
female_ends = [ 'a', 'na', 'ni', 'ra', 'n', 'ril', 'ma', 'nni', 'thra', 'ra', 'rta', 'tta' ]

surnames = [ 'Windhook', 'Kaylee', 'Dopson', 'Rayds', 'Hubari', 'Longbraid', 'Longblade', 'Kindle', 'Blackcheek', ]
surname_start = [ 'Wind', 'Long', 'Short', 'Far', 'Black', 'Red', 'Green', 'Sand', 'Sea', 'White' ]
surname_end = [ 'blade', 'braid', 'son', 'hook', 'leaf', 'stride', 'horn', 'beard', 'bone', 'staff', 'hawk' ]

thyatian_surnames = [ 'Karibus', 'Alexander', 'Meikros', 'Seilus', 'Seleukides', ]
daro_surnames = [ 'Matrongle', 'Van Hoorn', 'Marley', 'Teach', 'Rackham', 'Eddington', 'Rogers', 'Alvine', 'Elfinblood', 'Halfelven', 'Gentle' ] 
traladaran_surnames = [ 'Gogunov' ]

def get_name(gender):
        # Type of name :
        surname=''
        t='native'
        if d6() < 4 :
            t  = choice(['daro','thyatian', 'tradalaran' ] + ['native'] * 6)
            if t=='daro' : surname = choice(daro_surnames)
            elif t=='thyatian' : surname = choice(thyatian_surnames)
            elif t=='traladaran': surname = choice(traladaran_surnames)
            else : 
                if d6()< 3 : surname = choice(surnames)
                else : surname = choice(surname_start)+choice(surname_end)
        if d6() < 4 :
            res = choice(start) + ( choice(male_ends) if gender=='m' else choice(female_ends) )
        else :
            if t=='daro' : 
                from daro import male_names as dmn, female_names as dfn
                res = choice(dmn) if gender=='m' else choice(dfn)
            elif t=='thyatian' : 
                from thyatian import get_name as gn
                res = gn(gender)
            elif t=='traladaran' :
                from traladaran import get_name as gn
                res = gn(gender)
            else : res = choice(male_names) if gender=='m' else choice(female_names)
        if surname and d6()<6 :
            from string import split
            res=split(res)[0]+' '+surname
	return res

if __name__ == '__main__' :
   from sys import argv
   gender='m'
   if len(argv)>1 :
      if argv[1] in ['male', 'm', '-m'] : gender='m'
      if argv[1] in ['female', 'f', '-f'] : gender='f'
   res=get_name(gender)	 
   print res
