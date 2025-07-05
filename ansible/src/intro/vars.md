# Adding vars to the play


Variables can be defines in many locations, and we can get them from the facts gathering stage as well.

lets add some content to the nginx servers, create a file called `index.html.tpl` with the content:

{% embed include file="src/examples/aintro/index.html.tpl)

and run the playbook again:

```
yonit@ansible_server:~/ansible$ ansible-playbook nginx_install.yml
```

{% embed include file="src/examples/aintro/output1.out" %}

now lets see it:

```
yonit@ansible_server:~/ansible$ curl http://ubuntu-2/
```
{% embed include file="src/examples/aintro/output2.html)


