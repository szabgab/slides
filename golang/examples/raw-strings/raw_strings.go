package main

import "fmt"

func main() {
	x := "a\nb"
	y := `a\nb`
	fmt.Println(x)
	fmt.Println("-------")
	fmt.Println(y)
}
