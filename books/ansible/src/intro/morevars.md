# More vars


To get the index files to display the name of the server i need to use a variable in the template

lets rename the index.html file: `mv index.html.tpl index.html.j2`

and edit the playbook, change these line:

```
src=index.html.tpl
to
src=index.html.j2
```

and lets slightly change index.html.j2:

{% embed include file="src/examples/aintro/index.html.j2)

run the playbook:

```
yonit@ansible_server:~/ansible$ ansible-playbook nginx_install.yml
```
{% embed include file="src/examples/aintro/output4.out" %}

and now:

```
yonit@ansible_server:~/ansible$ curl http://ubuntu-2/
```

{% embed include file="src/examples/aintro/output5.html)


