package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	//fmt.Println(os.Args)
	if len(os.Args) != 4 {
		fmt.Println("Usage: calc.go NUMBER OPERATOR NUMBER")
		os.Exit(0)
	}

	var a, _ = strconv.Atoi(os.Args[1])
	var op = os.Args[2]
	var b, _ = strconv.Atoi(os.Args[3])
	var result int

	switch op {
	case "+":
		result = a + b
	case "*":
		result = a * b
	case "/":
		if b == 0 {
			fmt.Println("Cannot devide by 0")
			os.Exit(1)
		}
		result = a / b
	case "-":
		result = a - b
	default:
		fmt.Printf("Operator '%s' is not handled.\n", op)
		os.Exit(1)
	}

	fmt.Println(result)
}
