package main

import (
	"fmt"
)

func main() {
	var res [3]int

	fmt.Println(res)      // [0 0 0]
	fmt.Println(res[1])   // 0
	fmt.Println(len(res)) // 3

	fmt.Printf("%T\n", res) // [3]int

	res[1] = 85
	res[0] = 97
	res[2] = 93

	fmt.Println(res)      // [97 85 93]
	fmt.Println(res[1])   // 85
	fmt.Println(len(res)) // 3

	fmt.Printf("%T\n", res) // [3]int
}
