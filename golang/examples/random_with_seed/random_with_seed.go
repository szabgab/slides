package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	rand.Seed(time.Now().Unix())

	a := rand.Intn(10)

	fmt.Println(a)
}
