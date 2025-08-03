package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Printf("Usage: %s DIRNAME")
		os.Exit(1)
	}

	fmt.Println(os.Args[1])
	files, err := ioutil.ReadDir(".") //os.Args[1])
	if err != nil {
		fmt.Println("Error reading the directory list")
		log.Fatal(err)
	} else {
		for _, f := range files {
			fmt.Println(f.Name())
		}
	}
}
