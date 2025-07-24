# GitLab API

* List all the projects of user szabgab using a private access token

```
curl --silent "https://gitlab.com/api/v4/users/szabgab/projects?private_token=$GITLAB_PRIVATE_TOKEN"
curl --silent --header "PRIVATE-TOKEN: $GITLAB_PRIVATE_TOKEN"  "https://gitlab.com/api/v4/users/szabgab/projects"
# id  (can be also found on the main page of each project it is also available as $CI_PROJECT_ID during the CI run)
# visibility (private or public)
```

* List of pipelines of project with id 28402932

```
curl --silent --header "PRIVATE-TOKEN: $GITLAB_PRIVATE_TOKEN"  "https://gitlab.com/api/v4/projects/28402932/pipelines"
# has a field called "status"
```

* List of jobs:

```
curl --silent --header "PRIVATE-TOKEN: $GITLAB_PRIVATE_TOKEN"  "https://gitlab.com/api/v4/projects/28402932/jobs"
# has a field called "status"
# has a section called "pipeline"
```

There is an envrionment variable in the GitLab pipelines called `$CI_JOB_TOKEN` and it can be used for some things
but it is very limited in rights.
AFAIK Project level access tokens are only available to paying customer https://docs.gitlab.com/ee/user/project/settings/project_access_tokens.html
So I am using Personal Access Tokens stored as a secret.

* Go to Settings/CICD/Variables/Add Variable called GITLAB_PRIVATE_TOKEN


