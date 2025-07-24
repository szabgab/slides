# Install a package - failure


```
$ ansible virtualhosts -m apt -a "name=nginx state=present" -b
```

The `apt` command will fail - untill now we run everything with our user.

To run commands as root we need to give passwordless sudo permission for the user we connect as.


