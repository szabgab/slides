package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func main() {
	var err error
	if len(os.Args) != 2 {
		log.Fatal("Missing parameter: filename")
	}
	filename := os.Args[1]
	// fmt.Println(filename)

	fh, err := os.Open(filename)
	if err != nil {
		log.Fatalf("Could not open file '%v': %v", filename, err)
		os.Exit(1)
	}
	reader := bufio.NewReader(fh)
	for {
		line, err := reader.ReadString('\n')
		if err != nil {
			log.Fatal("Error while reading line")
		}
		fmt.Print(line)
		if line == "" {
			break
		}
	}
}
