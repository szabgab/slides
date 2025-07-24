# Overloaded Iterables

* [overloaded_iterables](https://github.com/Arkiralor/overloaded_iterables)

Steps to run tests on a docker container:

```
git clone https://github.com/Arkiralor/overloaded_iterables.git
cd overloaded_iterables
docker run -it --name overloaded_iterables -w /opt -v$(pwd):/opt python:3.11 bash
chmod +x scripts/*
sh scripts/run_tests.sh
```


