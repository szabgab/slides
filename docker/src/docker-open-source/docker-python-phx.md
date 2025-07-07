# PHX

* [PHX](https://github.com/PH-Tools/PHX)

```
$ git clone https://github.com/PH-Tools/PHX.git
$ cd PHX
```

For Windows:
CMD:

```
$ docker run -it --name phx-dev dev -w /opt -v %cd%:/opt python:3.7 bash
```

PowerShell:

```
$ docker run -it --name phx-dev -w /opt -v ${PWD}:/opt python:3.7 bash
```

For Linux:

```
$ docker run -it --name phx-dev -w /opt -v $(PWD):/opt python:3.7 bash
```

```
# pip install -r dev-requirements.txt && pip install -e .
# pytest
```

```
$ docker container start -i phx-dev
```


