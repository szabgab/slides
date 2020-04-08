package main

import (
	"fmt"
	"regexp"
)

func main() {
	text := "In this text there is a number 123456 and an age: 42 and another number 78"
	//	var match bool
	var res []byte
	//	var plex [][]byte
	var firstSubmtach [][]byte
	var allSubmtaches [][][]byte
	//	var str []string

	getAge := regexp.MustCompile(`age: (\d+)`)
	res = getAge.Find([]byte(text))
	fmt.Printf("%q\n", res)

	fmt.Println()
	firstSubmtach = getAge.FindSubmatch([]byte(text))
	fmt.Printf("%q\n", firstSubmtach)
	fmt.Printf("%q\n", firstSubmtach[1])

	fmt.Println()
	allSubmtaches = getAge.FindAllSubmatch([]byte(text), -1)
	fmt.Printf("%q\n", allSubmtaches)
	fmt.Printf("%q\n", allSubmtaches[0][1])
}
