package main

import (
	"fmt"
	"math"
	"strconv"
)

func main() {
	fmt.Println(math.Pi)

	var radiusStr string
	fmt.Print("radius: ")
	fmt.Scan(&radiusStr)

	radius, err := strconv.ParseFloat(radiusStr, 64)
	if err == nil {
		fmt.Println(radius)
		area := math.Pi * math.Pow(radius, 2)
		circumference := 2 * math.Pi * radius
		fmt.Printf("Area: %v\n", area)
		fmt.Printf("Cirumference: %v\n", circumference)
	}
}
