#!/usr/bin/python
if __name__=='__main__' :
	import sys
	sys.path.append("..")
from random import choice, randint
from dice import *

front = [ 'Hau', 'Ma', 'Ho', 'Tu', 'Ran', 'Ku', 'Ro', 'Rau', 'Moa' ]

mid = [ 'me', 'tui', 'pa', 'gi', 'ro', 'hu', 'le', 'ku', 'an', 'ta' ]

back_male = [ 'ka', 'pua', 'lea', 'tua', 'ora', 'ia', 'hua', 'noa', 'mai', 'moe', 'wa', 'hi' ] 

back_female = back_male

def __get_name(gender):
   back=back_female if gender=='f' else back_male
   res = choice(front) 
   if d6() < 3 : res+= choice(mid)
   if d6() < 2 : res+= choice(mid)
   if d6() < 2 : res+= choice(mid)
   res+= choice(back)
   return res

def get_name(gender):
    return __get_name(gender)+' '+__get_name(gender)

if __name__ == '__main__' :
   from sys import argv
   if len(argv)>1 :
      if argv[1] in ['male', 'm', '-m'] : gender='m'
      if argv[1] in ['female', 'f', '-f'] : gender='f'
   res=get_name(gender)	 
   print (res)
