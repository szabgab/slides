package main

import (
	"fmt"
)

func main() {
	planets := [...]string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn"}

	fmt.Println(planets)
	fmt.Println(len(planets))
	fmt.Println(cap(planets))
	fmt.Printf("%T\n", planets)

	part := planets[1:4]
	fmt.Println(part)
	fmt.Println(len(part))
	fmt.Println(cap(part))
	fmt.Printf("%T\n", part)
}
