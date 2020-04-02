package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	languages := [...]string{"English", "French", "Urdu", "Farsi", "Hungarian", "Hebrew"}
	for i, lang := range languages {
		fmt.Printf("%v) %v\n", i+1, lang)
	}
	var choiceStr string
	fmt.Print("Select a number: ")
	fmt.Scan(&choiceStr)
	fmt.Println(choiceStr)

	choice, err := strconv.Atoi(choiceStr)
	if err != nil {
		fmt.Printf("The selection '%v' was not an integer\n", choiceStr)
		fmt.Println(err)
		os.Exit(1)
	}

	if choice <= 0 || choice > len(languages) {
		fmt.Printf("The selection '%v' was out of range\n", choiceStr)
		os.Exit(1)
	}
	fmt.Printf("Selection: %v\n", languages[choice-1])

}
