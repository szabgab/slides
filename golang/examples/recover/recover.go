package main

import (
	"fmt"
	"log"
)

func main() {
	fmt.Println("Before")
	doSomething(true)
	fmt.Println("After")
}

func doSomething(bad bool) {
	fmt.Println("Start")
	defer func() {
		if err := recover(); err != nil {
			log.Print("Error: ", err)
			//panic(err)
		}
	}()
	if bad {
		panic("There is some problem here")
	}
	fmt.Println("End")
}
