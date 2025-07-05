# Running Ansible


there are 3 ways to run Ansible:

* running a command: `ansible GROUP -a COMMAND`
* running a module: `ansible GROUP -m MODULE`
* running a playbook: `ansible-playbook playbook.yml`

[Ansible extensive list of builtin modules](http://docs.ansible.com/ansible/latest/modules_by_category.html) there are about 450~ modules in the list, some popular ones are:

* `file`     - creates files and directories , sets permissions
* `apt/yum`  - manages packages - install, update, remove
* `service`  - manages services - stop, start, runlevel (at boot)
* `copy`     - copies files and directories
* `git`      - Deploy software (or files) from git checkouts
* `ping`     - Try to connect to host, verify a usable python and return pong on success

trying our first command:

```
ansible virtualhosts -m ping
```

this will fail since we did not setup the passwordless ssh.

```
ansible virtualhosts -m ping
SSH password:
ubuntu-1 | UNREACHABLE! => {
    "changed": false,
    "msg": "Authentication failure.",
    "unreachable": true
}
ubuntu-2 | UNREACHABLE! => {
    "changed": false,
    "msg": "Authentication failure.",
    "unreachable": true
}
```



