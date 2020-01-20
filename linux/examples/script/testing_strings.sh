#!/bin/bash

s1="abc def"
s2="abc"
echo "s1=$s1"
echo "s2=$s2"

if [ "$s1"  = "$s2" ]; then echo "equal"; fi
if [ "$s1" != "$s2" ]; then echo "not equal"; fi
if [ "$s1" \< "$s2" ]; then echo "smaller in lexical order"; fi
if [ "$s1" \> "$s2" ]; then echo "larger in lexical order"; fi
if [ -z "$s1" ]; then echo "length of string is zero"; fi
if [ -n "$s1" ]; then echo "length of string is NOT zero"; fi

# variables should be enclosed in ""
# in order to avoid issues with spaces in the variables.

