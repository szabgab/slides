package main

import (
    "os"
)

func main() {
    var filename = "data.txt"

    var fh, err = os.Create(filename)
    if err == nil {
        fh.WriteString("Some text\n")
        fh.Close()
    }
}

