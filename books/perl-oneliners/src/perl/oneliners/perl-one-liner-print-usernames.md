# One-liner: Print all usernames from /etc/passwd

```
perl -n -a -F: -e 'print "$F[0]\n"' /etc/passwd
```


