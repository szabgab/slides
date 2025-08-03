package main

import (
	"fmt"
	"os"
)

func main() {
	if len(os.Args) != 2 {
		fmt.Printf("Usage %s FILENAME\n", os.Args[0])
		os.Exit(1)
	}
	var filename = os.Args[1]
	var st, err = os.Stat(filename)
	if err != nil {
		fmt.Printf("Error: %s\n", err)
		if os.IsNotExist(err) {
			fmt.Printf("IsNotExist\n")
		}
		os.Exit(1)
	}
	fmt.Println(st)
	fmt.Printf("Name: %s\n", st.Name())
	fmt.Printf("Size: %d\n", st.Size())
}
