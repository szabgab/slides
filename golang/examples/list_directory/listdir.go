package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
)

func main() {
	fmt.Println("hello")
	fmt.Println(os.Args)
	if len(os.Args) < 2 {
		os.Exit(1)
	}

	fmt.Println(os.Args[1])
	files, err := ioutil.ReadDir(".") //os.Args[1])
	if err == nil {
		fmt.Println("Error reading the directory list")
		log.Fatal(err)
	} else {
		fmt.Println(files)
	}
}
