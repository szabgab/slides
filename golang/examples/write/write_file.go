package main

import (
	"fmt"
	"os"
)

func main() {
	var filename = "z/data.txt"

	text := "Some text"
	var fh, err = os.Create(filename)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	fh.WriteString(text + "\n")
	fh.Close()

}
