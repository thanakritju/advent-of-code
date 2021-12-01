.PHONY: install test

default: unittest

install:
	pipenv install --dev --skip-lock

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