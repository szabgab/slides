# Running the playbook


the command to run the playbook is a little different than the regular run command:

`ansible-playbook nginx_install.yml`

output would be:

{% embed include file="src/examples/aintro/output2.out" %}

playing the playbook again wont do anything if the state of the services and file is already identical:

```
yonit@ansible_server:~/ansible$ ansible-playbook nginx_install.yml
```
{% embed include file="src/examples/aintro/output3.out" %}


