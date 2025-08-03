package main

import (
	"fmt"
)

func main() {
	var res = [...]int{7, 5, 9}

	fmt.Println(res)
	fmt.Println(res[1])
	fmt.Println(len(res))

	fmt.Printf("%T\n", res)
}
