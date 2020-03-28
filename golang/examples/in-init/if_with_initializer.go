package main

import (
	"fmt"
)

func main() {
	counter := map[string]int{
		"foo": 2,
		"bar": 4,
	}

	name := "foo"
	if count, ok := counter[name]; ok {
		fmt.Printf("%v : %v\n", name, count)
	} else {
		fmt.Printf("%v has no value\n", name)
	}

	name = "zorg"
	if count, ok := counter[name]; ok {
		fmt.Printf("%v : %v\n", name, count)
	} else {
		fmt.Printf("%v has no value\n", name)
	}

}
