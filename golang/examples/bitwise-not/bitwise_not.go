package main

import "fmt"

func main() {
	fmt.Println("uint8")
	numbersUint8 := []uint8{1, 2, 5}
	for _, n := range numbersUint8 {
		fmt.Printf("%3v %9b\n", n, n)
		fmt.Printf("%3v %9b\n", ^n, ^n)

	}

	fmt.Println("\nint8")
	numbersInt8 := []int8{1, 2, 5}
	for _, n := range numbersInt8 {
		fmt.Printf("%3v %9b\n", n, n)
		fmt.Printf("%3v %9b\n", ^n, ^n)
	}

}
