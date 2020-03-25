# Skeleton
{id: skeleton}



## empty file
{id: empty-file}

![](examples/empty/empty.go)

```
go run empty.go

package main: empty.go:1:2: expected 'package', found 'EOF'
```

## Only package main
{id: package-main}

![](examples/package-main/package-main.go)

```
# command-line-arguments
runtime.package-main_main·f: function main is undeclared in the main package
```

## Other package name
{id: other-package-name}

![](examples/qqrq/qqrq.go)

```
go run: cannot run non-main package
```


## Skeleton file
{id: skeleton-file}

![](examples/skeleton/skeleton.go)

```
go run skeleton.go
```
