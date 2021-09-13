#!/usr/bin/python
from random import choice, randint
from string import lower
if __name__=='__main__' :
	import sys
	sys.path.append("..")
from dice import d6

surname = [ 'Wang', 'Li', 'Zh\=ang', 'Liu', 'Chen', 'Yang', 'Huang', "Zh\`ao", 'Wu', 'Zh\=ou', 'Xu', 'S\`un', 'Ma', 'Zh\=u', 'Hu', 'Gu\=o', 'He', 'G\=ao', 'Lin', 'Luo', 'Zheng', 'Liang', 'Hsieh', 'Sung', 'Tang', 'X\uu', 'Feng', 'Deng', 'Cao', 'Peng', 'Deng', 'Xiao', 'Z\=eng', 'Xi\=ao', 'Tian', 'Dong', 'Yuan', 'Pan', 'Yu', 'Jiang', 'Cai', 'Yu', 'Du', 'Ye', 'Cheng', 'Su', 'Wei', 'Lu', 'Ding', 'Ren', 'Shen' ]
front = ['Lao', 'Xiao', 'Li', 'Wei', 'Fang', 'Xiu', 'Min', 'Jing', 'Qiang', 'Lei', 'Jun', 'Yang', 'Yong', 'Y\=ong', 'Jie', 'Juan', 'Chao', 'Ping', 'Gang', 'Gui', 'Fei' ]
back = ['lan', 'ying']


def get_name(gender):
   res = choice(surname) +' ' 
   n = choice(front)
   res+= n
   if gender=='f' :
	if d6()<2 : res+=lower(n)
	elif d6()<2 : res+=lower(choice(front))
	elif d6()<2 : res+=choice(back)
   else :
	if d6()<5 : res+=lower(choice(front))
   return res


if __name__ == '__main__' :
   from sys import argv
   gender='m'
   if len(argv)>1 :
      if argv[1] in ['male', 'm', '-m'] : gender='m'
      if argv[1] in ['female', 'f', '-f'] : gender='f'
   print get_name(gender)	 
