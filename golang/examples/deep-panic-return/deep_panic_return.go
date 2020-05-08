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
		res, err := mydiv(dividend, divisor)
		if err != nil {
			fmt.Printf("Error: %v\n", err)
			continue
		}
		fmt.Println(res)
	}

	fmt.Println()
	fmt.Println("After")
}

func mydiv(a, b int) (res int, myerr error) {
	// var res int
	// var err error

	defer func() {
		if err := recover(); err != nil {
			//fmt.Printf("Error: %v\n", err)
			myerr = fmt.Errorf("%v", err)
			//log.Print("Error: ", err)
			//panic(err)
		}
	}()
	res = externalDiv(a, b)
	return
}

func externalDiv(a, b int) int {
	res := a / b
	return res
}
