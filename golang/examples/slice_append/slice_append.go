package main

import (
    "fmt"
)

func main() {
    var dwarfs = []string{}
    fmt.Println(dwarfs)
    fmt.Println(len(dwarfs))

    dwarfs = append(dwarfs, "Happy")
    fmt.Println(dwarfs)
    fmt.Println(len(dwarfs))

    dwarfs = append(dwarfs, "Grumpy", "Sleepy")
    fmt.Println(dwarfs)
    fmt.Println(len(dwarfs))
}

