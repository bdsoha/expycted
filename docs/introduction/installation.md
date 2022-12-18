# Installation

> Requirements: [Python 3.7+](https://www.python.org/downloads/).

**Expycted** can be installed from [PyPi](https://pypi.org/project/expycted/) using `pip` by running:

```sh
pip install expycted
```

::: info
Expycted won't clutter your environment, it is very small *(`8.9kB`)* and has no additional dependencies.
:::

## Development

Alternatively, you can clone the repository and build your own distribution using [Setuptools](https://setuptools.pypa.io/en/latest/):

```sh
# Clone the repository
git clone https://github.com/bdsoha/expycted.git

# (Optional) Create a virtual environment
python -m venv venv
source ./venv/bin/activate

# Install dependencies
pip install build
pip install -e .[dev]

# Run tests
pytest

# Build the package
python -m build
```
