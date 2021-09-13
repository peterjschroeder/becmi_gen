#!/usr/bin/python

__doc___ = """Non Player Character generator for BECMI

Generates the given number of randomly selected NPCs in a given level range.
"""

try :
    from os import environ
    denv = environ['DISPLAY']
except KeyError :
    def Gooey(f):
        """Fallback, empty decorator"""
        return f
else :
    try :
        from gooey import Gooey
    except ImportError :
        print ("no Gooey, falling back to command line")
        def Gooey(f):
            """Fallback, empty decorator"""
            return f

@Gooey
def main():
    from argparse import ArgumentParser
    from config import regions
    p = ArgumentParser()
    p.add_argument('-n', '--npc-num', type=int, help="Number of NPCs to generate", default=1)
    p.add_argument('-l', '--level', type=int, help="NPC level", default=1)
    p.add_argument('-m', '--level-min', type=int, help="Range of levels, minimum", default=0)
    p.add_argument('-t', '--level-top', type=int, help="Range of levels, maximum", default=0)
    p.add_argument('-o', '--output', type=str, help="Output file name", default="npcs.pdf")
    p.add_argument('-r', '--region', type=str, help="Region of origin for the NPCs", default="Norwold", choices=regions)
    p.add_argument('-p', '--npc-party', type=int, help="Generate an NPC party of the given average level", default=0)
    p.add_argument('-f', '--followers', type=int, help="Generate an NPC party composed of a high level NPC and his/her retinue", default=0)
    p.add_argument('-fq', '--freq_method', type=str, help="Frequency method", default='default', choices=['linear', 'quadratic', 'exponential', 'variant','default'])
    p.add_argument('-opt', '--optimize-always', action='store_true', help="Optimize always")
    p.add_argument('-s', '--spellbooks', type=str, help="Custom spell lists", default="Rules Cyclopedia", choices=['Tome of Mystaran Magic', 'Rules Cyclopedia'])
    p.add_argument('-hl', '--high-level-rolls', type=str, help="High level rolls (turn 1s to 2s in rolling HP and ability scores)", default="never", choices=['always', 'name'])
    args=p.parse_args()
    return args

def get_npc_list(args):
    from chargen import npc
    from random import choice, randint
    from dice import d10, d4 
    npclist=[]
    number = args.npc_num
    lmin, lmax=args.level, args.level
    if args.level_min and args.level_top :
        lmin = args.level_min 
        lmax = args.level_top
    if args.npc_party : 
        number = 4+d4()
        lmin, lmax = max(1,args.npc_party-2), min(36,args.npc_party+2)
    if args.followers :
        n = npc(level=args.followers, gender=choice(['m', 'f']), region=args.region, 
                        optimize_always=args.optimize_always, _freq=args.freq_method, 
                        custom_spellbooks=args.spellbooks, high_level_rolls=args.high_level_rolls)
        npclist.append(n)   
        number = d10(2)
        lmin = 1 
        lmax = args.followers/2
    for x in range(number):
        level=randint(lmin, lmax)
        n = npc(level=level, gender=choice(['m', 'f']), region=args.region, 
                        optimize_always=args.optimize_always, _freq=args.freq_method, 
                        custom_spellbooks=args.spellbooks, high_level_rolls=args.high_level_rolls)
        npclist.append(n)   

    npclist.sort(key=lambda t : t.name)
    return npclist

def genpdf(args):
    npclist = get_npc_list(args)
    with open("npctoc.tex", "w") as fout :
        fout.write("\\begin{tcolorbox}[breakable, title=Table of Contents]\n\\begin{supertabular}{p{0.8\columnwidth}r}\n")
        for n in npclist :
            fout.write('{:50} & \\pageref{{{:5}}}\\\\\n'.format(n.name, str(n.uuid)))   
        fout.write("\\end{supertabular}\n\\end{tcolorbox}")

    with open("npcgen.tex", "w") as fout:
        for n in npclist :
            #fout.write("\\addcontentsline{toc}{section}{"+n.name+"}\n")
            fout.write(n.to_latex())
    
    npclist = [ (n.name, n.cclass, n.level) for n in npclist ]
    with open("npcindex.tex", "w") as fout :
        npclist.sort(key=lambda t : t[-1]) # sort by level
        fout.write("\\begin{tcolorbox}[breakable, title=Index by level]\n\\begin{supertabular}{p{0.6\columnwidth}lr}\n")
        for i in range(len(npclist)):
            name, cclass, level = npclist[i]
            fout.write('{:50} & {:15} & {:5}\\\\\n'.format(name, cclass, level))    
        fout.write("\\end{supertabular}\n\\end{tcolorbox}\n")
        fout.write("\\clearpage\n")
        npclist.sort(key=lambda t : t[1]) # sort by class
        fout.write("\\begin{tcolorbox}[breakable, title=Index by class]\n\\begin{supertabular}{p{0.6\columnwidth}lr}\n")
        for i in range(len(npclist)):
            name, cclass, level = npclist[i]
            fout.write('{:50} & {:15} & {:5}\\\\\n'.format(name, cclass, level))    
        fout.write("\\end{supertabular}\n\\end{tcolorbox}")
    
        import os
        import sys
        os.system("pdflatex --interaction=batchmode npc.tex")
        # re-compile to build the table of contents
        os.system("pdflatex --interaction=batchmode npc.tex")
        if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
            os.system("mv npc.pdf "+args.output)
            os.system("echo \"Working in \" `pwd`")
        elif sys.platform.startswith('win'):
            os.system("move npc.pdf "+args.output)
            os.system("cd")

if __name__=='__main__' :
    genpdf(main())
    
