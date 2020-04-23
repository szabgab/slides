package main

import (
	"fmt"
)

func main() {
	ip := struct {
		address string
		name    string
	}{
		address: "127.0.0.1",
		name:    "home"}

	fmt.Println(ip)
	fmt.Println(ip.address)
	fmt.Println(ip.name)
}
