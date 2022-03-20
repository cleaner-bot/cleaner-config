install:
	pip install .

lint:
	flake8 . --max-line-length 88 --exclude build
	mypy . --exclude build
	codespell . --skip ".*"

test-all: coverage lint
