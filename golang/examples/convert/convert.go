package main

import (
    "fmt"
)

func main() {
    var n = 65
    var q = float32(n)
    fmt.Println(q)          // 65
    fmt.Printf("%T\n", q)   // float32

    var z = 42.23
    var p = int(z)
    fmt.Println(p)          // 42
    fmt.Printf("%T\n", p)   // int


    var ns = string(n)
    fmt.Println(ns)         // A
    fmt.Printf("%T\n", ns)  // string
}
