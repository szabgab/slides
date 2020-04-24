package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

const filename = "my.log"

func main() {
	debug("Hello")
	show()
	debug("World")
	show()
}

func show() {
	content, err := ioutil.ReadFile(filename)
	if err != nil {
		fmt.Printf("Could not open file '%v' for reading: %v", filename, err)
		return
	}
	fmt.Println(string(content))
	fmt.Println()
}

func debug(text string) {
	fh, err := os.OpenFile(filename, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		fmt.Println(err)
		return
	}
	fh.WriteString(text + "\n")
	fh.Close()
}
