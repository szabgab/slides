package main

import (
	"fmt"
)

func main() {
	var res = []int{97, 85, 93}
	var names []string
	fmt.Println(res)
	fmt.Println(res[1])
	fmt.Println(names)
	fmt.Println(len(res))
	fmt.Println(len(names))
	fmt.Printf("%T", names)
	//names[0] = "Mary"
	//names.append("Mary")
	//fmt.Println(names)
}
