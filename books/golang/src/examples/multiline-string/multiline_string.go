package main

import "fmt"

func main() {
	text := `This
is a long
string
with multiple lines
`
	fmt.Printf("Type: %T\n\n", text)
	fmt.Println(text)

}
