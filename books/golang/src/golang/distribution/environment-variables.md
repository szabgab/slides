# Environment variables

* GOROOT - path tpo the installation of go
* PATH=$PATH;$GOROOT/bin  - so the command line can find the go command
* GOPATH - where my libraries are going to be located
* PATH=$PATH;$GOPATH/bin

* GOPATH - can have multiple directories in in (but then we have to includ the bin directories related to them one-by-one)
* The first entry in GOPATH will be used by `go get` to install modules, but all the others will be used to find modules.



