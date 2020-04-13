package main

import (
	"fmt"
	"strconv"
)

func main() {
	var f float64
	var err error

	f, err = strconv.ParseFloat("4.2", 64)
	if err == nil {
		fmt.Printf("%v %T\n", f, f) // 4.2 float64
	} else {
		fmt.Println(err)
	}
}
