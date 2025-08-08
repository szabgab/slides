#!/bin/bash

acme[0]="Foo"
acme[1]="Bar"
acme[4]="Quix"

echo $acme
echo $acme[1]
echo ${acme[1]}
echo ${#acme}   # number of elements

echo '-----'
for i in 0 1
do
    echo ${acme[i]}
done

echo '----'
for x in ${acme[*]}
do
   echo $x
done

echo '----'
for x in ${acme[@]}
do
   echo $x
done
