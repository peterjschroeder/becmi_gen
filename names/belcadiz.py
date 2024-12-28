#!/usr/bin/python
from random import choice, randint

male_names = [ "Balthazar", "Diego", "Domingo", "Jos\`e", "Gonzalo", "Tello", "\\\'Alvaro", "Ponce", "Mart\\\'in", "Angel", "Xelmiro", "Lope", "Tristan", "Maximiliano", "Manrique","Alejandro", "Augusto", "Julio", "Manuel", "Gal\\\'indo", "Ramiro", "Armando", "Juan", "Carlos", "Ricardo", "Esteban", "Enrique", "Xavier", "Pablo", "Lucas", "Iago", "Santiago", "David", "Andr\\\'es", "Miguel", "Hernan", "G\\\'eraldo", "Cr\\\'istobal", "Dante", "Bernardo", "Guillermo", "Hugo", "Sancho", "Raul", "Garc\\\'ia", "Alfredo", "Jer\\\'onimo", "Egidio", "Teofilo", "Ramon", "Agustin", "I\~nigo", "Jimeno", "Alfonso", "Pedro", "Alonso", "Fernando", "Luis", "Rodrigo", "Mu\~no", "Felipe", "Francisco", "Jorge", "Eduardo" ]

female_names = [ "Marina", "Berenguela", "Mafalda", "Elvira", "Pilar", "Rosa", "Margarita", "Constanza", "Jimena", "Sancha", "Isabel", "Justa", "Toda", "Estefan\\\'ia", "Placencia", "Felicia", "Juana", "Catalina", "Esmeralda", "Blanca", "Ana", "Leonor", "Beatriz", "Magdalena", "Jer\\\'onima", "Francisca", "Munia", "Teresa", "Carmina", "Esperanza", "Dulcinea", "Angel\\\'ita" ]

surnames = [ "Aranjuez", "Montejo",  "Morales", "Dominguez", "Montoya", "Manzanas", "Linares", "Costa", "Marreras", "Casanegra", "L\\\'eon", "Villavieja", "Villanueva", "Alcazar", "Morales", "Prado", "Alvarez", "Fuentes", "Medina", "Moreno", "Toro", "Burgos", "Vega", "Lara", "Ayala", "T\\\'ellez", "Velez", "Campos", "Garc\\\'ia", "Molina", "Ya\~nez", "Rivera", "Sotto", "Lima", "Matac\\\'an", "Su\\\'arez", "Cu\\\'ellar",  "G\\\'omez", "Ordo\~nez", "Zamora", "Atienza", "Calahorra", "Raimundez", "Herrera", "Alcab\\\'on", "Traba", "Mart\\\'inez", "Menendez", "Perez", "Gonzalez", "Lopez", "Monz\\\'on", "Mu\~noz", "Vermudez", "Jimenez", "Ruiz", "Rodriguez", "Diaz", "Luna", "Viana", "Castro", "Mara\~n\\\'on", "Aguilar", "Enriquez", "Sanchez", "I\~niguez", "Fernandez", "Hernandez", "Torres", "Pel\\\'aez", "Vivar" ]

male_names_f = [ 'Juan', 'Luis', 'Carlos', 'Jos\`e', "Miguel", "Mart\\\'in" ]
female_names_f = [ 'Mar\\\'ia', 'Ana' ]


def get_name(gender):
	if randint(1,6)==1 : 
		res = choice(male_names_f) if gender=='m' else choice(female_names_f)
		res+='-'
	else :
		res = ''
	res += choice(male_names) if gender=='m' else choice(female_names)
	s = choice(surnames)
	if s[-1]=='z' or randint(1,3)==1:
		res+=' '+s
	else :
		res+=' de '+s
	if randint(1,3)==1 :
		res+=' y '+choice(surnames)
	return res

if __name__ == '__main__' :
   from sys import argv
   gender='m'
   if len(argv)>1 :
      if argv[1] in ['male', 'm', '-m'] : gender='m'
      if argv[1] in ['female', 'f', '-f'] : gender='f'
   res=get_name(gender)	 
   print (res)
