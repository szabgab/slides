# Deploy


* In Jenkins Configure the project again
* Add another step to the build process with the following content: `./deploy.sh`
* Create the `deploy.sh` in the Git repository with the following content:

```bash
#!/bin/bash
echo "Deploy!"

cd /home/gabor/work/demo-flask-project;
/usr/bin/git pull
sudo /usr/sbin/service uwsgi reload
```


