# ftp

```
$ sudo aptitude install proftpd
$ sudo /etc/init.d/proftpd start
$ sudo adduser   (user: foo pw: bar)
```
{% embed include file="src/examples/net/ftp.py" %}

```
-rw-rw-r--   1 foo      foo             6 Feb 18 19:18 a.txt
-rw-rw-r--   1 foo      foo             6 Feb 18 19:18 b.txt
226 Transfer complete
-------
file: b.txt
file: a.txt
-------
file: b.txt
file: a.txt
file: ssh.py
-------
file: b.txt
file: a.txt
```


