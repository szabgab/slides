package main

import (
	"fmt"
	"strconv"
)

func main() {
	var widthStr string
	fmt.Print("width: ")
	fmt.Scan(&widthStr)

	var lengthStr string
	fmt.Print("length: ")
	fmt.Scan(&lengthStr)

	// convert to integer

	width, errw := strconv.Atoi(widthStr)
	length, errl := strconv.Atoi(lengthStr)
	if errw == nil && errl == nil {
		fmt.Println(width)
		fmt.Println(length)
		area := width * length
		circumference := 2 * (width + length)
		fmt.Printf("Area: %v\n", area)
		fmt.Printf("Cirumference: %v\n", circumference)
	}
}
