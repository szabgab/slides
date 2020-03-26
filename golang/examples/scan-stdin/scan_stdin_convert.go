package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	var inputStr string
	fmt.Print("A numer: ")
	fmt.Scan(&inputStr)
	fmt.Printf("Input: %v Type %T\n", inputStr, inputStr)
	//number, err := strconv.Atoi(inputStr)
	number, err := strconv.ParseFloat(inputStr, 64)
	if err != nil {
		fmt.Printf("There was an error: %v\n", err)
		os.Exit(1)
	}
	fmt.Printf("Input: %v Type %T\n", number, number)
}
