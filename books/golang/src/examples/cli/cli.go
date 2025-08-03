package main

import (
	"fmt"
	"os"
)

func main() {
	fmt.Println(len(os.Args))
	fmt.Println(os.Args)
	fmt.Println(os.Args[0]) // the path to the compiled executable

	fmt.Printf("%T\n", os.Args) // []string   (slice)
}
