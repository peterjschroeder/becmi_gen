#!/usr/bin/python

from flask import Flask, request, redirect, send_from_directory

wapp = Flask(__name__, static_url_path='')
wapp.debug=True
print wapp.root_path
print wapp.instance_path

@wapp.route('/')
@wapp.route('/index')
def index():
	return """<html>
<title>
Mystara NPC Generator
</title>
<body>
<H1>Mystara NPC Generator</H1>
<form action="/generator" method="get"><h2>Region</h2>
<p><input type="radio" name="region" value="Norwold" checked>Norwold<br>
   <input type="radio" name="region" value="Thyatis">Thyatis<br>
   <input type="radio" name="region" value="Alphatia">Alphatia<br>
   <input type="radio" name="region" value="Ylaruam">Ylaruam<br>
   <input type="radio" name="region" value="Isle of Dawn">Isle of Dawn<br>
<h2>Levels</h2>
<p><input type="text" name="lmin" value="1">Minimum level<br>
   <input type="text" name="lmax" value="36">Maximum level<br>
   <input type="text" name="lavg" value="18">Average level<br>
<p><input type="text" name="lnum" value="16">Number of NPCs to generate<br>   
<p><input type="Submit" name="npclist" value="Generate NPCs">
<input type="Submit" name="npcparty" value="NPC Party"></p>
</form>
</body>
</html>"""

class Args():
	def __init__(self, num, lmin, lmax, region, npc_party=0):
		self.level_min = lmin
		self.level_top = lmax
		self.region = region
		self.npc_num = num
		self.output = 'npcs.pdf'
		self.npc_party = npc_party
	def __repr__(self):
		return '{} {} {} {}'.format(self.region, self.npc_num, self.level_min, self.level_top)

@wapp.route('/generator')
def generator():
	# cleanup
	from os import system
	system('rm -f '+wapp.root_path+'/npcs.pdf')
	# Start generation
	print 'Initializing generator'
	from genpdf import genpdf
	region='Norwold'
	lmin, lmax = 1, 36
	lnum = 16
	lavg = 18
	npc_party=0
	print 'Reading parameter'
	d = dict(request.args)
	print d
	try : 
		region=d['region'][0]
		lmin = int(d['lmin'][0])
		lmax = int(d['lmax'][0])
		lnum = int(d['lnum'][0])
		lavg = int(d['lavg'][0])
		npc_party=lavg if 'npcparty' in d.keys() else 0
	except Exception, e: 
		print e
		print request
	args = Args(lnum,lmin,lmax,region,npc_party)
	print 'Running genpdf'
	print args
	genpdf(args)
	print 'Sending file'
	return send_from_directory(wapp.root_path, 'npcs.pdf')

@wapp.after_request
def add_header(response):
	response.headers['Cache-Control'] = 'public, max-age=0'
	return response

if __name__ == '__main__' :	
	wapp.run()

