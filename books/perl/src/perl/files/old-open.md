# Open files in the old way


In old version of perl (before 5.6) we could not use scalar variables as file
handles so we used uppercase letters such as XYZ or INPUT, QQRQ or FILEHANDLE.

Also the function had only 2 parameters.

{% embed include file="src/examples/files-perl/open_file_old.pl" %}

Security problems.

Being global, difficult to pass as parameter to functions.

[Don't Open Files in the old way](https://perlmaven.com/open-files-in-the-old-way)




