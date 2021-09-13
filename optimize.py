#!/usr/bin/python

from config import primary_scores, get_adj
from dice import d6
from copy import copy

def tot_adj(abilities):
	return sum([ get_adj(abilities,a) for a in abilities ],0)

def attempt_opt(abilities, to_lower, to_raise):
	a=copy(abilities)
	a[to_lower]-=2
	a[to_raise]+=1
	return tot_adj(a)-tot_adj(abilities)

def optimize(cclass, abilities, always=True):
	abilities=copy(abilities)
	ps = set(primary_scores[cclass])
	to_lower = set(['str', 'int', 'wis']) - ps
	while d6()>4 or always :
		to_lower = set([ a for a in to_lower if abilities[a]>10 ])
		if not len(to_lower) : return abilities
		m_a, m_b, score = None, None, -36
		for a in to_lower :
			for b in ps :
				s = attempt_opt(abilities, a, b)
				if s>score and s>=0 :
					m_a, m_b, score = a, b, s
		if score>=0 :
			abilities[m_a]-=2
			abilities[m_b]+=1
		else :
			return abilities
	return abilities
	


if __name__ == '__main__' :
	print ('Test')
	print (optimize('Fighter', { 'str' :5, 'int':14, 'wis':10, 'dex':13, 'con':12, 'cha':11 }))
