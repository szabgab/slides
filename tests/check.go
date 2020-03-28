package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"path/filepath"
	"io/ioutil"
	"regexp"
)

func main() {
	fmt.Println("Checking Go started")
	root := "golang"

	errors := 0
	errors += check_file(filepath.Join("tests", "check.go"))
	errors += check_main_dir(root)
	errors += check_examples_dir(root)
	errors += check_examples(root)

	fmt.Println("Checking Go finished")
	if errors > 0 {
		fmt.Printf("%v errors found\n", errors)
		os.Exit(1)
	}
	os.Exit(0)
}

func check_examples(root string) int {
// TODO: make sure filenames are unique across the examples
// TODO: should filename be using underscores intsead of dashes?
	errors := 0
	path := filepath.Join(root, "examples")
	dirs, err := ioutil.ReadDir(path)
	if err != nil {
		fmt.Printf("Error: %v", err)
		os.Exit(1)
	}
	for _, dir := range dirs {
		if dir.Name() == "numbers.txt" {
			continue
		}
		dirpath := filepath.Join(path, dir.Name())
		//fmt.Println(dirpath)
		files, err := ioutil.ReadDir(dirpath)
		if err != nil {
			fmt.Printf("Error: %v", err)
			os.Exit(1)
		}
		for _, file := range files {
			//fmt.Printf("   %v\n", file.Name())
			if strings.HasSuffix(file.Name(), ".go") {
				errors += check_file(filepath.Join(path, dir.Name(), file.Name()))
			}
			// TODO: If there is a .go file and an .out file, run the .go file and compare the output
		}
	}
	return errors
}

// If there is a .go file check if the indentation is always tabs
func check_file(filepath string) int {
	//fmt.Println(filepath)
	errors := 0
	fh, err := os.Open(filepath)
	if err != nil {
		fmt.Printf("Error: %v", err)
		os.Exit(1)
	}
	reader := bufio.NewReader(fh)
	for true {
	   line, _ := reader.ReadString('\n')
			if strings.HasSuffix(line, " ") {
				fmt.Printf("Space suffix in file '%v' line: '%v'\n", filepath, line)
				errors++
			}
			if strings.HasPrefix(line, " ") {
				fmt.Printf("Space prefix in file '%v' line: '%v'\n", filepath, line)
				errors++
			}

	   if (line == "") {
		   break
	   }
	}

	return errors
}

func check_examples_dir(root string) int {
	errors := 0
	path := filepath.Join(root, "examples")
	dirs, err := ioutil.ReadDir(path)
	if err != nil {
		fmt.Printf("Error: %v", err)
		os.Exit(1)
	}
	validExampleDir := regexp.MustCompile(`^[a-z0-9-]+$`)
	//fmt.Println(path)
	for _, dir := range dirs {
		if dir.Name() == "numbers.txt" {
			continue
		}
		res := validExampleDir.MatchString(dir.Name())
		if !res {
			fmt.Printf("Invalid character in dirname: '%v'\n", dir.Name())
			errors++
		}
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
	for _, file := range files {
		if file.Name() == ".vscode" || file.Name() == "examples" || file.Name() == "go.json" {
			continue
		}
		if ! strings.HasSuffix(file.Name(), ".md") {
			fmt.Printf("Unrecognized entry: %v\n", file.Name())
			errors++
		}
	}
	return errors
}


//func walk() {
//	root := "golang"
//	subDirToSkip := "xyz"
//	err := filepath.Walk(root, func(path string, info os.FileInfo, err error) error {
//		if err != nil {
//			fmt.Printf("Cannot access dir at path %q: %v", path, err)
//			return err
//		}
//		if info.IsDir() && info.Name() == subDirToSkip {
//			fmt.Printf("Skipping directory %+v \n", info.Name())
//		}
//		//fmt.Printf("Visiting %q\n", path)
//		if ! info.Mode().IsRegular() {
//			return nil
//		}
//		fmt.Printf("Visiting %q\n", path)
//		return nil
//	})
//	if err != nil {
//		fmt.Printf("error walking the path %q: %v\n", root, err)
//	}
//}
