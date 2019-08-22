package main

import (
        "fmt"
        "math/rand"
        "time"
)

func main() {
        fmt.Println()
        fmt.Println(time.Now())
        rand.Seed(time.Now().Unix())
        fmt.Println(rand.Intn(10))
        t := time.Now()
        fmt.Println(t.Unix())
}

