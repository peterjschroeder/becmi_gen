#!/usr/bin/python
from random import choice, randint

if __name__=='__main__' :
	import sys
	sys.path.append("..")
from dice import d6

male_names = [ "Oleg", "Igor", "Volkh", "Yuri", "Gleb", "Sveta", "Boroda", "Zivon", "Yaro", "Dobrynya", "Volodya", "Stano" ]
female_names = [ "Olava", "Olga", "Malusha", "Zabava", "Liubava", "Rogneda" ]

front = [ "Nevi", "Volody", "Yaro", "Rado", "Vladi", "Svyato", "Rosti", "Misti", "Izya", "Vyshe", "Pred", "Premi", "Sudi", "Ostro",  "Vse", "Viache", "Volo", "Bryachi", "Puty", "Zby", "Vasy", "Gremi", "Verchu", "Stani", "Dobre" ]

back_male = [ "k", "lko", "slav", "myr", "ata", "polk", "mir", "gor", "volod", "dar" ]
back_female = [ "ka", "slava", "myra", "polka", "mira", "gora" ]

patronyms = [ "Olegov", "Igorov", "Volkhov", "Yurev", "Glebov", "Svetyev", "Borodyev", "Zivonov", "Yarov", "Dobryn", "Volodyev" ]
back_patronyms = [ "kov", "lkov", "slav", "myrov", "atav", "polkov", "mirov", "gorov", "volodov", "darov" ]


def get_name(gender):
	if d6()<3 :
		res = choice(male_names) if gender=='m' else choice(female_names)
	else :
		res = choice(front)
		res+= choice(back_male) if gender=='m' else choice(back_female)
	res+=' '
	if d6()<3 :
		res+= choice(patronyms)
	else :
		res+= choice(front)+choice(back_patronyms)	
	res+='ich' if gender=='m' else 'na'
	return res

if __name__ == '__main__' :
   from sys import argv
   gender='m'
   if len(argv)>1 :
      if argv[1] in ['male', 'm', '-m'] : gender='m'
      if argv[1] in ['female', 'f', '-f'] : gender='f'
   res=get_name(gender)	 
   print (res)
