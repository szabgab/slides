package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

func main() {
	filename := "slurp_file.go"
	dat, err := ioutil.ReadFile(filename)
	if err != nil {
		fmt.Printf("Error: %v\n", err)
		os.Exit(1)
	}
	fmt.Println(string(dat))
}
