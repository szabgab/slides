package main

import "fmt"

func main() {
	base := [...]string{"a", "b", "c", "d", "e", "f", "g", "h"}
	fmt.Println(base)
	fmt.Println(len(base))
	part := base[3:7]
	fmt.Println(part)
	fmt.Println(len(part))
	fmt.Println(cap(part))
	fmt.Println()

	part = append(part, "X") // the slice was extended in the same array
	fmt.Println(part)
	fmt.Println(base)
	fmt.Println(len(part))
	fmt.Println(cap(part))
	fmt.Println()

	part = append(part, "Y") // creates a new, larger array and copyes the data.
	fmt.Println(part)
	fmt.Println(base)
	fmt.Println(len(part))
	fmt.Println(cap(part))
}
