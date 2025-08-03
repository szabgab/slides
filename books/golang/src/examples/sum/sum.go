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
	var fh *os.File
	fh, err = os.Open(filename)
	//fmt.Printf("%T", fh)
	if err != nil {
		fmt.Printf("Error opening file '%v'\n%v\n", filename, err)
		os.Exit(1)
	}
	reader := bufio.NewReader(fh)
	var line string
	for true {
		line, _ = reader.ReadString('\n')
		//fmt.Print(line)
		for _, c := range line {
			if c == ' ' || c == '\n' {
				continue
			}
			fmt.Printf("%q\n", c)
		}
		if line == "" {
			break
		}
	}

}
