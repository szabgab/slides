# Continuous Integration for GitHub projects 
{id: index}

## Self introduction
{id: self-introduction}

* [Gabor Szabo](https://www.linkedin.com/in/szabgab/) @szabgab
* Helping with DevOps and Agility
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

* Compilation
* Unit tests
* Integration tests
* Acceptances tests
* ...
* Whatever you can

## CD - Continuous Delivery (or Deployment)
{id: cd}

* After tests are successful, automatially deploy the code.

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
* Add .travis.yml to the toot of the repository and push it out.

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

* [codeandtalk](https://github.com/szabgab/codeandtalk.com/)

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

## Coveralls
{id: coveralls}

* [Coveralls](https://coveralls.io/)

## Appveyor
{id: appveyor}

* Windows
* Now Linux as well

* Register at [Appveyor](https://www.appveyor.com/)
* Connect your GitHub account
* Enable the repository
* Create the `appveyor.yml` or `.appveyor.yml` file
* Push it out

## Appveyor Example
{id: appveyor-example}

* [codeandtalk](https://github.com/szabgab/codeandtalk.com/)

```
build: false

environment:
  matrix:
    - PYTHON: "C:\\Python34"
      PYTHON_VERSION: "3.4.1"
      PYTHON_ARCH: "32"

    - PYTHON: "C:\\Python36"
      PYTHON_VERSION: "3.6.3"
      PYTHON_ARCH: "32"
init:
  - "ECHO %PYTHON% %PYTHON_VERSION% %PYTHON_ARCH%"

install:
  - "%PYTHON%/Scripts/pip.exe install pytest"
  - "%PYTHON%/Scripts/pip.exe install ."

test_script:
- "%PYTHON%/Scripts/pytest.exe"
```

## Exercises
{id: exercises}

* [](https://github.com/collab-dev/python-with-test)
* [](https://github.com/collab-dev/python-without-test)

* For the repository so you have your own copy
* Clone the forked repo

* Enable Travis, Appveyor
* Add tests
* Add badges to the `README.md` of the repo.
* Add test coverage reporting

## Thank you
{id: thank-you}

* [Gabor Szabo](https://www.linkedin.com/in/szabgab/) @szabgab
* [Code Mavens Workshops](https://www.meetup.com/Code-Mavens/)

