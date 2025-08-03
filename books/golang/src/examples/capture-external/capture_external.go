package main

import (
	"bytes"
	"fmt"
	"log"
	"os/exec"
)

func main() {
	cmd := exec.Command("go", "run", "examples/external/external.go", "23")
	//cmd := exec.Command("ls", "xxx")
	var stdout, stderr bytes.Buffer
	cmd.Stdout = &stdout
	cmd.Stderr = &stderr
	err := cmd.Run()
	fmt.Println("-------")
	fmt.Println(stdout.String())
	fmt.Println("-------")
	fmt.Println(stderr.String())
	fmt.Println("-------")
	fmt.Println(cmd.ProcessState.String() == "exit status 2")
	fmt.Println(cmd.ProcessState)
	fmt.Println("-------")
	if err != nil {
		log.Fatal(err)
	}
}
