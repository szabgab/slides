# DVC

Storage can be
* local disk
* cloud
* HDFS


```
pip install dvc


git init   (creating .git)
dvc init   (creating .dvc and .dvcignore)


dvc remote add -d dvc-remote /tmp/dvc-demo-storage   (changing .dvc/config)


dvc add data/data.csv

git add .
git commit -m "data:  ...."
git tag -a v1 -m v1


dvc push
```

* Files are now in `/tmp/dvc-demo-storage`
* Files are also in `.dvc/cache`


```
dvc pull
dvs status
```

