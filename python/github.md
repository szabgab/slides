# GitHub
{id: github}


## GitHub API KEY (PERSONAL TOKEN)
{id: github-api-key}

* [Create a Personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

## GitHub REST API
{id: github-rest-api}

* [GitHub REST API](https://docs.github.com/en/rest)


## GitHub API GraphQL
{id: github-graphql-api}

* [GitHub GraphQL API](https://docs.github.com/en/graphql)

* [Scalars](https://docs.github.com/en/graphql/reference/scalars) (types)
* String!  means the field is string that cannot be null.

```
pip install gql[all]
```

## GitHub GraphQL execute query
{id: github-graphql-execute-query}

![](examples/github-graphql/run_query.py)

## GitHub GraphQL who am i
{id: github-graphql-login}

* Get the username of who provided the token

![](examples/github-graphql/login.gql)
![](examples/github-graphql/login.json)


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

