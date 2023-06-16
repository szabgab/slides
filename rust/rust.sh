#!/usr/bin/bash -e

if [ "$1" == "" ];
then
    echo "Usage: $0 path/to/file.rs"
    exit 1
fi

# rustc $1
# name=$(basename $1 .rs)
# ./$name

rustc $1 -o myexe
shift
if [ -f myexe ];
then
    ./myexe $*
    \rm myexe
fi
