#!/usr/bin/python
from random import choice, randint

if __name__=='__main__' :
	import sys
	sys.path.append("..")
from dice import d6

male_names = [ "Aki", "Alf", "Alfgeir", "Alrik", "Amundi", "Anskar", "Arinbjorn", "Armod", "Arnfinn", "Armgrim", "Arni", "Arnlaug", "Arnulf", "Asgrim", "Askold", "Askr", "Bergthor", "Bjarni", "Bjorn", "Bodvar", "Bork", "Borolf", "Brand", "Brynjolk", "Bunnbjorn", "Egil", "Eilif", "Einar", "Eindrini", "Eirik", "Eldgrim", "Erik", "Erlend", "Erling", "Eyjolf", "Eystein", "Eyvind", "Fhorgeir", "Finn", "Finnbogi", "Fjolnir", "Floki", "Flosi", "Geir", "Geirmund", "Geirstein", "Gest", "Gilli", "Glum", "Godfred", "Grani", "Gudmund", "Gunnbjorn", "Gunnlaug", "Hafgrim", "Haki", "Hakon", "Halfdan", "Halldor", "Hallfred", "Harald", "Harek", "Hastein", "Hauk", "Havard", "Hedin", "Helgi", "Hemming", "Hengist", "Herijar", "Herjolf", "Hjalti", "Hjort", "Hogni", "Holgi", "Hord", "Horik", "Hormstein", "Horsa", "Hoskuld", "Hrafn", "Hrapp", "Hrethel", "Hring", "Hroald", "Hrolf", "Hrut", "Hrothgar", "Illugi", "Ingald", "Ingjald", "Ingi", "Ivar", "Kalf", "Kari", "Karl", "Ketil", "Knut", "Knute", "Kolbein", "Kolskegg", "Lambi", "Ljot", "Ljotolf", "Lodin", "Mord", "Njal", "Odd", "Ofeig", "Ogmund", "Olaf", "Olvir", "Onund", "Orm", "Otkel", "Ottar", "Ragnar", "Rhorleif", "Rhorvald", "Ragnvald", "Rollo", "Rorik", "Runold", "Runolf", "Rurik", "Saemund", "Sighvat", "Sigmund", "Sigred", "Sigrid", "Sigurd", "Sigvaldi", "Skamkel", "Snorri", "Solmund", "Solvi", "Starkad", "Stein", "Steinthor", "Svan", "Svein", "Sven", "Svart", "Thjodolf", "Thjostolf", "Thorarin", "Thorbjorn", "Thorbrand", "Thord", "Thorfinn", "Thorgeir", "Thorgest", "Thorgils", "Thorgrim", "Thorhall", "Thorkell", "Thormund", "Thorvald", "Thorstein", "Tosti", "Ubbi", "Ulf", "Vagn", "Valgard", "Vandrad", "Vermund", "Vestein", "Vigfus", "Ynvar" ]

female_names = [ "Algifu", "Alfdis", "Althild", "Bera", "Astrid", "Gerloe", "Elsa", "Elva", "Erika", "Dotta", "Brynhild", "Bergthora", "Grimhilda", "Gunnhild", "Gudris", "Gudrun", "Gydi", "Halldis", "Hallfrid", "Hallgerd", "Halveig", "Helga", "Herdis", "Hild", "Hildigunn", "Hlif", "Hrefna", "Hrodyn", "Ingibjorg", "Ingigred", "Ingirid", "Ingunn", "Jorunn", "Katla", "Ragna", "Ragnhild", "Rannveig", "Rhora", "Siglinde", "Sigrid", "Svala", "Thjohild", "Thora", "Thordis", "Thorfinna", "Thorgunna", "Thorhalla", "Thyra", "Tovi", "Unn", "Volgerd", "Yrsa" ]

nicknames = [ "Bag-Nose", "Bare-legs", "the Black", "Bloodaxe", "Blue-Tooth", "Cod-Biter", "Flat-Nose", "Forkbeard", "Goat-Shoe", "Halftroll", "Hard-Mouth", "Hard-Sailer", "Hare-Foot", "Horse-Head", "Iron-Side", "Long-Leg", "Serpent-Tongue", "Silk-Beard", "Skull-Splitter", "Swift-Sailer", "Paunch-Shaker", "Pin-Leg", "War-Tooth", "Wry-Mouth", "Wry-Neck", "the Bitter", "the Candle", "the Clerk", "the Crow", "the Deep-Minded", "the Dueler", "the Easterner", "the Fat", "the Fecund", "the Fisher", "the Flayer", "the Fool", "the Fosterer", "the Gentle", "the Golden", "the Good", "the Grey", "the Hairy", "the Hoak", "the Huntsman", "the Mighty", "the Old", "the Pale", "the Peaceful", "the Peacock", "the Pious", "the Powerful", "the Priest", "the Quiet", "the Rascal", "the Raven", "the Red", "the Seal", "the Shabby", "the Short", "the Slender", "the Stone", "the Stout", "the Strong", "the Stubborn", "the Unruly", "the Wealthy", "the White", "the Wild", "the Young" ]

def get_name(gender,use_nicknames=False):
	res = choice(male_names) if gender=='m' else choice(female_names)
	if d6() < 2 and use_nicknames :
		res+=' '+choice(nicknames)
	else :
		res+=' '+choice(male_names)
		res+='sson' if gender=='m' else 'sdottir'
	return res

if __name__ == '__main__' :
   from sys import argv
   gender='m'
   if len(argv)>1 :
      if argv[1] in ['male', 'm', '-m'] : gender='m'
      if argv[1] in ['female', 'f', '-f'] : gender='f'
   res=get_name(gender, True)	 
   try:
       print (res)
   except Exception :
       print ('Sorry, accented i or y not available...')
       print (res.encode('ascii','replace'))
