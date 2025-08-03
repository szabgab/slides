package main

import (
	"fmt"
	"time"
)

func main() {
	t := time.Now()
	fmt.Printf("%T\n", t)
	fmt.Println(t)
	fmt.Println(t.Unix())
	fmt.Println(t.UnixNano())
}
