package main

import (
	"fmt"
)

type hash map[string]int

func (h hash) keys() []string {
	keys := make([]string, 0, len(h))
	for k := range h {
		keys = append(keys, k)
	}
	return keys
}

func main() {
	data := hash{
		"foo": 3,
		"bar": 17,
		"adi": 10,
	}
	fmt.Println(data)
	ks := data.keys()
	fmt.Println(ks)
}
