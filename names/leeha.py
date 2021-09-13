#!/usr/bin/python
from random import choice, randint

front_male = ["Ol", "Bello", "Jol", "Blas", "Bul", "Lev", "Dol", "Lod", "Bun", "Jen", "Horl", "Mul", "Jo", "Ul", "Og", "Shan", "Log" ]
mid = ["al", "len", "dy", "ab", "er" ]
back_male = ["myr", "mar", "thiir", "as", "tor", "tho", "kin", "thim", "am", "sar"]

front_female = ["Teth", "Zar", "Spiir", "Jal", "Osc", "Simmer", "Lob", "Maer", "Bel", "Sil"]
back_female = [ "a", "essa", "assa", "il", "agh", "linn", "atha" ]

clans = [ "Divotfoot", "Nimblefingers", "Gardener", "Merrybrook", "Highthicket", "Lowhill", "Harborhin", "Ironside", "Tremblay", "Gagnon", "Fortin", "Bouchard" ]

def process(s):
	s=unicode(s)
	import re
	# Replace duplicate "th" groups
	p=re.compile('thth')
	s=p.sub('th',s)
	for i in mid :
		p=re.compile(i+i)
		s=p.sub(i,s)
	return s

def get_base_name(gender='m'):
   back=back_female if gender=='f' else back_male
   front=front_female if gender=='f' else front_male
   res = choice(front) + choice([choice(mid),choice(mid), '', '', '','','','', choice(mid)+choice(mid)]) + choice(back)
   res = process(res)
   return res

def get_name(gender):
	res = get_base_name(gender)
	res+= ' son of ' if gender=='m' else ' daughter of '
	res+= get_base_name()
	res+= ' ' + choice(clans)
	return res


if __name__ == '__main__' :
   from sys import argv
   if len(argv)>1 :
      if argv[1] in ['male', 'm', '-m'] : gender='m'
      if argv[1] in ['female', 'f', '-f'] : gender='f'
   res=get_name(gender)	 
   print res
