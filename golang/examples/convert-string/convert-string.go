package main

import (
	"fmt"
	"strconv"
)

func main() {
	var i int
	var err error

	i, err = strconv.Atoi("42")
	if err == nil {
		fmt.Printf("%v %T\n", i, i) // 42 int
	} else {
		fmt.Println(err)
	}

	var f float64
	f, err = strconv.ParseFloat("4.2", 64)
	if err == nil {
		fmt.Printf("%v %T\n", f, f) // 4.2 float64
	} else {
		fmt.Println(err)
	}

	i, err = strconv.Atoi("23\n")
	if err == nil {
		fmt.Printf("%v %T\n", i, i)
	} else {
		fmt.Println(err) // strconv.Atoi: parsing "23\n": invalid syntax
	}

	i, err = strconv.Atoi("17x")
	if err == nil {
		fmt.Printf("%v %T\n", i, i)
	} else {
		fmt.Println(err) // strconv.Atoi: parsing "17x": invalid syntax
	}

	var str = strconv.Itoa(42)
	fmt.Printf("%s\n", str) // 42
}
