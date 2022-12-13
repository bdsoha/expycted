# Installation

> Requirements: [Python 3.7+](https://www.python.org/downloads/).

**Expycted** has no additional dependencies and can be installed from [PyPi](https://pypi.org/project/expycted/) using `pip` by running:

```sh
$ pip install expycted
```

## Development

Alternatively, you can clone the repository and build your own distribution using [Setuptools](https://setuptools.pypa.io/en/latest/):

```sh
# Clone the repository
$ git clone https://github.com/bdsoha/expycted.git

# (Optional) Create a virtual environment
$ python -m venv venv
$ source ./venv/bin/activate

# Install dependencies
$ pip install build
$ pip install -e .[dev]

# Run tests
$ pytest

# Build the package
$ python -m build
```
