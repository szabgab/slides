package main

import "fmt"

func main() {
	ch := make(chan string)
	ch <- "Hello"

	text := <-ch
	fmt.Println(text)
}
