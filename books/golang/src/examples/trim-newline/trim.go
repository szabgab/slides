package main

import (
	"fmt"
	"strings"
)

func main() {
	line := "hello\n"
	line = strings.TrimSuffix(line, "\n") // remove newline
	fmt.Printf("'%s'\n", line)

	line = strings.TrimSuffix(line, "\n") // not bothered if there was no newline
	fmt.Printf("'%s'\n", line)

	line = "hello\n\n"
	line = strings.TrimSuffix(line, "\n") // removing only one newline
	fmt.Printf("'%s'\n", line)
}
