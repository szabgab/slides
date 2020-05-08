package main

import (
	"fmt"
)

func main() {
	fmt.Println("Start")
	c := make(chan string)

	go sendMessage(c)

	msg := <-c
	fmt.Println(msg)

	fmt.Println("End")
}

func sendMessage(c chan string) {
	c <- "Hello World"
}
