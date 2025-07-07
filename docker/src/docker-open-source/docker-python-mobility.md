# mobility

* [mobility](https://github.com/mobility-team/mobility)

```
$ git clone https://github.com/mobility-team/mobility.git
$ cd mobility
```

For Windows:
CMD:

```
$ docker run -it --name mobility-dev -w /opt -v %cd%:/opt python:3.9 bash
```

PowerShell:

```
$ docker run -it --name mobility-dev -w /opt -v ${PWD}:/opt python:3.9 bash
```

For Linux:

```
$ docker run -it --name mobility-dev -w /opt -v $(PWD):/opt python:3.9 bash
```

```
# pip install -r requirements.txt && pip install -e .
# pip install pytest
# pytest
```

```
$ docker container start -i mobility-dev
```


