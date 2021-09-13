#!/usr/bin/python
from random import choice, randint

front = [ "Appi", "Aul", "Cai", "Luci", "Mamerc", "Mani", "Marc", "Prim", "Publi", "Quint", "Secund", "Sext", "Servi", "Spuri", "Terti", "Tiberi", "Tit", "Aeli", "Aemili", "Antoni", "Appulei", "Arri", "Atil", "Aureli", "Caeli", "Cassi", "Claudi", "Corneli", "Decim", "Domiti", "Fabi", "Flavi", "Furi", "Gavi", "Iuli", "Iuni", "Curti", "Livi", "Licini", "Mari", "Marci", "Manli", "Octavi", "Oppi", "Papiri", "Rutili", "Vani", "Titi", "Publi", 'Acas', 'Adron', 'Alex', 'Angel', 'Bessar', 'Aster', 'Demet', 'Leon', 'Helen', 'Petron', 'Stefan', 'Taras', 'Theo', 'Theodo', 'Zen', 'Adri', 'Constant', 'Diocleti', 'Maxim', 'Ruf', 'Paul', 'Valent', 'Var', 'Reteb' ]

back_male = [ "ius", "ianus", "ine", "inius", "inus", "us", "anus", "in", "an", "es", "ites", "ian" ]
back_female = [ "ia", "iana", "ina", "anna", "ira", "inia", "iela", "ita", "ana", "a", "ana" ]

back_male_surname = back_male + [ 'anicus', 'ianicus', 'icus', 'cus', 'anitas', 'anites', 'arius' ]
back_female_surname = back_female + [ 'ica', 'ianica', 'ca', 'anita', 'aria' ]

def process(s):
   s=unicode(s)
   import re
   # Replace duplicate "th" groups
   p=re.compile('thth')
   s=p.sub('th',s)
   # Replace duplicate "i" with "^i"
   p=re.compile('ii')
   s=p.sub('i',s)
   # Replace duplicate "y" with ":i"
   p=re.compile('yy')
   s=p.sub('y',s)
   return s


def get_name(gender):
	back=back_female if gender=='f' else back_male
	res = choice(front) + choice(back)
	res+=' '
	back=back_female_surname if gender=='f' else back_male_surname
	res+= choice(front) + choice(back)
	res = process(res)
	return res

if __name__ == '__main__' :
   from sys import argv
   if len(argv)>1 :
      if argv[1] in ['male', 'm', '-m'] : gender='m'
      if argv[1] in ['female', 'f', '-f'] : gender='f'
   res=get_name(gender)	 
   print res
