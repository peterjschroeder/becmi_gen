#!/usr/bin/python
from random import choice, randint

front_name = [ 'Da', 'Tah', 'Ha', 'Mah', 'Ah', 'Ho', 'E', 'Dy', 'Ta', 'Do', 'Po', 'To' ]
mid_name = [ 'ma', 'ka', 'tta', 'lin', 'wa', 'le', 'a', '', '', '' ]
male_back_name = [ 'ndo', 'nel', 'ri', 'rri', 'guk', 'var', 'kuan', 'ya', 'ti', 'tti', 'ni', 'nni', 'nto' ]
female_back_name = [ 'nel', 'ri', 'rri', 'ya', 'ti', 'ni', 'nni', 'sha' ]

astro = [ 'Sun', 'Moon', 'Star', 'Mist', 'Cloud', 'Sky' ]
front_adj = [ 'Stalking', 'Running', 'Silent', 'Spotted', 'Crazy', 'Laughing', 'Little', 'Big', 'Wise', 'Lone', 'Sure', 'Fast', 'Quick', 'Crashing', 'Sitting', 'Jumping', 'Flying', 'Burning', 'Mighty', 'Deep', 'Red', 'Black', 'White', 'Yellow', 'Green', 'Blue', 'Grey' ]
front_adj_body = [ 'Quick', 'Fast', 'Strong', 'Long' ]
animal = [ 'Deer', 'Elk', 'Tiger', 'Horse', 'Puma', 'Sparrow', 'Raccoon', 'Duck', 'Wolf', 'Bull', 'Crow', 'Turtle', 'Bird', 'Hawk', 'Owl', 'Badger' ]
item = [ 'Wave', 'Spear', 'Axe', 'Arrow', 'Surf', ] 
body = [ 'Fingers', 'Legs', 'Hand', 'Arm', 'Foot', 'Horn', 'Tail' ]
back_agent = [ 'Seeker', 'Maker', 'Hunter', 'Rider', 'Watcher', 'Stalker', 'Dancer' ]

def get_name(gender='m', cclass=None):
   res  = choice(front_name)+choice(mid_name)
   res += choice(male_back_name) if gender=='m' else choice(female_back_name)
   res += ' '
   front = front_adj
   back = choice(item+body+back_agent+animal)
   if back in body : front = front_adj_body
   elif back in back_agent : front = animal+item+astro
   elif back in animal : front = front_adj+astro
   res += choice(front) + ' ' + back
   return res

if __name__ == '__main__' :
   from sys import argv
   gender='m'
   if len(argv)>1 :
      if argv[1] in ['male', 'm', '-m'] : gender='m'
      if argv[1] in ['female', 'f', '-f'] : gender='f'
   res=get_name(gender)	 
   print (res)
