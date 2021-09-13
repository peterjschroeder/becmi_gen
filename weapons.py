#!/usr/bin/python

from random import choice
from dice import *
from config import common_weapons

w_bludgeons = [ 'Club', 'Mace', 'Warhammer', 'Throwing Hammer', 'Sling', 'Staff' ]
w_thief = [ 'Short Sword', 'Dagger', 'Blackjack', 'Short Bow', 'Sling', 'Long Bow', 'Light Crossbow', 'Long Sword', 'Hand Axe', 'Whip', 'Spear', 'Javelin' ]
w_fighter = [ 'Long Sword', 'Battle Axe', 'Halberd', 'Two Handed Sword', 'Bastard Sword', 'Pole Axe' ]
w_missile = [ 'Long Bow', 'Short Bow', 'Light Crossbow', 'Heavy Crossbow', 'Sling', 'Javelin', 'Hand Axe', 'Dagger', 'Net' ]
w_muser = [ 'Dagger', 'Staff', 'Net', 'Whip', 'Sling' ]
w_halfling = [ 'Short Sword', 'Bastard Sword', 'Dagger', 'Sling', 'Short Bow', 'Light Crossbow', 'Spear', 'Hand Axe' ]
w_dwarf = [ 'Battle Axe', 'Hand Axe', 'Light Crossbow', 'Heavy Crossbow', 'Warhammer', 'Mace', 'Throwing Hammer', 'Long Sword', 'Pole Axe' ]
w_elf = [ 'Long Sword', 'Short Sword', 'Dagger', 'Spear', 'Long Bow', 'Short Bow', 'Net' ]
w_unusual = [ 'Lance', 'Pike', 'Rapier', 'Bolas', 'Chakram', 'Six-Shooter' ]
w_rakasta = [ 'War Claws' ]
w_swords = [ 'Long Sword', 'Short Sword', 'Two Handed Sword', 'Bastard Sword' ]
w_all = list(set(w_bludgeons + w_thief + w_fighter + w_missile + w_muser + w_halfling + w_dwarf + w_elf + w_unusual ))
w_ethengar = [ 'Long Sword', 'Long Bow', 'Lance', 'Spear', 'Hand Axe', 'Bolas'] 

by_class = {
	'Horse Warrior' : w_ethengar,
	'Bratak' : w_thief,
	'Hakomon' : w_muser,
	'Fighter' : w_all,
	'Dwarf' : w_dwarf,
	'Elf' : w_all,
	'Halfling' : w_halfling,
	'Cleric' : w_bludgeons,
	'Thief' : w_thief,
	'Magic User' : w_muser,
	'Druid' : [ 'Club', 'Staff', 'Warhammer', 'Sling' ],
	'Mystic' : [ 'Chakram', 'Bullroarer Knife', 'Staff', 'Long Sword', 'Dagger', 'Spear' ],
	'Forester' : w_all,
	'Shaman' : w_swords + w_bludgeons,
        'Dervish' : w_all,
}
by_class['Bard'] = by_class['Thief']
by_class['Rake'] = by_class['Thief']
by_class['Dwarf Cleric'] = by_class['Dwarf']
by_class['Shamani'] = by_class['Druid']

weapondmg_basic = {
	'Bastard Sword' : '1d6+1/1d8+1',
	'Battle Axe' : '1d8',
	'Blackjack' : '1d2',
	'Bolas' : '1d2',
	'Club' : '1d4',
	'Dagger' : '1d4',
	'Halberd' : '1d10',
	'Hand Axe' : '1d6',
	'Heavy Crossbow' : '2d4',
	'Javelin' : '1d6',
	'Lance' : '1d10',
	'Light Crossbow' : '1d6',
	'Long Bow' : '1d6',
	'Long Sword' : '1d8',
	'Mace' : '1d6',
	'Net' : 'Entangle', 
	'Pike' : '1d10',
	'Pole Axe' : '1d10',
	'Rapier' : '2d4-1',
	'Short Bow' : '1d6',
	'Short Sword' : '1d6',
	'Sling' : '1d4',
	'Spear' : '1d6',
	'Staff' : '1d6',
	'Chakram' : '1d6',
	'Throwing Hammer' : '1d4',
	'Two Handed Sword' : '1d10',
	'War Claws' : '1d4',
	'Warhammer' : '1d6',
	'Whip' : '1d2',
	'Trident' : '1d6',
	'Cestus' : '1d3', 
	'Blowgun' : 'Poison',
	'Bullroarer Knife' : '1d6',
	'Six-Shooter' : '1d4',
}

