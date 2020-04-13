package main

import (
	"fmt"
	"reflect"
)

func main() {
	a := 42
	fmt.Println(reflect.TypeOf(a)) // int

	b := 3.14
	fmt.Println(reflect.TypeOf(b)) // float64

	c := "hello world"
	fmt.Println(reflect.TypeOf(c)) // string

	d := []string{}
	fmt.Println(reflect.TypeOf(d)) // []string
}
