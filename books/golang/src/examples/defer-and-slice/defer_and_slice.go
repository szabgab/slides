package main

import "fmt"

func main() {
	words := []string{"zero", "one", "two"}
	defer say(words)
	words[0] = "END"
}

func say(text []string) {
	fmt.Println(text)
}
