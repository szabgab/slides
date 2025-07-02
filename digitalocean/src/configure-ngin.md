# Configure nginx


```
ls -l /etc/nginx/sites-enabled/
rm /etc/nginx/sites-enabled/default
ln -s /home/dev/python-flask-demo/config/demo-nginx.conf /etc/nginx/sites-enabled/demo-nginx.conf
```

If there are problems you can take a look at this file:

```
/var/log/nginx/python-flask-demo.error.log
```



