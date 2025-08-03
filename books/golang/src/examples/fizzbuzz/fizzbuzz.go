package main

import (
	"fmt"
	"strconv"
)

func main() {
	for i:=1; i < 16; i++ {
		fmt.Println(fb(i))
	}
}

func fb(n int) string {
	resp := ""

	if n % 3 == 0 {
		resp += "Fizz"
	}
	if n % 5 == 0 {
		resp += "Buzz"
	}
	if resp == "" {
		resp = strconv.Itoa(n)
	}
	return resp
}
