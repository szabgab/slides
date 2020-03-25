package main

import (
	"fmt"
)

func main() {
	var dwarfs = []string{"Doc", "Grumpy", "Happy", "Sleepy", "Bashful", "Sneezy", "Dopey"}
	theSeven := dwarfs

	fmt.Println(dwarfs)
	fmt.Println(theSeven)

	dwarfs[1] = "Snowwhite"

	fmt.Println(dwarfs)
	fmt.Println(theSeven)
}
