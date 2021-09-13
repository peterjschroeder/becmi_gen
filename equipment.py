basic_3 = { "Large sack": 1, "Waterskin" : 1 }
basic_12 = { "Backpack": 1, "Waterskin" : 2, "Normal Rations" : 1 }

general_6 = [ { "Small sack": 4, "Iron Spike": 12, "50' Rope" : 1 },
{ "Large sack": 2, "Torch" : 6, "10' Pole" :1  },
{ "Large sack": 1, "Iron Spike": 12, "Small Hammer" : 1 } ]

general_25 = [ { "Lantern" : 1, "Oil Flask" : 3, "Tinderbox" : 1, "Mirror" : 1 }, 
{ "Grappling Hook"   : 1 },
{ "Holy Water (Vial)": 1 } ]

armor = [ 'Shield', 'Leather armor', 'Scale armor', 'Chain armor', 'Banded armor', 'Plate armor' ]

other_items = { "50' Rope" : 1, "Tinderbox" : 3, "Holy Water (Vial)": 25, 'Oil Flask' : 2, 'Mule with saddle bags' : 35, 'Pony with saddle' : 60, 'Garlic' : 5, 'Wolfsbane' : 10, 'Wineskin' : 2, 'Clothes, middle class' : 5, 'Clothes, fine' : 20, 'Clothes, extravagant' : 50, 'Riding Horse (with saddle and saddle bags)' : 105, 'War Horse (with saddle and saddle bags)' : 280, 'Sailing Boat' : 2000, 'Square Keep' : 75000, 'Tower' : 30000, 'Castle' : 250000, 'Longship' : 15000, 'War Galley': 60000, 'Small Sailing Ship' : 20000 }

weaponcosts = {
	'Bastard Sword' : 15,
	'Battle Axe' : 7,
	'Blackjack' : 5,
	'Bolas' : 5,
	'Club' : 3,
	'Dagger' : 3,
	'Halberd' : 7,
	'Hand Axe' : 4,
	'Heavy Crossbow' : 61,
	'Javelin' : 1,
	'Lance' : 10,
	'Light Crossbow' : 41,
	'Long Bow' : 46,
	'Long Sword' : 10,
	'Mace' : 5,
	'Net' : 5, 
	'Pike' : 3 ,
	'Pole Axe' : 5,
	'Rapier' : 10,
	'Short Bow' : 31,
	'Short Sword' : 7,
	'Sling' : 3,
	'Spear' : 3,
	'Staff' : 5,
	'Chakram' : 5,
	'Throwing Hammer' : 4,
	'Two Handed Sword' : 15,
	'War Claws' : 10,
	'Warhammer' : 5,
	'Whip' : 10,
	'Trident' : 5,
	'Cestus' : 5, 
	'Blowgun' : 6,
	'Bullroarer Knife' : 10,
	'Six-Shooter' : 100,
}

armored_class = [ 'Fighter', 'Cleric', 'Dwarf', 'Dwarf Cleric', 'Elf', 'Halfling', 'Forester', 'Horse Warrior' ]
light_class = [ 'Thief', 'Bard', 'Druid', 'Shaman', 'Dervish', 'Shamani', 'Bratak' ]
unarmored_class = [ 'Mystic', 'Magic User', 'Hakomon' ]

from random import choice
from dice import d6

def get_cost_max_min(weapons):
	'''Returns the less costly and most costly weapon in the set'''
	d = { w : weaponcosts[w] for w in weapons }
	s = sorted(d, key=lambda k: d[k])
	return s[0], s[-1]

