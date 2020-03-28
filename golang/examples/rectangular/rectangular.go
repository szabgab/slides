package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	// convert to integer
	w, _ := strconv.Atoi(os.Args[1]) // this will convert a string like "abc" or "2x" to 0 and set err
	h, _ := strconv.Atoi(os.Args[2])
	fmt.Println(w)
	fmt.Println(h)

	fmt.Println("The size of the rectangular is: ", w*h)
}
