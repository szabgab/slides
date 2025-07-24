# removing a package


Testing before running:

```
ansible virtualhosts -C -m service -a "name=nginx state=stopped" -b
```

will test the command without actualy running it.

we can remove the nginx package with these commands,

stopping:

```
ansible virtualhosts -m service -a "name=nginx state=stopped" -b

ubuntu-1 | SUCCESS => {
    "changed": true,
    "name": "nginx",
    "state": "stopped",
    "status": {
        "ActiveEnterTimestamp": "Tue 2018-03-20 23:22:34 IST",
        "ActiveEnterTimestampMonotonic": "2363436511",
        "ActiveExitTimestamp": "Tue 2018-03-20 23:20:30 IST",
```

and removing:

```
ansible virtualhosts -m apt -a "name=nginx state=absent purge=yes autoremove=yes" -b

ubuntu-2 | SUCCESS => {
    "changed": true,
    "stderr": "",
    "stderr_lines": [],
    "stdout": "Reading package lists...\nBuilding dependency tree...\nReading state information...\n
```


