# Shell command


When running the ad-hoc command line on with ansible, it does not go through shell.
So some parsing or rediredting might not work.
To fix that you can use the shell module:

```
$ ansible virtualhosts -m shell -a "hostname ; date ; uptime ; free"

ubuntu-2 | SUCCESS | rc=0 >>
ubuntu-2
Mon Mar 19 01:50:03 IST 2018
 01:50:03 up  3:36,  2 users,  load average: 0.00, 0.00, 0.00
              total        used        free      shared  buff/cache   available
Mem:        1012448       85280      415244        3276      511924      775784
Swap:        483800           0      483800

ubuntu-1 | SUCCESS | rc=0 >>
ubuntu-1
Mon Mar 19 01:50:03 IST 2018
 01:50:03 up  7:49,  1 user,  load average: 0.00, 0.00, 0.00
              total        used        free      shared  buff/cache   available
Mem:        1012448       79836      422828        3264      509784      781300
Swap:        483800           0      483800
```

One last module to check is the setup module which lists tons of information on our servers:

```
$ ansible virtualhosts -m setup

sample output:
        "ansible_distribution": "Ubuntu",
        "ansible_distribution_file_parsed": true,
        "ansible_distribution_file_path": "/etc/os-release",
        "ansible_distribution_file_variety": "Debian",
        "ansible_distribution_major_version": "17",
        "ansible_distribution_release": "artful",
        "ansible_distribution_version": "17.10",
```

```
ansible virtualhosts -m setup |more |grep -i ubuntu
ubuntu-1 | SUCCESS => {
        "ansible_distribution": "Ubuntu",
        "ansible_fqdn": "ubuntu-1",
        "ansible_hostname": "ubuntu-1",
            "description": "Ubuntu 17.10",
            "id": "Ubuntu",
        "ansible_nodename": "ubuntu-1",
```


