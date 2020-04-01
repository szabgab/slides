package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	fmt.Println(time.Now().Unix())

	rand.Seed(time.Now().Unix())

	a := rand.Float64()

	fmt.Println(a)
}
