# Continuous Integration for GitHub projects 
{id: index}

## Self introduction
{id: self-introduction}

* [Gabor Szabo](https://www.linkedin.com/in/szabgab/) @szabgab
* [Code Mavens Workshops](https://www.meetup.com/Code-Mavens/)

## Git
{id: git}

* Distributed Version Control System

## GitHub
{id: github}

* Cloud-based hosting for git repositories
* Now owned by Microsoft

## CI - Continuous Integration
{id: ci}

* As frequently as possible
* Check if all the code works together

## When to run?
{id: when-to-run}

* "Nightly build"
* ...
* On each push

## What to run?
{id: what-to-run}

* Compile
* Unit tests
* Integration test
* Whatever you can

## Cloud-based CI system
{id: cloud-based-ci}

* [Travis-CI](https://travis-ci.org/)
* [Appveyor](https://www.appveyor.com/)
* [Circle CI](https://circleci.com/)
* ...


## Travis-CI
{id: travis-ci}

* Register at [Travis-CI](https://travis-ci.org/) using yout GitHub credentials.
* Tell Travis to sync the accounts if needed (if it is a recently created repo).
* Add .travis.yml to the repository and push it out.

## Travis Examples: simple verification
{id: travis-examples-1}

* [simple verification](https://github.com/collab-dev/participants)

```
language: python
python:
  - "3.6"
script: python test.py
```

## Travis Examples: several keys
{id: travis-examples-2}

* [](https://github.com/szabgab/codeandtalk.com/)

```
language: python
python:
  - "3.5"
  - "3.6"
install:
  - pip install pytest
  - pip install pytest-cov
  - pip install coveralls
  - pip install -r requirements.txt
before_script:
  - python bin/generate.py
script:
  - pytest --cov=cat/
after_success:
- coveralls
```

## Exercises
{id: exercises}

* [](https://github.com/collab-dev/python-with-test)
* [](https://github.com/collab-dev/python-without-test)


## Thank you
{id: thank-you}

* [Gabor Szabo](https://www.linkedin.com/in/szabgab/) @szabgab
* [Code Mavens Workshops](https://www.meetup.com/Code-Mavens/)
