# Python penn



[penn](https://github.com/interactiveaudiolab/penn)


There is no contribution file, but there is an explanation of how to clone and run the project in the readme file.
Added a [contribution.md](https://github.com/interactiveaudiolab/penn/pull/4) file with the following instructions:

```
git clone https://github.com/interactiveaudiolab/penn
cd penn
docker run -it --name penn_test -w /opt -v <working directory>\penn:/opt python:3.11 bash
$ pip install -r requirements.txt && pip install -e .
```


