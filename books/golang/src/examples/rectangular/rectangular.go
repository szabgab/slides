package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	var err error
	var width int
	var height int

	if len(os.Args) != 3 {
		fmt.Printf("Usage: %v WIDTH HEIGHT\n", os.Args[0])
		os.Exit(1)
	}

	width, err = strconv.Atoi(os.Args[1])
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	height, err = strconv.Atoi(os.Args[2])
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	fmt.Println(width)
	fmt.Println(height)

	area := width * height
	fmt.Printf("The area of the rectangular is: %v\n", area)
}
