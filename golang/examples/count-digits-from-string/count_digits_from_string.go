package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	count := [10]int{}

	dgts := "3767913713127648173"
	fmt.Println(dgts)
	digits := strings.Split(dgts, "")
	fmt.Println(digits)

	for _, digitStr := range digits {
		digit, _ := strconv.Atoi(digitStr)
		count[digit]++
	}

	for i, cnt := range count {
		fmt.Printf("%v %v\n", i, cnt)
	}
}
