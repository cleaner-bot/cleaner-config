install:
	pip install .

test:
	pytest .

coverage:
	coverage run -m pytest .
	coverage report -m --fail-under 100

lint:
	flake8 . --max-line-length 88
	mypy .
	codespell . --skip ".*"

test-all: coverage lint
