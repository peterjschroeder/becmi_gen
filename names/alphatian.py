#!/usr/bin/python
from random import choice, randint

front = [ 'Aend', 'Aik', 'Alph', 'Amphi', 'Andru', 'Arb', 'Ash', 'Astr', 'Bur', 'Cypr', 'Doln', 'Eadr', 'Ec', 'Edj', 'Edr', 'Ei', 'El', 'Eldr', 'Elsh', 'Em', 'Er', 'Er', 'Hal', 'Hast', 'Hug', 'Kal', 'Kav', 'Ker', 'Kob', 'Kra', 'Kryn', 'La', 'Laz', 'Lern', 'Llyn', 'Lod', 'Lodr', 'Mad', 'Mar', 'Myler', 'Pir', 'Pof', 'Qirk', 'Quan', 'Quis', 'Ram', 'Stil', 'Sud', 'Sula', 'Tal', 'Ta', 'Ter', 'Tesk', 'Thyl', 'Tim', 'Tor', 'Tred', 'Trist', 'Tsal', 'Tyl', 'Un', 'Ur', 'Uth', 'Vert', 'Vol', 'Xer', 'Zan', 'Zin', 'Zum', 'Zyn' ]

mid = [ 'ad', 'adn', 'ak', 'ar', 'as', 'az', 'ba', 'bash', 'da', 'de', 'dr', 'dy', 'en', 'etar', 'eth', 'i', 'ic', 'i', 'a', 'il', 'in', 'li', 'or', 'ori', 'osp', 'oth', 'ri', 'rul', 'tend' ]

back_male = [ 'ad', 'ak', 'al', 'al', 'al', 'all', 'an', 'ar', 'ar', 'ari', 'arys', 'as', 'as', 'az', 'az', 'bash', 'don', 'dor', 'dy', 'ear', 'el', 'en', 'er', 'er', 'etar', 'eth', 'eth', 'i', 'ig', 'il', 'il', 'il', 'im', 'in', 'ing', 'ion', 'ior', 'ion', 'ior', 'ion', 'ior', 'issur ', 'lan', 'li', 'lin', 'ol', 'ori', 'orth', 'oska', 'oth', 'oth', 'than ', 'ucks', 'un', 'ur', 'yl', 'yr','yl', 'yr' ]

back_female = [ 'a', 'a', 'ala', 'alla', 'alta', 'ana', 'ara', 'ari', 'arys', 'ba', 'da', 'de', 'dy', 'ella', 'era', 'era', 'eth', 'i', 'ila', 'ila', 'ila', 'ilia', 'itsa', 'lya', 'na', 'na', 'nia', 'oska', 'yla', 'yra' ]

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

def get_name(gender):
   back=back_female if gender=='f' else back_male
   res = choice(front) + choice([choice(mid),choice(mid), '','','','', choice(mid)+choice(mid)]) + choice(back)
   res = process(res)
   return res


if __name__ == '__main__' :
   from sys import argv
   if len(argv)>1 :
      if argv[1] in ['male', 'm', '-m'] : gender='m'
      if argv[1] in ['female', 'f', '-f'] : gender='f'
   res=get_name(gender)	 
   try:
       print res
   except Exception :
       print 'Sorry, accented i or y not available...'
       print res.encode('ascii','replace')
