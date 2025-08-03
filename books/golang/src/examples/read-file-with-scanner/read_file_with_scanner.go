package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	filename := "random.txt"
	fh, err := os.Open(filename)
	if err != nil {
		fmt.Printf("Could not open file '%v': %v", filename, err)
		os.Exit(1)
	}
	scanner := bufio.NewScanner(fh)
	for scanner.Scan() {
		line := scanner.Text()
		fmt.Printf("Line: %v\n", line)
	}
	if err := scanner.Err(); err != nil {
		fmt.Fprintln(os.Stderr, "reading:", err)
	}
}
