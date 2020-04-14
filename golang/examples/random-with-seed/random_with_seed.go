package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	fmt.Println(time.Now().UnixNano())

	rand.Seed(time.Now().UnixNano())

	a := rand.Float64()

	fmt.Println(a)
}
