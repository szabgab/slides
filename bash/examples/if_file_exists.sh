#!/usr/bin/env bash

filename=$1

if [[ -e $filename ]]; then
   echo "File $filename exists"
fi

