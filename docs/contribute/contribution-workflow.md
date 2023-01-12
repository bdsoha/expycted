# Contribution Workflow & Styleguides

## Code of Conduct

This project and everyone participating in it is governed by the [Expycted Code of Conduct](https://github.com/bdsoha/expycted/blob/master/.github/CODE_OF_CONDUCT.md).
By participating, you are expected to uphold this code. Please report unacceptable behavior to support@expycted.com.

## We Develop with GitHub

We utilize GitHub's services at the core of our development:

- To host code.
- To track issues and feature requests.
- Accept and review pull requests.

## Workflow

### Branching Scheme

Our project utilized the **GitFlow** branching scheme. GitFlow utilizes the core feature of Git, which is the power of branches. More information about this workflow can be found in this [cheatsheet](https://danielkummer.github.io/git-flow-cheatsheet/) or [GitFlow examples](https://gitversion.readthedocs.io/en/latest/git-branching-strategies/gitflow-examples/).

In this model, a repository has two main branches:

1. **Master:** This is a highly stable branch that is always production-ready and contains the lastest release version of the published package.

2. **Develop:** Derived from the master branch, the development branch serves as a branch for integrating different features planned for an upcoming release. This branch may or may not be as stable as the master branch. It is where developers collaborate and merge feature branches. It contains a version that is due to be released in an upcoming version.

::: warning
The previous two branches are the starting points for any project. They are very important and should be protected against accidental deletion and merging. Only authorized contributors or project owners should be given the responsibility to merge changes from other branches -- such as the feature branch, which we’ll discuss later -- to the `develop` or `master` branches.
:::

Apart from the two abovementioned primary branches, there are other branches in the workflow:

1. **Feature:** The feature branch splits from the develop branch and merges back to the develop branch after a feature is complete. The conventional naming of this branch starts with `feature/*` in lower-kebab-case *(i.e. `feature/some-new-super-cool-feature`)*. This branch is mostly created and used by developers collaborating with teams. The purpose of the feature branch is to develop small modules of a feature in a project. The lifetime of a feature branch ends once it merges with the develop branch. Features are generally not published to the remote repository, unless multiple developers or teams are working on the same feature.

2. **Hotfix:** The hotfix branch is derived from the master branch and merged back after completion to the develop and master branches. By convention, the name of this branch starts with `hotfix/*` in lower-kebab-case *(i.e. `hotfix/oops-we-found-a-not-so-cool-bug`)*. This branch is created and used after a particular version of product is released to provide critical bug fixes for the production version.

### Creating a Fork

Just head over to [Expycted's GitHub](https://github.com/bdsoha/expycted) page and click the "Fork" button. It's just that simple. Once you've done that, you can use your favorite git client to clone your repo or just head straight to the command line:

```sh
# Clone your fork to your local machine
git clone git@github.com:{USERNAME}/expycted.git  # <--- Replace with your username
```


## Styleguides

### Git Commit Messages

- Start all commit messages with a capital letter.
- Use the present tense *(i.e. "Add feature..." not "Added feature...")*.
- Use the imperative mood *(i.e. "Move cursor to..." not "Moves cursor to...")*.
- Limit the first line to 72 characters or less.
- Reference issues and pull requests at the end of the first line following a `,` *(i.e. "Add feature log, closes #44")*.

### Python Styleguide

All Python code is formatted with [Black](https://github.com/psf/black) and linted using [Ruff](https://github.com/charliermarsh/ruff).
Both of the above mentioned tools are automatically executed using *pre-commit-hooks*. Have a look at [Development Install →](/development-install) for more details on installing and running the hooks.

### Documentation Styleguide

**@TODO:** TBD

### File Naming Conventions

**@TODO:** TBD

## License

**Any contributions you make will be under the *MIT Software License*.**
In short, when you submit code changes, your submissions are understood to be under the same [MIT License](https://github.com/bdsoha/expycted/blob/master/LICENSE) that covers the project. Feel free to contact support@expycted.com if that's a concern.
