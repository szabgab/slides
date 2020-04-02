package main

import (
	"fmt"
)

func main() {
	celestialObjects := []string{"Moon", "Gas", "Asteroid", "Dwarf", "Asteroid", "Moon", "Asteroid"}
	fmt.Println(celestialObjects)
	var location int
	var found bool
	var str string

	str = "Asteroid"
	location, found = findElement(str, celestialObjects)
	if found {
		fmt.Printf("Found %v in %v\n", str, location)
	} else {
		fmt.Printf("Not found %v in %v\n", str, location)
	}

	str = "Star"
	location, found = findElement(str, celestialObjects)
	if found {
		fmt.Printf("Found %v in %v\n", str, location)
	} else {
		fmt.Printf("Not found %v in %v\n", str, location)
	}

}

func findElement(elem string, elements []string) (int, bool) {
	for i, value := range elements {
		if value == elem {
			return i, true
		}
	}
	return -1, false
}