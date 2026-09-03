# ML Base Template

A logical, opinionated project structure for machine learning work — training, feature stores, experiment tracking, and serving — generated with [Copier](https://copier.readthedocs.io/).

Inspired by [Cookiecutter Data Science](https://github.com/drivendataorg/cookiecutter-data-science).

## Requirements

- Python 3.11+ (default template target is configurable)
- [uv](https://docs.astral.sh/uv/)
- [Copier](https://copier.readthedocs.io/)

```bash
# Recommended: install Copier with uv
uv tool install copier
```

## Starting a new project

```bash
copier copy https://github.com/lennon-cruz/ml-base-template.git path/to/your-project
```

Copier will prompt for project name, Python package name, author, and Python version, then render the tree below.

### After generation

```bash
cd path/to/your-project
make install   # uv sync
make lint      # ruff
make test      # pytest
make train     # run modeling/train.py
```

## Project structure

```
├── LICENSE                 <- MIT license
├── Makefile                <- Convenience commands (install, lint, test, train)
├── README.md               <- You are here
├── Dockerfile              <- Multi-stage image for the FastAPI serve path
├── pyproject.toml          <- Package metadata and dependencies (uv / PEP 621)
├── configs/
│   └── model.yaml          <- Model hyperparameters (tracked by MLflow)
├── data
│   ├── raw                 <- Original, immutable data dump
│   ├── staging             <- Landing / lightly cleaned extracts
│   ├── silver              <- Cleaned, conformed datasets
│   └── gold                <- Feature-ready / modeling tables
├── docs                    <- Project documentation
├── feature_repo            <- Feast feature store (feature_store.yaml, feature_views)
├── models                  <- Trained artifacts (gitignored except .gitkeep)
├── notebooks               <- Exploratory Jupyter notebooks
├── src
│   └── credit_classification_pipeline   <- Installable Python package
│       ├── config.py       <- Pydantic validation for configs
│       ├── data/           <- Data loading and transforms
│       ├── features/       <- Feature engineering helpers
│       ├── modeling
│       │   ├── predict.py  <- Inference with trained models
│       │   └── train.py    <- Training entrypoint
│       └── serve
│           └── app.py      <- FastAPI service
└── tests                   <- Pytest suite
```

## Stack

| Concern            | Tool                          |
|--------------------|-------------------------------|
| Packaging / env    | uv + `pyproject.toml`         |
| Tabular ML         | scikit-learn, XGBoost, pandas |
| Experiment tracking| MLflow                        |
| Feature store      | Feast                         |
| Serving            | FastAPI                       |
| Lint               | Ruff                          |

## License

MIT — see [LICENSE](LICENSE).
