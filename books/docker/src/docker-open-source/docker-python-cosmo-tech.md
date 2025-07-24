# Cosmo-Tech


* [Cosmo-Tech](https://github.com/Cosmo-Tech/CosmoTech-Acceleration-Library)

```
$ git clone https://github.com/Cosmo-Tech/CosmoTech-Acceleration-Library.git
$ cd CosmoTech-Acceleration-Library
```

For Windows:
CMD:

```
$ docker run -it --name cosmotech-acceleration-library-dev -w /opt -v %cd%:/opt python:3.11 bash
```

PowerShell:

```
$ docker run -it --name cosmotech-acceleration-library-dev -w /opt -v ${PWD}:/opt python:3.11 bash
```

For Linux:

```
$ docker run -it --name cosmotech-acceleration-library-dev -w /opt -v $(PWD):/opt python:3.11 bash
```

```
# pip install -r requirements.txt
# pip install pytest
# pytest
```

```
$ docker container start -i cosmotech-acceleration-library-dev
```


