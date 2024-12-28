#!/usr/bin/python
from random import choice, randint

if __name__=='__main__' :
	import sys
	sys.path.append("..")
from dice import d6, d10

front = [ 'Bal', 'Belf', 'Bif', 'Bol', 'Bomb', 'D', 'Dor', 'Dorf', 'Dur', 'Dwal', 'Far', 'Fil', 'Gil', 'Glo', 'Gor', 'Kon', 'Kor', 'Kur', 'Lyr', 'Mor', 'Na', 'No', 'Nor', 'O', 'Or', 'Thor', 'Thra', 'Tor', 'Thro', 'Whar', ]

prefix = ['Dran', 'Dras', 'Jur', 'Jyr', 'Kher', 'Kur', 'Lem', 'Lum', 'Mol', 'Nur', 'Syr', 'Tyr', 'Wan',]

suffix_male = [ 'dehk', 'dul', 'dyn', 'egk', 'gyr', 'lak', 'mehr', 'neg', 'nohk', 'rak', 'uld', ]
suffix_female = [ 'dah', 'dri', 'ehr', 'gid', 'vid', ]

nicknames = [ "Orcslayer", "Fire-eye", "Cliffscaler", "Longbeard", "Redhand", "Blackbrow", "Rockcutter", "Goblinsbane", "Manfriend", "Elf-friend", "Songsmith", "Bloodaxe", "Bluetooth", "Forkbeard", "Blackheart", "Hardmouth", "Ironside", "Silkbeard", "Skullsplitter"  ]

surname = ['blys','bol','buhr','den','dwal','eft','est','far','fil','fotar','gardar','hraken','hruk','hur','hurgon','hwyr','jhyr','karats','ker','kon','kor','kres','lin','list','mor','mur','or','puhn','pyr','rad','radas','rak','rast','rutar','shyld','skyr','smag','stahl','syhar','syr','tar','tor','tordar','toren','torrad','warf','wyr']

clan = ['Felwig','Hurgon','Karlheig','Yardrak',]

def get_family_name(back):
	res = choice(front) 
	if d6()<4 :
		res+= choice(back)
	res+= choice(surname)
	return res
	

def get_patronym(gender):
	#pat='daughter of ' if gender=='f' else 'son of '
	
	back=back_female if gender=='f' else back_male	
	pat=choice(front) + choice(back) + 'warf'
	
	return pat


def get_name(gender):
	back=suffix_female if gender=='f' else suffix_male
	res = choice(front) + choice(back)
	
	#if d6()<2 :
	#	res+=' "'+choice(nicknames)+'"'
	#res+=' '
	
	#res+=get_patronym(gender)
	
	# there should be a chance here to be of the main family branch (using the clan name as family name)
	#if d10()<8 :
	#	res+=' ' + get_family_name(back)
	
	res+=' of Clan ' + choice(clan)
		
	return res



if __name__ == '__main__' :
   from sys import argv
   if len(argv)>1 :
      if argv[1] in ['male', 'm', '-m'] : gender='m'
      if argv[1] in ['female', 'f', '-f'] : gender='f'
   res=get_name(gender)	 
   print (res)
