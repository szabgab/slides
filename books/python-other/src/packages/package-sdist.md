# Create tar.gz file

```
$ python setup.py sdist
```

* mymath.egg-info/
* dist/mymath-0.1.tar.gz



```
running sdist
running egg_info
creating mymath.egg-info
writing mymath.egg-info/PKG-INFO
writing top-level names to mymath.egg-info/top_level.txt
writing dependency_links to mymath.egg-info/dependency_links.txt
writing manifest file 'mymath.egg-info/SOURCES.txt'
reading manifest file 'mymath.egg-info/SOURCES.txt'
writing manifest file 'mymath.egg-info/SOURCES.txt'
warning: sdist: standard file not found: should have one of README, README.txt

creating mymath-0.1
creating mymath-0.1/mymath
creating mymath-0.1/mymath.egg-info
making hard links in mymath-0.1...
hard linking setup.py -> mymath-0.1
hard linking mymath/__init__.py -> mymath-0.1/mymath
hard linking mymath.egg-info/PKG-INFO -> mymath-0.1/mymath.egg-info
hard linking mymath.egg-info/SOURCES.txt -> mymath-0.1/mymath.egg-info
hard linking mymath.egg-info/dependency_links.txt -> mymath-0.1/mymath.egg-info
hard linking mymath.egg-info/not-zip-safe -> mymath-0.1/mymath.egg-info
hard linking mymath.egg-info/top_level.txt -> mymath-0.1/mymath.egg-info
Writing mymath-0.1/setup.cfg
creating dist
Creating tar archive
removing 'mymath-0.1' (and everything under it)
```

