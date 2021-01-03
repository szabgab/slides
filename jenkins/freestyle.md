# Jenkins Freestyle projects
{id: jenkins-freestyle}

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



