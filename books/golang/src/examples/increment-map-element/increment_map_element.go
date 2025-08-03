package main

import "fmt"

func main() {
	counter := map[string]int{}
	fmt.Println(counter)
	counter["Foo"]++
	fmt.Println(counter)

}
