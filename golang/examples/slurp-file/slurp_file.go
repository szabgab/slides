package main

import (
	"fmt"
	"io/ioutil"
)

func main() {
	filename := "slurp_file.go"
	dat, err := ioutil.ReadFile(filename)
	if err != nil {
		fmt.Printf("Error: %v\n", err)
		return
	}
	fmt.Println(string(dat))
}
