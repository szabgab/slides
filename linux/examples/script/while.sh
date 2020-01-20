#!/bin/bash

secret="my password"
guess=""
while [ "$secret" != "$guess" ]
do
   read -p "What is your secret? " guess
done

echo "Congratulations, you passed the test"
