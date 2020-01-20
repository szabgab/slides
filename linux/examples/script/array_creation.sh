#!/bin/bash

declare -a week=(Mon Tue Wed Thu Fri Sat Sun)
echo $week
echo '-----'

for day in ${week[*]}
do
   echo $day
done
