# Setup Droplet for demo


```
apt-get update
apt-get install -y python3-pip python3-virtualenv
pip3 install flask
```

copy the webhook file

```
FLASK_APP=webhook flask run --host 0.0.0.0 --port 80
```

* [GitHub Repository used for demo](https://github.com/szabgab/github-actions-demo-20201224/)


