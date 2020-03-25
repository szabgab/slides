package main

import (
    "fmt"
)

func main() {
    fmt.Println("Hello")
    dwarfs := []string{"Doc", "Grumpy", "Happy", "Sleepy", "Bashful", "Sneezy", "Dopey"}

    fmt.Println(dwarfs)

    for i, name := range dwarfs {
        fmt.Printf("location: %d  name: %s\n", i, name)
    }
}
