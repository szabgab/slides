package main

import (
	"fmt"
	"io/ioutil"
)

func main() {
	filename := "read_file.go"
	dat, _ := ioutil.ReadFile(filename)
	fmt.Println(string(dat))
}
