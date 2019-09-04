package main

import (
	"fmt"
	"strconv"
)

func main() {
	var i int

	i, _ = strconv.Atoi("42")
	fmt.Printf("%d %T\n", i, i) // 42 int

	var f float64
	f, _ = strconv.ParseFloat("4.2", 64)
	fmt.Printf("%f %T\n", f, f) // 4.200000 float64

	var str = strconv.Itoa(42)
	fmt.Printf("%s\n", str) // 42

	var err error
	i, err = strconv.Atoi("23\n")
	fmt.Println(err) // strconv.Atoi: parsing "23\n": invalid syntax

	i, err = strconv.Atoi("17x")
	fmt.Println(err) // strconv.Atoi: parsing "17x": invalid syntax
}
