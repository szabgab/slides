package main

import (
	"fmt"
)

func main() {
	celestialObjects := []string{"Moon", "Gas", "Asteroid", "Dwarf", "Star", "Commet"}
	fmt.Println(celestialObjects)

	celestialObjects = append(celestialObjects[:3], celestialObjects[4:]...)
	fmt.Println(celestialObjects)

}
