package main

import (
	"fmt"
	"math/rand"
)

func main() {
	x := rand.Float64()
	fmt.Println(x)

	y := rand.Int()
	fmt.Println(y)

	a := rand.Intn(10) // between [0, n)
	fmt.Println(a)
	b := rand.Intn(10) // between [0, n)
	fmt.Println(b)

}
