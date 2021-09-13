#!/usr/bin/python
from random import choice, randint

# Ramenhotep

front = [ "Ra", "Hap", "To", "Per", "Khne", "Dje", "Hasha", "Ar", "At", "Isi", "Tur", "Ki", "Fa", "Bel", "Ta", "Ke", "Hu", "Ti", "Auri", "Khom", "Im", "In", "Ne", "Me", "Sen" ]

mid = [ "men", "ho", "tu", "ko", "ram", "mo", "met", "bur", "mi", "ke", "en", "no", "na", "fa", "si", "da", "ta", "her", "sa", "fru", "ma"]

back_male = [ "om", "tep", "ses", "thep", "se", "mon", "urt", "mun", "nal", "lam", "man", "nut", "ak", "bub", "pher", "ris", "ah", "tre", "ra", "sra", "mut" ] 

back_female = [ "theti", "titi", "yat", "ra", "ma", "sri", "sra", "lam", "tri", "na", "mun", "kha", "shet" ] 

def process(s):
   s=unicode(s)
   import re
   # Replace duplicate "th" groups
   p=re.compile('thth')
   s=p.sub('th',s)
   # Replace duplicate "dr" groups
   p=re.compile('drdr')
   s=p.sub('dr',s)
   p=re.compile('drd')
   s=p.sub('dr',s)
   p=re.compile('dd')
   s=p.sub('d',s)
   p=re.compile('td')
   s=p.sub('t',s)
   p=re.compile('shdr')
   s=p.sub('sh\^edr',s)
   # Replace duplicate "i" with "^i"
   p=re.compile('ii')
   s=p.sub('\^i',s)
   # Replace duplicate "y" with ":i"
   p=re.compile('yy')
   s=p.sub('\^y',s)
   return s

def get_name(gender='m'):
   back=back_female if gender=='f' else back_male
   res = choice(front) + choice([choice(mid),choice(mid), '','','','', choice(mid)+choice(mid)]) + choice(back)
   res = process(res)
   return res


if __name__ == '__main__' :
   from sys import argv
   gender='m'
   if len(argv)>1 :
      if argv[1] in ['male', 'm', '-m'] : gender='m'
      if argv[1] in ['female', 'f', '-f'] : gender='f'
   res=get_name(gender)	 
   try:
       print res
   except Exception :
       print 'Sorry, accented i or y not available...'
       print res.encode('ascii','replace')
