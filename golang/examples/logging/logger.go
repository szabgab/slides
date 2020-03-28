package main

import (
	"fmt"
	"log"
)

func main() {
	fmt.Println("First")
	log.Print("First log")
	log.Print(log.Flags)
	log.SetFlags(log.Lshortfile | log.LstdFlags)
	log.Print("After setting flags")
	log.Fatal("Oups")
	fmt.Println("Last")
}
