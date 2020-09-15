# CI

We have the following CI workflows in CirclCI.

## integrate

The main workflow for new commits. The following jobs are done:
- Check project codestyle.
- Build and test toppra on Python 3 and the C++ API.

## release

Check release branch for proper version.


## publish

Publish source code to venues (PyPI). NOTE: This is currently not done.


# Github Action
Some tasks are done directly with Github Action. 

- Linting for C++ code with clang-tidy.

  Note: `cppcoreguidelines-pro-bounds-array-to-pointer-decay` leads to false reported error, thus disabled.

