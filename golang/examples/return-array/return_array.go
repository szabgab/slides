package main

import (
	"fmt"
	"reflect"
)

func main() {
	a := [3]int{}
	fill(a)
	// fmt.Println(time.Now().UnixNano())
	// rand.Seed(time.Now().UnixNano())
	// n := 1 + rand.Intn(10)
	// fmt.Println(n)
	// slc := make([]int, 0, n)
	// fmt.Println(slc)
	// fmt.Println(len(slc))
	// fmt.Println(cap(slc))
}

func fill(arr interface{}) {
	fmt.Println(arr)
	fmt.Println(reflect.TypeOf(arr))
	x = array(arr)
	//fmt.Println(len(arr))
	// for i, val := range arr {
	// 	fmt.Printf("%v %v", i, val)
	// }
}
