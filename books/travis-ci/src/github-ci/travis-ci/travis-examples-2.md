# Travis Examples: several keys


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


