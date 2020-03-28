package main

import (
	"fmt"
	"path/filepath"
)

func main() {
	path := filepath.Join("main", "sub", "other") // main/sub/other   main\sub\other
	fmt.Println(path)
}
