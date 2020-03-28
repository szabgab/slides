package main

import (
	"fmt"
	"strings"
)

func main() {
	var count = make(map[string]int)
	var text = "hello world how are you world and how are you"
	//fmt.Println(text)

	var words = strings.Split(text, " ")
	//fmt.Println(words)
	for _, word := range words {
		count[word]++
	}
	//fmt.Println(count)

	for k, v := range count {
		fmt.Printf("%s: %d\n", k, v)
	}

}
