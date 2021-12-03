.PHONY: install test

default: unittest

install:
	python3 -m pipenv install --dev --skip-lock

shell:
	python3 -m pipenv shell

unittest:
ifndef VIRTUAL_ENV
	$(error must run target inside python virtualenv)
endif
	PYTHONPATH=. pytest -m "not puzzle"

test:
ifndef VIRTUAL_ENV
	$(error must run target inside python virtualenv)
endif
	PYTHONPATH=. pytest --durations=0

test2018:
ifndef VIRTUAL_ENV
	$(error must run target inside python virtualenv)
endif
	PYTHONPATH=. pytest --durations=0 aoc2018

test2021:
ifndef VIRTUAL_ENV
	$(error must run target inside python virtualenv)
endif
	PYTHONPATH=. pytest --durations=0 aoc2021

format:
ifndef VIRTUAL_ENV
	$(error must run target inside python virtualenv)
endif
	autopep8 --in-place --recursive .