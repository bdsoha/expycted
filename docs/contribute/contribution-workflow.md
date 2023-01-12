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

The **Forking Workflow** is fundamentally different than other popular Git workflows. Instead of using a single server-side repository to act as the *central* codebase, it gives every developer their own server-side repository.

The main advantage of the **Forking Workflow** is that contributions can be integrated without the need for everybody to push to a single central repository. Developers push to their own server-side repositories, and only the project maintainer can push to the official repository. This allows the maintainer to accept commits from any developer without giving them write access to the official codebase.

The workflow typically follows a branching model based on the [Gitflow Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow). This means that complete feature branches will be purposed for merge into the original project maintainer's repository.

In this model, a repository has two main branches:

1. **Master:** This is a highly stable branch that is always production-ready and contains the lastest release version of the published package.

2. **Develop:** Derived from the master branch, the development branch serves as a branch for integrating different features planned for an upcoming release. This branch may or may not be as stable as the master branch. It is where developers collaborate and merge feature branches. It contains a version that is due to be released in an upcoming version.

::: warning
The previous two branches are the starting points for any project. They are very important and should be protected against accidental deletion and merging. Only authorized contributors or project owners should be given the responsibility to merge changes from other branches -- such as the feature branch, which we’ll discuss later -- to the `develop` or `master` branches.
:::

Apart from the two abovementioned primary branches, there are other branches in the workflow:

1. **Feature:** The feature branch splits from the develop branch and merges back to the develop branch after a feature is complete. The conventional naming of this branch starts with `feature/*` in lower-kebab-case *(i.e. `feature/some-new-super-cool-feature`)*. This branch is mostly created and used by developers collaborating with teams. The purpose of the feature branch is to develop small modules of a feature in a project. The lifetime of a feature branch ends once it merges with the develop branch. Features are generally not published to the remote repository, unless multiple developers or teams are working on the same feature.

2. **Hotfix:** The hotfix branch is derived from the master branch and merged back after completion to the develop and master branches. By convention, the name of this branch starts with `hotfix/*` in lower-kebab-case *(i.e. `hotfix/oops-we-found-a-not-so-cool-bug`)*. This branch is created and used after a particular version of product is released to provide critical bug fixes for the production version.

#### Step-by-Step

::: tip
The section below was extracted from an online tutorial, for a more in-depth explaination, have a look at the [orginial tutorial](https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow).
:::

The following is a step-by-step example of this workflow:

1. A developer creates a [*fork*](https://github.com/bdsoha/expycted/fork) of Expycted.
2. Cloned to their local system.
3. A Git remote path for the *official* repository is added to the local clone.
4. A new local feature branch is created *(usually a `feature/*` branch)*.
5. The developer makes changes on the new branch.
6. New commits are created for the changes.
7. The branch gets pushed to the developer's fork.
8. The developer opens a pull request from the new branch to the *official* repository.
9. The pull request gets approved for merge and is merged into the original server-side repository.

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

[Pydocstyle](https://github.com/PyCQA/pydocstyle) is used as a static analysis tool for checking compliance of docstring conventions.

We ignore the follow rules *(for a [full set of available rules](http://www.pydocstyle.org/en/2.1.1/error_codes.html))*:

- `D100`
- `D101`
- `D105`
- `D107`
- `D202`
- `D203`

### File Conventions

#### File Structure

The project structure is split into various folder for organizational purposes.
The tree below displays the main files and folders and their intended use.

```text
.
├── .github                 // Workflows, issue templates, pull request templates, and other GitHub related
├── .gitignore              // Files to not track in `git`
├── build                   // Automatically generated build (git-ignored)
├── dist                    // Automatically generated build (git-ignored)
├── docs                    // Documentation resources
│   ├── .vitepress          // Configuration for the documentation website
│   ├── *.md                // Actual docmentation files
│   └── index.md            // Documentation entrypoint
├── node_modules            // Node packages for documentation (git-ignored)
├── package.json            // Node package dependencies for docs (should be changed using `npm`)
├── src                     // The main programming directory
│   └── core                // Core functionality shared accross the package
│   ├── matchers            // Common matchers provided with package as default
│   └── ...                 // Additional custom matchers
├── test                    // The main test directory
│   ├── helpers             // Global test utilities
│   ├── unit                // Unit test (follow the same folder layout as `src`)
│   └── conftest.py         // Setup the test suite
├── pyproject.toml          // Build system requirements and information, used by pip to build the package
└── yarn.lock               // Current status of the installed modules (should not be edited)
```

#### Naming Conventions

Your files should follow the conventions below:

- Must end in a `.py`.
- Must be in *snake_case*, *(use underscore characters `_` instead of dashes `-`)*.
- Lowercase characters only.
- Should represent the *main* exported `class` or `function`.

Your folders should follow the conventions below:

- May not contain any special charachters *(including spaces)*.
- Lowercase characters only.

## License

**Any contributions you make will be under the *MIT Software License*.**
In short, when you submit code changes, your submissions are understood to be under the same [MIT License](https://github.com/bdsoha/expycted/blob/master/LICENSE) that covers the project. Feel free to contact support@expycted.com if that's a concern.