weapondmg_skilled = {
	'Bastard Sword' : '1d6+3/1d8+3',
	'Battle Axe' : '1d8+2',
	'Blackjack' : '2d2',
	'Bolas' : '1d3',
	'Club' : '1d6+1',
	'Dagger' : '1d6',
	'Halberd' : '1d10+2',
	'Hand Axe' : '1d6+2',
	'Heavy Crossbow' : '2d6',
	'Javelin' : '1d6+2',
	'Lance' : '1d10+3',
	'Light Crossbow' : '1d6+2',
	'Long Bow' : '1d8+1',
	'Long Sword' : '1d12',
	'Mace' : '2d4',
	'Net' : 'Entangle', 
	'Pike' : '1d12+2',
	'Pole Axe' : '1d10+3',
	'Rapier' : '1d8+1',
	'Short Bow' : '1d6+2',
	'Short Sword' : '1d6+2',
	'Sling' : '1d6',
	'Spear' : '1d6+2',
	'Staff' : '1d6+2',
	'Chakram' : '1d6+2',
	'Throwing Hammer' : '1d4+2',
	'Two Handed Sword' : '2d6+1',
	'War Claws' : '1d6',
	'Warhammer' : '1d6+2',
	'Whip' : '1d4',
	'Trident' : '1d8+1',
	'Cestus' : '1d4+1', 
	'Blowgun' : 'Poison',
	'Bullroarer Knife' : '1d6+2',
	'Six-Shooter' : '1d6',
}

weapondmg_expert = {
	'Bastard Sword' : '1d6+5/1d8+5',
	'Battle Axe' : '1d8+4',
	'Blackjack' : '1d4+1',
	'Bolas' : '1d3+1',
	'Club' : '1d6+3',
	'Dagger' : '2d4',
	'Halberd' : '1d10+5',
	'Hand Axe' : '1d6+3',
	'Heavy Crossbow' : '2d6+2',
	'Javelin' : '1d6+4',
	'Lance' : '1d10+7',
	'Light Crossbow' : '1d6+4',
	'Long Bow' : '1d10+2',
	'Long Sword' : '2d8',
	'Mace' : '2d4+2',
	'Net' : 'Entangle', 
	'Pike' : '1d12+5',
	'Pole Axe' : '1d10+6',
	'Rapier' : '1d8+2',
	'Short Bow' : '1d6+2',
	'Short Sword' : '1d6+4',
	'Sling' : '2d4',
	'Spear' : '2d4+2',
	'Staff' : '1d8+2',
	'Chakram' : '1d6+4',
	'Throwing Hammer' : '1d6+2',
	'Two Handed Sword' : '2d8+2',
	'War Claws' : '1d8',
	'Warhammer' : '1d8+2',
	'Whip' : '1d4+1',
	'Trident' : '1d8+4',
	'Cestus' : '2d4', 
	'Blowgun' : 'Poison',
	'Bullroarer Knife' : '1d6+4',
	'Six-Shooter' : '2d4',
}

