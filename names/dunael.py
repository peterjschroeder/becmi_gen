#!/usr/bin/python
from random import choice, randint

male_names = [ "Cormac", "Donegal", "Connor", "Duncan", "Bruce", "Bran", "Malcolm", "Donall", "Conall", "Eachain", "Finnegar", "Lunn", "Dylan", "Penn", "Crinan", "Malmore", "Dunmail", "Godric", "Kenneth", "Brian", "Farquhar", "Fergus", "Angus", "Finnlaech", "Lulach", "Oengus", "Maldred", "Neil", "Domangart", "Alpin", "Fingal", "Fingan", "Lachlan", "Ossian", "Ringan", "Teague", "Torquil" ]

female_names = [ "Deirdre", "Fenella", "Fiona", "Branwenn", "Bethoc", "Olith", "Eithne", "Derborgaill", "Finnguala", "Ela", "Muirgaill", "Gruoch", "Eithne", "Fergusa", "Keyne", "Callwen", "Donwen", "Eimhir", "Ailis", "Bride", "Kenna", "Malvina", "Una", "Morag", "Mildred" ]


def get_name(gender):
	res = choice(male_names) if gender=='m' else choice(female_names)
	res+=' mac' if gender=='m' else ' nic'
	res+=' '+choice(male_names)
	return res

if __name__ == '__main__' :
   from sys import argv
   gender='m'
   if len(argv)>1 :
      if argv[1] in ['male', 'm', '-m'] : gender='m'
      if argv[1] in ['female', 'f', '-f'] : gender='f'
   res=get_name(gender)	 
   print res
