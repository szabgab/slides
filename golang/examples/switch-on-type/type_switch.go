package main

import (
	"fmt"
)

func main() {
	var x interface{}
	x = 1
	//x = "other"
	//x = 3.14
	switch x.(type) {
	case int:
		fmt.Println("int")
	case float64:
		fmt.Println("float64")
	default:
		fmt.Println("other")
	}

}
