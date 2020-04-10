package main

import (
	"log"
)

func main() {
	log.Print("standard (default)")

	log.SetFlags(log.LstdFlags | log.Lshortfile)
	log.Print("standard + shortfile")

	log.SetFlags(log.LstdFlags | log.Llongfile)
	log.Print("standard + shortfile")

	log.SetFlags(log.Lshortfile)
	log.Print("shortfile")
}
