package main

import "fmt"

func main() {
	var str1 string
	var str2 string
	fmt.Print("First string: ")
	fmt.Scan(&str1)
	fmt.Print("Second string: ")
	fmt.Scan(&str2)

	if str1 < str2 {
		fmt.Printf("The first string '%s' is ahead of '%s'\n", str1, str2)
	} else if str1 > str2 {
		fmt.Printf("The second string '%s' is ahead of '%s'\n", str2, str1)
	} else {
		fmt.Printf("The two string '%s' and '%s' are equal.\n", str2, str1)
	}
}
