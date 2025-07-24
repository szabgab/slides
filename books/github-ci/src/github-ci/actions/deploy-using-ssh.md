# Deploy using ssh

```
ssh-keygen -t rsa -b 4096 -C "user@host" -q -N "" -f ./do
ssh-copy-id -i do.pub user@host
```

* Add Secret:
*   Name: PRIVATE_KEY
*   Value: ... the content of the 'do' file ...

```
ssh-keyscan host
```

* Add Secret:
*   Name: KNOWN_HOSTS
*   Value: ... the output of the keyscan command ...


