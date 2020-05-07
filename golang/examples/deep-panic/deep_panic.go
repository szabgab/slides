package main

import (
	"fmt"
)

func main() {
	fmt.Println("Before")
	fmt.Println()

	dividend := 16
	divisors := []int{8, 4, 0, 2}
	for _, divisor := range divisors {
		mydiv(dividend, divisor)
	}

	fmt.Println()
	fmt.Println("After")
}

func mydiv(a, b int) {
	defer func() {
		if err := recover(); err != nil {
			fmt.Printf("Error: %v\n", err)
			//log.Print("Error: ", err)
			//panic(err)
		}
	}()
	externalDiv(a, b)
}

func externalDiv(a, b int) {
	//fmt.Println("Start")

	res := a / b
	fmt.Printf("%v / %v = %v\n", a, b, res)

	//fmt.Println("End")
}
