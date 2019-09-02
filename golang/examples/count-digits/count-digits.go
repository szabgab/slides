package main

import "fmt"

func main() {
    count := make([]int, 10)
    fmt.Println("count", count)

    digits := []int{3, 7, 6, 7, 9, 1, 3, 7}
    fmt.Println(digits)

    for i := 0; i < len(digits); i++ {
        //fmt.Println(digits[i])
        count[ digits[i] ]++
    }
    for i := 0; i < 10; i++ {
        fmt.Printf("%d: %d\n", i, count[i])
    }
}

