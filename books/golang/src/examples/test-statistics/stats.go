package main

import "fmt"

func main() {
	numbers := []int{2, 3, 5, -1, 1, 8}
	fmt.Println(numbers)
	if len(numbers) == 0 {
		fmt.Println("We cannot provide stats on empty set of numbers")
		return
	}

	min, max, total, average := stats(numbers)

	//fmt.Println(min(numbers))
	fmt.Printf("Total: %v\n", total)
	fmt.Printf("Average: %v\n", average)
	fmt.Printf("Min: %v\n", min)
	fmt.Printf("Max: %v\n", max)
}

func stats(numbers []int) (int, int, int, float32) {
	total := 0
	min := numbers[0]
	max := numbers[0]
	for _, num := range numbers {
		if num < min {
			min = num
		}
		if num > max {
			max = num
		}
		total += num
	}
	average := float32(total) / float32(len(numbers))

	return min, max, total, average
}
