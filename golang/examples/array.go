package main

import (
    "fmt"
)

func main() {
    //var res int = 42
    var res = [3]int{97, 85, 93}
    //var res = [...]int{97, 85, 93}
    var names [3]string
    fmt.Println(res)
    fmt.Println(res[1])
    fmt.Println(names)
    names[0] = "Mary"
    fmt.Println(names)
}


