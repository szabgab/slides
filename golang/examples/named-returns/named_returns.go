package main

import "fmt"

func main() {
	a, err := div(6, 2)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Printf("6/2 = %v\n", a)

	b, err := div(6, 0)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Printf("6/0 = %v\n", b)
}

func div(a, b float32) (result float32, err error) {
	if b == 0 {
		err = fmt.Errorf("Can't divide by 0")
		return
	}

	result = a / b
	return
}
