package main

import (
	"fmt"
	"os"
)

func main() {
	if len(os.Args) < 3 {
		fmt.Printf("Usage: %s PARAM PARAM\n", os.Args[0])
		os.Exit(2)
	}
	fmt.Println(os.Args)
}
