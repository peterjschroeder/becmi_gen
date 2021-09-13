#!/usr/bin/python

from random import randint, choice

def dX(x):
    def d(n=1, remove_ones=False):
        r = range(1,x+1) if not remove_ones else range(2,x+1)+[2]
        return sum([choice(r) for i in range(n)])
    return d

d100=dX(100)
d20=dX(20)
d12=dX(12)
d10=dX(10)
d8=dX(8)
d6=dX(6)
d4=dX(4)
