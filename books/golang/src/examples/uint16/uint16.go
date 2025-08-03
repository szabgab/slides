package main

import (
	"fmt"
	"unsafe"
)

func main() {
	var z uint16
	fmt.Println(z)
	z--
	fmt.Println(z)

	fmt.Println(unsafe.Sizeof(z))
}
