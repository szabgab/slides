package main

import "fmt"

func main() {
    // var g map[string]int   // defined type but does not create the container for it
    // fmt.Printf("%T\n", g)   // map[string]int

    grades := make(map[string]int)
    fmt.Printf("%T\n", grades)   // map[string]int

    grades["Mary"] = 99
    grades["Jane"] = 88
    grades["Bob"]  = 93

    fmt.Println(grades)           // map[Bob:93 Jane:88 Mary:99]

    fmt.Println(grades["Jane"])   // 88

    for k, v := range grades {
        fmt.Printf("k: %s v: %d\n", k, v)
    }
}
