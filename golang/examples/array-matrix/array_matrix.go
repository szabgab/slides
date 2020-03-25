package main

import (
	"fmt"
)

func main() {
	var matrix [3][3]int = [3][3]int{[3]int{1, 0, 0}, [3]int{0, 1, 0}, [3]int{0, 0, 1}}
	fmt.Println(matrix)
	fmt.Println(matrix[0])
	fmt.Println(matrix[0][0])
}
