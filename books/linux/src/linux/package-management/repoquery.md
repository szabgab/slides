# CentOS repoquery

```
$ yum -y install yum-utils

$ repoquery --requires NAME                         - list of (immediate) dependencies
$ repoquery --requires --resolve NAME               - list of (immediate) dependencies - packages
$ repoquery --requires --resolve --recursive NAME   - list of all the dependencies
```



