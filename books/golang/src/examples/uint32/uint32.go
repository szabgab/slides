package main

import (
	"fmt"
	"unsafe"
)

func main() {
	var z uint32
	fmt.Println(z)
	z--
	fmt.Println(z)

	fmt.Println(unsafe.Sizeof(z))
}
