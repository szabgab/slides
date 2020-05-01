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
	result, err := calc(a, op, b)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	fmt.Println(result)
}

func calc(a int, op string, b int) (int, error) {
	var result int

	if op == "+" {
		result = a + b
	} else if op == "*" {
		result = a * b
	} else if op == "/" {
		if b == 0 {
			return 0, fmt.Errorf("Cannot devide by 0")
		}
		result = a / b
	} else if op == "-" {
		result = a - b
	} else {
		return 0, fmt.Errorf("operator '%s' is not handled", op)
	}
	return result, nil
}
