package main

import (
	"fmt"
)

var y int

func main() {
	showY()
	setY()
	showY()
}

func setY() {
	y = 42
}
func showY() {
	fmt.Println(y)
}
