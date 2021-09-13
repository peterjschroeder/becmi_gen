#!/usr/bin/python

from dice import *

def get_age(race, level):
	if   race=='Human' : return 14+(level/2) + d10(2) + (0 if d6()<3 else d10())
	elif race=='Dwarf' : return 16+(level*2) + d10(3) + (0 if d6()<6 else d10(2))
	elif race=='Halfling' : return 16+ level + d10(4) + (0 if d6()<5 else d10(3))
	elif race=='Elf'   : return 20+(level*4) + d10(6) + (0 if d6()<6 else d10(4))
	elif race=='Lupin' : return 15+(level/2) + d10(2) + (0 if d6()<3 else d10())
	elif race=='Rakasta' : return 14+(level/2) + d8(2) + (0 if d6()<3 else d10())
	else : return 20+d10(3)
