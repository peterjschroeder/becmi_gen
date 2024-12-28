#!/usr/bin/python

basic_spells = set([ 'Detect Magic', 'Read Magic' ])

spell_lists = {
	
}

from spellbooks.generic import spells as generic_spells
spells = generic_spells

from random import choice
from dice import *
from copy import copy

def set_spell_list(region, origin):
	global spells
	from importlib import import_module
	try : 
		m = import_module('spellbooks.'+spell_lists[region,origin])
		spells = m.spells
		return
	except Exception as e: print ('failed to load spells', e)
	from string import lower
	norm_origin = lower(origin)
	norm_region = lower(region)
	# Replace ' ' with '_'
	import re
	p=re.compile(' ')
	norm_origin = p.sub('_',norm_origin)
	norm_region = p.sub('_',norm_region)
	# Try loading from origin
	try : 
		m = import_module('spellbooks.'+norm_origin)
		spells = m.spells
		return 
	except Exception as e: print ('failed to load spells', e)
	try : 
		m = import_module('spellbooks.'+norm_region)
		spells = m.spells
		return
	except Exception as e: print ('failed to load spells', e)
	print ('failed to load spells from any source, falling back to generics')

def get_spellbook(cclass, level):
	spellbook = { }
	spellbook[1] = copy(basic_spells)
	for l in range(1,level+1):
		if l==1 :
			spellbook[1]|=set([choice(list(spells[1]-spellbook[1]))])
			spellbook[1]|=set([choice(list(spells[1]-spellbook[1]))])
		elif l==2 :
			try :
				spellbook[1]|=set([choice(list(spells[1]-spellbook[1]))])
			except IndexError :
				print (spells)
				print (spellbook)
		elif l==3 :
			spellbook[2]=set([choice(list(spells[2]))])
		elif l==4 :
			spellbook[2]|=set([choice(list(spells[2]-spellbook[2]))])
		elif l==5 :
			spellbook[3]=set([choice(list(spells[3]))])
		elif l==6 :
			spellbook[3]|=set([choice(list(spells[3]-spellbook[3]))])
		elif l==7 :
			spellbook[4]=set([choice(list(spells[4]))])
			spellbook[1]|=set([choice(list(spells[1]-spellbook[1]))])
		elif l==8 :
			spellbook[4]|=set([choice(list(spells[4]-spellbook[4]))])
			spellbook[2]|=set([choice(list(spells[2]-spellbook[2]))])
		elif l==9 :
			spellbook[5]=set([choice(list(spells[5]))])
			spellbook[3]|=set([choice(list(spells[3]-spellbook[3]))])
		elif l==10 :
			spellbook[5]|=set([choice(list(spells[5]-spellbook[5]))])
			spellbook[4]|=set([choice(list(spells[4]-spellbook[4]))])
		elif l==11 :
			spellbook[6]=set([choice(list(spells[6]))])
			spellbook[1]|=set([choice(list(spells[1]-spellbook[1]))])
		elif l==12 :
			spellbook[2]|=set([choice(list(spells[2]-spellbook[2]))])
			spellbook[3]|=set([choice(list(spells[3]-spellbook[3]))])
		elif l==13 :
			spellbook[6]|=set([choice(list(spells[6]-spellbook[6]))])
		elif l==14 :
			spellbook[4]|=set([choice(list(spells[4]-spellbook[4]))])
			spellbook[5]|=set([choice(list(spells[5]-spellbook[5]))])
	if level>15 and cclass != 'Elf' : print ('Spellbooks over level 15 not supported')
	return spellbook

if __name__ == "__main__" :
	from sys import argv
	level=int(argv[1]) if len(argv)>1 else 1
	s = get_spellbook('Elf', level)
	l=s.keys()
	l=sorted(l)
	for i in l :
		print (i, s[i])
 
