package main

import (
	"fmt"
	"log"
	"os/exec"
	"time"
)

func main() {
	cmd := exec.Command("sleep", "2")
	fmt.Printf("%v - Start.\n", time.Now().Unix())
	err := cmd.Start()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("%v - We could do here something before we wait for the job to finish.\n", time.Now().Unix())
	err = cmd.Wait()
	fmt.Printf("%v - Command finished\n", time.Now().Unix())
	if err != nil {
		fmt.Printf("There was an error in the process: %v\n", err)
	}
}
