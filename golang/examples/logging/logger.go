package main

import (
	"log"
)

func main() {
	log.Print("First log")
	log.Print("Each log line is on its own")
	log.Println("Despite its name it does not add any extra newline")
	log.Printf("Value: %v seen", 42)
}
