# GitHub
{id: github}

## GitHub data
{id: github-data}

* Users / Organizations
* Repositories
* Commits
* Issues
* Pull-Requests
* ...

## GitHub API: REST vs GraphQL
{id: github-api-rest-vs-graphql}

* **REST API**
* Get data in the structure as the API provider though you'll need it.
* Usually all the data from one table in the database.

* **GraphQL API**
* Have a mapping (edges) between pieces of data that are connected

* Getting the data you need, nothing more
* Nested fields
* Strong typing of the data
* Rare limits

## Where is it used
{id: github-api-where-is-it-used}

* [Open Source Develeopment Courses](https://osdc.code-maven.com/)
* [Open Source by Organizations](https://osdc.code-maven.com/open-source-by-organizations/)
* Weekly report

## GitHub get organization members
{id: github-get-organization-members}

![](examples/github-rest/rest_get_org_members.py)

`python examples/github-rest/rest_get_org_members.py`

![](examples/github-graphql/get_org_members.gql)

`python examples/github-graphql/run_query_requests.py examples/github-graphql/get_org_members.gql out.json`

## Details about an orgarnization REST
{id: rest-details-about-organization}

![](examples/github-rest/details-about-org.py)

```
python examples/github-rest/details-about-org.py github
python examples/github-rest/details-about-org.py kantoniko
python examples/github-rest/details-about-org.py osdc-code-maven

python examples/github-rest/details-about-org.py szabgab          error, this is a user
```

## Details about an user REST
{id: rest-details-about-user}

![](examples/github-rest/details-about-user.py)

```
python examples/github-rest/details-about-org.py szabgab

             but these also work:

python examples/github-rest/details-about-org.py github
python examples/github-rest/details-about-org.py kantoniko
python examples/github-rest/details-about-org.py osdc-code-maven
```

## REST - List of repositories by organization (pagination!)
{id: github-rest-list-of-repositories-by-organization}

![](examples/github-rest/repos-of-org.py)


```
python examples/github-rest/repos-of-org.py github
python examples/github-rest/repos-of-org.py kantoniko

python examples/github-rest/repos-of-org.py szabgab        error, this is a user
```

## REST - List of reposistories by user (pagination!)
{id: github-rest-list-of-repositories-by-user}

![](examples/github-rest/repos-of-user.py)

```
python examples/github-rest/repos-of-user.py szabgab

        but these also work:
python examples/github-rest/repos-of-user.py kantoniko
python examples/github-rest/repos-of-user.py osdc-code-maven
```


## GitHub API KEY (PERSONAL TOKEN)
{id: github-api-key}

* [Create a Personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)


## GitHub REST API
{id: github-rest-api}

* [GitHub REST API](https://docs.github.com/en/rest)

```
pip install requests
```

## GitHub REST API execute query
{id: github-rest-api-execute-query}

![](examples/github-rest/github_rest_api.py)



## GitHub API GraphQL
{id: github-graphql-api}

* [GitHub GraphQL API](https://docs.github.com/en/graphql)

* [Scalars](https://docs.github.com/en/graphql/reference/scalars) (types)
* String!  means the field is string that cannot be null.

```
pip install gql[all]
```

## GitHub GraphQL explorer
{id: github-graphql-explorer}

[GrapQL explorer](https://docs.github.com/en/graphql/overview/explorer)

## GitHub GraphQL execute query
{id: github-graphql-execute-query}

![](examples/github-graphql/run_query_requests.py)

![](examples/github-graphql/run_query.py)

## GitHub GraphQL who am i
{id: github-graphql-login}

* Get the username of who provided the token

![](examples/github-graphql/login.gql)
![](examples/github-graphql/login.json)

## GitHub GraphSQL paging
{id: github-graphql-paging}

![](examples/github-graphql/paging.py)

## GitHub GraphQL list my repositories
{id: github-graphql-list-my-repositories}

![](examples/github-graphql/list_my_repositories.gql)

![](examples/github-graphql/list_my_repositories.json)


## GitHub GraphQL list of repositories by username
{id: github-graphql-list-of-repositories-by-username}

![](examples/github-graphql/list_repositories_by_username.gql)

![](examples/github-graphql/list_repositories_by_username.json)

## GitHub GraphQL list issues by username
{id: github-graphql-list-issues-by-username}

![](examples/github-graphql/list_issues_by_username.gql)

![](examples/github-graphql/list_issues_by_username.json)

## GitHub GraphQL list issues using parameter
{id: github-graphql-list-issues-using-parameter}

![](examples/github-graphql/list_issues_using_parameter.py)

## GitHub GraphQL list issues using several parameters
{id: github-graphql-list-issues-using-several-parameters}

![](examples/github-graphql/list_issues_many_parameters.py)

## GitHub GraphQL contribution counts
{id: github-graphql-contribution-counts}

![](examples/github-graphql/countributions_count.gql)

* Defaults to the last 1 year

![](examples/github-graphql/countributions_count_time_range.gql)

* Can set the start-date (defaults to now - 1 year)
* Can set the end-date (defaults to start-date + 1 year)

## GitHub GraphQL list Pull-Requests
{id: github-graphql-pull-requests}

* List all the PRs created by a user in a time-range

![](examples/github-graphql/list_pull_requests.py)

![](examples/github-graphql/list_contributions_pull_requests.py)

## GitHub GraphQL activities
{id: github-graphql-activities}


* List all the activities of a user in a time-range

* All the issues opened / commented on / closed
* All the commits

* All the activities of a list of users in a time-range


* Get a list of projects written in python, that have between 2-5 stars and were updated in the last 5 weeks.
* Given a repository list all the changes that are were done in all the forks.


