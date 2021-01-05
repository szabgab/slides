# Jenkins Freestyle projects
{id: jenkins-freestyle}

## Create new Job
{id: jenkins-create-new-job}

```
Create new jobs: test-python, Freestyle project
GitHub Porject: https://github.com/szabgab/test-python
Soucre Code Management: Git
     Repository URL: https://github.com/szabgab/test-python.git
     Credentials: None
     Branch Specifier: */master
Build:
     Execute Shell:
     #!/bin/bash
     echo Hello World
Save and click on Build Now, then look at the Console Output
```


## Demo Freestyle project
{id: demo-freestyle-project}

* [GitHub project](https://github.com/szabgab/demo-flask-project)
* [Demo Application](http://demo.code-maven.com:9090/)

## Freestyle Project
{id: freestyle-project}

* Enter a name: Demo
* click on Freestle project


* GitHub Project: https://github.com/szabgab/demo-flask-project
* (this is only used to create an html link to the project)

* Source Code Management
* Git: https://github.com/szabgab/demo-flask-project
* Save

* Build Now

* This will clone the current version of the project.
* We can see it in the "Workspace"
* See "Build history"

* Click around, see console output


## Scheduling builds by polling the repository
{id: jenkins-scheduling-builds-poll-scm}

```
Configure
    Build Triggers
        Poll SCM: H/5 * * * *
```


## Scheduling builds by GitHub hook
{id: jenkins-scheduling-builds-github-hook}

```
Configure
    Build Triggers
        GitHub hook trigger for GITScm polling
```


## Jenkins: Add user - github
{id: jenkins-add-user}

```
Add a user to Jenkins called "github":
Manage Jenkins
   Manage Users
      Create User
```

## Jenkins: GitHub trigger
{id: jenkins-github-trigger}

```
In GitHub
    Settings
        Integrations and Services
             Add Service: Jenkins (GitHub plugin)
                 http://github:secret@162.243.46.181:8080/github-webhook/
```


## Configure
{id: configure}

Build - execute shell

```
./run_jenkins.sh
```

Build Now

This will try to run the `run_jenkins.sh` script that does not exist in our repo and thus it will fail.

## Add Jenkins script
{id: add-jenkins-script}

In the project directory create the `run_jenkins.sh` file  with the following content:

```
#!/bin/bash

virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
pytest
```

Make it executable by running:

```
chmod +x run_jenkins.sh
```

Commit it to the git repository and push it out.

Then click on "Build Now" on the Jenkins UI.

It should build successfully now.


