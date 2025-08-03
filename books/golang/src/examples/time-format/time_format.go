package main

import (
	"fmt"
	"time"
)

func main() {
	t := time.Now()
	fmt.Println("Default format:", t)
	fmt.Println("Unix format:   ", t.Format(time.UnixDate))
	fmt.Println("RFC3339 format:", t.Format(time.RFC3339))
	fmt.Println("My format:     ", t.Format("Mon Jan 2 15:04:05 MST 2006"))
	fmt.Println("My format:     ", t.Format("2006-01-02 15:04:05"))

}
