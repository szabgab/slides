package main

import (
	"fmt"
	//    "os"
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
		fmt.Printf("The area of the rectangular is: %v\n", area)

	}

}
