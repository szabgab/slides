package main

import (
	"fmt"
	"os"
	"path/filepath"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Printf("Usage: %s DIRNAME", os.Args[0])
		os.Exit(1)
	}
	root := os.Args[1]

	// TODO: list of skips or regex for skip or function call to check skip
	subDirToSkip := "skip"

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
