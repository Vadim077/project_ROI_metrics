FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt .

COPY . .

ENTRYPOINT ["python", "-m", "app.cli.main", "tests/fixtures/sample_data.json"]