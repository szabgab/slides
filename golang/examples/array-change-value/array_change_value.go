package main

import (
	"fmt"
)

func main() {
	var res = [...]int{1, 2, 3}

	fmt.Println(res)
	res[1] = 42
	fmt.Println(res)
}
