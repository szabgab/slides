package main

import (
	"fmt"
	"runtime"
)

func main() {
	_, file, _, _ := runtime.Caller(0)
	fmt.Println(file)
}
