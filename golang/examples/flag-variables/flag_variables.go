package main

import (
	"flag"
	"fmt"
)

func main() {
	var debug bool
	var score int
	var name string

	flag.BoolVar(&debug, "debug", false, "Debug or not?")
	flag.IntVar(&score, "score", 0, "The score")
	flag.StringVar(&name, "name", "", "The name")
	flag.Parse()

	fmt.Println(debug)
	fmt.Println(score)
	fmt.Println(name)
}
