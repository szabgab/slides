#!/bin/bash

read -p "Please type in your name: " name
if [ "$name" = "" ]
then
    echo "Name was missing"
    exit 1
fi
