package main

import (
    "fmt"
    "os"
)

func main() {
    fmt.Println(len(os.Args))
    fmt.Printf("%T\n", os.Args)  // []string   (slice)

    fmt.Println(os.Args[0])
    fmt.Println(os.Args)

    fmt.Println(len(os.Args))
}
