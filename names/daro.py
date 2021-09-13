#!/usr/bin/python
from random import choice, randint

if __name__=='__main__' :
	import sys
	sys.path.append("..")
from dice import d6

male_names = [ 'Aden', 'Ansel', 'Mithras', 'Santhral', 'Charles', 'Corwyn', 'Rypien', 'Vardon', 'Atwell', 'Wilhon', 'Arturo', 'Eshram', 'Kalafi', 'Tahir', 'Allen', 'Mendel', 'Bertram', 'Sasheme', 'Greenleaf', 'Lucius', 'Henry', 'Jons', 'Millington', 'Reynard', 'Derek', 'Anders', 'Wesley', 'Quint', 'Roger', 'Francino', 'Boris', 'Davon', 'Eldram', 'Tomas', 'Simon', 'Clement', 'Avral', 'Morgan', 'Filip', 'Raymund', 'Allen', 'Vernon', 'Dafford', 'Randel', 'Rundel', 'Ceolfed', 'Ioric', 'Korlim', 'Corinn', 'Haldmun', 'Haralan', 'Harenel', 'Iolan', 'Lorren', 'Orren', 'Tohm', 'Aron', 'Arthon', 'Harathan', 'Indol', 'Kareth', 'Rindall', 'Tybalt', 'Rithen', 'Darius', 'Maros', 'Tomes', 'Astinius', 'Calen', 'Aldon', 'Rarold', 'Reginald', 'Falstair', 'Arnad', 'Aeren', 'Doran', 'Harel', 'Emilio', 'Edgar', 'Brin', 'Filibar', 'Grindolf', 'Niall', 'Oakleaf', 'Geraint', 'Rolph', 'Hugh', 'Arnulf', 'Wolfram', 'Jocko', 'Davvi', 'Herek', 'Xavier', 'Johannes', 'Anselm', 'Merdith', 'Delbert', 'Ferdibor', 'Enzo', 'Dorn', 'Jason', 'Olaf', 'Dominick', 'Quintus', 'Murr', ]

female_names = [ 'Lydia', 'Natalie', 'Elissa', 'Matrissa', 'Ruthera', 'Maggie', 'Millana', 'Cassandra', 'Sharlissa', 'Emilia', 'Ellisa', 'Jamila', 'Allana', 'Sarah', 'Corinna', 'Ara', 'Artha', 'Martha', 'Rindala', 'Santha', 'Mara', 'Vetha', 'Myra', 'Lystra', 'Adena', 'Iolanna', 'Lowetha', 'Tohma', 'Sanda', 'Ansa', 'Lyasa', 'Lillana', 'Dora', 'Scrutina', 'Estella', 'Lillian', 'Hilda', 'Dulcet', 'Dina', 'Oleena', 'Mellisandre', 'Marlys' ] 

surnames = [ 'Hoff', 'Kalimi', 'Mauntea', 'Hallonica', 'Vickers', 'Attleson', 'Page', 'Consortia', 'Al-Azrad', 'Franich', 'Corun', 'Callister', 'Linton', 'Pennydown', 'Bancohr', 'Ithel', 'Brandifirth', 'Vonaday', 'Varsho', 'Vanisi', 'Pounder', 'Arorat', 'Wocken', 'Bostitch', 'Tremontaine', 'Sagar', 'Falstead', 'Staffleheim', 'Mendel', 'Rand', 'Hundley', 'Miggs', 'LeDouce', 'Stone', 'Grey', 'Ramsey', 'Weston', 'Argyle', 'Ansimont', 'Tydian', 'Lorenson', 'Randelson', 'Corinson', 'Allenson', 'Ioricson', 'Cranor', 'Ithel', 'Ardel', 'Corran', 'Iolanson', 'Tohmson', 'Arthonson', 'Sashell', 'Taidar', 'Elstar', 'Strellard', 'Lynnwith', 'Galadin', 'Bentilun', 'Fadon', 'Trest', 'Eskarden', 'Petriu', 'Karethson', 'Conwyn', 'Arkari', 'Diaura', 'Whitehall', 'Donthiir', 'Duchamp', 'Bramble', 'Kosseauf', 'Green', 'Plowshare', 'Longfurrow', 'Hornscraper', 'Dalewander', 'Sweetsong', 'Alesworthy', 'Dalberry', 'Longwalker', 'Darkspell', 'Quickblade' ] 

def get_name(gender):
	res = choice(male_names) if gender=='m' else choice(female_names)
	res+= ' '+ choice(surnames)
	return res

if __name__ == '__main__' :
   from sys import argv
   gender='m'
   if len(argv)>1 :
      if argv[1] in ['male', 'm', '-m'] : gender='m'
      if argv[1] in ['female', 'f', '-f'] : gender='f'
   res=get_name(gender)	 
   print res
