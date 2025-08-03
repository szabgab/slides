package main

import (
	"fmt"
	"os"
)

func main() {
	fmt.Println("To STDOUT using fmt.Println")
	fmt.Fprintln(os.Stderr, "To STDERR using fmt.Fprintlt")
	os.Stderr.WriteString("To STDERR using os.Stderr.WriteString\n")
}
