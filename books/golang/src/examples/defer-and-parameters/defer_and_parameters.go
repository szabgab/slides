package main

import "fmt"

func main() {
	text := "start"
	defer fmt.Println(text)
	defer say(text)
	text = "end"
	fmt.Printf("end: %v\n", text)
}

func say(text string) {
	fmt.Println(text)
}