def get_equipment(cclass, weapons, money):
	res = {}
	# Fix class-specific needs
	if cclass in [ 'Thief', 'Bard', 'Rake', 'Bratak' ] : 
		money-=25
		res["Thieves' Tools"]=1
	if cclass in [ 'Cleric', 'Druid', 'Dervish', 'Shaman', 'Shamani' ] :
		money-=25
		res["Holy Symbol"]=1
	
	# Fix basics
	if money>15 :
		money-=12
		for e in basic_12 :
			res[e]=basic_12[e]
	else : 
		money-=3
		for e in basic_3 :
			res[e]=basic_3[e]

	# Define budgets
	budget_type = 'default'
	if cclass in unarmored_class : est_armor = 0
	elif cclass in light_class : est_armor = 30
	elif cclass in armored_class :  est_armor = 70
	else : est_armor = 20

	if cclass == 'Mystic' :
		max_w='Cestus'
		min_w='Cestus'
	else :
		min_w, max_w = get_cost_max_min(weapons)

	if est_armor + weaponcosts[max_w] + 35 < money : budget_type = 'rich' # buy best armor and weapon
	elif 3*est_armor/2 + weaponcosts[min_w] + 15 < money : budget_type = 'moderate' # buy moderate armor and weapon
	elif est_armor/2 + weaponcosts[min_w] + 10 < money : budget_type = 'constrained' # buy moderate armor and weapon
	else : budget_type = 'poor' # buy moderate weapon, low or no armor
	
	# Fix primary weapon
	if budget_type == 'rich' and money>weaponcosts[max_w] : 
		money-=weaponcosts[max_w]
		res[max_w]=1
	else :
		money-=weaponcosts[min_w]
		res[min_w]=1
	
	# Fix armor
	if budget_type == 'rich' :
		if cclass in armored_class : 
			money-=70
			res['Plate armor']=1
			res['Shield']=1
		if cclass in light_class :
			money-=20
			res['Leather armor']=1
	elif budget_type == 'moderate' :
		if cclass in armored_class :
			money-=40
			res['Chain armor']=1
		if cclass == 'Druid' :
			money-=20
			res['Leather armor']=1
	elif budget_type == 'constrained' :
		if cclass in armored_class :
			money-=30
			res['Scale armor']=1
		if cclass == 'Druid' :
			money-=10
			res['Shield']=1
	elif budget_type == 'poor' :
		if cclass in armored_class and money>20 :
			money-=20
			res['Leather armor']=1
	
	# Fix residual equipment
	if budget_type == 'rich' and money>25 :
		money-=25
		eq = choice(general_25)
		for e in eq :
			res[e]=eq[e]
	elif money>6 and budget_type != 'poor' :
		money-=6
		eq = choice(general_6)
		for e in eq :
			res[e]=eq[e]
		
	# Buy secondary weapon
	if budget_type == 'rich' and money>weaponcosts[min_w] :
		money-=weaponcosts[min_w]
		res[min_w]=1
	elif money>weaponcosts[max_w] :
		money-=weaponcosts[max_w]
		res[max_w]=1
	
	# Buy shield and, eventually, a third weapon
	if money>10 and cclass in armored_class+['Druid'] and 'Shield' not in res :
		money-=10
		res['Shield']=1
	other_w = [ w for w in weapons if w!=max_w and w!=min_w ]
	for w in other_w :
		if money>weaponcosts[w] :
			money-=weaponcosts[w]
			res[w]=1
		
	# Buy other items
	while money>5 and d6()>2 :
		i=choice(list(other_items.keys()))
		if other_items[i]<money-1 :
			money-=other_items[i]
			res[i]=1

	if   'Plate armor'   in res : AC = 3
	elif 'Banded armor'  in res : AC = 4
	elif 'Chain armor'   in res : AC = 5
	elif 'Scale armor'   in res : AC = 6
	elif 'Leather armor' in res : AC = 7
	else : AC = 9
	if 'Shield' in res : AC -= 1
	return res, money, AC


