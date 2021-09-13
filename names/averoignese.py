#!/usr/bin/python
from random import choice, randint

male_names = [ "Alexandre", "Alain", "Jean", "Charles", "Richard", "\\\'Etienne", "Henri", "Simon", "Malachie", "Luc", "Jehan", "Jacques", "David", "Andre\\\'e", "Michel", "Hubert", "G\\\'erard", "Christophe", "Hilaire", "Bernard", "Guillaume", "Hugh", "Quentin", "Raoul", "Blaise", "Ambrose", "G\^erome", "Gilles", "Theophile", "Robert", "Augustin", "Cl\\\'ement", "Gaspard", "Stephane", "Pierre", "Paul", "Hughes", "Louis", "Anselme", "Olivier", "J\^erome", "Hi\\\'erome", "Claude", "Georges", "Gaston", "Fran\c{c}ois", "\\\'Edouard", 'Alphonse', 'Antoine', 'Yves', "Philippe", "Denis" ]

female_names = [ "Eleanor", "Fleurette", "Agathe", "Ang\\\'elique", "Beatrix", "Nicolette", "Sabine", "Isabelle", "Catherine", "Marguerite", "Marie", "H\\\'el\`ene", "Th\\\'er\`ese", "Diane", "Antoinette", "Doroth\\\'ee", "Adele", "Nicole", "Isidore", "Monique", "Madeilene", "Jeanette", "Camille", "Constance", "Rose", "Blanche", "Genevi\`eve", "Suzanne", "D\\\'esir\\\'ee", "Am\\\'elie", "Jeanne", "Claude", "Fran\c{c}oise", "Fleur", "G\\\'eraldine", "Huguette", "Jacqueline", "V\\\'eronique", 'Yvette', "Simone", "St\\\'ephanie", "Perrine", "Louise", "Bernadette" ]

surnames = [ 'Morand', 'de Vaillantcoeur', 'des Lys', 'de Venteillon', "de l'Automme", 'Cochin', 'Reynard', 'Maspier', 'Mazzal', 'Coupain', 'Villom', 'Grenier', 'le Chaudronnier', 'Mauvassoir', "des \\\'Emaux", "du Nord", "des Fl\`eches", "du Framboisier", "du Montoir", "de la Foudrage", "Dindonneau", "le Morve", "Morin", "de For\^et", "Gravelotte", "de Montagnevert", "Beaumarys", "des Coteaux", "du Vrai", "Hiltier", "Chonere", "de l'Ouest", "de l'Hiver", "le Tailleur", "le Tonnelier", "le Forgeron", "le Poissonnier", "le Ferronier", "le Roux", "le Meunier", "du Bois", "du Mont", "le Clerc", "Moreau", "le Petit", "le Blanc", "du Val" ]

male_names_f = [ 'Jean', 'Louis', 'Charles', 'Fran\c{c}ois', 'Claude' ]
female_names_f = [ 'Marie', 'Anne' ]


def get_name(gender):
	if randint(1,6)==1 : 
		res = choice(male_names_f) if gender=='m' else choice(female_names_f)
		res+='-'
	else :
		res = ''
		if gender=='m' and randint(1,3)==1 : res+='Jean-'
	res += choice(male_names) if gender=='m' else choice(female_names)
	res+=' '+choice(surnames)
	return res

if __name__ == '__main__' :
   from sys import argv
   gender='m'
   if len(argv)>1 :
      if argv[1] in ['male', 'm', '-m'] : gender='m'
      if argv[1] in ['female', 'f', '-f'] : gender='f'
   res=get_name(gender)	 
   print res
