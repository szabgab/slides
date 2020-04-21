package main

import "fmt"

func main() {
	var grades map[string]int  // defined type but does not create the container for it
	fmt.Printf("%T\n", grades) // map[string]int

	grades["Mary"] = 99
}
