.PHONY: install test

default: unittest

install:
	pipenv install --dev --skip-lock

unittest:
ifndef VIRTUAL_ENV
	$(error must run target inside python virtualenv)
endif
	pytest -m "not puzzle" $(ARGS)

test:
ifndef VIRTUAL_ENV
	$(error must run target inside python virtualenv)
endif
	pytest $(ARGS)

format:
ifndef VIRTUAL_ENV
	$(error must run target inside python virtualenv)
endif
	autopep8 --in-place --recursive .