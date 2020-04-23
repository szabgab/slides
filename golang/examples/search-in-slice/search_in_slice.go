package main

import (
	"fmt"
	"sort"
)

func main() {
	dwarfs := []string{"Doc", "Grumpy", "Happy", "Sleepy", "Bashful", "Sneezy", "Dopey"}
	fmt.Println(dwarfs)
	fmt.Println(sort.StringsAreSorted(dwarfs))
	fmt.Println(len(dwarfs))
	res := sort.SearchStrings(dwarfs, "Sleepy")
	fmt.Println(res)

	res = sort.SearchStrings(dwarfs, "Snow White")
	fmt.Println(res)

}
