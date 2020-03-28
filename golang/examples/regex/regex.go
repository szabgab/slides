package main

import (
	"fmt"
	"regexp"
)

func main() {
	text := "In this text there is a number 123456 and an age: 42 and another number 78"

	getNumber := regexp.MustCompile(`\d+`)
	res1 := getNumber.MatchString(text)
	fmt.Println(res1)

	res2 := getNumber.Find([]byte(text))
	fmt.Printf("%q\n", res2)

	res3 := getNumber.FindAll([]byte(text), -1)
	fmt.Printf("%q\n", res3)

	getAge := regexp.MustCompile(`age: (\d+)`)
	res4 := getAge.Find([]byte(text))
	fmt.Printf("%q\n", res4)

	res5 := getAge.FindAllSubmatch([]byte(text), -1)
	fmt.Printf("%q\n", res5)

	//var validID = regexp.MustCompile(`^[a-z]+\[[0-9]+\]$`)
	//fmt.Println(validID.MatchString("adam[23]"))
}
