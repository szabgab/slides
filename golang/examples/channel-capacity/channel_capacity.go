package main

import "fmt"

func main() {
	ch := make(chan string, 2)
	ch <- "One"
	ch <- "Two"
	//	ch <- "Three"

	text := <-ch
	fmt.Println(text)

	fmt.Println(<-ch)

	//	fmt.Println(<-ch)
}
