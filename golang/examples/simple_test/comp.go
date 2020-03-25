package main

import (
    "fmt"
)

func main() {
    fmt.Println("Hello")
    fmt.Println(add(2, 3))
}

func add(a, b int) int {
    return a + b
}
