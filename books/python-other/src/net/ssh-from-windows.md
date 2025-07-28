# ssh from Windows

```
$ ssh foobar@hostname-or-ip
  -o "StrictHostKeyChecking no" 

$ plink.exe -ssh foobar@hostname-or-ip -pw "password" -C "uname -a"
$ plink.exe", "-ssh", "foobar@username-or-ip", "-pw", "no secret", "-C", "uname -a"
```
{% embed include file="src/examples/net/ssh_plink.py" %}


