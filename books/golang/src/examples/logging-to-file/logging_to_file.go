package main

import (
	"log"
	"os"
)

func main() {
	var filename = "logging_to_file.log"
	var fh, err = os.Create(filename)
	if err != nil {
		log.Fatalf("Could not open file '%v': %v", filename, err)
	}
	log.SetOutput(fh)

	log.Print("Hello logfile")
	log.Fatal("This is bad")
}
