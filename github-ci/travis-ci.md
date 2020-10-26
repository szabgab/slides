# Travis-CI
{id: travis-ci}

## Enable Travis-CI
{id: enable-travis-ci}

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


