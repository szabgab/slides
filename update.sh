#!/usr/bin/bash

pull=$(git pull)
if [ "$pull" == "Already up to date." ]
then
    echo "skipping"
else
    echo doing
    /home/gabor/work/slides/venv3/bin/python generate_slides.py --keep --ext '' > /tmp/slides.out 2>/tmp/slides.err
fi

