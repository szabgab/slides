# Add public key

```
$ scp .ssh/id_rsa.pub foo@localhost:

$ ssh foo@localhost

# if .ssh does not exist yet:

$ mkdir .ssh
$ ls -ld .ssh
drwxrwxr-x 2 foo foo 4096 Jul 17 05:51 .ssh/
$ chmod 0700 .ssh/


$ cat id_rsa.pub >> .ssh/authorized_keys
$ rm id_rsa.pub
```



