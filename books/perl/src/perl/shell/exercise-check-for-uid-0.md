# Exercise: Check for UID 0


In UNIX/Linux the information about users is kept in the
/etc/passwd file. Each line represents a user. The fields
in each line are as follows:
`username, password,UID,GID,Gecos,home directory,shell`
Today the passwords are usually kept separately hence in this file you will only
see an x in the second field.




When someone breaks in to a UNIX/Linux machine she might try to
setup a user with UID 0 in order to gain root (superuser) access
to the machine. Please check the following file
and print a message if there is a user with 0 as UID which is NOT
the root user.


{% embed include file="src/examples/shell/etc_passwd.txt" %}


