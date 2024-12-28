#!/usr/bin/python
from random import choice, randint

male_names = [ "Bartolomeu", "Dinis", "Sebasti\~ao", "Jos\\\'e", "Ant\\\'onio", "Manuel", "Jo\~ao", "Carlos", "Ricardo", "Henrique", "Paulo", "Miguel", "Sancho", "Afonso", "Pedro", "Fernando", "Lu\\\'is", "Nuno", "Filipe", "Jorge", "Duarte", "Jaime", "Teod\\\'osio", "J\\\'ulio", "\\\'Alvaro", "Fern\~ao", "Diogo", "Rodrigo", "Gon\c{c}alo", "Leonel", "Vasco", "Louren\c{c}o", "Guilherme", "Marcelo", "Paio", "Gil", "Gaspar", "Martim", "Mem", "Egas", "Soeiro", "Gomes", "Lopo", "Rafael", "Trist\~ao" ]

female_names = [ "Maria", "Domin\\\'ica", "Sancha", "Catarina", "Augusta", "Vit\\\'oria", "Am\\\'elia", "Beatriz", "Iria", "Leonor", "Mariana", "Violante", "Teresa", "Isabel", "Rosa", "Filipa", "Elvira", "Gontinha", "Madalena", "Margarida", "Mafalda", "Constan\c{c}a", "Branca", "Dulce", "Urraca", "M\\\'ecia", "In\^es", "Aldon\c{c}a", "Joana", "Lu\\\'isa", "Louren\c{c}a" ]

surnames = [ "Pereira", "\\\'Alvares", "Gon\c{c}alves", "Rodrigues", "Coutinho", "Casal", "Vilanova", "Sousa", "Menezes", "Esteves", "Gil", "Martins", "Gomes", "Fernandes", "Almeida", "Henriques", "Carvalho", "Vasques", "Peres", "Coronado", "Lopes", "Lima", "Costa", "Alvim", "Lara", "Borges", "Ribeira", "Pinto", "Silva", "Oliveira", "Mata", "Mendes", "Nunes", "Pires", "Horta", "Soares", "Coelho", "Le\~ao", "Teles", "Sanches", "Machado", "Melo", "Riba", "Paiva", "Giraldes", "Barroso", "Freire", "Lobeira", "Dinis", "Aguiar", "Abreu", "Alves", "Andrade", "Aranha", "Barbosa", "Campos", "Castelo", "Cunha", "Dias", "Domingues", "Duarte", "Esteves", "Falc\~ao", "Fragoso", "Lagos", "Leite", "Luz", "Macedo", "Mendo\c{c}a", "Monteiro", "Moura", "Nobre", "Palma", "Pedroso", "Ramos", "Reis", "Ribas", "S\\\'a", "Souto", "Teixeira", "Teves", "Veiga", "Veloso", "Vilalobos", "Peixe", "Caldeira", "Cardoso", "Antunes" ]

male_names_f = [ 'Jo\~ao', 'Lu\\\'is', 'Rui', 'Jos\\\'e', "Manuel", "Pedro" ]
female_names_f = [ 'Mar\\\'ia', 'Ana' ]


def get_name(gender):
	if randint(1,6)==1 : 
		res = choice(male_names_f) if gender=='m' else choice(female_names_f)
		res+=' '
	else :
		res = ''
	res += choice(male_names) if gender=='m' else choice(female_names)
	s = choice(surnames)
	if s[-1]=='s' or randint(1,3)==1:
		res+=' '+s
	else :
		res+=' de '+s
	if randint(1,3)==1 :
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
