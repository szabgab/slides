package main

import (
	"fmt"
	"unsafe"
)

func main() {
	var z int8 = 126

	fmt.Println(z)
	z++
	fmt.Println(z)
	z++
	fmt.Println(z)
	z--
	fmt.Println(z)

	fmt.Println(unsafe.Sizeof(z))
}
