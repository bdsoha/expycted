# Development Install

Before you begin, check your Python version with the following command:
```sh
$ python --version
Python 3.9.10
```
If your version is `3.7` or greater, you're ready to go.
Otherwise, follow the link to download a newer version of [Python](https://www.python.org/downloads/).

You can clone the repository and build your own distribution using [Setuptools](https://setuptools.pypa.io/en/latest/):

#### 1. Clone the repository
```sh
git clone https://github.com/bdsoha/expycted.git
```

#### 2. *(Optional)* Create a virtual environment
```sh
python -m venv venv
source ./venv/bin/activate
```

#### 3. Install dependencies
```sh
pip install build
pip install -e .[dev]
```

#### 4. Run tests
```sh
python -m pytest
```

#### 5. *(Optional)* Setup pre-commit & run
```sh
pre-commit install
pre-commit run --all-files
```

#### 6. Build the package
```sh`
python -m build
```
