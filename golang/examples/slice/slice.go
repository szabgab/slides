package main

import (
    "fmt"
)

func main() {
    var dwarfs = []string{"Doc", "Grumpy", "Happy", "Sleepy", "Bashful", "Sneezy", "Dopey"}

    fmt.Println(len(dwarfs))   // 7
    fmt.Println(dwarfs)
    fmt.Println(dwarfs[1])     // Grumpy
}
