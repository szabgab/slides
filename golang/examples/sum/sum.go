package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var err error
	if len(os.Args) != 2 {
		fmt.Printf("Missing filename.\nUsage: %v FILENAME\n", os.Args[0])
		os.Exit(1)
	}

	filename := os.Args[1]
	//fmt.Println(filename)
	fh, err := os.Open(filename)
	if err != nil {
		fmt.Printf("Error opening file '%v'\n%v\n", filename, err)
		os.Exit(1)
	}
	reader := bufio.NewReader(fh)
	for true {
		line, _ := reader.ReadString('\n')
		fmt.Print(line)
		if line == "" {
			break
		}
	}

}
