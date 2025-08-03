package main

import (
	"fmt"
	"sort"
)

func main() {
	dwarfs := []string{"Doc", "Grumpy", "Happy", "Sleepy", "Bashful", "Sneezy", "Dopey"}
	fmt.Println(dwarfs)
	fmt.Printf("Length: %v\n", len(dwarfs))
	fmt.Printf("StringsAreSorted: %v\n", sort.StringsAreSorted(dwarfs))
	res := sort.SearchStrings(dwarfs, "Sleepy")
	fmt.Printf("Index of Sleepy %v\n", res)

	name := "Snow White"
	res = sort.SearchStrings(dwarfs, name)
	fmt.Printf("Index of '%v': %v\n", name, res)

}
