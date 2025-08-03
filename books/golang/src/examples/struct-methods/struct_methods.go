package main

import (
	"fmt"
	"math"
)

type myCircle struct {
	x float64
	y float64
	r float64
}

func (c myCircle) area() float64 {
	return c.r * c.r * math.Pi
}

func main() {
	a := myCircle{
		x: 2,
		y: 3,
		r: 4,
	}
	fmt.Println(a)

	theArea := a.area()
	fmt.Println(theArea)
}
