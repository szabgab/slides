#!/bin/bash

declare -i a=2 
declare -i b=3
echo $a
echo $b

a=a+b
echo $a

echo '-----'

a=1
while (( a <= 10 ))
do
   echo $a
   a=$a+1
done
