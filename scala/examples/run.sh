#!/bin/bash
if [ "$1" == "" ]
then
   echo "Usage: $0 Some"
   exit 1
fi
echo $1
scalac $1.scala
scala $1
