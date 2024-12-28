#!/usr/bin/python
from random import choice, randint

if __name__=='__main__' :
	import sys
	sys.path.append("..")
from dice import d6

male_names = [ "Anton", "Antonie", "Isaac", "Simon", "Vanserie", "Wilfried", "Pieter", "Eeuwke", "Jorg", "Namoor", "Mirn", "Ludo", "Maas", "Emil", "Dries", "Jissel", "Wilhelm", "Barend", "Andreis", "Bernardus", "Vincent", "Ernst", "Petrus", "Frans", "Ruudgart", "Garnaar", "Ruud", "Rodolphus", "Frederick", "Michel", "Moritz", "Jacob", "Willem", "Johann", "Haak", "Hena", "Jan", "Horst" ] 

female_names = [ "Juliana", "Sinaria", "Wilhelmina", "Leena", "Anneke", "Magda", "Johanna", "Rowena", "Fredericka", "Margretha", "Hana", "Rhonda", "Seelen", "Thiere", "Klara",  ] 

surnames = [ "Vlaadoen", "Verlien", "Krollnar", "Vandehaar", "Vanderleest", "de Gheyn", "Tijlen", "Moroden", "Vandeeker", "Pienants", "Van Drees", "Madhorsen", "Maarsten", "Van Agt", "Rjeven", "Van Dijke", "Postbrad", "Deegaer", "Jonsen", "de Wajden", "de Meers", "Krijlens", "Sager", "van Haast", "Glietnen", "Handjeer", "Loeten", "Wjesmans" ]

def get_name(gender):
	res = choice(male_names) if gender=='m' else choice(female_names)
	res+=' '+choice(surnames)
	return res

if __name__ == '__main__' :
   from sys import argv
   gender='m'
   if len(argv)>1 :
      if argv[1] in ['male', 'm', '-m'] : gender='m'
      if argv[1] in ['female', 'f', '-f'] : gender='f'
   res=get_name(gender)	 
   print (res)
