#!/bin/bash

[ -e "$some_file" ] && rm -f "$some_file"

[ -e "$some_file" ] || touch  "$some_file"
