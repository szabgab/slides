package main

import (
    "fmt"
    "os"
    "strings"
    "path/filepath"
    "io/ioutil"
)

func main() {
    fmt.Println("Checking the Go slides")
    root := "golang"

    errors := 0
    errors += check_main_dir(root)
    errors += check_examples_dir(root)

    fmt.Println("Checking Go finished")
    if errors > 0 {
        fmt.Printf("%v errors found", errors)
        os.Exit(1)
    }
    os.Exit(0)
}

func check_examples_dir(root string) int {
    errors := 0
    path := filepath.Join(root, "examples")
    files, err := ioutil.ReadDir(path)
    if err != nil {
        fmt.Printf("Error: %v", err)
        os.Exit(1)
    }
    fmt.Println(path)
    // TODO check for valic characters instead of invalid ones: a-z-
    for _, f := range files {
        if strings.Contains(f.Name(), "_") {
            fmt.Printf("Underscore in dirname: %v\n", f.Name())
            errors++
        }
        //fmt.Printf("%v\n", f.Name())
    }
    return errors
}

func check_main_dir(root string) int {
    errors := 0
    files, err := ioutil.ReadDir(root)
    if err != nil {
        fmt.Printf("Error: %v", err)
        os.Exit(1)
    }
    for _, f := range files {
        if f.Name() == ".vscode" || f.Name() == "examples" || f.Name() == "go.json" {
            continue
        }
        if ! strings.HasSuffix(f.Name(), ".md") {
            fmt.Printf("Unrecognized entry: %v\n", f.Name())
            errors++
        }
    }
    return errors
}


//func walk() {
//    root := "golang"
//    subDirToSkip := "xyz"
//    err := filepath.Walk(root, func(path string, info os.FileInfo, err error) error {
//        if err != nil {
//            fmt.Printf("Cannot access dir at path %q: %v", path, err)
//            return err
//        }
//        if info.IsDir() && info.Name() == subDirToSkip {
//            fmt.Printf("Skipping directory %+v \n", info.Name())
//        }
//        //fmt.Printf("Visiting %q\n", path)
//        if ! info.Mode().IsRegular() {
//            return nil
//        }
//        fmt.Printf("Visiting %q\n", path)
//        return nil
//    })
//    if err != nil {
//        fmt.Printf("error walking the path %q: %v\n", root, err)
//    }
//}
