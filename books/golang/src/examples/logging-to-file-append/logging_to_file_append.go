package main

import (
	"log"
	"os"
)

func main() {
	var filename = "logging_to_file_append.log"
	var fh, err = os.OpenFile(filename, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		log.Fatalf("Could not open file '%v': %v", filename, err)
	}
	log.SetOutput(fh)

	log.Print("Hello logfile")
	log.Fatal("This is bad")
}
