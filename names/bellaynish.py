#!/usr/bin/python
from random import choice, randint


male = [ "Purceval", "Lionel", "Hume", "Archibald", "Mortimer", "Edward", "Rodney", "Winston", "Melville", "Humphrey", "Jasper", "Gilbert", "Walter", "Richard", 'Cecil' ]

female = [ "Catherine", "Meghan", 'Elizabeth', 'Mary', 'Blanche', 'Lettice', 'Anne', 'Joyce', 'Rose', 'Isabel', 'Jocasta', 'Margaret', 'Margery', 'Maud' ]

front = [ "Hay", "Putt", "Purring", "Cocker", "Whit", "Glad", "Hill", "Paw", "Nor", "Fur", "Wisker", "Claw", "Kitt", "Mal", "South", "Black", "Moor", "Walling", "Ruther", "Piker", "Chat", "Ald", "Glen", "Hamp", "Old", "Tatter", "Leo", "Brom", 'Rock', "Purr" ] 

back = [ "stoke", "field", "worth", "well", "worthy", "borough", "chester", "ton", "don", "ings", "burn", "heath", "ford", "wark", "hythe", "stead", "gate", "sbury", "ham", "tow" ]

def get_name(gender='m'):
	res = choice(male) if gender == 'm' else choice(female)
	f = choice(front) 
	b = choice(back)
	if f[-1]==b[0] or (randint(1,2) and b[0] not in [ 'c', 'i', 'd', 's' ]) == 1 :
		res += ' '+ f+'s'+b
	else : res += ' '+ f+b
	return res

if __name__ == '__main__' :
   from sys import argv
   gender='m'
   if len(argv)>1 :
      if argv[1] in ['male', 'm', '-m'] : gender='m'
      if argv[1] in ['female', 'f', '-f'] : gender='f'
   res=get_name(gender)	 
   print res
