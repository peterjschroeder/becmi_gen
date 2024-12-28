#!/usr/bin/python
from random import choice, randint

back = [ 'rrgai', "rrk'os", 'rren', 'rrtthogh', 'sa', 'ta', 'yah', 'tthe',  'derrba', 'cho', 'xath' ]
front = [ 'Tsa', 'Sas', 'Gah', 'Des', 'Bes', 'Dlie', 'Taghe', 'Denie', 'Tha', 'Tsi', 'Lue' ]
clans = [ 'Delgaike', 'Delzenke', 'Delk\'oske', 'Deltseske', 'Delbaike', 'Y\\\'ath\\\'o\\ce', 'Sastses', 'Dl\\\'ie', 'Ta\\\'a', 'Gah', 'Dzen' ]

def process(s):
	s=str(s)
	import re
	# Replace duplicate "th" groups
	p=re.compile('thth')
	s=p.sub('th',s)
	return s

def get_name(gender='m'):
   res = choice(front) + '-' + choice(back)
   res += ' of the ' + choice(clans) + ' Ch\\\'ize'
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
       print (res)
   except Exception :
       print ('Sorry, accented i or y not available...')
       print (res.encode('ascii','replace'))
