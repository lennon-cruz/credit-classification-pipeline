# Contributing to the ML Pipeline

We follow Trunk-Based Development and strict Conventional Commits to keep our ML workflows auditable and our CI/CD pipelines automated.

**Branching Strategy**
Do not commit directly to `main`. Create short-lived branches using these prefixes:

- `feat/`: New models, features, or pipeline stages.
- `fix/`: Bug fixes or resolving pipeline crashes.
- `chore/`: Tooling, dependency, or configuration updates.
- `exp/`: Exploratory Jupyter notebooks and data investigations.
- `refactor/`: Code restructuring (e.g., extracting logic into a `DataLoader` or `FeatureBuilder`).

**Commit Message Format**
We enforce the Conventional Commits standard: `type(scope): description`.

**Allowed Types:**

- `feat`: Adds new ML functionality or endpoint.
- `fix`: Resolves an issue.
- `refactor`: Restructures code without changing behavior.
- `docs`: Updates to README or documentation.
- `test`: Adding or fixing unit tests.
- `chore`: Maintenance tasks.

*Example:* `feat(model): train logistic regression baseline`

**Install the Commit-Message Hook**

```bash
uv run pre-commit install --hook-type commit-msg
```

```bash
uv run pre-commit install --hook-type pre-commit --hook-type commit-msg
```