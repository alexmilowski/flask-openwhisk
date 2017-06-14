ACTION=flask

all: build

setup:
	virtualenv virtualenv
	. virtualenv/bin/activate; pip install -r requirements.txt
	. virtualenv/bin/activate; pip install .

clean:
	rm -rf virtualenv web.zip

build:
	zip -r web.zip __main__.py web.py virtualenv/

create:
	wsk action create $(ACTION) --kind python:3 web.zip --web raw

update:
	wsk action update $(ACTION) --kind python:3 web.zip --web raw

delete:
	wsk action delete $(ACTION)

test:
	curl $(OPENWHISK)/flask/echo
