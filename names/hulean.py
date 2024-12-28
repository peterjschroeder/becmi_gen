#!/usr/bin/python
from random import choice, randint

if __name__=='__main__' :
	import sys
	sys.path.append("..")
from dice import d6

male_names = [ 'Atman', 'Orhan', 'Murad', 'Ertughul', 'Bayezid', 'Fatih', 'Selim', 'Cihangir', 'Seljuq', 'Tughril', 'Arslan', 'Chaghri', 'Timur', 'Jahangir', 'Qilij', 'Qutalmish', 'D\\\"undar', 'Barlas', 'Durmush', 'Alp', 'Birol', 'Erdal', 'Cahit', 'Erqan', 'Cem', 'Celiq', 'Demir', 'Bahri', 'Do\u{g}an', 'Ayteq', 'Aydin', 'G\\\"urqan', 'G\\\"ursel', 'G\\\"uven', 'G\\\"unesh', '\\\"Ozer', 'Veysel', 'Taner', 'Yener', 'Shenol', 'Sheqer', 'Togan' ]

female_names = [ 'Nil\\\"ufer', 'Malhun', 'G\\\"ulchicheq', 'Devlet', 'Emine', 'H\\\"uma', 'G\\\"ulbahar', 'Hafsa', 'H\\\"urrem', 'Nurbanu', 'Q\\\"osem', 'Ayshe', 'Neslihan',  'Asli', 'Nalan', 'Nezihe', 'Oya', 'Aysel', 'Semiha', 'Cansever', 'Cemre', 'Yeliz', 'Zuhal', 'T\\\"ulin' ] 


def get_name(gender):
	res = choice(male_names) if gender=='m' else choice(female_names)
	res+=' '+choice(male_names)+'oghlu'
	return res

if __name__ == '__main__' :
   from sys import argv
   gender='m'
   if len(argv)>1 :
      if argv[1] in ['male', 'm', '-m'] : gender='m'
      if argv[1] in ['female', 'f', '-f'] : gender='f'
   res=get_name(gender)	 
   print (res)
