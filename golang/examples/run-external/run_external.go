package main

import (
	"fmt"
	"log"
	"os/exec"
	"time"
)

func main() {
	cmd := exec.Command("sleep", "2")
	fmt.Printf("%v - start\n", time.Now().Unix())
	err := cmd.Run()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("%v - Only after command has finished\n", time.Now().Unix())

	// perl, err := exec.LookPath("perl")
	// if err != nil {
	// 	fmt.Println("Could not find path")
	// 	os.Exit(1)
	// }

	// //fmt.Printf("%v %T", er, path)

	// //perl -E 'say "Hello from Perl"'
	// cmd := exec.Command(perl, "-E", `x'say "Hello from Perl"'`)
	// fmt.Printf("%v\n", cmd)
	// cmd.Stdout = os.Stdout
	// cmd.Stderr = os.Stderr

	// err = cmd.Run()
	// if err != nil {
	// 	fmt.Println(err)
	// 	os.Exit(1)
	// }

	// cmd := exec.Command("ls", "-l")
	// fmt.Printf("%v\n", cmd)
	// cmd.Stdout = os.Stdout
	// cmd.Stderr = os.Stderr

	// err := cmd.Run()
	// if err != nil {
	// 	fmt.Println(err)
	// 	os.Exit(1)
	// }

}
