package main

import (
	"fmt"
)

func main() {
	joeGrades := []int{2, 3, 4}
	fmt.Println(joeGrades)
	janeGrades := []int{7, 9, 5, 10}
	fmt.Println(janeGrades)

	people := make(map[string][]int)
	fmt.Println(people)
	people["joe"] = joeGrades
	people["jane"] = janeGrades
	fmt.Println(people)
}
