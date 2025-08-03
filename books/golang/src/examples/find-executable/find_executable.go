package main

import (
	"fmt"
	"os"
	"os/exec"
)

func main() {
	path, err := exec.LookPath("python")
	if err != nil {
		fmt.Println("Could not find path")
		os.Exit(1)
	}
	fmt.Printf("%v %T\n", path, path)
}
