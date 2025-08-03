package main

import (
	"io/ioutil"
	"log"
	"os"
)

func main() {
	log.Print("One")
	log.SetOutput(ioutil.Discard)
	log.Print("Two")
	log.SetOutput(os.Stderr)
	log.Print("Three")
}
