# Networking
{id: python-net}

## Secure shell
{id: secure-shell}

* subprocess + external ssh client
* [Paramiko](http://www.paramiko.org/)
* [Fabric](http://www.fabfile.org/)



## ssh
{id: ssh}

* On Windows install [putty](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html)

![](examples/net/ssh.py)


## ssh from Windows
{id: ssh-from-windows}

```
$ ssh foobar@hostname-or-ip
  -o "StrictHostKeyChecking no" 

$ plink.exe -ssh foobar@hostname-or-ip -pw "password" -C "uname -a"
$ plink.exe", "-ssh", "foobar@username-or-ip", "-pw", "no secret", "-C", "uname -a"
```
![](examples/net/ssh_plink.py)


## Parallel ssh
{id: parallel-ssh}

* [parallel-ssh](http://parallel-ssh.readthedocs.io/)
* **pip install parallel-ssh**

![](examples/net/parallel_ssh.py)


## telnet
{id: telnet}
![](examples/net/telnet.py)


## prompt for password
{id: get-password}

![](examples/net/prompt_password.py)


## ftp
{id: ftp}

```
$ sudo aptitude install proftpd
$ sudo /etc/init.d/proftpd start
$ sudo adduser   (user: foo pw: bar)
```
![](examples/net/ftp.py)

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




