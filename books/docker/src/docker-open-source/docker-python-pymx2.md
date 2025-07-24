# pymx2



* [pymx2](https://github.com/vpaeder/pymx2)

```
$ git clone https://github.com/vpaeder/pymx2.git
$ cd pymx2
```

For Windows:
CMD:

```
$ docker run -it --name pymx2-dev -w /opt -v %cd%:/opt python:3.11 bash
```

PowerShell:

```
$ docker run -it --name pymx2-dev -w /opt  -v ${PWD}:/opt python:3.11 bash
```

For Linux:

```
$ docker run -it --name pymx2-dev -w /opt  -v $(PWD):/opt python:3.11 bash
# python -m setup install
```

```
# python -m unittest
```

```
$ docker container start -i pymx2-dev
```


