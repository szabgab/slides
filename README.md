# Slides
[![Build Status](https://travis-ci.org/szabgab/slides.png)](https://travis-ci.org/szabgab/slides)

The source of most of the slides at https://code-maven.com/slides/


## Processing

Processing assumes https://github.com/szabgab/slider-py is cloned next to this directory.

```
python ../slider-py/slider/__init__.py --md linux-intro/intro.md --html --dir html --templates templates/ --static static/
```

Generate all the slides by running:

```
./generate_slides.py
```

or just some of them by listing their names:

```
./generate_slides.py golang groovy
```

Processing errors are reported in https://code-maven.com/slides/errors.txt

To test locally or in a connected browser use

```
python app.py
```
