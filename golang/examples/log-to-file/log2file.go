package main

import (
    "log"
    "fmt"
    "os"
)

func main() {
    fmt.Println("First")

    var filename = "log.log"
    var fh, _ = os.Create(filename)
    log.SetOutput(fh)

    log.Print("First log")
    log.Print(log.Flags)
    log.SetFlags(log.Lshortfile | log.LstdFlags)
    log.Print("After setting flags")
    log.Fatal("Oups")

    fmt.Println("Last")
}
