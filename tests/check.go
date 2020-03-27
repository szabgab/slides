package main

import (
    "fmt"
    "os"
    "path/filepath"
)

func main() {
    fmt.Println("Checking the Go slides")
    walk()
}


func walk() {
    root := "golang"
    subDirToSkip := "xyz"
    err := filepath.Walk(root, func(path string, info os.FileInfo, err error) error {
        if err != nil {
            fmt.Printf("Cannot access dir at path %q: %v", path, err)
            return err
        }
        if info.IsDir() && info.Name() == subDirToSkip {
            fmt.Printf("Skipping directory %+v \n", info.Name())
        }
        fmt.Printf("Visiting %q\n", path)
        return nil
    })
    if err != nil {
        fmt.Printf("error walking the path %q: %v\n", root, err)
    }
}