weapondmg_master = {
	'Bastard Sword' : '1d8+8/1d10+8 H -- 1d6+7/1d8+7 M',
	'Battle Axe' : '1d8+8 M -- 1d8+6 H',
	'Blackjack' : '1d4+3 H -- 1d6+1 M',
	'Bolas' : '1d3+2 A',
	'Club' : '1d6+5 M -- 1d4+5 H',
	'Dagger' : '3d4 H -- 2d4+2 M',
	'Halberd' : '1d8+10 H -- 1d8+8 M',
	'Hand Axe' : '2d4+4 M -- 1d6+4 H',
	'Heavy Crossbow' : '3d6+2 H -- 1d12+4 M',
	'Javelin' : '1d6+6 H -- 1d4+6 M',
	'Lance' : '1d8+12 M -- 1d8+10 H',
	'Light Crossbow' : '1d8+6 H -- 1d4+6 M',
	'Long Bow' : '3d6 M -- 1d10+4 H',
	'Long Sword' : '2d8+4 H -- 2d6+4 M',
	'Mace' : '2d4+4 A',
	'Net' : 'Entangle', 
	'Pike' : '1d12+9 H -- 1d10+8',
	'Pole Axe' : '1d10+10 H -- 1d10+8 M',
	'Rapier' : '1d12 H -- 1d10 M',
	'Short Bow' : '1d8+6 M -- 1d4+6 H',
	'Short Sword' : '1d6+7 H -- 1d4+7 H',
	'Sling' : '3d4 H -- 1d8+2 M',
	'Spear' : '2d4+4 A',
	'Staff' : '1d8+5 A',
	'Chakram' : '1d8+6 H -- 1d4+6 M',
	'Throwing Hammer' : '1d6+4 M -- 1d4+4 H',
	'Two Handed Sword' : '3d6+3 M -- 2d8+3 H',
	'War Claws' : '1d10+1 M -- 1d8+1 H',
	'Warhammer' : '1d8+5 H -- 1d6+4 M',
	'Whip' : '1d4+3 M -- 1d3+2 H',
	'Trident' : '1d8+6 M -- 1d6+6 H',
	'Cestus' : '2d4+1 H -- 1d4+3 M', 
	'Blowgun' : 'Poison',
	'Bullroarer Knife' : '2d4+4 A',
	'Six-Shooter' : '2d6 H -- 1d6+2 M',
}

weapondmg_gmaster = {
	'Bastard Sword' : '1d8+10/1d12+10 H -- 1d6+8/1d10+8 M',
	'Battle Axe' : '1d10+10 M -- 1d8+8 H',
	'Blackjack' : '1d4+5 H -- 1d6+2 M',
	'Bolas' : '1d3+3 A',
	'Club' : '1d6+6 M -- 1d4+6 H',
	'Dagger' : '4d4 H -- 3d4+1 M',
	'Halberd' : '1d6+15 H -- 1d6+12 M',
	'Hand Axe' : '2d4+7 M -- 1d6+6 H',
	'Heavy Crossbow' : '4d4+4 H -- 1d10+6 M',
	'Javelin' : '1d6+9 H -- 1d4+8 M',
	'Lance' : '1d8+16 M -- 1d6+12 H',
	'Light Crossbow' : '1d6+7 H -- 2d4+5 M',
	'Long Bow' : '4d4+2 M -- 1d10+6 H',
	'Long Sword' : '2d6+8 H -- 2d4+8 M',
	'Mace' : '2d4+6 A',
	'Net' : 'Entangle', 
	'Pike' : '1d10+14 H -- 1d8+10',
	'Pole Axe' : '1d8+16 H -- 1d8+12 M',
	'Rapier' : '1d12 H -- 1d10 M',
	'Short Bow' : '1d10+8 M -- 1d6+7 H',
	'Short Sword' : '1d6+9 H -- 1d4+9 H',
	'Sling' : '4d4 H -- 1d10+2 M',
	'Spear' : '2d4+6 A',
	'Staff' : '1d8+7 A',
	'Chakram' : '1d8+6 H -- 1d4+6 M',
	'Throwing Hammer' : '1d6+6 M -- 1d4+6 H',
	'Two Handed Sword' : '3d6+6 M -- 3d6+2 H',
	'War Claws' : '1d10+1 M -- 1d8+1 H',
	'Warhammer' : '1d8+7 H -- 1d6+7 M',
	'Whip' : '1d4+5 M -- 1d3+3 H',
	'Trident' : '1d6+9 M -- 1d4+8 H',
	'Cestus' : '3d4+1 H -- 2d4+3 M', 
	'Blowgun' : 'Poison',
	'Bullroarer Knife' : '2d4+4 A',
	'Six-Shooter' : '2d6 H -- 1d6+2 M',
}

