package main

import (
	"fmt"
	"os"
)

func main() {
	fmt.Println(len(os.Args))
	fmt.Println(os.Args[0])
	fmt.Println(os.Args)
}
