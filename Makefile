.PHONY: install lint test train data

install:
	uv sync --group dev

lint:
	uv run ruff check src/ tests/

test:
	uv run pytest tests/

train:
	uv run python src/credit_classification_pipeline/modeling/train.py

data:
	uv run python -m credit_classification_pipeline.data.ingest