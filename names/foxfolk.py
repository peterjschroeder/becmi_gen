#!/usr/bin/python
from random import choice, randint

from heldanner import male_names, female_names

element = [ 'Fire', 'Water', 'Earth', 'Sky' ]
totem = [ 'Salmon', 'Eagle', 'Hare', 'Snake', 'Elk' ]
village = [ 'Larch', 'Fir', 'Elm', 'Oak', 'Birch', 'Ash', 'Spruce', 'Poplar', 'Walnut', 'Hickory', 'Maple', 'Locust', 'Pine' ]

def get_name(gender='m', cclass=None):
   res = choice(male_names) if gender=='m' else choice(female_names)
   res += ' '
   if cclass == 'Druid' : res += choice(totem) + '-' + choice(village)
   else : res += choice(element) + '-' + choice(totem)
   return res

if __name__ == '__main__' :
   from sys import argv
   gender='m'
   if len(argv)>1 :
      if argv[1] in ['male', 'm', '-m'] : gender='m'
      if argv[1] in ['female', 'f', '-f'] : gender='f'
   res=get_name(gender)	 
   print (res)
