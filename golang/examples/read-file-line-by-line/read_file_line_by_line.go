package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	filename := "read_file.go"
	fh, _ := os.Open(filename)
	reader := bufio.NewReader(fh)
	for true {
		line, _ := reader.ReadString('\n')
		fmt.Print(line)
		if line == "" {
			break
		}
	}
}
