.PHONY: install lint test train

install:
	uv sync

lint:
	uv run ruff check src/ tests/

test:
	uv run pytest tests/

train:
	uv run python src/credit_classification_pipeline/modeling/train.py