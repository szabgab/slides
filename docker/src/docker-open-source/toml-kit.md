# TOML Kit

* [tomlkit](https://github.com/sdispater/tomlkit)

Steps to run tests on a docker container:

```
git clone --recurse-submodules https://github.com/sdispater/tomlkit.git
cd tomlkit
docker run -it --name toml -w /opt -v$(pwd):/opt python:3.11 bash
pip install poetry
pip install pytest
poetry install
poetry run pytest -q tests
```


