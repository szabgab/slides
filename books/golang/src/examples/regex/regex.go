package main

import (
	"fmt"
	"regexp"
)

func main() {
	text := "In this text there is a number 123456 and an age: 42 and another number 78"
	var match bool
	var res []byte
	var plex [][]byte
	var str []string

	getNumber := regexp.MustCompile(`\d+`)
	match = getNumber.MatchString(text)
	fmt.Println(match)

	res = getNumber.Find([]byte(text))
	fmt.Printf("%q\n", res)

	str = getNumber.FindStringSubmatch(text)
	fmt.Printf("%q\n", str)

	plex = getNumber.FindAll([]byte(text), -1)
	fmt.Printf("%q\n", plex)
}
