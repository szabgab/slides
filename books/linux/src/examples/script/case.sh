#!/bin/bash

case "$1" in
   "foo")
        echo "it is foo";;
   [a-z][a-z][a-z])
        echo "3 letters";;
   [0-9][0-9])
        echo "2 digits";;
   42)
        echo "the answer";; 
   *)  
       echo "default";;
esac

