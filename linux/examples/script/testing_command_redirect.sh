#!/bin/bash

if [ $# != 1 ]
then
    echo "Usage: $0 username"
    exit 1
fi

if grep "$1" /etc/passwd > /dev/null
then
    echo "Found $1 in /etc/passwd"
fi

