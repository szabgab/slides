package main

import (
	"log"
)

func main() {
	log.SetPrefix("Foo ")
	log.Print("First")
	log.Print("Second")
	log.SetPrefix("Bar ")
	log.Print("Third")
}
