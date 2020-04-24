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

	// to iterate over interface one needs to use the .(T) modifyer
	for index, name := range person["children"].([]string) {
		fmt.Printf("  %v %v\n", index, name)
	}
}
