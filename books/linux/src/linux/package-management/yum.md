# yum on CentOS  7.2 x64

* yum

```
$ yum search STRING    - search for packages matching that string
$ yum install NAME     - install given package and its dependencies
$ yum -y install NAME  - don't wait for confirmation
$ yum list installed NAME - check if package installed 

$ yum check-update     - check which packages have newer versions
$ yum update           - update packages (install newer versions)

$ yum whoprovides  /path/to/file  - list of package(s) that installed the given file

$ yum deplist perl-Test-Perl-Critic     - list of dependencies
```



