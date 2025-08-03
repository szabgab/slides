package main

import (
	"fmt"
	"reflect"
)

type aPerson struct {
	id       int    `unique:"true"`
	name     string `required:"true" max:"100"`
	children []string
}

func main() {
	t := reflect.TypeOf(aPerson{})
	field, ok := t.FieldByName("id")
	if ok {
		fmt.Printf("id: %v\n", field.Tag)
		fmt.Println(field.Tag.Get("unique"))
		fmt.Println(field.Tag.Get("required"))

		value, ok := field.Tag.Lookup("unique")
		if ok {
			fmt.Printf("unique value: %v\n", value)
		}
	}
	field, ok = t.FieldByName("children")
	if ok {
		fmt.Printf("children: %v\n", field.Tag)
	}

	a := aPerson{
		id: 1,
	}
	fmt.Println(a)
}
