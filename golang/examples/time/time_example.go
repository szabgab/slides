package main

import (
    "fmt"
    "time"
)

func main() {
    fmt.Println(time.Now())
    fmt.Println(time.Now().Unix())

    t := time.Now()
    fmt.Println(t.Unix())
}

