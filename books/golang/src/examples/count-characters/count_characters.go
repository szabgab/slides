package main

import "fmt"

func main() {
	text := "This is a very long text. OK, maybe it is not that long after all."
	counter := make(map[string]int)
	for _, c := range text {
		//fmt.Printf("%v", string(c))
		if string(c) != " " {
			counter[string(c)]++
		}
	}

	fmt.Println(text)
	for char, count := range counter {
		fmt.Printf("%v: %v\n", char, count)
	}

}
