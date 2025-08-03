package main

import (
	"flag"
	"fmt"
)

func main() {
	var debug = flag.Bool("debug", false, "Debug or not?")
	var score = flag.Int("score", 0, "The score")
	var name = flag.String("name", "", "The name")
	flag.Parse()
	fmt.Println(*debug)
	fmt.Println(*score)
	fmt.Println(*name)
}
