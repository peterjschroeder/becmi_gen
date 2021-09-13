#!/usr/bin/python

from dice import *

traits = [ 'Cautious/Rash', 'Modest/Proud', 'Peaceful/Violent', 'Generous/Greedy', 'Courageous/Fearful', 'Reverent/Godless', 'Forgiving/Vengeful', 'Energetic/Lazy', 'Honest/Deceitful', 'Trusting/Suspicious', 'Loyal/Unreliable', 'Dogmatic/Open-Minded' ]

def trait_roll(alignment):
    if alignment == 'Lawful' : 
        return lambda :  5+d6()+d8()
    elif alignment == 'Neutral' : 
        return lambda :  5+d10()
    else :  
        return lambda :  d8()+d6()

def get_traits(cclass, race, origin, align):
        t=trait_roll(align)
        chr_traits = { x : t() for x in traits }
        if cclass in [ 'Fighter', 'Forester', 'Rake' ] :
            chr_traits['Courageous/Fearful']+=3
            chr_traits['Cautious/Rash']-=3
        elif cclass in [ 'Cleric', 'Druid', 'Shaman', 'Dervish' ] :
            chr_traits['Reverent/Godless']+=3
            chr_traits['Dogmatic/Open-Minded']+=2
            chr_traits['Loyal/Unreliable']+=1
        elif cclass == 'Magic User' :
            chr_traits['Courageous/Fearful']-=2
            chr_traits['Cautious/Rash']+=2
            chr_traits['Trusting/Suspicious']-=2
        elif cclass in [ 'Thief' , 'Bard' ] :
            chr_traits['Honest/Deceitful']-=2
            chr_traits['Cautious/Rash']+=2
            chr_traits['Trusting/Suspicious']-=2
        if race == 'Dwarf' :    
            chr_traits['Trusting/Suspicious']-=2
            chr_traits['Dogmatic/Open-Minded']+=2
            chr_traits['Generous/Greedy']-=2
        elif race == 'Elf' :    
            chr_traits['Honest/Deceitful']+=2
            chr_traits['Cautious/Rash']+=2
            chr_traits['Modest/Proud']-=2
        elif race == 'Halfling' :   
            chr_traits['Peaceful/Violent']+=2
            chr_traits['Cautious/Rash']+=2
            chr_traits['Energetic/Lazy']-=2
        elif race == 'Rakasta' :    
            chr_traits['Courageous/Fearful']+=2
            chr_traits['Cautious/Rash']-=1
            chr_traits['Energetic/Lazy']-=2
        elif race == 'Lupin' :  
            chr_traits['Loyal/Unreliable']+=2
            chr_traits['Dogmatic/Open-Minded']+=1
            chr_traits['Trusting/Suspicious']-=2
        if origin == 'Heldanner' :
            chr_traits['Loyal/Unreliable']+=2
            chr_traits['Courageous/Fearful']+=1
            chr_traits['Cautious/Rash']-=1
            chr_traits['Forgiving/Vengeful']-=1
        elif origin == 'Thyatian' :
            chr_traits['Honest/Deceitful']-=1
            chr_traits['Trusting/Suspicious']-=1
        elif origin == 'Ochalean' :
            chr_traits['Honest/Deceitful']+=1
            chr_traits['Peaceful/Violent']+=1
            chr_traits['Dogmatic/Open-Minded']+=1
        elif origin == 'Daro' :
            chr_traits['Honest/Deceitful']+=1
            chr_traits['Peaceful/Violent']+=1
            chr_traits['Dogmatic/Open-Minded']-=1
        elif origin == 'Alphatian' :
            chr_traits['Reverent/Godless']-=1
            chr_traits['Dogmatic/Open-Minded']-=2
        elif origin == 'Alasiyan' :
            chr_traits['Reverent/Godless']+=2
            chr_traits['Dogmatic/Open-Minded']+=2
            chr_traits['Honest/Deceitful']+=1
        elif origin == 'Heldannic' :
            chr_traits['Reverent/Godless']+=1
            chr_traits['Dogmatic/Open-Minded']+=1
        elif origin == 'Dunael' :
            chr_traits['Energetic/Lazy']+=1
            chr_traits['Generous/Greedy']+=1
        elif origin == 'Vatski/Vrodniki' :
            chr_traits['Peaceful/Violent']-=2
            chr_traits['Trusting/Suspicious']-=1
            chr_traits['Courageous/Fearful']+=1
        elif origin == 'Makai' :
            chr_traits['Peaceful/Violent']+=1
            chr_traits['Generous/Greedy']+=1
        elif origin == 'Ierendian' : 
            chr_traits['Energetic/Lazy']+=1
            chr_traits['Dogmatic/Open-Minded']-=1
        return chr_traits
