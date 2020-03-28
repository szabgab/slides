package main

import (
	"os"
)

func main() {
	var filename = "data.txt"

	text := "Some text"
	var fh, err = os.Create(filename)
	if err == nil {
		fh.WriteString(text + "\n")
		fh.Close()
	}
}
