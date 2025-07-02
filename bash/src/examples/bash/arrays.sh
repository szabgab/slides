#!/usr/bin/env bash

count[2]="two"

echo $count[2]      # [2]
echo ${count[2]}    # two

names=(Foo Bar Baz Moose)
echo $names         # Foo
echo ${names[0]}    # Foo
echo ${names[1]}    # Bar
