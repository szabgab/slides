package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	filename := "random1.txt"
	fh, err := os.Open(filename)
	if err != nil {
		fmt.Printf("Could not open file '%v': %v", filename, err)
		os.Exit(1)
	}
	reader := bufio.NewReader(fh)
	for {
		line, err := reader.ReadString('\n')
		if err != nil {
			break
		}
		fmt.Printf("Line: %v", line)
	}
}
