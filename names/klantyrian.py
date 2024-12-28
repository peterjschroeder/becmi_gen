#!/usr/bin/python
from random import choice, randint

male_names = [ "Alasdair", "Alan", "Iain", "Duncan", "Bruce", "Bran", "Malcolm", "Donald", "Connor", "Findlay", "Murdoch", "Macbeth", "Malise", "James", "David", "Sean", "Eachainn", "Kenneth", "Brian", "Farquhar", "Fergus", "Angus", "Quentin", "Edward", "Maldred", "Edmund", "Wallace", "Angan", "Edgar", "Roibert", "Lachlan", "Ossian", "Adam", "William", "Morgan" ]

female_names = [ "Deirdre", "Fenella", "Fiona", "Branwenn", "Beatrix", "Olith", "Eithne", "Isabelle", "Edith", "Bridig", "Mary", "Margaret", "Marjorie", "Fergusa", "Keyne", "Callwen", "Barbara", "Dorothy", "Amabel", "Bride", "Kenna", "Malvina", "Una", "Morag", "Mildred" ]

surnames = [ 'Donnell', 'Donald', 'Murdoch', 'Bride', 'Lachlan', 'Gregor', 'Clintock', 'Duff', 'Allister', 'Dougall', 'Intyre', 'Leod', 'Culloch', 'Muir', 'Intosh', 'Tavish', 'Allan' ]


def get_name(gender):
	res = choice(male_names) if gender=='m' else choice(female_names)
	res+=' Mc'+choice(surnames)
	return res

if __name__ == '__main__' :
   from sys import argv
   gender='m'
   if len(argv)>1 :
      if argv[1] in ['male', 'm', '-m'] : gender='m'
      if argv[1] in ['female', 'f', '-f'] : gender='f'
   res=get_name(gender)	 
   print (res)
