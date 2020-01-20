#!/bin/bash

while true
do 
    v=$RANDOM
    if [ "$v" -gt 16000 ]
    then
        echo $v Error
    else
        echo $v Good
    fi
    sleep 0.1
done

