package main

import (
	"log"
	"os/exec"
)

func main() {
	cmd := exec.Command("sleep", "5")
	err := cmd.Start()
	if err != nil {
		log.Fatal(err)
	}
	log.Printf("Waiting for command to finish...")
	err = cmd.Wait()
	log.Printf("Command finished with error: %v", err)

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
