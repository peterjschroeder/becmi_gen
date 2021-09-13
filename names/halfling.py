#!/usr/bin/python
from leeha import *

clans = [ 'Dustyboots', 'Gallidox', 'Darkeyes', 'Greybeard', 'Littlelaughs', 'Seaeyes', 'Belchiir', 'Coppertoes', 'Astlar', 'Dundershields', 'Jollybars', 'Lollos', 'Longwinkle', 'Hillhallow', 'Mulgor', 'Fernshiver', 'Nixnoddle', 'Raggedleap', 'Tumblebrook', 'Boldnose', 'Hoefurrow', 'Rallytongue', 'Shindlewood', 'Alehill', 'Trundlestump', 'Bristlebur', 'Streamford', 'Treeshadow', 'Belnoise', 'Mouldwalk', 'Proudstride', 'Quizzinglas', 'Vindlewalk', 'Woodword', 'Brambleshun', 'Littleglad', 'Woodgrott', 'Elintel', 'Hairytoes', 'Forestfar', 'Kittledance', 'Lamintar', 'Whisperrun', 'Cindertoes', 'Deepdell', 'Gullybuck', 'Ilingall', 'Pytchplume', 'Summergarth', 'Dappleglade', 'Mistwalker', 'Heartwood', 'Hardflask', 'Idelwise', 'Niblefoot', 'Knackwell', 'Nudgestone', 'Yollershield', 'Vailswash', 'Horsetail', 'Pipesmoke', 'Foxhollow', 'Omblestaff', 'Zindlestone', 'Voluteye', 'Stormweather', 'Darkforest', 'Ogglemurk', 'Wanderfence', 'Flintfoot', 'Janthobell', 'Longquaff', 'Nogknock', 'Plodmoot', 'Roughleap', 'Slowleaf', 'Longbottom' ]

def get_name(gender):
	res = get_base_name(gender)
	res+= ' son of ' if gender=='m' else ' daughter of '
	res+= get_base_name()
	res+= ' ' + choice(clans)
	return res

if __name__ == '__main__' :
   from sys import argv
   if len(argv)>1 :
      if argv[1] in ['male', 'm', '-m'] : gender='m'
      if argv[1] in ['female', 'f', '-f'] : gender='f'
   res=get_name(gender)	 
   print res
