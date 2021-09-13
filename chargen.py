#!/usr/bin/python

from dice import *
from config import *
from skills import skill_scores, spirit_guide
from traits import traits

def get_race_origin(region, abilities):
    race = choice(races_selector(region))
    if abilities['con']<9 and race in ['Dwarf' , 'Halfling' ] :
        race = 'Human'
    if abilities['dex']<9 and race == 'Halfling' :
        race = 'Human'
    if abilities['int']<9 and race == 'Elf' :
        race = 'Human'
    origin = choice(origin_selector(region,race))
    return race, origin

class npc:
    '''Main class of the generator. Creating an instance creates a new NPC.
    '''
    def get_adj(self,ability):
        score=self.abilities[ability]
        if score == 18 : return 3
        elif score > 15: return 2
        elif score > 12: return 1
        elif score > 8 : return 0
        elif score > 5 : return -1
        elif score > 3 : return -2
        else : return -3

    def __init__(self, name="NPC", level=1, gender='m', region='Norwold', 
                    optimize_always=True, _freq="variant", custom_spellbooks=False,
                    high_level_rolls = 'never'):
        '''New NPC generation
name          NPC name (leave default to generate an appropriate name)
level         level of the NPC (default 1)
gender        gender of the NPC (default male)'''
        # Set frequency method
        init_config(_freq)
        # Set unique id
        from uuid import uuid4
        self.uuid = uuid4()
        # Set level and gender
        self.level=level
        self.gender = gender
        self.region = region # Not really needed
        # Set ability scores
        remove_ones = False
        if high_level_rolls == 'always' or (high_level_rolls == 'name' and self.level>=9) :
            remove_ones = True
        self.abilities = { x : d6(3, remove_ones) for x in abilities }
        # Set Race and Origin
        self.race, self.origin = get_race_origin(region, self.abilities)
        from age import get_age
        self.age = get_age(self.race, self.level)
        # Set Name
        from namegen import get_name
        self.name=get_name(self.race,self.origin,self.gender, region=self.region)
        # Correct level and abilities by race, set attack rank
        self.attack_rank = 0
        if self.race in [ 'Lupin', 'Rakasta' ] and ( self.level<3 or (self.level==4 and d6()<4 )) : 
            # Rakasta and Lupin PCs start at -2000 XP
            self.level = max(1, self.level-1)
        elif self.race == 'Dwarf' and self.level>=12 :
            self.attack_rank = min((self.level-8)/2,12)
            self.level = 12
        elif self.race == 'Elf' and self.level>=10 :
            self.attack_rank = min((self.level-8)/2,12)
            self.level = 10
        elif self.race == 'Halfling' and self.level>=8 :
            self.attack_rank = min((self.level-8)/2,10)
            self.level = 8
        if self.race == 'Lupin' :
            self.abilities['int']=min(17,self.abilities['int'])
            self.abilities['wis']=min(17,self.abilities['wis'])
        if self.race == 'Rakasta' :
            self.abilities['dex']=min(18,self.abilities['dex']+2)   
        # Set class and alignment
        from cclass import get_class
        self.cclass, self.align = get_class(self.race, self.origin, self.region)
        # Fix Forester level (as elf)
        if self.cclass == 'Forester' and self.level>=10 :
            self.attack_rank = min((self.level-8)/2,12)
            self.level = 10
        # Fix aftereffects of class choice
        if self.cclass == 'Forester' and (self.abilities['int']<12 or self.abilities['str']<12) : 
            self.cclass = 'Fighter'
        if self.cclass == 'Mystic' and (self.abilities['wis']<13 or self.abilities['dex']<13) : 
            self.cclass=choice([ 'Fighter', 'Cleric', 'Thief' ])
        if self.cclass == 'Mystic' and self.level>16 : self.level=16
        if self.cclass == 'Dervish' and self.abilities['con'] < 13  :
            self.cclass == choice(['Cleric', 'Fighter', 'Thief'])
        if self.region=='Norwold' and  self.origin == 'Foxfolk' and self.cclass == 'Druid' : 
            self.name=get_name(self.race, self.origin, self.gender,'Druid')
        # Ability score training adjustment
        from optimize import optimize
        self.abilities=optimize(self.cclass, self.abilities, always=optimize_always)
        # Set traits
        from traits import get_traits 
        self.traits = get_traits(self.cclass, self.race, self.origin, self.align)
        # Set Weapon Masteries
        from weapons import get_weapons
        self.weapons = get_weapons(self.cclass, self.race, self.level)
        # Set General Skills
        from skills import get_skills
        self.skills, self.spirit_guide=get_skills(self.abilities['int'],self.cclass, self.race, self.origin, self.level, languages(region), region)
        # Set HP 
        self.hp = self.roll_hp(remove_ones)
        # Set Equipment
        self.sp = d6(3)*100*self.level # starting money in silver coins
        from equipment import get_equipment, get_magical_equipment
        eq, residual, base_ac = get_equipment(self.cclass, self.weapons.keys(), self.sp/10)
        self.equipment=eq
        self.sp=residual*10
        # Compute AC and WR
        self.AC=base_ac-self.get_adj('dex')
        if self.cclass == 'Mystic' : self.AC = 10 - self.level - self.get_adj('dex')
        self.WR=base_ac + self.level/2 + self.level%2 + self.get_adj('dex') + self.get_adj('str')
        # Set Spellbook 
        if self.cclass in [ 'Magic User', 'Elf', 'Forester', 'Hakomon' ] :
            from spellbook import get_spellbook, set_spell_list
            if custom_spellbooks == 'Tome of Mystaran Magic' :  
                set_spell_list(self.region, self.origin) 
            self.spellbook = get_spellbook(self.cclass, self.level)
        # Set religion
        from immortals import get_immortal
        self.religion, trait_adj = get_immortal(self.cclass, self.race, self.origin, self.align, region)
        if trait_adj :
            for t in trait_adj :
                self.traits[t]+=trait_adj[t]
        # Set social class of family
        from social import get_status as get_social_status
        self.family = get_social_status(self.region, self.race, self.origin)
        # Set lifepath
        from lifepath import lifepath
        self.skill_bonuses = set([])
        self.life_events, effect = lifepath(self.cclass)
        for e in effect :
            if e in traits : 
                x=self.traits[e]+effect[e]
                if x<16 and x>5 : self.traits[e]=x
            elif e in self.abilities.keys() : 
                x=self.abilities[e]+effect[e]
                if x<16 and x>6 : self.abilities[e]=x
            elif e == 'item' : 
                self.equipment.append(effect[e])
            elif e == 'skill' :
                ls = self.skills
                while len(self.skill_bonuses)<effect[e]:
                    self.skill_bonuses.add(choice(ls))
            else : raise Exception (e)
        # Fix traits max and min values after all adjustments
        for t in traits :
            if self.traits[t]>20 : self.traits[t]=20
            if self.traits[t]<1 : self.traits[t]=1
        # Set magic items
        magical_equipment, replaced, ac_bonus = get_magical_equipment(self.cclass, self.level, self.equipment)
        for i in magical_equipment.keys() :
            if i in self.equipment : 
                self.equipment[i]+=magical_equipment[i]
            else :
                self.equipment[i]=magical_equipment[i]
        for i in replaced :
            del self.equipment[i]
        self.AC -= ac_bonus
        # Fix nickname (after traits have been finalized)
        # FIXME
        from nicknames import get_nickname, set_nicknames
        if min(self.traits.values())<6 or max(self.traits.values())>15 or min(self.abilities.values())<6 or max(self.abilities.values())>15 :
            if d100()<(self.level*3): 
                set_nicknames(self.origin, self.gender)
                nick = get_nickname(self.traits,self.abilities)
                if self.race in [ 'Rakasta', 'Halfling', 'Dwarf' ] or self.origin in [ 'Caurenzan', 'Ethengar', 'Thyatian', 'Dunael', 'Heldanner', 'Heldannic', 'Eusdrian', 'Renardois Folk', 'Bouchon', 'Ispan', 'Verdan', 'Papillon', 'Narvaezan Maremma', 'Carrasquito', 'Traladaran', 'Hulean' ] :
                    name_components = self.name.split(' ')
                    self.name = name_components[0]+' '+nick+' '+''.join(name_components[1:])
                else :
                    self.name+=' '+nick
        # Set size
        from physique import physique
        self.height, self.weight = physique(self.race, self.origin, self.abilities['str'], self.gender)
        # Set title and high level class
        self.vclass = None
        self.title = None
        if self.level>9 or self.attack_rank>0 :
            from titles import high_level_class, get_title
            self.vclass = high_level_class(self.cclass, self.align)
            if not self.vclass : self.vclass = self.cclass
            self.title = get_title(self.region, self.race, self.origin, self.vclass, self.gender)
        if not self.vclass : self.vclass = self.cclass
    
    
    def __repr__(self):
        if self.race in ['Dwarf','Elf', 'Halfling'] :
            res = u"""{}
{} {} {}
""".format(self.name, self.align, self.cclass, self.level)
        elif self.origin!='Norwold' :
            res = u"""{}
{} {} {} {}
""".format(self.name, self.align, self.origin, self.cclass, self.level)
        else :
            res = u"""{}
{} {} {} {}
""".format(self.name, self.align, self.race, self.cclass, self.level)

        res += '\n' + 'HP: ' + self.hp + '\n\n'

        res += """
Str {p[str]:{width}}  Int {p[int]:{width}}  Wis {p[wis]:{width}} 
Dex {p[dex]:{width}}  Con {p[con]:{width}}  Cha {p[cha]:{width}} 

""".format(p=self.abilities, width='2')
        for t in traits :
            res+= "{:20} {:>2}\n".format(t, self.traits[t])
        res+="""
Weapon Masteries
"""
        for w in self.weapons :
            res+= "{:20} {:10}\n".format(w, self.weapons[w])
        res+="""
        
General Skills
"""
        for s in self.skills :
            res+= "{}, ".format(s)
        res=res[:-2] # remove last comma
        
        res+="""
        
Equipment
"""
        for s in self.equipment :
            if self.equipment[s]>1 : res+='{} {}, '.format(self.equipment[s], s)
            else : res+='{}, '.format(s)
        res+=self.sp/10 + ' gp, ' + self.sp%10 + ' sp.'
        return res


    def to_latex(self, header=False):
        '''Generate LaTeX fragment for the single NPC. The fragment employs the tcolorbox, array, tabularx, and colortbl packages. Geometry is also useful.
Header file not included by default'''
        from titles import set_title
        name = set_title(self.name, self.title)
        res=''
        if header :
            res+="""\\documentclass[twocolumn,a4paper]{article}
\\usepackage{tcolorbox}
\\usepackage[a4paper,margin=5mm,top=20mm]{geometry}
\\usepackage{array,tabularx}
\\usepackage{colortbl}
\\pagestyle{empty}
\\newcolumntype{Y}{>{\\centering\\arraybackslash}X}
\\tcbsetforeverylayer{colback=white}

\\begin{document}

"""
        gender = '\\mars' if self.gender=='m' else '\\female'
        res+="""\\begin{tcolorbox}[label="""+str(self.uuid)+""",title="""
        if self.race in ['Dwarf','Elf', 'Halfling'] :
            res+="""{}]
{} {} {} {}""".format(name, gender, self.align, self.vclass, self.level)
            if self.attack_rank :
                res+='('+chr(self.attack_rank+65)+')'
        elif self.origin != self.region :
            from config import get_origin_name
            res+= u"""{}]
{} {} {} {} {}""".format(name, gender, self.align, get_origin_name(self.region,self.origin), self.vclass, self.level)
        else :
            res+= u"""{}]
{} {} {} {} {}""".format(name, gender, self.align, self.race, self.vclass, self.level)
        
        if self.cclass == 'Shaman' : 
            res += """, follower of the {} spirit""".format(self.spirit_guide)
        else :
            res += """, follower of {}""".format(self.religion)

        res += """
\\begin{tcolorbox}[tabularx={YYY||YYYYY}]
   &    &    & \\scriptsize{Death/} &                    & \\scriptsize{Par/}  & \\scriptsize{Breath} & \\scriptsize{Rod}\\\\
HP & AC & WR & \\scriptsize{Poison} & \\scriptsize{Wand} & \\scriptsize{Stone} & \\scriptsize{Atks} & \\scriptsize{Spell}\\\\
"""
        res += '%d & %d & %d' % (self.hp, self.AC, self.WR)
        from savingthrows import get_ST_table
        for i in get_ST_table(self.race,self.cclass,self.level):
            res += ' & %d' % i
        res+='\\\\\n'

        res += """\\end{tcolorbox}

\\begin{tcolorbox}[title=Ability Scores,tabularx={XrrXrrXrr}]"""
        res+="""
Str & {p[str]} & ({a[str]:+d}) & Int & {p[int]} & ({a[int]:+d}) & Wis & {p[wis]} & ({a[wis]:+d})\\\\
Dex & {p[dex]} & ({a[dex]:+d}) & Con & {p[con]} & ({a[con]:+d}) & Cha & {p[cha]} & ({a[cha]:+d})\\\\
""".format(p=self.abilities, a={ x : self.get_adj(x) for x in self.abilities.keys()})
        res+="""\\end{tcolorbox}

\\begin{tcolorbox}[title=Personal Information,tabularx={XcXcXc}]
"""
        res+="""Height & {} cm & Weight & {} kg & Age & {}\\\\""".format(self.height,self.weight,self.age)
        

        res+="""\\end{tcolorbox}

\\begin{tcolorbox}[title=Traits,tabularx={XcXc},fontupper=\scriptsize]
"""
        i=0
        for t in traits :
            res+= "{:20} & {:>2}".format(t, self.traits[t])
            res+= "\\\\\n" if i%2 else " & "
            i+=1
        res+="""\\end{tcolorbox}

\\begin{tcolorbox}[title=Weapon Masteries,tabularx={Xp{0.2\columnwidth}X}]
"""
        from weapons import get_weapondmg
        for w in self.weapons :
            res+= "{} & {} & {}\\\\\n".format(w, self.weapons[w], get_weapondmg(w,self.weapons[w]))
        res+="""\\end{tcolorbox}
        
\\begin{tcolorbox}[title=General Skills,tabularx={Xlr}]
"""
        for s in self.skills :
            bonus = 1 if s in self.skill_bonuses else 0
            if 'Language' == s[:len('Language')] :
                res+= "{} & {} & {} \\\\\n".format(s, 'Int', self.abilities['int']+bonus)
            else :
                res+= "{} & {} & {} \\\\\n".format(s, skill_scores[s].capitalize(), self.abilities[skill_scores[s]]+bonus)
        res+="""\end{tcolorbox}
        
\\begin{tcolorbox}[title=Equipment]
"""
        for s in self.equipment :
            if self.equipment[s]>1 : res+='{} {}, '.format(self.equipment[s], s)
            else : res+='{}, '.format(s)
        res+='%d gp, %d sp.' % (self.sp/10, self.sp%10)
        res+="""
\\end{tcolorbox}
"""
        
        if self.cclass in [ 'Magic User', 'Elf', 'Forester', 'Hakomon' ] and self.level<20 :
            res+="""    
\\begin{tcolorbox}[title=Spellbook]
"""
            for lvl in self.spellbook.keys() :
                for spell in self.spellbook[lvl] :
                    res+='{}, '.format(spell)
            res=res[:-2] # remove last comma
            res+="""
\\end{tcolorbox}
"""     
        
        res+="""\\begin{tcolorbox}[title=Life Experiences]"""
        res+="""The character comes from a {} family. 
""".format(self.family)
        for i in self.life_events :
            res+='{}. '.format(i)
        
        res+="""
\\end{tcolorbox}
\\end{tcolorbox}"""
        if header :
            res+="""\\end{document}
"""
        return res

    def roll_hp(self, remove_ones=False):
        """Compute HP for a given class, level, and Con score"""
        con = self.get_adj('con')
        res = con*min(9,self.level)
        lr_bonus = 1 if self.race in [ 'Lupin', 'Rakasta' ] else 0
        if self.cclass in [ 'Fighter', 'Dwarf', 'Dwarf Cleric', 'Horse Warrior' ] : 
            res+= d8(min(9,self.level)+lr_bonus, remove_ones) 
        elif self.cclass in [ 'Magic User', 'Shaman', 'Thief', 'Bard', 'Rake', 'Hakomon', 'Bratak' ] : 
            res+= d4(min(9,self.level)+lr_bonus, remove_ones) 
            if self.cclass == 'Hakomon' : res+=min(9,self.level)
        elif self.cclass in [ 'Shamani', 'Mystic', 'Elf', 'Cleric', 'Halfling', 'Druid', 'Forester', 'Dervish' ] : 
            res+= d6(min(9,self.level)+lr_bonus, remove_ones) 
        else : raise Exception ("Unknown class "+self.cclass)
        if res<self.level : res=self.level
        if self.cclass in [ 'Fighter', 'Mystic', 'Thief', 'Elf', 'Forester', 'Bard', 'Horse Warrior', 'Bratak' ] : 
            res+= 2*max(0,(self.level-9))
        elif self.cclass in [ 'Shamani', 'Cleric', 'Shaman', 'Druid', 'Magic User', 'Hakomon', 'Dervish' ] :
            res+= max(0,(self.level-9))
        elif self.cclass in [ 'Dwarf', 'Dwarf Cleric' ] :
            res+= 3*max(0,(self.level-9))
        return res

    
if __name__=='__main__' :
    # Main, generates a single NPC
    from sys import argv 
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("-l", "--level", help="Set the character level", type=int, default=1)
    parser.add_argument("-m", "--male", action="store_true", help="Set gender to male")
    parser.add_argument("-f", "--female", action="store_true", help="Set gender to female")
    args=parser.parse_args()
    gender = 'f' if args.female else 'm'
    x = npc(level=args.level, gender=gender)
    print (x)
