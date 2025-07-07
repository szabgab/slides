# Python Automation Framework

* [python-automation-framework](https://github.com/mreiche/python-automation-framework)

Steps to run tests on a docker container:

```
git clone https://github.com/mreiche/python-automation-framework.git
cd python-automation-framework
docker run -it --name python-automation-framework -w /opt -v$(pwd):/opt python:3.11 bash
pip install pytest
pip install -r requirements.txt
PYTHONPATH="." pytest --numprocesses=4 --cov=paf test
```



