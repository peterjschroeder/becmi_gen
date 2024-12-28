#!/usr/bin/python
from random import choice, randint

front = [ "Aith", "Arl", "Beth", "Brend", "Carl", "Dath", "Del", "Dor", "Draug", "Dru", "Durif", "Dy", "Dyr", "Elsp", "Enor", "Fal", "Fead", "Fill", "Firn", "Gall", "Gar", "Gen", "Gilf", "Glan", "Gylh", "Lach", "Le", "Lynn", "Mafl", "Malsh", "Meal", "Men", "Mil", "Myr", "Porph", "Qant", "Qen", "Quan", "Shal", "Tar", "Tel", "Thal", "Then", "Tor", "Uned", "Van" ]

mid = [ "o", "y", "on", "il", "i", "an", "a", "ar", "edi", "yr", "ri", "ane", "isa" ] 

back_male = [ "ath", "el", "eth", "n", "r", "s", "rn", "len", "dan", "der", "dil", "dir", "dor", "dyl", "fel", "gin", "mon", "quil", "ric", "ster", "wyll" ]
back_female = [ "el", "eth", "n", "s", "len", "dil", "dyl", "fel", "gin",  "ster", "wyll", "a", "ra", "sa", "na" ]


def process(s):
   s=str(s)
   import re
   # Replace duplicate "th" groups
   p=re.compile('thth')
   s=p.sub('th',s)
   # Replace duplicate "rnr" groups
   p=re.compile('rnr')
   s=p.sub('nr',s)
   # Insert extra vowels
   p=re.compile('([^aeiouy][^aeiouy])([^aeiouy][^aeiouy])')
   s=p.sub('\\1e\\2',s)
   # Replace duplicate "i" with "^i"
   p=re.compile('ii')
   s=p.sub(r'\^i',s)
   # Replace "iy" with "'i"
   p=re.compile('iy')
   s=p.sub("\'i",s)
   # Replace "yi" with "'i"
   p=re.compile('yi')
   s=p.sub(r'\`i',s)
   # Replace duplicate "e" with "^e"
   p=re.compile('ee')
   s=p.sub(r'\^e',s)
   # Replace duplicate "y" with "^y"
   p=re.compile('yy')
   s=p.sub(r'\^y',s)
   return s

def get_name(gender):
   back=back_female if gender=='f' else back_male
   res = choice(front) + choice([choice(mid),choice(mid), choice(mid)+choice(mid)]) + choice(back)
   res = process(res)
   return res


if __name__ == '__main__' :
   from sys import argv
   if len(argv)>1 :
      if argv[1] in ['male', 'm', '-m'] : gender='m'
      if argv[1] in ['female', 'f', '-f'] : gender='f'
   res=get_name(gender)	 
   try:
       print (res)
   except Exception :
       print ('Sorry, accented i or y not available...')
       print (res.encode('ascii','replace'))
