package main

import "fmt"

func main() {
    grades := make(map[string]int)
    fmt.Printf("%T\n", grades)   // map[string]int

    grades["Mary"] = 99
    grades["Jane"] = 88
    grades["Bob"]  = 93

    fmt.Println(grades)           // map[Bob:93 Jane:88 Mary:99]

    delete(grades, "Jane")

    fmt.Println(grades)           // map[Bob:93 Mary:99]
}

