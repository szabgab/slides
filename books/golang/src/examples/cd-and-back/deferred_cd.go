package main

import (
	"fmt"
	"log"
	"os"
)

func main() {
	var dir string
	dir, _ = os.Getwd()
	fmt.Printf("Before  %v\n", dir)
	cd("..", showDir)
	dir, _ = os.Getwd()
	fmt.Printf("After %v\n", dir)
}

func showDir() {
	fmt.Println("Hello")
	dir, _ := os.Getwd()
	fmt.Printf("Inside:  %v\n", dir)
}

func cd(path string, f func()) {
	//fmt.Println(path)
	cwd, err := os.Getwd()
	if err != nil {
		log.Panic(err)
	}
	defer os.Chdir(cwd)
	err = os.Chdir(path)
	f()
}
