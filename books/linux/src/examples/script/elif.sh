if [ $# = 2 ]
then
   echo there are 2 parameters
elif [ $# = 1 ]
then
   echo there is 1 parameter 
else
   echo The number of parameters is $#
fi

