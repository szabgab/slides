package main

import (
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	if len(os.Args) != 2 {
		fmt.Printf("Usage: %s EXPRESSION (put the whole thing in quotes)\n", os.Args[0])
		os.Exit(1)
	}
	expression := os.Args[1]
	//fmt.Println(expression)
	parts := strings.Fields(expression)
	//fmt.Println(parts)
	//fmt.Println(len(parts))
	result := rpc(parts)
	fmt.Println(result)

}

func rpc(parts []string) float64 {
	stack := []float64{}
	for _, value := range parts {
		//fmt.Println(value)
		if value == "=" {
			log.Println("=")
			if len(stack) == 0 {
				panic("Operator = received and we have no value to print")
			}
			a := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			return a
		}
		if value == "+" || value == "*" || value == "-" || value == "/" {
			log.Println(value)
			if len(stack) < 2 {
				panic("Operator + received too early")
			}
			b := stack[len(stack)-1]
			a := stack[len(stack)-2]
			var c float64
			switch value {
			case "+":
				c = a + b
			case "-":
				c = a - b
			case "*":
				c = a * b
			case "/":
				c = a / b
			default:
				panic("How could this happen?")
			}

			stack = stack[:len(stack)-2]
			stack = append(stack, c)
			continue
		}
		number, err := strconv.ParseFloat(value, 64)
		if err != nil {
			panic(fmt.Sprintf("Unhandled value %v", value))
		}
		log.Println(number)
		stack = append(stack, number)
	}
	return 0
}
