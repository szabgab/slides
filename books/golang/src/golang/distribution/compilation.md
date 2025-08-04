# Corss Compilation

Create a file called `application.go` in which you have all of your code.

You can run it as

```
go run application.go
```

You can create an executable binary (for the current Operating System and architecture) using:

```
GOBIN=/tmp go install application.go
```

This will create a file called `application` in the `/tmp` directory.


```
GOARCH=386 GOBIN=/tmp go install use.go
```

This will create for the same Opereating system but 32 bit.


```
GOOS=OS GOARCH=architecture go build PATH_TO
GOOS=OS GOARCH=architecture go install PATH_TO
```

GOOS:

```
android
darwin
dragonfly
freebsd
linux
netbsd
openbsd
plan9
solaris
windows
```

GOARCH

```
arm
arm64
386
amd64
ppc64
ppc64le
mips
mipsle
mips64
mips64le
```

* [build](https://golang.org/pkg/go/build/)