def get_weapondmg(weapon, level):
	if   level == 'Basic'   : return weapondmg_basic[weapon]
	elif level == 'Skilled' : return weapondmg_skilled[weapon]
	elif level == 'Expert'  : return weapondmg_expert[weapon]
	elif level == 'Master'  : return weapondmg_master[weapon]
	elif level == 'Grand Master'  : return weapondmg_gmaster[weapon]
	else : return 'TBD'	

def get_weapons(cclass, race, level, origin=None):
		weapons={}
		favorite = (common_weapons[origin]+common_weapons['any']) if origin in common_weapons.keys() else common_weapons['any']
		favorite = [ x for x in favorite if x in by_class[cclass] ]
		if cclass in [ 'Fighter', 'Forester' ] :
			weapons[choice(favorite + w_fighter)]='Basic'
			weapons[choice(favorite + w_missile)]='Basic'
			if race=='Rakasta' and d6()<5 : weapons['War Claws']='Basic'
			while (len(weapons)<4) :
				weapons[choice(favorite + w_all)]='Basic'
		if cclass == 'Horse Warrior' :
			while(len(weapons)<4):
				weapons[choice(favorite+w_ethengar)]='Basic'
		if cclass in [ 'Mystic' ] :
			weapons['Cestus']='Basic'
			if race=='Rakasta' and d6()<3 : weapons['War Claws']='Basic'
			while (len(weapons)<3) :
				weapons[choice(favorite + w_all)]='Basic'			
		if cclass in [ 'Cleric', 'Druid', 'Shamani' ] :
			while (len(weapons)<2) :
				weapons[choice(favorite + w_bludgeons)]='Basic'
		if cclass in [ 'Shaman', 'Dervish' ] :
			while (len(weapons)<2) :
				weapons[choice(favorite + w_bludgeons+w_swords)]='Basic'
		if cclass in [ 'Hakomon', 'Magic User' ] :
			while (len(weapons)<2) :
				weapons[choice(favorite + w_muser)]='Basic'
		if cclass in [ 'Bratak', 'Thief', 'Bard', 'Rake' ] :
			if race=='Rakasta' and d6()<3 : weapons['War Claws']='Basic'
			while (len(weapons)<2) :
				weapons[choice(favorite + w_thief)]='Basic'
		if cclass in [ 'Dwarf', 'Dwarf Cleric' ] :
			while (len(weapons)<4) :
				weapons[choice(favorite + w_dwarf)]='Basic'
		if cclass == 'Elf' :
			while (len(weapons)<4) :
				weapons[choice(favorite + w_elf)]='Basic'
		if cclass == 'Halfling' :
			while (len(weapons)<4) :
				weapons[choice(favorite + w_halfling)]='Basic'
		for l in range(1, level+1):
			if (cclass in [ 'Halfling', 'Elf', 'Dwarf', 'Dwarf Cleric', 'Forester' ] and l%4==0) or (cclass not in [ 'Halfling', 'Elf', 'Dwarf', 'Dwarf Cleric', 'Forester' ]  and l%3==0) :
				i = choice(weapons.keys()) if d6()<5 else choice(favorite+by_class[cclass])
				if i not in weapons.keys() : 
					weapons[i]='Basic' if cclass not in [ 'Halfling', 'Elf', 'Dwarf', 'Dwarf Cleric' ] else 'Skilled'
				elif weapons[i]=='Master' : weapons[i]='Grand Master'
				elif weapons[i]=='Expert' : weapons[i]='Master'
				elif weapons[i]=='Skilled' : weapons[i]='Expert'
				elif weapons[i]=='Basic' : weapons[i]='Skilled'
				
		return weapons


if __name__ == '__main__' :
	for w in weapondmg_basic.keys():
		print ('{:20} {:12} {:12} {:12} {:20} {:20}'.format(w, get_weapondmg(w,'Basic'), get_weapondmg(w,'Skilled'), get_weapondmg(w,'Expert'), get_weapondmg(w,'Master'), get_weapondmg(w,'Grand Master')))
