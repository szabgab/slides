package main

import (
    "fmt"
    "strconv"
)

func main() {
    var x = "42"
    var r, _ = strconv.Atoi(x)
    fmt.Printf("%d %T\n", r, r)     // 42 int



    var y = "4.2"
    var z, _ = strconv.ParseFloat(y, 64)
    fmt.Printf("%f %T\n", z, z)    // 4.200000 float64
}
