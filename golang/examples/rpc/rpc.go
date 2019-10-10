package main

import (
    "fmt"
    "os"
    "strings"
)

func main() {
    if len(os.Args) != 2 {
        fmt.Printf("Usage: %s EXPRESSION (put the whole thing in quotes)\n", os.Args[0])
        os.Exit(1)
    }
    expression := os.Args[1]
    fmt.Println(expression)
    parts := strings.Fields(expression)
    fmt.Println(parts)
    fmt.Println(len(parts))
}
