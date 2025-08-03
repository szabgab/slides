package main

import (
	"fmt"
	"regexp"
)

func main() {
	text := "There are no numbers in this text"
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
