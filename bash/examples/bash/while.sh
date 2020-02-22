#!/usr/bin/env bash

while [[ -f /tmp/run ]]
do
  echo "Running"
  sleep 2
done

echo done

