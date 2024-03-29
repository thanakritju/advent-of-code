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
	PYTHONPATH=. pytest -m "not puzzle" $(folder)

test:
ifndef VIRTUAL_ENV
	$(error must run target inside python virtualenv)
endif
	PYTHONPATH=. pytest --durations=0 $(folder)

format:
ifndef VIRTUAL_ENV
	$(error must run target inside python virtualenv)
endif
	autopep8 --in-place --recursive .

lint:
ifndef VIRTUAL_ENV
	$(error must run target inside python virtualenv)
endif
	pylint aoc2021