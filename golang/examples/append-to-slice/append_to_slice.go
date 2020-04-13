package main

import "fmt"

func main() {
	base := [10]string{"a", "b", "c", "d", "e", "f", "g", "h", "i", "j"}
	fmt.Println(base)
	part := base[3:7]
	fmt.Println(part)
	fmt.Println(len(part))
	fmt.Println(cap(part))
	fmt.Println()

	part = append(part, "x") // the slice was extended in the same array
	fmt.Println(part)
	fmt.Println(base)
	fmt.Println(len(part))
	fmt.Println(cap(part))
	fmt.Println()

	part = append(part, "1", "2", "3", "4") // creates a new, larger array and copyes the data.
	fmt.Println(part)
	fmt.Println(base)
	fmt.Println(len(part))
	fmt.Println(cap(part))
}
