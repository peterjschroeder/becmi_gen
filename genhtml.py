#!/usr/bin/python

from genpdf import main, get_npc_list

header_template = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>Mystara BECMI NPC Generator</title>
<meta http-equiv="Content-Language" content="English" />
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link rel="stylesheet" type="text/css" href="static/style.css" media="screen" />
</head>
<body>
<div id="banner">
<H1>Mystara  BECMI NPC Generator</H1>
</div>
<div id="wrap">
'''

footer_template = '''
</div>
</body>
</html>
'''

npc_template = '''
<article>
<div id="header">
<H1>{}</H1>
<H2>{} {}</H2>
</div>
<div id="content">
<TABLE>
<TR>
<TD>HP</TD><TD>AC</TD><TD>WR</TD> 
<TD>Death/Poison</TD><TD>Wands</TD><TD>Par/Stone</TD><TD>Breath</TD><TD>Rod/Spell</TD>
</TR><TR>
<TD>{}</TD><TD>{}</TD><TD>{}</TD> 
<TD>{st[0]}</TD><TD>{st[1]}</TD><TD>{st[2]}</TD><TD>{st[3]}</TD><TD>{st[4]}</TD>
</TR>
</TABLE>
</div>
<div id="content">
<H2>Ability Scores</H2>
<TABLE>
<TR>
<TD>Str	</TD><TD> {abi[str]} ({adj[str]:+d})</TD>
<TD>Int	</TD><TD> {abi[int]} ({adj[int]:+d})</TD>
<TD>Wis	</TD><TD> {abi[wis]} ({adj[wis]:+d})</TD>
</TR><TR>
<TD>Dex	</TD><TD> {abi[dex]} ({adj[dex]:+d})</TD>
<TD>Con	</TD><TD> {abi[con]} ({adj[con]:+d})</TD>
<TD>Cha	</TD><TD> {abi[cha]} ({adj[cha]:+d})</TD>
</TR>
</TABLE>
</div>

<div id="content">
<H2>Personal Information</H2>
<TABLE>
<TR>
<TD>Weight</TD><TD>Height</TD><TD>Age</TD> 
</TR><TR>
<TD>{}</TD><TD>{}</TD><TD>{}</TD> 
</TR>
</TABLE>
</div>
'''

npc_footer = '''
</article>
'''


def printnpc(npc):
    from titles import set_title
    name = set_title(npc.name, npc.title)
    gender = npc.gender
    # Class, Level, Align
    c = ''
    if npc.race in ['Dwarf', 'Elf', 'Halfling']:
        c += "{} {} {} {}".format(gender, npc.align, npc.vclass, npc.level)
        if npc.attack_rank:
            c += '('+chr(npc.attack_rank+65)+')'
    elif npc.origin != npc.region:
        from config import get_origin_name
        c += "{} {} {} {} {}".format(gender, npc.align, get_origin_name(
            npc.region, npc.origin), npc.vclass, npc.level)
    else:
        c += "{} {} {} {} {}".format(gender, npc.align,
                                     npc.race, npc.vclass, npc.level)
    # religion
    r = ', follower of '
    if npc.cclass == 'Shaman':
        r += "the {} spirit".format(npc.spirit_guide)
    else:
        r += "{}".format(npc.religion)
    # saving throws
    from savingthrows import get_ST_table
    st = get_ST_table(npc.race, npc.cclass, npc.level)

    adj = {x: npc.get_adj(x) for x in npc.abilities.keys()}
    out = npc_template.format(name, c, r, npc.hp, npc.AC, npc.WR,
                              npc.weight, npc.height, npc.age,
                              st=st, abi=npc.abilities, adj=adj
                              )

    from traits import traits
    out += '<div id="content">\n<H2>Traits</H2>'
    out += "<TABLE><TR>"
    i = 0
    for t in traits:
        out += "<TD>{:20} </TD><TD> {:>2}</TD>".format(t, npc.traits[t])
        out += "</TR>\n<TR>" if i % 2 else " "
        i += 1
    out = out[:-5]
    out += "</TABLE></div>"

    from weapons import get_weapondmg
    out += '<div id="content">\n<H2>Weapon Masteries</H2>'
    out += "<TABLE>"
    for w in npc.weapons:
        out += "<TR><TD>{} </TD><TD> {} </TD><TD> {}</TD></TR>\n".format(w,
                                                                         npc.weapons[w], get_weapondmg(w, npc.weapons[w]))
    out += "</TABLE></div>"

    from skills import skill_scores
    out += '<div id="content">\n<H2>General Skills</H2>'
    out += "<TABLE>"
    for s in npc.skills:
        bonus = 1 if s in npc.skill_bonuses else 0
        if 'Language' == s[:len('Language')]:
            out += "<TR><TD>{} </TD><TD> {} </TD><TD> {} </TD></TR>\n".format(s,
                                                                              'Int', npc.abilities['int']+bonus)
        else:
            out += "<TR><TD>{} </TD><TD> {} </TD><TD> {} </TD></TR>\n".format(s,
                                                                              skill_scores[s].capitalize(), npc.abilities[skill_scores[s]]+bonus)
    out += "</TABLE></div>"

    out += '<div id="content">\n<H2>Equipment</H2><P>'
    for s in npc.equipment:
        if npc.equipment[s] > 1:
            out += '{} {}, '.format(npc.equipment[s], s)
        else:
            out += '{}, '.format(s)
    out += 'npc.sp/10' + ' gp, ' + 'npc.sp%10' + ' sp.'
    out += "</P></div>"

    if npc.cclass in ['Magic User', 'Elf', 'Forester'] and npc.level < 20:
        out += '<div id="content">\n<H2>Spellbook</H2><P>'
        for lvl in npc.spellbook.keys():
            for spell in npc.spellbook[lvl]:
                out += '{}, '.format(spell)
        out = out[:-2]  # remove last comma
        out += "</P></div>"

    out += '''<div id="content">
<H2>Life Experiences</H2><P> 
The character comes from a {} family. '''.format(npc.family)
    for i in npc.life_events:
        out += '{}. '.format(i)
    out += "</P></div>"
    out += npc_footer
    return latex_to_html_special_chars(out)


def latex_to_html_special_chars(s):
    s = str(s)
    import re
    p = re.compile(r'\\\'(\w)')
    s = p.sub(r'&\1acute;', s)
    p = re.compile(r'\\\"(\w)')
    s = p.sub(r'&\1uml;', s)
    p = re.compile(r'\`(\w)')
    s = p.sub(r'&\1grave;', s)
    p = re.compile(r'\\\~(\w)')
    s = p.sub(r'&\1tilde;', s)
    p = re.compile(r'\\\^(\w)')
    s = p.sub(r'&\1circ;', s)
    p = re.compile(r'\c{c}')
    s = p.sub(r'&ccedil;', s)
    return s


def genhtml(args, debug=False):
    npclist = get_npc_list(args)
    out = header_template
    for n in npclist:
        out += printnpc(n)
    out += footer_template
    if debug:
        print ('NPC List:', out)
    return out


if __name__ == '__main__':
    args = main()
    out = genhtml(args)
    with open(args.output, "w") as fout:
        fout.write(out)
