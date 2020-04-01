package main

import (
	"fmt"
	"strconv"
)

func main() {
	pi := 3.14

	var radiusStr string
	fmt.Print("radius: ")
	fmt.Scan(&radiusStr)

	radius, err := strconv.ParseFloat(radiusStr, 64)
	if err == nil {
		fmt.Println(radius)
		area := pi * radius * radius
		circumference := 2 * pi * radius
		fmt.Printf("Area: %v\n", area)
		fmt.Printf("Cirumference: %v\n", circumference)
	}
}
