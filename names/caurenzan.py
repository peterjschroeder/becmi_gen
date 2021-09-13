#!/usr/bin/python
from random import choice, randint

male_names = [ 'Agostino', 'Innocenti', 'Baldassarre', 'Camillo', 'Orlando', 'Flaminio', 'Borso', 'Jacopo', 'Ottone', 'Galeotto', 'Manfredo', 'Tiberio', 'Antonio', 'Corrado', 'Giulio', 'Astolfo', 'Bernab\\`o', 'Antonio', 'Corrado', 'Luchino', 'Lapo', 'Lupo', 'Griseo', 'Guiscarda', 'Azzo', 'Ranuccio', 'Odoardo', 'Ghiaio', 'Ferruccio', 'Cesare', 'Lamberto', 'Ildebrando', 'Manente', 'Braccio', 'Brando', 'Muzio', 'Ezzelino', 'Mosca', 'Schiatta', 'Cesare', 'Azzone', 'Nico\\`o', 'Ugo', 'Vincenzo', 'Falco', 'Galeotto', 'Obizzo', 'Oberto', 'Rinaldo', 'Ascanio', 'Leonello', 'Leone', 'Ippolito', 'Ercole', 'Aldobrando', 'Contardo', 'Almerico', 'Folco', 'Salinguerra', 'Cavalcante', 'Alighiero', 'Adalberto', 'Aleramo', 'Tedisio', 'Cacciaguida', 'Brunetto', 'Bonifazio', 'Scipione', 'Giovanni', 'Galeazzo', 'Ludovico', 'Ottavio', 'Ottaviano', 'Guido', 'Bonifacio', ]

female_names = [ 'Vittoria', 'Laura', 'Altachiara', 'Marzia', 'Bella', 'Concordia', 'Ginevra', 'Melchina', 'Berta', 'Elisa', 'Lucrezia', 'Bona', 'Beatrice', 'Vanna', 'Vannozza', 'Giulia', 'Eleonora', 'Cecilia', 'Costanza', 'Cassandra', 'Bianca', 'Elena', 'Caterina', 'Isabella', 'Matilde', 'Giovanna', 'Ippolita', 'Rosabianca', 'Ludovica', 'Livia', 'Drusiana', 'Polissena', 'Viola', 'Gualandra', 'Adriana', 'Fiamma', 'Filippa', 'Violante', 'Margherita', 'Lucia', 'Anna', 'Flora', 'Camilla' ]

surnames = [ 'Patrizio', 'dal Pozzo', 'degli Arcani', 'di Malapietra', 'da Oreggiano', 'del Balzo', 'degli Oberti', 'degli Ippoliti', 'de\' Bracci', 'da Verazzano', 'Finiberti', 'Fulvina', 'da Polenta', 'da Grolla', 'di Cajoli', 'Zeula', 'dei Gusberti', 'da Traviale', 'Odilone', 'dei Ciacchi', 'Alfieri', 'da Traversara', 'da Montacuto', 'da Nesci', 'da Padula', 'degli Speziali', 'di Randazzi', 'degli Amidei', 'Fifanti', 'Lupi', 'dei Lamberti', 'dei Cavalcanti', 'di Sfonti', 'da Petraja', 'Ottaviani', 'Flachi', 'da Nesci', 'Menescaldi', 'da Scarvento', 'di Tarento', 'Leoni', 'Aldobrandi', 'Ildebrandi', 'Bozzolo', 'Novellara', 'Rinaldi', 'degli Ezzelini', 'di Corenveni', 'd\'Ascioti', 'Guidi' ] 

male_names_f = [ 'Gian', 'Pier' ]
female_names_f = [ '' ]

def get_name(gender):
	if randint(1,6)==1 and gender=='m': 
		res = choice(male_names_f)
		res+='-'
	else :
		res = ''
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
