test:
	pytest -v -s $(ARGS)

format: isort black flake8

isort:
	isort crypto/ tests/

black:
	black .

flake8:
	flake8 .

cleanup-dist:
	rm -rf dist

build-package:
	python -m build

upload-package:
	python -m twine upload dist/*
