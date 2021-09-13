#!/usr/bin/python

from random import choice
from config import freq, classes_by_origin, align_by_origin, class_selector, align_selector

def get_class(race, origin, region):
		cclass = choice(class_selector(race, origin, region))
		aligns = align_selector(race, origin)
		if cclass == 'Thief' : aligns = [ a for a in aligns if a!='Lawful' ]
		align = choice(aligns)
		if cclass in [ 'Forester', 'Shamani' ] : align = 'Lawful'
		if cclass == 'Druid' : align = 'Neutral'
		return cclass, align

if __name__ == '__main__' :
	get_class('Human', 'Thyatian')
