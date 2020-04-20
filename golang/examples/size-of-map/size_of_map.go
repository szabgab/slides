package main

import "fmt"

func main() {
	scores := map[string]int{"Alma": 23, "Cecilia": 12, "Berta": 78}
	fmt.Println(len(scores))
	scores["David"] = 37
	fmt.Println(len(scores))
	delete(scores, "Alma")
	fmt.Println(len(scores))
}
