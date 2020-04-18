package main

import "fmt"

func main() {
	var str1 string
	var str2 string
	fmt.Print("First string: ")
	fmt.Scan(&str1)
	fmt.Print("Second string: ")
	fmt.Scan(&str2)

	fmt.Println("1) by length")
	fmt.Println("2) by abc")
	fmt.Print("How shall we compare them? ")
	var choice string
	fmt.Scan(&choice)

	result := 0
	switch choice {
	case "1":
		if len(str1) < len(str2) {
			result = 1
		}
		if len(str1) > len(str2) {
			result = 2
		}
	case "2":
		if str1 < str2 {
			result = 1
		}
		if str1 > str2 {
			result = 2
		}
	}
	fmt.Println(result)
	switch result {
	case 1:
		fmt.Printf("The first string '%s' is ahead of '%s'\n", str1, str2)
	case 2:
		fmt.Printf("The second string '%s' is ahead of '%s'\n", str2, str1)
	default:
		fmt.Printf("The two string '%s' and '%s' are equal.\n", str2, str1)
	}
}