magic_items = { 'Potion of Healing' : 2000, 'Ring of Protection +1' : 20000, 'Ring of Protection +2' : 30000, 'Ring of Protection +3' : 40000, 'Ring of Protection +4' : 50000, 'Potion of Super-Healing': 4000, 'Potion of Polymorph Self' : 5000, 'Potion of Sight' : 3000, 'Potion of Flying' : 5000, 'Potion of ESP' : 3000, 'Potion of Human Control' : 5000, 'Potion of Invisibility' : 3000, 'Ring of Three Wish' : 113000, 'Rod of Dominion' : 125000, 'Ring of Regeneration' : 80000 }
muser_items = { 'Scroll of Magic Missile' : 5000, 'Scroll of Sleep' : 5000, 'Scroll of Web' : 10000, 'Scroll of Fireball' : 15000, 'Staff of Striking (20 charges)': 90000, 'Wand of Lightning (10 charges)' : 50000, 'Wand of Magic Missiles (10 charges)' : 15000, 'Wand of Cold (10 charges)' : 60000, 'Wand of Fireballs (10 charges)' : 50000, 'Wand of Illusions (10 charges)' : 20000, 'Scroll of Portals': 25000, 'Staff of Power (20 charges)' : 360000, 'Staff of Wizardry (20 charges)' : 600000, 'Crystal Ball' : 25000, 'Crystal Ball with clairaudience' : 50000 }
cleric_items = { 'Scroll of Cure Light Wounds' : 5000, 'Scroll of Protection from Evil' : 5000, 'Scroll of Bless' : 10000, 'Scroll of Cure Disease' : 15000, 'Staff of Striking (20 charges)': 90000, 'Staff of Healing (20 charges)' : 210000, 'Scroll of Dispel Evil' : 25000, 'Scroll of Cure Serious Wounds' : 20000, 'Snake Staff' : 90000, 'Rod of Health' : 300000 }
from spellbook import spells

def get_magical_equipment(cclass, level, equipment):
	ac_bonus = 0
	money = (2**min(9,level-1))*200 + max(level-9,0)*12000
	magical_equipment = { }
	while money>2000 :
		if cclass in  [ 'Elf', 'Magic User', 'Hakomon' ] or (cclass in [ 'Thief', 'Rake', 'Bard' ] and level>9) :
			for item in muser_items : 
				if money > muser_items[item] and d6()<3 : 
					money-=muser_items[item] 
					if item in magical_equipment.keys() :
						magical_equipment[item]+=1
					else :
						magical_equipment[item]=1
		if cclass in  [ 'Cleric', 'Druid', 'Shaman', 'Shamani' ] or (cclass in [ 'Thief', 'Rake', 'Bard' ] and level>9) :
			for item in cleric_items : 
				if money > cleric_items[item] and d6()<3 : 
					money-=cleric_items[item] 
					if item in magical_equipment.keys() :
						magical_equipment[item]+=1
					else :
						magical_equipment[item]=1
		for item in equipment :
			if (item in weaponcosts.keys() or item == 'Shield') and d6()<3 :
				if money>5000 :
					money-=5000
					if item == 'Shield' : ac_bonus+=1
					if item in magical_equipment.keys() :
						magical_equipment[item]+=1
					else :
						money-=5000
						magical_equipment[item]=1
			elif item in armor and d6()<4 :
				if money>10000 :
					money-=10000
					ac_bonus+=1
					if item in magical_equipment.keys() :
						magical_equipment[item]+=1
					else :
						money-=10000
						magical_equipment[item]=1
		for item in magic_items : 
			if money > magic_items[item] and d6()<3 : 
				money-=magic_items[item] 
				if item in magical_equipment.keys() :
					magical_equipment[item]+=1
				else :
					magical_equipment[item]=1
	res = {}
	replaced = []
	for i in magical_equipment :
		if i in weaponcosts.keys() or i in armor :
			res[i+' +'+'magical_equipment[i]']=1
			replaced.append(i)
		else :
			res[i]=magical_equipment[i]
		if i == 'Ring of Protection +1' : ac_bonus+=1
		elif i == 'Ring of Protection +2' : ac_bonus+=2
		elif i == 'Ring of Protection +3' : ac_bonus+=3
	return res, replaced, ac_bonus
