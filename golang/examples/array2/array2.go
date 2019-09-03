package main

import (
    "fmt"
)

func main() {
    var res = [...]int{97, 85, 93}

    fmt.Println(res)         // [97 85 93]
    fmt.Println(res[1])      // 85
    fmt.Println(len(res))    // 3

    fmt.Printf("%T\n", res)  // [3]int
}

