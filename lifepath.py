#!/usr/bin/python

from dice import *

afflictions = {
1 : ['Suffered from the brown plague', { 'con': -d6()}],
2 : ['Suffered from brain rot', {'str':-1, 'dex':-1, 'con':-1, 'int':-1, 'wis':-1, 'cha':-1}],
3 : ['Suffered from a fading of youthful enthusiasm', {'con':-1, 'str':-1}],
4 : ['Suffered a minor injury to arm or leg', {'dex':-1}],
5 : ['Suffered a head injury', {'int':-1}],
6 : ['Suffered an injury affecting breathing or digestion', {'con':-1} ],
7 : ['Suffered an accident which caused disfiguring scars', {'cha':-2} ],
8 : ['Had a bad fall or riding accident', {'str':-1, 'dex':-1} ],
9 : ['Suffers from gut worms', {}],
10: ['Had arthritis or a back injury', { 'dex':-1} ],
91: ['Suffered from dysentery', { 'con':-1} ],
92: ['Suffered from dysentery', {} ],
93: ['Suffered from dysentery', {} ],
94: ['Suffered from sheep pox', { 'cha':-1, 'str':-1, 'dex':-1} ],
95: ['Suffered from sheep pox', { 'cha':-1} ],
96: ['Suffered from sheep pox', { 'cha':-1} ],
97: ['Is out of shape', { 'dex':-1, 'str':-1 } ],
98: ['Suffers from poor mental health', { 'int':-1, 'wis':-3 } ],
99: ['Was hit by the carrot fever', {'str':-1, 'dex':-1, 'con':-1, 'int':-1, 'wis':-1, 'cha':-1 } ],
100:['Had a very serious accident', { 'dex':-d6() } ],
}

past = {
1 : [ 'Had a complete dedication to the training', {'str':1, 'con':1 } ],
2 : [ 'Endured a brutal training schedule', { 'skill':2 } ],
3 : [ 'Endured a hard training', { 'str':1, 'con':1 } ],
4 : [ 'Suffered a training accident', {'dex': -1 }],
5 : [ 'Learned to concentrate on the work at hand', { 'int':1 } ],
6 : [ 'Patiently practiced',  {'dex':1} ],
7 : [ 'Had a generous teacher' , { 'con':1, 'skill': 1} ],
8 : [ 'Showed a sincere effort in training', { 'skill':1 } ],
20: [ 'Had a competent teacher', { 'skill':1 }],
21: [ 'Had a good advisor', {'wis':1 } ],
22: [ 'Met a famous priest', { 'Reverent/Godless':4, 'item': 'Healing potion' } ],
23: [ 'Had a good health and good training environment', { 'str':1 } ],
24: [ 'Learn bad habits', {'int':-1} ],
25: [ 'Enjoyed access to good library', { 'int':1 } ],
26: [ 'Inherited an heirloom', {'item':'Dagger +1, continual light'} ],
27: [ 'Had a fundamental insight during training', { 'int':1, 'skill':1 }]
}

build = {
1 : [ 'Was betrayed by a close friend', { 'Loyal/Unreliable':-2 } ],
2 : [ 'Was humiliated and thrashed by a bully', { 'Peaceful/Violent':-2, 'Forgiving/Vengeful':-2 } ],
3 : [ 'Was widely praised for a small achievement', { 'Modest/Proud':-2 } ],
4 : [ 'Was cheated by a fast-talking acquaintance', { 'Trusting/Suspicious':-1, 'Generous/Greedy':-1} ],
5 : [ 'Was inspired by the actions of a spiritual hero', { 'Reverent/Godless':3 } ],
6 : [ 'Was mocked for timid behaviour', { 'Courageous/Fearful':1, 'Cautious/Rash':-3 } ],
7 : [ 'Was discouraged by poor luck', { 'Energetic/Lazy':-1, 'Cautious/Rash':2 } ],
8 : [ 'Achieved success by misleading a comrade', { 'Honest/Deceitful':-1, 'Loyal/Unreliable':-1 } ],
9 : [ 'Protected a friend from an attack', { 'Loyal/Unreliable':1, 'Courageous/Fearful':1 } ],
10: [ 'Defended the honor of a family member', { 'Loyal/Unreliable':1, 'Courageous/Fearful':2 } ],
11: [ 'Lost several opportunities through esitation', { 'Cautious/Rash':-1 } ],
12: [ 'Forgave a miscreant who becomes a close friend', { 'Forgiving/Vengeful':2 } ],
13: [ 'Got caught in a complicated lie', { 'Honest/Deceitful':1, 'Cautious/Rash':1 } ],
14: [ 'Ignored a personal principle with disastrous results', { 'Dogmatic/Open-Minded':2 } ],
15: [ 'Accidentally injured an innocent person', { 'Cautious/Rash':1, 'Peaceful/Violent':2 } ],
}


combat = {
1 : [ 'Was seriously injured in war', { 'con':-2, 'str': -1 } ],
2 : [ 'Is a war veteran, survived uninjured', { 'Courageous/Fearful':2, 'Peaceful/Violent':-2 } ],
3 : [ 'Was injured in war', { 'Courageous/Fearful':1, 'con':-1 } ],
4 : [ 'Is a war veteran, but saw little danger', { 'Courageous/Fearful':2 } ],
5 : [ 'Was injured in raid or small action', { 'Cautious/Rash':1, 'con':-1 } ],
6 : [ 'Is a veteran of a raid or small action, survived uninjured', { 'Courageous/Fearful':1, 'Peaceful/Violent':-1 } ],
7 : [ 'Is a veteran of a raid or small action, with little danger', { 'Courageous/Fearful':1 } ],
18: [ 'Was injured in combat', { 'Courageous/Fearful':-1, 'Cautious/Rash':2, 'con':-1 } ],
19: [ 'Was badly injured in combat', { 'Courageous/Fearful':-3, 'Cautious/Rash':+3, 'con':-1 } ],
}


def merge(d1, d2):
    res={}
    for i in d1 :
        res[i]=d1[i]
    for i in d2 :
        if i in res :
            res[i]+=d2[i]
        else :
            res[i]=d2[i]
    return res

equiv_classes = {
        'Horse Warrior' : 'Fighter',
        'Hakomon' : 'Magic User',
}

def lifepath(cclass):
    # Fix classes
    if cclass in equiv_classes : 
        cclass = equiv_classes[cclass]
    # Roll Afflictions
    a=d100()
    res = afflictions[a] if a in afflictions.keys() else [ 'Enjoyed good health in youth', {} ]
    desc, eff = [res[0]], res[1]
    if a==2 or a==99 : return desc, eff
    # Roll Training
    p=d4(4)
    if cclass=='Fighter' : p-=3
    if cclass=='Magic User' : p+=3
    res = past[p] if p in past.keys() else None
    if res : 
        desc.append(res[0])
        eff=merge(eff, res[1])
    # Roll Character Building
    b = d20()
    res = build[b] if b in build.keys() else None
    if res :
        desc.append(res[0])
        eff=merge(eff, res[1])
    # Roll Combat Experience
    c = d4(4)
    if cclass=='Fighter' : p-=3
    if cclass=='Magic User' : p+3
    res = combat[c] if c in combat.keys() else None
    if res :
        desc.append(res[0])
        eff=merge(eff, res[1])
    return desc, eff

if __name__ == '__main__' :
    print (lifepath('Magic User'))
    print (lifepath('Fighter'))
    print (lifepath('Cleric'))

