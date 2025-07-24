# Install and configure uwsgi


```
apt-get install uwsgi
apt-get install uwsgi-plugin-python3
ln -s /home/dev/python-flask-demo/config/demo-uwsgi.ini /etc/uwsgi/apps-enabled/demo-uwsgi.ini
service uwsgi restart
```

If there is a problem you might find help by looking at the log file:

```
/var/log/uwsgi/app/demo-uwsgi.log
```


