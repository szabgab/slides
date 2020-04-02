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
	var threed [][][]byte
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

	getAge := regexp.MustCompile(`age: (\d+)`)
	res = getAge.Find([]byte(text))
	fmt.Printf("%q\n", res)

	threed = getAge.FindAllSubmatch([]byte(text), -1)
	fmt.Printf("%q\n", threed)
	fmt.Printf("%q\n", threed[0][1])

	//var validID = regexp.MustCompile(`^[a-z]+\[[0-9]+\]$`)
	//fmt.Println(validID.MatchString("adam[23]"))
}
