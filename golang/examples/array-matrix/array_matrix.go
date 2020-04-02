package main

import (
	"fmt"
)

func main() {
	matrix := [3][3]int{
		[3]int{1, 2, 3},
		[3]int{4, 1, 0},
		[3]int{0, 0, 1},
	}
	fmt.Println(matrix)
	fmt.Println(matrix[0])
	fmt.Println(matrix[1][0])
}

// 	matrix := [...][3]int{    Would also work
//  var matrix [3][3]int      Is to define without giving values
