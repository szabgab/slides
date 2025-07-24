# Docker: Mounting external host directory as a volume (Windows hosts)


In CMD window:

```
> docker run -it --rm -v %cd%:/opt/ mydocker
```

In Power Shell:

```
> docker run -it --rm -v ${PWD}:/opt/ mydocker
```

In any case the path to the folder must only contain [a-zA-Z0-9_.-] character so no spaces, no Hebrew characters, etc.


