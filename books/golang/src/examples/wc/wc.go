package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strings"
)

func main() {
	fmt.Println(os.Args)
	wc(os.Args[1:])
}

func wc(filenames []string) (int, int, int) {
	rows := 0
	words := 0
	chars := 0
	filename := filenames[0]
	fh, err := os.Open(filename)
	if err != nil {
		os.Exit(1)
	}
	reader := bufio.NewReader(fh)
	for {
		line, err := reader.ReadString('\n')
		if err != nil {
			if err != io.EOF {
				fmt.Println(err)
			}
			break
		}
		rows++
		words += len(strings.Fields(line))
		chars += len(line)
	}
	return rows, words, chars
}
