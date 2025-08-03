package main

import (
	"fmt"
	"os"
)

func main() {
	var filename = "data.txt"

	answer := 42

	fh, err := os.Create(filename)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	text := fmt.Sprintf("%d\n", answer)
	fh.WriteString(text)
	fh.Close()

}
