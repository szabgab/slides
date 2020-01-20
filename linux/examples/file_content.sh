#!/bin/bash

DIR='file_content'
FILE=$DIR/data.txt

if [ -e $DIR ]
then
   echo "$DIR already exists"
   exit
fi

echo "Creating directory $DIR"
mkdir $DIR

cat<<TEXT > $FILE
Hello World
This is the second line
1 hundred 2 hunderd 3 hundred
TEXT

