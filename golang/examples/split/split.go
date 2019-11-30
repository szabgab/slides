package main

import (
    "fmt"
    "strings"
)

func main() {
    text := "Hello World!"
    fmt.Println(text)

    chars := strings.Split(text, "")
    fmt.Println(chars)

    new_text := strings.Join(chars, "-")
    fmt.Println(new_text)
}

