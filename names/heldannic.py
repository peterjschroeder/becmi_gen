#!/usr/bin/python
from random import choice, randint

if __name__=='__main__' :
	import sys
	sys.path.append("..")
from dice import d6

male_names = [ "Alban", "Albrecht", "Alfons", "Ansgar", "Anton", "Armin", "Arndt", "Arnold", "Artur", "Barnabas", "Benedikt", "Bernd", "Burkhard", "Detlef", "Diederick", "Dieter", "Dietrich", "Eberhard", "Eckhard", "Edmund", "Egon", "Elias", "Emmerich", "Engel", "Engelbert", "Erich", "Erwin", "Ewald", "Fabian", "Franz", "Friedemann", "Friedhelm", "Friedrich", "Fritz", "Georg", "Gerhardt", "Gottfried", "Gregor", "Gunther", "Gustaff", "Hans", "Harald", "Hartmann", "Hartwig", "Heinrich", "Heinz", "Helmut", "Hermann", "Hilbert", "Hildebert", "Horst", "Hubert", "Hugo", "Ingolf", "Jakob", "Jan", "Johann", "J\\\"org", "Josef", "J\\\"urgen", "Karl", "Karlmann", "Kaspar", "Klaas", "Klaus", "Konrad", "Kurt", "Lamprecht", "Linus", "Lothar", "Ludger", "Ludwig", "Luitger", "Luitpold", "Lukas", "Lutz", "Manfred", "Mattias", "Maximilian", "Norbert", "Olaf", "Oral", "Ortwin", "Oskar", "Otto", "Pankraz", "Raimund", "Rainer", "Reinhold", "Rolf", "Ruediger", "Rudolf", "Severin", "Siegbert", "Siegmund", "Silvester", "Thomas", "Ulrich", "Utz", "Viktor", "Walter", "Wendel", "Werner", "Wolfgang", "Wolfram" ]

female_names = [ "Agnes", "Alena", "Amalia", "Andrea", "Anna", "Annelie", "Ava", "Barbara", "Beatrix", "Bertha", "Brunhilde", "Dietlinde", "Dorothea", "Ebba", "Edith", "Elfriede", "Elisa", "Elsa", "Emilie", "Erika", "Ermentraude", "Eva", "Felicie", "Flora", "Frauke", "Frieda", "Gerda", "Gertud", "Gitta", "Greta", "Gretchen", "Gretel", "Gudrun", "Hanna", "Hedwig", "Heidi", "Helga", "Helmine", "Hertha", "Hilda", "Hildegard", "Ida", "Ilsa", "Inge", "Ingrid", "Johanna", "Jutta", "Karin", "Karla", "Karoline", "Katrina", "Klara", "Kora", "Krimhilde", "Krista", "Lara", "Lea", "Luise", "Luitgard", "Lydia", "Lysanne", "Magdalene", "Monika", "Natalie", "Nina", "Nora", "Renata", "Roswitha", "Sandra", "Silke", "Suse", "Swanhild", "Theresa", "Trudi", "Ursula", "Viktoria", "Wilma" ]

surnames = [ "L\\\"owe", "Vogel", "Hammer", "Weide", "Grauenberg", "Klagendorf", "Erstenlicht", "Blutfelden", "Hundkopf", "Liebknecht", "Schwarzenegger", "Osterhaus", "Stamhoffer", "Adler", "Bismark", "Bohr", "Luger", "Weill", "Hendriks", "Schmidt", "Gottfried", "Hohenhaus", "Himmelbrand", "Pfefferlind", "Stahlfaust", "Feuergeist", "Meinhard", "Wilhiem", "Heldring", "Degensinger", "Strauss", "Donnerschlag", "Himmerstein", "Strand", "Kindelbaum", "Holmstein", "Grauwald", "Grauenberg",  "Scharnheim", "Morgenhammer", "Goldzig", "Totenfuss", "Einaugen", "Riesenstein", "Adalard", "Thargau", "Eisenturm", "Hockstein", "Altendorf", "Spielberg", "Pflanzen", "Friedemann", "Wolfram", "Beck", "Severin", "Karlmann", "Hartmann", "Hartwig", "Burkhard", "Eberhard", "Eckhard", "B\\\"ottcher", "Schneider", "Schuster", "M\\\"uller", "Fischer", "K\\\"urschner", "Sch\\\"afer" ]

def get_name(gender):
	res = choice(male_names) if gender=='m' else choice(female_names)
	if d6() < 2 :
		res+=' von'
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
