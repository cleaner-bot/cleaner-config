install:
	pip install .

lint:
	codespell . --skip ".*"

test-all: coverage lint
