package main

import (
	"fmt"
	"os"
)

func main() {
	var filename = "data.txt"

	answer := 42

	var fh, err = os.Create(filename)
	if err == nil {
		fh.WriteString(fmt.Sprintf("%d\n", answer))
		fh.Close()
	}
}
