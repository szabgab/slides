package main

import "fmt"

func main() {
	var str string
	fmt.Print("The string: ")
	fmt.Scan(&str)

	fmt.Printf("%v \n", len(str))
}
