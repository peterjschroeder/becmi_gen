BECMI NPC generator

**Command line version
run:
	./genpdf.py -h
for help

**Desktop GUI version
install Gooey:
	pip install Gooey
then run
	./genpdf

**Web-based version
For a web interface, run as server:
	./flask_webapp.py 

Then connect to http://localhost:5000

**Dockerized version (Debian/Linux):
Run:
	docker build -t mystara:npcs-slim .
	docker run -p 5000:5000 mystara:npcs-slim 

Then connect to http://localhost:5000

