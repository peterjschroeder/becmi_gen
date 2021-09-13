#!/usr/bin/python

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	return """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>Mystara BECMI NPC Generator</title>
<meta http-equiv="Content-Language" content="English" />
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link rel="stylesheet" type="text/css" href="/static/style.css" media="screen" />
</head>
<body>
<div id="banner">
<H1>Mystara BECMI NPC Generator</H1>
</div>
<div id="wrap">
<div id="content">
<H1>Mystara NPC Generator</H1>
<form action="/generator" method="get"><h2>Region</h2>
<p><input type="radio" name="region" value="Norwold" checked>Norwold<br>
   <input type="radio" name="region" value="Thyatis">Thyatis<br>
   <input type="radio" name="region" value="Alphatia">Alphatia<br>
   <input type="radio" name="region" value="Ylaruam">Ylaruam<br>
   <input type="radio" name="region" value="Isle of Dawn">Isle of Dawn<br>
   <input type="radio" name="region" value="Karameikos">Karameikos<br>
   <input type="radio" name="region" value="Glantri">Glantri<br>
   <input type="radio" name="region" value="Savage Coast">Savage Coast<br>
   <input type="radio" name="region" value="Rockhome">Rockhome<br>
   <input type="radio" name="region" value="Ethengar Khanate">Ethengar Khanate<br>
   <input type="radio" name="region" value="Darokin">Darokin<br>
   <input type="radio" name="region" value="Hule">Hule<br>
   <input type="radio" name="region" value="Alfheim">Alfheim<br>
   <input type="radio" name="region" value="Ierendi">Ierendi<br>
   <input type="radio" name="region" value="Atruaghin Clans">Atruaghin Clans<br>
   <input type="radio" name="region" value="Shimmering Lands">Shimmering Lands<br>
</p>
<H2>Ability Score Optimization</H2>
<p><input type="radio" name="opt_scores" value="sometimes" checked>Optimize ability scores, but not always<br>
   <input type="radio" name="opt_scores" value="always">Always optimize ability scores<br>
</p>
<H2>High Level Rolls</H2>
<p><input type="radio" name="high_level_rolls" value="never" checked>Use the standard score and HP generation<br>
   <input type="radio" name="high_level_rolls" value="always">Always transform a roll of 1 to 2<br>
   <input type="radio" name="high_level_rolls" value="name">Transform a roll of 1 to 2 only for name level NPCs<br>
</p>
<h2>Levels</h2>
<p><input type="text" name="lmin" value="1">Minimum level<br>
   <input type="text" name="lmax" value="36">Maximum level<br>
   <input type="text" name="lavg" value="18">Average level<br>
   <input type="text" name="lnum" value="16">Number of NPCs to generate<br>   
</p>
<H2>Frequency Definition</H2>
<p><input type="radio" name="frequencies" value="default">Frequencies Method 1 (prevalent = 6x very rare)<br>
   <input type="radio" name="frequencies" value="variant" checked>Frequencies Method 2 (prevalent = 8x very rare)<br>   
   <input type="radio" name="frequencies" value="linear" checked>Frequencies Method linear (prevalent = 8x very rare)<br>   
   <input type="radio" name="frequencies" value="quadratic" checked>Frequencies Method quadratic (prevalent = 25x very rare)<br>   
   <input type="radio" name="frequencies" value="exponential" checked>Frequencies Method exponential (prevalent = 16x very rare)<br>   
</p>
<H2>Custom Spell Lists</H2>
<p><input type="radio" name="spellbooks" value="Tome of Mystaran Magic" checked>Tome of Mystaran Magic<br>
   <input type="radio" name="spellbooks" value="Rules Cyclopedia">Rules Cyclopedia<br>
</p>
<p><input type="Submit" name="npclist" value="Generate NPCs">
   <input type="Submit" name="npcparty" value="NPC Party">
   <input type="Submit" name="followers" value="Followers"></p>
</form>
</div>
</div>
</body>
</html>"""

class Args():
	def __init__(self, num, lmin, lmax, region, freq_method, 
                    npc_party=0, opt_scores=False, followers=0, spells="Generic",
                    high_lvl_rolls='never'):
		self.level_min = lmin
		self.level_top = lmax
		self.region = region
		self.npc_num = num
		self.output = 'npcs.pdf'
		self.npc_party = npc_party
		self.level=1
		self.followers=followers
		self.optimize_always= True if opt_scores=='always' else False
		self.freq_method = freq_method
		self.spellbooks = spells
                self.high_level_rolls = high_lvl_rolls
def __repr__(self):
		return '{} {} {} {}'.format(self.region, self.npc_num, self.level_min, self.level_top)

@app.route('/generator')
def generator():
	# Start generation
	from genhtml import genhtml
	region='Norwold'
	lmin, lmax = 1, 36
	lnum = 16
	lavg = 18
	npc_party=0
	followers=0
	opt_scores='always'
	freq_method='default'
	spellbooks='Generic'
        high_lvl_rolls = 'never'
        d = dict(request.args)
	try : 
		region=d['region'][0]
		lmin = int(d['lmin'][0])
		lmax = int(d['lmax'][0])
		lnum = int(d['lnum'][0])
		lavg = int(d['lavg'][0])
		npc_party=lavg if 'npcparty' in d.keys() else 0
		followers=lavg if 'followers' in d.keys() else 0
		freq_method = d['frequencies'][0]
		spellbooks = d['spellbooks'][0]
                high_lvl_rolls = d['high_level_rolls'][0]
	except Exception as e: 
		print e
		print d
	args = Args(lnum,lmin,lmax,region,freq_method,npc_party,opt_scores,
                    followers,spellbooks,high_lvl_rolls)
	return genhtml(args)

if __name__=='__main__' :
	wapp.run()
