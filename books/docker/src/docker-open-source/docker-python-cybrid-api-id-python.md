# cybrid-api-id-python

* [cybrid-api-id-python](https://github.com/Cybrid-app/cybrid-api-id-python)

```
$ git clone https://github.com/Cybrid-app/cybrid-api-id-python.git
$ cd cybrid-api-id-python
```

For Windows:
CMD:

```
$ docker run -it --name cybrid-api-id-python-dev -w /opt -v %cd%:/opt python:3.11 bash
```

PowerShell:


```
$ docker run -it --name cybrid-api-id-python-dev -w /opt  -v ${PWD}:/opt python:3.11 bash
```

For Linux:

```
$ docker run -it --name cybrid-api-id-python-dev -w /opt  -v $(PWD):/opt python:3.11 bash
```

```
# pip install -r requirements.txt && pip install pytest
# pytest
```

```
$ docker container start -i cybrid-api-id-python-dev
```


