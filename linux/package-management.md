# Package Management - Installing software
{id: package-management}

## App-store
{id: app-store}

* /etc/apt/sources.list



## Package formats
{id: package-formats}

* RPM (Red Hat Package Management)
* DEB (Debian, Ubuntu, etc.
* Source code



## Package managemnt tools
{id: package-tools}

* search
* install
* uninstall
* upgrade
* Which package contains a given file?
* List dependencies



## Instalation with apt-get
{id: apt-get}
{i: apt-get}

```
# apt-get update
# apt-get install package-name
```


## apt-cache
{id: apt-cache}
{i: apt-cache}

```
$ apt-cache search PARTIAL-PACKAGE-NAME
$ apt-cache show PACKAGE-NAME
$ apt-cache showpkg PACKAGE-NAME
$ apt-cache depends PACKAGE-NAME
```


## aptitude
{id: aptitude}
{i: aptitude}

```
# aptitude update
# aptitude safe-upgrade                   (updating fixes)
$ aptitude search PARTIAL-PACKAGE-NAME
# aptitude 

# aptitude upgrade
```


## dpkg
{id: dpkg}
{i: dpkg}

```
dpkg --list package_name - list installed packages
```


## yum on CentOS  7.2 x64
{id: yum}
{i: yum}

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


## CentOS repoquery
{id: repoquery}

```
$ yum -y install yum-utils

$ repoquery --requires NAME                         - list of (immediate) dependencies
$ repoquery --requires --resolve NAME               - list of (immediate) dependencies - packages
$ repoquery --requires --resolve --recursive NAME   - list of all the dependencies
```


## yes
{id: yes}
{i: yes}

```
# aptitude safe-upgrade
# yes | aptitude safe-upgrade


# aptitude -y safe-upgrade
```


## Exercise: Package management
{id: exercise-package-management}

* Install a package (e.g. a web server or an editor)





