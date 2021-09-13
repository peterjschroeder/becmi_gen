#!/usr/bin/python
from random import choice, randint

front = [ 'Ala', 'Thoris', 'Theodo', 'Wale', 'Nant', 'Wulf',  'Bili', 'Ful', 'Ermen', 'Ger', 'Liut', 'Luit', 'Wite', 'Liuva', 'Reca', 'Balt', 'Artha', 'Sigis', 'Uth', 'On', 'Beo', 'Theoda', 'Eu', 'Alda', 'Theude', 'Childe', 'Chilpe', 'Clot', 'Chlodo',  'Frede', 'Sige', 'Dago', 'Halde', 'Ingo', 'Ing', 'Godo', 'Rade', 'Berth', 'Bade', 'In', 'Mero', 'Chari', ] 

back = [ 'ulf', 'vild', 'gar', 'vig', 'mir', 'ric', 'gund', 'mund', 'prand', 'hild', 'mar', 'red', 'har', 'bert', 'mer', 'bald', 'gard', 'ver', 'berg', ]

back_female = [ 'a' ]

def process(s):
   s=unicode(s)
   import re
   # Replace duplicate "ou" groups
   p=re.compile('ou')
   s=p.sub('u',s)
   return s

def get_base_name(gender='m'):
   res = choice(front) + choice(back)
   res+= choice(back_female) if gender=='f' else ''
   res = process(res)
   return res

def get_name(gender):
   res = get_base_name(gender)
   res+= ' son of ' if gender=='m' else ' daughter of '
   res+= get_base_name()
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
