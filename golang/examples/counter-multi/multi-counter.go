package main

import (
    "fmt"
    "os"
)

func main() {
    // var filename = "counter.json"
    if len(os.Args) != 2 {
        fmt.Printf("Usage: %s NAME\n", os.Args[0])
        os.Exit(1)
    }
    var name = os.Args[1]
    var count = map[string]int{}
    //  use file 
    count[name]++
    fmt.Printf("%s %d\n", name, count[name])
}
