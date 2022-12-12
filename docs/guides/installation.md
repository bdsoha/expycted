# Installation

> Requirements: [Python 3.7+](https://www.python.org/downloads/).

**Expycted** can be installed from [PyPi](https://pypi.org/project/expycted/) via `pip` by running:

```sh
$ pip install expycted
```

## Development

Alternatively, you can clone the repository and build your own distribution using [Poetry](https://python-poetry.org):
```sh
# Clone the repository
$ git clone https://github.com/petereon/expycted.git

# Install dependencies
$ pipenv install

# Run tests
$ pipenv run test

# Build the package
$ pipenv run build
```

Then you can install it using:
```sh
$ pip install ./dist/expycted-<version>-py3-none-any.whl
```