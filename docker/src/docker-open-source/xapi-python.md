# xapi-python

* [xapi-python](https://github.com/pawelkn/xapi-python)

Steps to run tests on a docker container:

```
git clone https://github.com/pawelkn/xapi-python.git
cd xapi-python
docker run -it --name xapi-python -w /opt -v$(pwd):/opt python:3.11 bash
python3 -m unittest discover tests
```


