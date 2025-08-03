package main

import (
	"fmt"
	"reflect"
)

func main() {
	a := "name"
	b := 42
	c := 19.23
	d := true

	fmt.Println(fmt.Sprintf("%T", a)) // string
	fmt.Println(fmt.Sprintf("%T", b)) // int
	fmt.Println(fmt.Sprintf("%T", c)) // float64
	fmt.Println(fmt.Sprintf("%T", d)) // bool

	fmt.Println(reflect.TypeOf(a)) // string
	fmt.Println(reflect.TypeOf(b)) // int
	fmt.Println(reflect.TypeOf(c)) // float64
	fmt.Println(reflect.TypeOf(d)) // bool
}
