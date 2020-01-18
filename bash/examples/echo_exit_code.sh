#!/usr/bin/env bash

ls  / > /dev/null 2> /dev/null
echo $?         # 0

ls  /qqrq > /dev/null 2> /dev/null
echo $?         # 1

