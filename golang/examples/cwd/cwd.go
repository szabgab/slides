package main

import (
	"fmt"
	"log"
	"os"
)

func main() {
	fmt.Println("hello")
	cwd, err := os.Getwd()
	if err != nil {
		log.Panic(err)
	} else {
		fmt.Println(cwd)
	}
}
