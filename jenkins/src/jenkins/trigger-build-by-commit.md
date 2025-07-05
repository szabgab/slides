# Trigger build by commit


* Jenkins UI: Jenkins / Manage Jenkins / Configure System
* Look for "GitHub Servers" and click on the blue ?-mark it will show the URL:
*  http://jenkins.szabgab.com:8080/github-webhook/
*  Remember this


* Goto the GitHub page: https://github.com/szabgab/demo-flask-project
* Settings
* Webhooks
*   Payload URL: the above URL
*   Content type: application/x-www-form-urlencoded
*   Secret:    (no secret)
*   Just the push event
*   Active


* Jenkins UI: Configure the project
* Build Triggers
*    "GitHub hook trigger for GITScm polling"
* Save

* Make some changes to the project in the local git repo and push it out to Github
* Observe that after a few seconds the build starts.



