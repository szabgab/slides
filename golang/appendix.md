# Appendix
{id: appendix}


## Some advanced topics
{id: advanced-topics}

* struct
* closures
* pointers
* go-routines
* classes (there are no classes)
* methods (attached to types), but no classes
* interfaces
* Stringers - stringification
* Cross compilation
* many standard packages
* many external packages

## Resources
{id: resources}

* [Golang tour](https://tour.golang.org/welcome/1)
* [Video](https://www.youtube.com/watch?v=YS4e4q9oBaU)
* [Video](https://youtu.be/YS4e4q9oBaU?t=6927)


## Compilation
{id: compilation}

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


## Packages
{id: packages}

```
.
├── src
│   └── mymath
│       └── mymath.go
└── use.go
```

![](examples/package-example/use.go)

![](examples/package-example/src/mymath/mymath.go)

```
GOPATH=$(pwd) go run use.go
```

## Cross compile
{id: cross-compile}

How to compile a golang application and distribute to multiple platforms. How to cross-compile golang application.

```
env GOOS=target-OS GOARCH=target-architecture go build package-import-path
```

[](https://www.digitalocean.com/community/tutorials/how-to-build-go-executables-for-multiple-platforms-on-ubuntu-16-04)


## Sort
{id: sort}
{i: sort}

![](examples/sort/sort.go)


## Split and join
{id: split}

![](examples/split/split.go)

