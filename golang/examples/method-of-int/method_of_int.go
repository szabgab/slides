package main

import (
	"fmt"
	"math"
)

type myint int

func (i myint) abs() float64 {
	return math.Abs(float64(i))
}

func main() {
	var n myint = -3
	fmt.Println(n.abs())
}
