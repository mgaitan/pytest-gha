# pytest-gha-logs-fold

A pytest plugin designed to enhance the readability of pytest outputs in GitHub Actions logs. It groups sections of verbose outputs, making it easier to navigate and read logs in the GitHub Actions environment.

## Features

- **Folding**: Automatically collapses sections of pytest outputs that can become too verbose, like the collecting phase.
- **Adaptive**: Only activates when the `--fold-for-gha` argument is passed to pytest.
- **Seamless Integration**: Designed specifically for GitHub Actions, but can be used in other CI environments that support the same folding syntax.

## Installation

You can install `pytest-gha-logs-fold` via pip:

```bash
pip install pytest-gha-logs-fold
```

## Usage
To activate the folding feature, simply pass the `--gha-logs-fold` argument when you run pytest:

```
pytest --gha-logs-fold ...
```

## License

MIT

## Contributions

Contributions are welcome! Please submit a pull request or open an issue if you have any enhancements, bug fixes, or suggestions.