# Development Install

We're really excited that you are interested in contributing to Expycted. Before submitting your contribution, please make sure to take a moment and read through the following guidelines:

- [Code of Conduct →](https://github.com/bdsoha/expycted/blob/master/.github/CODE_OF_CONDUCT.md)
- [Contribution Workflow *(Optional)* →](/get-involved/contribution-workflow)
- [Pull Request Guidelines →](/get-involved/pull-request-guidelines)

## Prerequisites

Before you begin, check your Python version with the following command:

```sh
$ python --version
Python 3.9.10
```

If your version is `3.7` or greater, you're ready to go.
Otherwise, follow the link to download a newer version of [Python](https://www.python.org/downloads/).

## Setup

You can clone the repository and build your own distribution using [Setuptools](https://setuptools.pypa.io/en/latest/):

### 1. Clone the repository

```sh
git clone https://github.com/bdsoha/expycted.git
```

### 2. *(Optional)* Create a virtual environment

```sh
python -m venv venv
source ./venv/bin/activate
```

### 3. Install dependencies

```sh
pip install build
pip install -e .[dev]
```

### 4. Run tests

```sh
python -m pytest
```

### 5. *(Optional)* Setup pre-commit & run

```sh
pre-commit install
pre-commit run --all-files
```

::: tip
This step is automatically run on all *PR*s and *commits*.
If you choose to skip this step, thats OK, we will run it for you during *CI*.
:::

### 6. Build the package

```sh
python -m build
```
