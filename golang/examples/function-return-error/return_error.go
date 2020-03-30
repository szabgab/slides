package main

import "fmt"

func main() {
	fmt.Println("Hello World")
	a, err := div(3, 1)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(a)
}

func div(a, b float32) (float32, error) {
	if b == 0 {
		return 0.0, fmt.Errorf("Problem")
	}

	result := a / b
	return result, nil
}
