# Exercise: OOP


Take the code from the "Read only attributes" examples and change
the module so that it will throw an exception is someone tries
to set the value.


Once that's ready, change the script that it will catch the exception,
display a warning and keep running.


Take a look at the code.pl file in the "Singleton" example.
It tells the problem is in the Conf.pm file. This is not true.
The problem was actually in the calling script, it was discovered
in the Conf.pm module. Change the module so the exception will include
the file name and line number in the script.

Take the wedding example and change it so if we call ->marry
once we will end up with both names changed to the same combined name.


Take the code where people can get married and for each person in the couple
add a way to access the object of the other person. Check (in a destructor)
what happens when of the object goes out of scope?


Fix the code in the class-method example, to reduce the counter when the object goes out of scope.



