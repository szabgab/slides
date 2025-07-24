# Teiphy

* [Teiphy](https://github.com/jjmccollum/teiphy)

Steps to run tests on a docker container:

```
git clone https://github.com/jjmccollum/teiphy.git
cd teiphy
docker run -it --name teiphy -w /opt -v$(pwd):/opt python:3.11 bash
pip install poetry
poetry install
poetry run pytest
```


