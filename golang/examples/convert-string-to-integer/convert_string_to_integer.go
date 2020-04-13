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
}
