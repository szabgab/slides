package main

import (
	"log"
)

func main() {
	log.Print(log.Ldate)         // 1
	log.Print(log.Ltime)         // 2
	log.Print(log.LstdFlags)     // 3 Ldate | Ltime
	log.Print(log.Lmicroseconds) // 4
	log.Print(log.Llongfile)     // 8
	log.Print(log.Lshortfile)    // 16
	log.Print(log.LUTC)          // 32

	log.Print("")
	log.Print(log.Flags()) // 3
}
