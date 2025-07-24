#!/usr/bin/env bash

ls  / > /dev/null 2> /dev/null
exit_code=$?
echo $exit_code
if [ $exit_code = 0 ]; then
    echo /
fi

ls  /qqrq > /dev/null 2> /dev/null
exit_code=$?
echo $exit_code
if [ $exit_code = 0 ]; then
    echo /qqrq
fi

