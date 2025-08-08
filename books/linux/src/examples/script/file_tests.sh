if [ $# != 1 ]
then
   echo "Usage $0 FILE"
   exit 1
fi

if [ ! -e $1 ]
then
    echo "$1 does NOT exist"
    exit
fi

if [ -f $1 ]
then
   echo $1 if a file
   exit
fi

if [ -d $1 ]
then
   echo $1 if a directory
   exit
fi

