package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	var aStr string
	var bStr string
	var operator string
	var a float64
	var b float64
	var err error
	var result float64

	fmt.Print("a: ")
	fmt.Scan(&aStr)
	a, err = strconv.ParseFloat(aStr, 64)
	if err != nil {
		fmt.Printf("The value '%v' could not be converted to a floating point number. %v\n", aStr, err)
		os.Exit(1)
	}

	fmt.Print("op: ")
	fmt.Scan(&operator)

	fmt.Print("b: ")
	fmt.Scan(&bStr)
	b, err = strconv.ParseFloat(bStr, 64)
	if err != nil {
		fmt.Printf("The value '%v' could not be converted to a floating point number. %v\n", bStr, err)
		os.Exit(1)

	}

	switch operator {
	case "+":
		result = a + b
	case "-":
		result = a - b
	case "*":
		result = a * b
	case "/":
		result = a / b
	default:
		fmt.Printf("Unhandled operator: '%v'\n", operator)
		os.Exit(1)
	}
	fmt.Printf("%v %v %v = %v\n", a, operator, b, result)

}
