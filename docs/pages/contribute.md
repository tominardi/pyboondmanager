# Contributor’s Guide

## Pre-commit

We use a tool called [pre-commit](https://pre-commit.com/) to run a lot of validation before commiting. Before working on the repository, please run the following command :

```bash
pre-commit install
```

## Code

When contributing code, you’ll want to follow this checklist:

1. Fork the repository on GitHub.
2. Run the tests to confirm they all pass on your system. If they don’t, you’ll need to investigate why they fail. If you’re unable to diagnose this yourself, raise it as a bug report by following the guidelines in this document: Bug Reports.
3. Write tests that demonstrate your bug or feature. Ensure that they fail.
4. Make your change.
5. Run the entire test suite again, confirming that all tests pass including the ones you just added.
6. Commit your changes, with a clear message. Please send your changes in logical commits, basically one commit for one feature. Consider to amend your commit if needed.
7. Send a GitHub Pull Request to the main repository’s main branch. GitHub Pull Requests are the expected method of code collaboration on this project.

The following sub-sections go into more detail on some of the points above.

## Code style

We follow the pep8, and we use pylint. The `setup.cfg` file contains all the settings for these two tools.

## Bug reports

Please report bugs on GitHub.
