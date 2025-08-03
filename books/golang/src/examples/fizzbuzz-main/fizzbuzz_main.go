package main

import (
	"fmt"
	"strconv"
)

func main() {
	for n := 1; n < 100; n++ {
		resp := ""

		if n%3 == 0 {
			resp += "Fizz"
		}
		if n%5 == 0 {
			resp += "Buzz"
		}
		if resp == "" {
			resp = strconv.Itoa(n)
		}

		fmt.Println(resp)
	}
}
