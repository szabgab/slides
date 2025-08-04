# Packages

```
.
├── src
│   └── github.com
│         └── szabgab
│                └── myrepo
│                      └── mymath.go
├── bin
├── pkg
    └── use.go
```

{% embed include file="src/examples/package-example/use.go" %}

{% embed include file="src/examples/package-example/src/mymath/mymath.go" %}

```
GOPATH=$(pwd) go run use.go
```


