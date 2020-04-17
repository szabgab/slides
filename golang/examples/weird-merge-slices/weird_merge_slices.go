package main

import (
	"fmt"
)

func main() {
	celestialObjects := []string{"Moon", "Gas", "Asteroid", "Dwarf", "Star", "Commet"}
	fmt.Println(celestialObjects)

	fmt.Println(celestialObjects[:3])
	fmt.Println(celestialObjects[4:])
	fmt.Println()

	part := append(celestialObjects[:3], celestialObjects[4:]...)
	fmt.Println(part)
	fmt.Println(celestialObjects)
	fmt.Printf("part - len: %v cap: %v\n", len(part), cap(part))
	fmt.Printf("orig - len: %v cap: %v\n", len(celestialObjects), cap(celestialObjects))
}
