.PHONY: run test check clean

run:
	python -m app.cli.main tests/fixtures/sample_data.json

test:
	python -m unittest discover -s tests

check: test run

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +