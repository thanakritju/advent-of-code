.PHONY: install test

default: test

install:
	pipenv install --dev --skip-lock

test:
ifndef VIRTUAL_ENV
	$(error must run target inside python virtualenv)
endif
	pytest

format:
ifndef VIRTUAL_ENV
	$(error must run target inside python virtualenv)
endif
	autopep8 --in-place --recursive .