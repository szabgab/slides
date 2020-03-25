package main

import (
    "fmt"
)

func main() {
    age := 42
    if age >= 18 {
        fmt.Println("You can vote!")
    } else {
        fmt.Println("Sorry you cannot vote yet.")
    }
}
