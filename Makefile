.PHONY: run test check clean compose-up compose-down

run:
	python -m app.cli.main tests/fixtures/sample_data.json

test:
	python -m unittest discover -s tests

check: test run

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +

compose-up:
	docker compose -f infra/compose.yaml run --rm ads-calculator

compose-down:
	docker compose -f infra/compose.yaml down -v

build-lib:
	python -m pip install build
	python -m build

install-lib-local:
	pip install -e .