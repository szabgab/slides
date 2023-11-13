# Slides
[![Build Status](https://travis-ci.org/szabgab/slides.png)](https://travis-ci.org/szabgab/slides)

The source of most of the slides at https://code-maven.com/slides/

The original source is on [GitHub](https://github.com/szabgab/slides)

## Processing

Processing assumes https://github.com/szabgab/slider-py is cloned next to this directory.

```
virtuelenv -p python3 venv
. venv/bin/activate
pip install -r ../slider-py/requirements.txt
```

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

Drakula for pygments
https://github.com/dracula/pygments

## Local server

Install rustatic from https://github.com/szabgab/rustatic

```
rustatic --path html/ --indexfile index.html --nice --port 5000
```
