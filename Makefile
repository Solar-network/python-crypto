test:
	pytest -v -s $(ARGS)

format: isort black flake8

isort:
	isort crypto/ tests/

black:
	black .

flake8:
	flake8 .
