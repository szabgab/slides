package main

import (
	"fmt"
	"strings"
)

func main() {
	original := "abcdefghijklmnopqrstyvwxyz ABCQRS !?¡ñ"
	//original = "Hello World!"
	fmt.Println(len(original))
	encrypted := rot13(original)
	decrypted := rot13(encrypted)

	fmt.Println(original)
	fmt.Println(encrypted)
	fmt.Println(decrypted)
	fmt.Println(original == decrypted)
}

func rot13(input string) string {
	result := make([]string, 0, len(input))
	for _, chr := range input {
		if 'a' <= chr && chr <= 'z' {
			chr = ((chr - 'a' + 13) % 26) + 'a'
		}
		if 'A' <= chr && chr <= 'Z' {
			chr = ((chr - 'A' + 13) % 26) + 'A'
		}
		result = append(result, string(chr))
	}
	output := strings.Join(result, "")
	return output
}
