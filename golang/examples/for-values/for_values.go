package main

import "fmt"

func main() {
	dwarfs := []string{"Doc", "Grumpy", "Happy", "Sleepy", "Bashful", "Sneezy", "Dopey"}
	for _, name := range dwarfs {
		fmt.Println(name)
	}
}
