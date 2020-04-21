package main

import "fmt"

func main() {
	person := make(map[string]interface{})
	person["name"] = "Foo Bar"
	person["year"] = 1998
	person["children"] = []string{"Joe", "Jane", "Jannet"}
	fmt.Println(person)

	for key, value := range person {
		fmt.Printf("%v %T\n", key, value)
	}

	// cannot range over interface
	// for index, name := range person["children"] {
	// 	fmt.Printf("  %v %v", index, name)
	// }
}
