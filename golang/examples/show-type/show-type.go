package main

import "fmt"

func main() {
    var name = "Foo"
    var age = 42.5
    var married = true
    var children = 2

    fmt.Printf("%T\n", name)      // string
    fmt.Printf("%T\n", age)       // float64
    fmt.Printf("%T\n", married)   // bool
    fmt.Printf("%T\n", children)  // int
}
