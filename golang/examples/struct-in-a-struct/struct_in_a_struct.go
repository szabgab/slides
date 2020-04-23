package main

import "fmt"

type myPoint struct {
	x float64
	y float64
}

type myLine struct {
	a myPoint
	b myPoint
}

func main() {
	p1 := myPoint{
		x: 2.1,
		y: 3.1,
	}
	p2 := myPoint{
		x: -0.1,
		y: 1.1,
	}
	fmt.Println(p1)
	fmt.Println(p2)

	line := myLine{
		a: p1,
		b: p2,
	}
	fmt.Println(line)
	fmt.Println(line.a.x)
}
