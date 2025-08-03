package main

import (
	"fmt"
	"io"
	"strings"
)

func main() {
	someString := "hello world\nand hello go and more"
	myReader := strings.NewReader(someString)

	fmt.Printf("%T", myReader) // *strings.Reader

	buffer := make([]byte, 10)
	for {
		count, err := myReader.Read(buffer)
		if err != nil {
			if err != io.EOF {
				fmt.Println(err)
			}
			break
		}
		fmt.Printf("Count: %v\n", count)
		fmt.Printf("Data: %v\n", string(buffer))
	}

}
