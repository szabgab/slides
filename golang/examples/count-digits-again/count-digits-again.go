package main

import "fmt"
import "strings"
import "strconv"

func main() {
    count := make([]int, 10)
    fmt.Println("count", count)

    dgts := "37679137"
    digits := strings.Split(dgts, "")
    fmt.Println(digits)

    for _, digit_str := range digits {
        digit, _ := strconv.Atoi(digit_str)
        count[ digit ]++
    }
    fmt.Println("count", count)
}

