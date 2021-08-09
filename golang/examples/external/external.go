package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	if len(os.Args) != 2 {
		fmt.Fprintln(os.Stderr, "Needs to get the expected exit code as a parameter")
		os.Exit(1)
	}
	exit_code, err := strconv.Atoi(os.Args[1])
	if err != nil {
		fmt.Fprintln(os.Stderr, "Expected integer on the command line")
		os.Exit(-1)
	}

	fmt.Println("To STDOUT")
	fmt.Fprintln(os.Stderr, "To STDERR")
	os.Exit(exit_code)
}
