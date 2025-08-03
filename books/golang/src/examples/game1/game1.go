package main

import (
	"fmt"
	"math/rand"
	"os"
	"strconv"
	"time"
)

func main() {
	fmt.Println("Welcome to the game!")
	max := 20

	rand.Seed(time.Now().UnixNano())
	hidden := rand.Intn(max) + 1

	fmt.Printf("The hidden number is %v\n", hidden)
	fmt.Printf("Your guess [1-%v]: ", max)

	var input string
	fmt.Scan(&input)

	guess, err := strconv.Atoi(input)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	if guess < hidden {
		fmt.Println("Too small")
	} else if guess > hidden {
		fmt.Println("Too big")
	} else {
		fmt.Println("Direct hit!")
	}
}
