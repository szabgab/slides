package main

import (
	"fmt"
	"os"
)

func main() {
	var filename = "data.txt"

	text := "Some text"
	var fh, err = os.Create(filename)
	if err != nil {
		fmt.Println(err)
		return
	}
	fh.WriteString(text + "\n")
	fh.Close()

}
