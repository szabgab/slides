# nats-python

* [nats-python](https://github.com/Gr1N/nats-python)

Steps to run tests on a docker container:

```
git clone https://github.com/Gr1N/nats-python.git
cd nats-python
docker run -it --name nats-python -w /opt -v$(pwd):/opt python:3.11 bash
pip install poetry
poetry install
make install
make test
```


