package main

import (
	"fmt"
	"time"
)

func main() {
	t := time.Now()
	fmt.Printf("%T\n", t)
	fmt.Printf("Now:              %v\n", t)

	d2 := t.AddDate(0, 0, 2)
	fmt.Printf("2 days from now:  %v\n", d2)

	y1 := t.AddDate(1, 0, 0)
	fmt.Printf("A year from now:  %v\n", y1)

	m1 := t.AddDate(0, -1, 0)
	fmt.Printf("Last month:       %v\n", m1)

	fmt.Println()
	fmt.Printf("Now:              %v\n", t)

}
